#! /usr/bin/env python3
# coding: utf-8

import analysis.csv as c_an
import analysis.xml as x_an

import argparse
import logging as lg

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import re

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of the file to analyse. Is it CSV or XML ?""")
    parser.add_argument("-d", "--datafile", help="""Name of File to analyse""")
    parser.add_argument("-v", "--verbose", action='store_true', help="""Get Debugging and all log messages""")
    parser.add_argument("-b", "--by_party", action='store_true', help="""Get information by political party""")
    parser.add_argument("-i", "--info", action='store_true', help="""Get total number of MPs""")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    if args.verbose:
        lg.basicConfig(level=lg.DEBUG)
    try:
        datafile = args.datafile
        if datafile == None:
            raise Warning("You must indicate a file as parameter !")
    except Warning as e:
        lg.warning("You must indicate a datafile sir !!!")
    else:
        e = re.search(r'^.+\.(\D{3})$', args.datafile)
        extension = e.group(1)
        try:
            if extension == 'xml':
                x_an.launch_analysis(args.datafile)
            elif extension == 'csv' or args.extension == 'csv':
                c_an.launch_analysis(args.datafile, args.by_party, args.info)
            elif args.extension == 'xml':
                x_an.launch_analysis(args.datafile)
            else:
                raise Warning("Extension of file can't be treated now")
        except Warning as e:
            lg.warning(e)
        except FileNotFoundError as e:
            lg.critical("File " + args.datafile + " not found ! Original message = ", e)
        finally:
            lg.info("################## Analyse is over ##################")
    
