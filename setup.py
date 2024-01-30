from setuptools import setup

setup(
    name="msd_common",
    version="0.0.1",
    author="msd",
    author_email="87383399+msd@users.noreply.github.com",
    description="Utility library",
    # license = "BSD",
    # keywords = "example documentation tutorial",
    install_requires=["requests", "brotli", "bs4", "lxml"],
    url="https://github.com/msd/py_common",
    packages=["msd_common"],
    long_description="Utility functions for http headers, downloading files"
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],
)
