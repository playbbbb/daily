# daily
日报
D:\Programs\Python\Python36-32\Scripts\pyinstaller.exe
C:\Users\chuyuting\AppData\Local\Microsoft\OneDrive\18.044.0301.0006
D:\python\one\scrapyspider\venv\Lib\site-packages
D:\Programs\Python\Python36-32\Scripts\pyinstaller.exe -p D:\python\one\scrapyspider\venv\Lib\site-packages  --add-data="dailyPython.html;dailyPython.html"  -F  dailyPython.py
D:\Programs\Python\Python36-32\Scripts\pyinstaller.exe -p D:\python\one\scrapyspider\venv\Lib\site-packages;D:\Programs\Python\Python36-32\Lib  --add-data="dailyPython.html;."  --onedir  dailyPython.py
D:\Programs\Python\Python36-32\Scripts\pyinstaller.exe -p D:\python\one\scrapyspider\venv\Lib\site-packages;C:\Users\chuyuting\AppData\Local\Microsoft\OneDrive\18.044.0301.0006  --add-data="dailyPython.html;." --hidden-import=queue --path D:\python\one\scrapyspider\venv\Lib\site-packages\PyQt5\Qt\bin  --clean -c  dailyPython.py
D:\Programs\Python\Python36-32\Scripts\pyinstaller.exe -p D:\Programs\Python\Python36-32\Lib\site-packages;C:\Users\chuyuting\AppData\Local\Microsoft\OneDrive\18.044.0301.0006  --add-data="dailyPython.html;." --hidden-import=queue --path D:\Programs\Python\Python36-32\Lib\site-packages\PyQt5\Qt\bin  --clean -c  dailyPython.py

打包后还有问题，暂未能解决
D:\python\daily\dist\dailyPython>dailyPython
filename D:\python\daily\dist\dailyPython\PyQt5.Qt.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.Qt.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtCore.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtCore.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtCore.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtGui.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtGui.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtGui.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtNetwork.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtNetwork.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtNetwork.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtWidgets.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtWidgets.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtWidgets.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtPrintSupport.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtPrintSupport.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtPrintSupport.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtWebChannel.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtWebChannel.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtWebChannel.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtWebEngineCore.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtWebEngineCore.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtWebEngineCore.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtWebEngineWidgets.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtWebEngineWidgets.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtWebEngineWidgets.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtCore.cp36-win32.pyd
filename D:\python\daily\dist\dailyPython\PyQt5.QtCore.pyd
ImportError:: D:\python\daily\dist\dailyPython\PyQt5.QtCore.pyd
Traceback (most recent call last):
  File "site-packages\PyInstaller\loader\rthooks\pyi_rth_qt5.py", line 61, in <module>
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 656, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 628, in _load_backward_compatible
KeyError: 'PyQt5.QtCore'
[11208] Failed to execute script pyi_rth_qt5
