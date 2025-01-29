import typer
from rich import print as rprint
# import wat

from github import get_all_user_repositories


app = typer.Typer()
repo_app = typer.Typer()
app.add_typer(repo_app, name="repo")


@repo_app.command(name="list", help="list user repository")
def list_repos(user: str = typer.Option(..., "--user", "-u", help="github user name")):
    repos = get_all_user_repositories(username=user)
    rprint(repos)
    rprint(f'num public repos: {len(repos)}')
    # rprint(f'repos type: {type(repos)}, repos element type: {type(repos[0])}')
    # wout = wat.short / ['repos']
    # rprint(wout)


if __name__ == "__main__":
    app()
