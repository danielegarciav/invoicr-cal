import helpers.ExceptionHandling
import json
import datetime
from helpers.GCalWrapper import GCalWrapper
from helpers.InvoiceBuilder import InvoiceBuilder
from helpers.ChromePrintToPDF import print_to_pdf


def tgc(filename: str) -> str:
    """ Get filename with test generated content path appended. """
    TGC_FOLDER = "test_generated_content"
    return "{}/{}".format(TGC_FOLDER, filename)


class InvoicrModel:
    SETTINGS_FILE = 'invoicr_settings.json'
    DEFAULT_SETTINGS_FILE = "default_assets/default_settings.json"

    def __init__(self):
        self.gc = GCalWrapper()
        self.gcs = self.gc.service
        self.settings = self.get_settings()
        self.tlc = None

    def get_settings(self):
        try:
            with open(self.SETTINGS_FILE) as f:
                return json.load(f)
        except:
            print("Generating settings file")
            with open(self.DEFAULT_SETTINGS_FILE) as df:
                settings = json.load(df)
                with open(self.SETTINGS_FILE, 'w') as f:
                    json.dump(settings, f, indent=2)
                return settings

    def get_timelog_calendar(self):
        target_name = self.settings['timelog_calendar_name']
        output = None
        cals_result = self.gcs.calendarList().list().execute()
        with open(tgc('all_calendars.json'), 'w') as f:
            json.dump(cals_result, f)

        for calendar in cals_result['items']:
            if calendar['summary'] == target_name:
                output = calendar
                break

        return calendar

    def get_timelog_events(self):
        if not self.tlc:
            return None
        events = self.gcs.events().list(calendarId=self.tlc['id']).execute()
        with open(tgc('timelog_events.json'), 'w') as f:
            json.dump(events, f)
        return events

    def execute(self):
        print("Getting timelog calendar")
        self.tlc = self.get_timelog_calendar()
        if not self.tlc:
            print("Timelog calendar not found")
            print("Check your settings and try again")
            return

        print("Getting events")
        events = self.get_timelog_events()

        # For testing purposes
        print("Generating HTML file")
        InvoicrModel.test_generate_files()
        print("Generating PDF file")
        InvoicrModel.test_print_to_pdf()

    @classmethod
    def test_generate_files(cls):
        ib = InvoiceBuilder()
        items = [{'title': 'Item 1', 'hours': '0.5', 'price': '$8.00'},
                 {'title': 'Item 2', 'hours': '10', 'price': '$160.00'},
                 {'title': 'Item 3', 'hours': '0.25', 'price': '$4.00'}]
        ib.generate_files(items)

    @classmethod
    def test_print_to_pdf(cls):
        print_to_pdf(InvoiceBuilder.get_html_filename(), tgc('invoice.pdf'))


def main():
    print("Setting Invoicr up")
    im = InvoicrModel()
    im.execute()
    print("Execution finished")


if __name__ == '__main__':
    main()
