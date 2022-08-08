from setuptools import setup
from pathlib import Path

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname: str) -> str:
    return (Path(__file__).parent / fname).read_text(encoding="utf-8")

setup(
    name = "msd_common",
    version = "0.0.1",
    author = "msd",
    author_email = "87383399+msd@users.noreply.github.com",
    description = "common functions and classes used by msd",
    # license = "BSD",
    # keywords = "example documentation tutorial",
    url = "https://github.com/msd/my_common",
    packages=["msd_common"],
    long_description=read('readme')
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],
)