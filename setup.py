from distutils.core import setup

setup(
    # Application name:
    name="MYOB Pre-Interview Test",

    # Version number (initial):
    version="1.0",

    # Application author details:
    author="Kunal Nanda",
    author_email="kunal.nanda@outlook.com",

    # Packages
    packages=["app"],

    # Include additional files into the package
    include_package_data=True,

    # license="LICENSE.txt",
    description="Package for test Hello World python app using REST APIs for MYOB test.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
        "flask-restful",
        "healthcheck"
    ],
)