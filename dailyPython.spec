# -*- mode: python -*-

block_cipher = None


a = Analysis(['dailyPython.py'],
             pathex=['D:\\Programs\\Python\\Python36-32\\Lib\\site-packages', 'C:\\Users\\chuyuting\\AppData\\Local\\Microsoft\\OneDrive\\18.044.0301.0006', 'D:\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'D:\\python\\daily'],
             binaries=[],
             datas=[('dailyPython.html', '.')],
             hiddenimports=['queue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='dailyPython',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='dailyPython')
