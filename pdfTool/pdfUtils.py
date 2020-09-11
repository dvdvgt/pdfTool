#!/bin/python3
import PyPDF2 as pdf
import sys
import argparse
from . import parser

def join(input_files, output_file):
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
    try:
        writer = pdf.PdfFileWriter()
        reader = pdf.PdfFileReader(input_file)
        for n in pages:
            writer.addPage(reader.getPage(n))
        writer.write(output_file)
    finally:
        input_file.close()