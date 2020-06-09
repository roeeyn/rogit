from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

version = "1.3"

setup(
    name="rogit",
    version=version,
    license="MIT",
    description="This is a little git automation for lazy devs. Add, commit and push in one single command.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="roeeyn",
    author_email="rodrigo.medina.neri@gmail.com",
    url="https://github.com/roeeyn/rogit",
    download_url=f"https://github.com/roeeyn/rogit/releases/download/{version}/rogit-{version}.tar.gz",
    keywords=["git", "automation"],
    py_modules=["app"],
    install_requires=["Click",],
    classifiers=[
        "Development Status :: 5 - Production/Stable",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points="""
        [console_scripts]
        rogit=app:rogit
    """,
)
