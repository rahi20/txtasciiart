from setuptools import setup

with open("README.md", "r") as readme_file :
    README = readme_file.read()

setup(
    name="txtasciiart",
    version="0.1.0",
    description="Print ASCII Art",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rahi20/txtasciiart",
    author="rahi20",
    author_email="largorahima@gmail.com",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GPL-3.0 License",
        "Programming Language :: Python :: 3",
    ],
    py_modules=["txtasciiart"],
    entry_points={"console_scripts": ["txtasciiart=txtasciiart:main"]}
)