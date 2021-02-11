# -*- mode: python ; coding: utf-8 -*-
from kivymd import hooks_path
from kivy_deps import sdl2, glew
block_cipher = None


a = Analysis(['desktop\\main.py'],
             pathex=['D:\\GIT\\indicadores'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[hooks_path],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='teste',
          debug=False,
          bootloader_ignore_signals=False,
          upx=True,
          console=False,
          strip=False,
          upx_exclude=[],
          )
