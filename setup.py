from setuptools import setup

setup(
    name="rogit",
    version="1.0",
    license="MIT",
    description="This is a little git automation for lazy devs. Add, commit and push in one single command.",
    author="roeeyn",
    author_email="rodrigo.medina.neri@gmail.com",
    url="https://github.com/roeeyn/rogit",
    download_url="https://github.com/roeeyn/rogit/archive/v_01.tar.gz",
    keywords=["git", "automation"],
    py_modules=["app"],
    install_requires=["Click",],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
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
