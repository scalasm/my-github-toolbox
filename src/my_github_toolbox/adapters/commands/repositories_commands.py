"""GitHub Commands."""
import logging

import click
from github import Github

from my_github_toolbox.adapters.commands.utilities import common_options
from my_github_toolbox.adapters.output_formatters import OutputFormat
from my_github_toolbox.adapters.output_formatters import get_serializer
from my_github_toolbox.core.configuration import read_github_config
from my_github_toolbox.core.usecases.repositories import list_repositories


@click.group(name="repositories", help="Repositories commands.")
@click.pass_context
def cli(_: click.Context) -> None:
    """Repositories commands."""
    pass


@cli.command(name="list", help="List GitHub repositories.")
@common_options
def list_repositories_command(ctx: click.Context, output_format: OutputFormat) -> None:
    """List GitHub repositories.

    Args:
        ctx: Click context object (unused)
        output_format: Output format to use for command output.
    """
    logging.debug("Listing GitHub repositories...")

    # TODO Pass this through the context object
    config = read_github_config()
    github_client = Github(config.access_token)

    repositories = list_repositories(github_client)

    repository_names: list[str] = [repository.name for repository in repositories]

    logging.debug(f"Found {len(repositories)} repositories.")
    click.echo(get_serializer(output_format)(repository_names))
