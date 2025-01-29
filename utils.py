from typing import List
from options import OutputOption
import csv
import sys


def print_beauty(list_of_dict: List[dict], output: OutputOption):
    
    if output == OutputOption.csv:
        fieldnames = list_of_dict[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(list_of_dict)
        