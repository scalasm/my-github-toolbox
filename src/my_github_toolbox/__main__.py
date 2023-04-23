"""Command-line interface."""
import click

from my_github_toolbox.adapters.commands.repositories_commands import (
    cli as repositories_cli,
)
from my_github_toolbox.core.configuration import setup_logging_config


@click.group(help="GitHub Toolbox CLI")
@click.version_option()
@click.pass_context
def main(ctx: click.Context) -> None:  # pragma: no cover
    """Command-line interface.

    Args:
        ctx: Click context object
    """
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)


main.add_command(repositories_cli)

if __name__ == "__main__":  # pragma: no cover
    setup_logging_config()

    main(prog_name="my-github-toolbox")
