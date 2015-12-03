from setuptools import setup, find_packages
from codecs import open
import os
from libmproxy import version

# Based on https://github.com/pypa/sampleproject/blob/master/setup.py
# and https://python-packaging-user-guide.readthedocs.org/

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

console_scripts = ["%s = libmproxy.main:%s" % (s, s) for s in ("mitmproxy", "mitmdump", "mitmweb")]

setup(
    name="mitmproxy",
    version=version.VERSION,
    description="An interactive, SSL-capable, man-in-the-middle HTTP proxy for penetration testers and software developers.",
    long_description=long_description,
    url="http://mitmproxy.org",
    author="Aldo Cortesi",
    author_email="aldo@corte.si",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Security",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Software Development :: Testing"
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': console_scripts
    },
    install_requires=[
        "netlib>=%s, <%s" % (version.MINORVERSION, version.NEXT_MINORVERSION),
        "pyasn1~=0.1.9",
        "tornado~=4.3.0",
        "configargparse~=0.10.0",
        "pyperclip~=1.5.22",
        "blinker~=1.4",
        "pyparsing~=2.0.5",
        "html2text~=2015.11.4",
        "construct~=2.5.2",
        "six~=1.10.0",
        "lxml~=3.4.4",
        "Pillow~=3.0.0",
        "watchdog~=0.8.3",
        "click~=6.2",
    ],
    extras_require={
        ':sys_platform == "win32"': [
            "pydivert~=0.0.7",
        ],
        ':sys_platform != "win32"': [
            "urwid~=1.3.1",
        ],
        ":python_version < '3.4'": [
            "enum34~=1.0.4",
        ],
        'dev': [
            "mock>=1.0.1",
            "pytest>=2.8.0",
            "pytest-xdist>=1.13.1",
            "pytest-cov>=2.1.0",
            "coveralls>=0.4.1",
            "pathod>=%s, <%s" % (version.MINORVERSION, version.NEXT_MINORVERSION),
            "sphinx>=1.3.1",
            "sphinx-autobuild>=0.5.2",
            "sphinxcontrib-documentedlist>=0.2",
        ],
        'contentviews': [
            "pyamf~=0.7.2",
            "protobuf~=2.6.1",
            "cssutils~=1.0.1",
        ],
        'examples': [
            "pytz~=2015.7",
            "harparser~=0.2",
            "beautifulsoup4~=4.4.1",
        ],
    }
)
