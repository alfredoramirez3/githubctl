# 27. Add --sort_by Option
import os

import typer
from rich import print
from dotenv import load_dotenv
import jmespath

from github import get_all_user_repositories
from utils import print_beauty
from options import OutputOption
from utils import sort_by_key

if os.path.isfile(".env"):
    load_dotenv()


app = typer.Typer()
repo_app = typer.Typer()
app.add_typer(repo_app, name="repo")



@repo_app.command(name="list", help="list user repository")
def list_repos(user: str = typer.Option(..., "--user", "-u", help="github user name"),
               output: OutputOption = typer.Option(OutputOption.table, "--output", "-o", help="output format"),
               query: str = typer.Option(None, "--query", "-q", help="query with jmespath"),
               sort_by: str = typer.Option(None, "--sort_by", "-s", help="sort by key"),):
    repos = get_all_user_repositories(username=user)
    # print(repos)
    # print(f'num public repos: {len(repos)}')
    if query:
        repos = jmespath.search(query, repos)
    if sort_by:
        if sort_by.startswith('~'):
            reverse = True
            sort_by = sort_by[1:]
        else:
            reverse = False
        repos = sort_by_key(list_of_dict=repos, key=sort_by, reverse=reverse)
    print_beauty(repos, output=output)




if __name__ == "__main__":
    app()
