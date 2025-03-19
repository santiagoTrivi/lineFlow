# Installation

```
pip install pyqt5

pip install pyqt5-tools

pip reportlab

pip install numpy
```

# Steps to develop this calculator

1. Script to iu python file

```
pyuic5 -x lineFlow.ui -o lineFlow.py

pyuic5 -x Generator.ui -o Generator.py
```

2. To get images ready

```
pyrcc5 ./icons/logo.qrc -o ./logo_rc.py
```

3. To run the app

```
python main.py
```

# Make executable

```
pyinstaller -F main.py --noconsole --icon wind.ico
```
