#!/usr/bin/env python

"""
Arraytolatex: As from the name, the purpose of this tool is to convery numpy's array into a valid latex code. 
"""
import os
import warnings
import numpy as np
import pandas
import csv
import re

def get_type(data):
    return type(data)


def tolatex(array, header, caption="My table", label="table_something", output_file=False):
    """
    This function converts numpy ndarray into a valid latex table.
    """
    string_array = np.array2string(array)[2:][:-2] # I use this for tables items
    regex_space_bracket = r"\s+?\]"
    regex_1 = "\]\n "
    regex_2 = r"\[|\]"
    regex_3 = "(-?\d*\.?\d+)\s+"
    repl_1 = r"\\\\\n"
    repl_2 = r""
    repl_3 = r"\1 & "
    repl_space_bracket = r"\]"
    
    a_string = re.sub(regex_1, repl_1, string_array) # I use this to compute the largest number length
    string_table_items = a_string.replace("\n", "").split(" ")
    length_table_items = max(len(str(i)) for i in string_table_items)
    
    template = """\\begin{table}[]
      \\caption{%s}
      \\label{%s}
      \\begin{tabular}{@{%s}@{}}
      \\toprule
    """ % (caption, label, len(header) * "l")
    length_header_items = max(len(i) for i in header)
    padding = " " * (max(length_table_items, length_header_items) // 2 - 2) + "&" + " " * (max(length_table_items, length_header_items) // 2 - 2)
    midrule = "  " + padding.join(header) + r"\\" + "\n" + " "* (max(length_table_items, length_header_items) // 2 + 2) + "\midrule" + "\n"
    template += midrule
    rows, columns = array.shape
    if columns != len(header):
        warnings.warn("The length of header doesn't match with the length of \
        the column. We will placeholder it with an empty string.")
    for regex_repl in zip((regex_space_bracket, regex_1, regex_2, regex_3), (repl_space_bracket, repl_1, repl_2, repl_3)):
        string_array = re.sub(regex_repl[0], regex_repl[1], string_array.rstrip())
        
    string_array = string_array + "\\\\\n" + "    \\bottomrule" + "\n" + "    \\end{tabular}" + "\n" + "\\end{table}"
    
    if output_file:
        curdir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(curdir, output_file), 'w') as f:
            f.writelines(template + string_array)
    else:
        return template + string_array
        