import os
import os.path
import subprocess

#CHROME_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
CHROME_PATH = os.path.join(
    'C:\\', 'Program Files (x86)', 'Google', 'Chrome', 'Application', 'chrome.exe')
BAT_NAME = "print_to_pdf.bat"


def print_to_pdf(input_path: str, output_path: str, overwrite: bool = True) -> bool:
    html_abs = os.path.abspath(input_path)
    if not os.path.isfile(html_abs):
        return False

    pdf_abs = os.path.abspath(output_path)
    if os.path.isfile(pdf_abs):
        if not overwrite:
            return False
        os.remove(pdf_abs)

    args = ['"{}"'.format(CHROME_PATH),
            '--headless',
            '--disable-gpu',
            '--print-to-pdf="{}"'.format(pdf_abs),
            '--no-margins',
            '"file://{}"'.format(html_abs)]

    line = ' '.join(args)
    line = '{q}{l}{q}'.format(q='', l=line)

    with open(BAT_NAME, 'w') as bat:
        bat.write('@echo off\n')
        bat.write(line + '\n')
        bat.write('(goto) 2>nul & del "%~f0"')

    with open(os.devnull, 'w') as fnull:
        subprocess.call([BAT_NAME], stdout=fnull, stderr=fnull)

    return True
