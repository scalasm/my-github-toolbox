"""Application configuration management."""
# Read a json from a configuration file

import json
import logging
import os
from dataclasses import dataclass


def setup_logging_config() -> None:
    """Setup logging configuration."""
    logging.basicConfig(level=logging.INFO)  # pragma: no cover


@dataclass
class GitHubConfiguration:
    """GitHub configuration."""

    access_token: str


class GitHubConfigurationError(Exception):
    """GitHub configuration error."""

    pass


DEFAULT_CONFIGURATION_FILE = os.path.expanduser("~/.github_config.json")


def read_github_config(
    configuration_file: str = DEFAULT_CONFIGURATION_FILE,
) -> GitHubConfiguration:
    """Read GitHub configuration from a JSON file.

    Args:
        configuration_file: Path to the configuration file.

    Returns:
        GitHub configuration.

    Raises:
        GitHubConfigurationError: If the configuration file is not found or
            is not a valid JSON.
    """
    try:
        property_dict = json.loads(open(configuration_file).read())
        return GitHubConfiguration(**property_dict)
    except FileNotFoundError as e:
        raise GitHubConfigurationError(
            f"Configuration file {configuration_file} not found"
        ) from e
    except json.decoder.JSONDecodeError as e:
        raise GitHubConfigurationError(
            f"Configuration file {configuration_file} is not a valid JSON"
        ) from e
