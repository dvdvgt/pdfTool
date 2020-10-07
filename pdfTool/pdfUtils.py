#!/bin/python3
import PyPDF2 as pdf
import sys
import argparse
from . import parser

def join(input_files, output_file:):
    """
    Parameters
    ----------
    input_files: list
        list of filepaths of PDF files to merge.
    outputfile
        Path/name of the resulting PDF file.
    """
    input_streams = []
    try:
        for input_file in input_files:
            input_streams.append(input_file)
        writer = pdf.PdfFileWriter()
        for reader in map(pdf.PdfFileReader, input_streams):
            for n in range(reader.getNumPages()):
                writer.addPage(reader.getPage(n))
        writer.write(output_file)
    finally:
        for f in input_streams:
            f.close()

def extract(input_file, output_file, pages: list):   
    """
    Parameters
    ----------
    input_file
        File from which to extract certain pages.
    output_file
        PDF file containing the extracted pages.
    """ 
    try:
        writer = pdf.PdfFileWriter()
        reader = pdf.PdfFileReader(input_file)
        for n in pages:
            writer.addPage(reader.getPage(n))
        writer.write(output_file)
    finally:
        input_file.close()