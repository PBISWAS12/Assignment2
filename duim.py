#!/usr/bin/env python3

import subprocess, sys
import os
import argparse



'''
OPS435 Assignment 2 - Summer 2021
Program: duim.py 
Author: "Prangon Biswas"
The python code in this file (duim.py) is original work written by
"Prangon Biswas". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 27th july 2021
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2021")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    # add argument for "target". set number of args to 1.
    args = parser.parse_args()


def percent_to_graph(percent, total_chars):
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    if 0 <= percent <= 100:
            numbertoprint - int((percent/100) * total chars)
            numberofspaces - int(total_chars - numbertoprint)
            return (("'" + "#" * numbertoprint) + (" " * numberofspaces) + "'")
    else:
            print("Usage: Percentage value has to be between 0 and 100")
    

def call_du_sub(location):
    "use subprocess to call `du -d 1 + location`, rtrn raw list"
    pass

def create_dir_dict(raw_dat):
    "get list from du_sub, return dict {'directory': 0} where 0 is size"
    pass


if __name__ == "__main__":
    pass
