from typing import List
from options import OutputOption
import csv
import sys
from rich import print_json
import json
from rich.console import Console
from rich.table import Table

def print_beauty(list_of_dict: List[dict], output: OutputOption):
    
    if output == OutputOption.csv:
        fieldnames = list_of_dict[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(list_of_dict)
    elif output == OutputOption.json:
        print_json(json.dumps(list_of_dict))
    elif output == OutputOption.table:
        # table = Table(title="Star Wars Movies")
        table = Table()
        headers = list_of_dict[0].keys()
        for h in headers:
            table.add_column(str(h))
            # table.add_column("Released", justify="right", style="cyan", no_wrap=True)
            # table.add_column("Title", style="magenta")
            # table.add_column("Box Office", justify="right", style="green")
        for repo in list_of_dict:
            table.add_row(*[str(r) for r in repo.values()])
            # table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
            
        console = Console()
        console.print(table)
        
        
        