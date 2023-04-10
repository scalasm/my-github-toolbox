"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """My Github Toolbox."""


if __name__ == "__main__":
    main(prog_name="my-github-toolbox")  # pragma: no cover
