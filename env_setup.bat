@echo off
echo Creating virtual environment
python -m venv pyenv
echo Activating virtual environment
call pyenv\Scripts\Activate.bat
echo Updating pip
python -m pip install --upgrade pip
echo Installing dependencies
pip install -r requirements.txt
echo Environment is set up and ready to go