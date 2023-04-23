"""Units tests for the core configuration module."""

import json
from pathlib import PosixPath

import pytest

from my_github_toolbox.core.configuration import GitHubConfiguration
from my_github_toolbox.core.configuration import GitHubConfigurationError
from my_github_toolbox.core.configuration import read_github_config


@pytest.fixture
def config_file(tmp_path: PosixPath) -> str:
    config = {"access_token": "my_access_token"}
    config_path: PosixPath = tmp_path / "config.json"

    with open(config_path, "w") as f:
        json.dump(config, f)

    return str(config_path)


def test_read_github_config(config_file: str) -> None:
    config = read_github_config(config_file)

    assert isinstance(config, GitHubConfiguration)
    assert config.access_token == "my_access_token"


def test_read_github_config_missing_file() -> None:
    with pytest.raises(GitHubConfigurationError) as exc_info:
        read_github_config("nonexistent_file.json")

    assert "Configuration file nonexistent_file.json not found" in str(exc_info.value)


def test_read_github_config_invalid_json(tmp_path: PosixPath) -> None:
    config_path = str(tmp_path / "invalid.json")
    with open(config_path, "w") as f:
        f.write("not a valid json")

    with pytest.raises(GitHubConfigurationError) as exc_info:
        read_github_config(config_path)

    assert "Configuration file" in str(exc_info.value)
    assert "is not a valid JSON" in str(exc_info.value)
