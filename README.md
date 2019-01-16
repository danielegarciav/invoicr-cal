# Invoicr

Script to generate PDF invoices from Google Calendar events

## Requirements

- Python 3.5 or greater
- The [pip](https://pypi.python.org/pypi/pip) package management tool
- A Google account with Google Calendar enabled
- Google Chrome 59 or greater

## Setup

### Google API credentials setup

Invoicr uses a file located at `gcal_credentials/credentials.json` to authenticate your API credentials. You may create and download your own API credentials by visiting Google's [Google Calendar API Python Quickstart](https://developers.google.com/calendar/quickstart/python) webpage and following the first step (_"Step 1: Turn on the Google Calendar API"_).

Ensure your `credentials.json` file is under the `gcal_credentials` directory.

### Environment setup

#### Windows

Run `env_setup.bat`. Remember to activate the environment using `pyenv\Scripts\Activate.bat`

#### Other OS

1. Create a virtual environment

```bash
python3 -m venv pyenv
```

2. Activate the environment

```bash
source pyenv/scripts/activate
```

3. Update pip (optional)

```bash
python3 -m pip install --upgrade pip
```

4. Install dependencies

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
# Windows
python invoicr.py

# Other OS
python3 invoicr.py
```

## Notice

Invoicr is a work in progress. More documentation is planned.

PDF generation is only implemented for Windows at the moment (in file `helpers/ChromePrintToPDF.py`).