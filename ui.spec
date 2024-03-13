# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ui.py'],
    pathex=["F:\\unet_42_light\\model"],
    binaries=[("F:\\unet_42_light\\weights\\best_model.pth","weights")],
    datas=[
        ("F:\\unet_42_light\\edges","edges"),
        ("F:\\unet_42_light\\model","model"),
        ("F:\\unet_42_light\\images","images"),
        ("F:\\unet_42_light\\results_windows","results_windows"),
        ("F:\\unet_42_light\\utils","utils")
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ui',
)
