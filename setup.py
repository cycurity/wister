import setuptools as st
import os

exec(open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "wister/version.py")).read())
readme = open("README.md").read()

st.setup(
    include_package_data=True,
    name="wister",
    keywords=["wister", "wordlist", "hacking", "cybersecurity", "bruteforcing"],
    version=__version__,
    description="A wordlist generator tool, that allows you to supply a set of words, giving you the possibility to craft multiple variations from the given words, creating a unique and ideal wordlist to use regarding a specific target.",
    url="https://github.com/cycurity/wister",
    author="Cycurity",
    author_email="cycurity@tutanota.com",
    long_description=readme + "\n\n",
    long_description_content_type="text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Natural Language :: English",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Security",
        "Topic :: Utilities"
    ],
    package_data={"": ["*.dic"]},
    packages=st.find_packages(),
    entry_points={"console_scripts": ["wister=wister.wister:main"]}
)