SET var=%cd%

IF EXIST "%var%\venv" (
	cd venv/Scripts/
	call activate.bat
	cd ../../
	call jupyter notebook
) ELSE (
	call python3 -m venv venv
	cd venv/Scripts/
	call activate.bat
	cd ../../
	call python -m pip install --upgrade pip
	pip install -r "%var%\requirements.txt"
	call jupyter notebook
)

PAUSE