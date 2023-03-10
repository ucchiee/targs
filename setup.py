from setuptools import setup, find_packages

DESCRIPTION = "targs: tmux + xargs"
NAME = "tmux_xargs"
AUTHOR = "Yusuke Uchida"
AUTHOR_EMAIL = "fantomyuu0623@gmail.com"
URL = "https://github.com/ucchiee/targs"
LICENSE = "MIT"
DOWNLOAD_URL = URL
VERSION = "0.0.8"
PYTHON_REQUIRES = ">=3.9"
KEYWORDS = "tmux xargs targs"
with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
PY_MODULES = ["targs"]
ENTRY_POINTS = {"console_scripts": ["targs = targs:main"]}

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    license=LICENSE,
    keywords=KEYWORDS,
    install_requires=[],
    packages=find_packages(),
    py_modules=PY_MODULES,
    entry_points=ENTRY_POINTS,
)
