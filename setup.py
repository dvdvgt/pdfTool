from setuptools import setup, find_packages
import os

with open('README.md', "r") as file:
    long_description = file.read()

setup(
    name='pdfTool',
    version='0.1',
    packages=find_packages(),
    author='David Voigt',
    author_email='David.Voigt1998@gmail.com',
    description='Command line application for manipulating PDF files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Xcal1bur/pdfTool',
    license='MIT',
    install_requires=['PyPDF2'],
    entry_points={'console_scripts': ['pdfTool = pdfTool.parser:main']},
)