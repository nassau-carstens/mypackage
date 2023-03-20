from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    license="MIT",
    description="EDSA example python package",
    long_description=open("readme.md").read(),
    install_requires=["numpy"],
    url="https://github.com/<username>/<package-name>",
    author="Nassau Carstens",
    author_email="nassaucarstens@gmail.com"
)
