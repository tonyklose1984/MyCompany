# -*- mode: python -*-

block_cipher = None


a = Analysis(['wxbot01.py'],
             pathex=['C:\\Users\\TonyHu\\PycharmProjects\\untitled\\Exciese'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='wxbot01',
          debug=False,
          strip=False,
          upx=True,
          console=True )
