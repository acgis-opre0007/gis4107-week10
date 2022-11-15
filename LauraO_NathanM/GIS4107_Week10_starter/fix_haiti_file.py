#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
#
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      David Viljoen
#
# Created:     09/11/2021
#-------------------------------------------------------------------------------
import os
import csv

def fix_file(in_csv, out_csv, admin_code_column_index = 0):
    """in_csv = file where a column contains a admin_code that needs fixing.
                That is, the 5th character in admin_code needs to be removed.
       out_csv = file with same contents as in_csv with fixed admin_code
       admin_code_column_index = 0-based index of column containing the
                                 admin_code
    """
    #haiti_folder = gis4107_week_10_starter
    haiti_folder = os.path.dirname(os.path.abspath(__file__))
    in_csv = os.path.join(haiti_folder, "data", "haiti_admin_names.csv")
    out_csv = os.path.join(haiti_folder, "data", "haiti_admin_names_fixed.csv")
    with open(in_csv) as f:
        reader = csv.reader(f)
        header = next(reader)
        admin_code_column_index = header[0]
        for admin_code in admin_code_column_index:
            _fix_code(admin_code)
            fixed_code = _fix_code(admin_code)
            admin_code = fixed_code
            return admin_code        
    with open(out_csv, 'w', newline='') as newfile:
        writer = csv.writer(newfile, delimiter='\t')
        writer.writerow(header)
        for admin_code in header[0]:
            writer.writerow(admin_code)
            return admin_code

def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
       given HT12345-01, return "HT1245-01"""
    fixed_code = (admin_code[:4] + admin_code[5:])
    return fixed_code

























