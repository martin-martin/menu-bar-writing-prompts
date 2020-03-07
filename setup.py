from setuptools import setup


APP = ['prompt.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'memo.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='Writing Prompts',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)
