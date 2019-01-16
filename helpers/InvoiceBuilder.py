import os
import os.path
from jinja2 import Environment, Template, PackageLoader, select_autoescape

class InvoiceBuilder:
    PKG_NAME = 'invoicr'
    TEMPL_DIR = 'default_assets/invoice_template'
    TEMPL_HTML_NAME = 'invoice.html'
    TEMPL_CSS_NAME = 'invoice.css'
    OUTPUT_DIR = 'output'
    OUTPUT_NAME = 'generated_invoice'

    def __init__(self):
        self.env = Environment(
            loader=PackageLoader(self.PKG_NAME, self.TEMPL_DIR),
            autoescape=select_autoescape(['html', 'xml']))
        self.inv_templ = self.env.get_template(self.TEMPL_HTML_NAME)
        if not os.path.exists(self.OUTPUT_DIR):
            os.makedirs(self.OUTPUT_DIR)

    def build_html(self, items: dict) -> str:
        return self.inv_templ.render(items=items, title=self.OUTPUT_NAME)

    def generate_files(self, items: dict) -> None:
        html = self.build_html(items)

        html_fname = '{}/{}.html'.format(self.OUTPUT_DIR, self.OUTPUT_NAME)
        with open(html_fname, 'w') as html_file:
            html_file.write(html)

        css_in = '{}/{}'.format(self.TEMPL_DIR, self.TEMPL_CSS_NAME)
        css_out = '{}/{}.css'.format(self.OUTPUT_DIR, self.OUTPUT_NAME)
        with open(css_in) as css_file_in:
            with open(css_out, 'w') as css_file_out:
                css_file_out.writelines(css_file_in.readlines())
    
    @classmethod
    def get_html_filename(cls):
        return '{}/{}.html'.format(cls.OUTPUT_DIR, cls.OUTPUT_NAME)

