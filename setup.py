from setuptools import setup


setup(
    name="targs",
    version="0.0.1",
    install_requires=['wheel'],
    py_modules=['targs'],
    entry_points={
        "console_scripts": [
            "targs = targs:main"
        ]
    }
)
