# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Application.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('WINQSB', 'WINQSB'),
        ('resources', 'resources')
    ],
    hiddenimports=['src.Common'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='x64_WinQSB安装程序',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='WinQSB_version_info.txt',
    icon=['resources\\img\\ui\\icon.ico'],
    optimize=0,
)