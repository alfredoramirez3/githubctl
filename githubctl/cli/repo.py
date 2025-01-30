import typer
import jmespath


from githubctl.options import OutputOption
from githubctl.github import get_all_user_repositories
from githubctl.utils import print_beauty, sort_by_key


repo_app = typer.Typer()


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
            sort_by = sort_by[1:].split(",")
        else:
            reverse = False
        repos = sort_by_key(list_of_dict=repos, key_list=sort_by, reverse=reverse)
    print_beauty(repos, output=output)