"""Test the repositories commands."""

from typing import Any
from unittest.mock import Mock

import pytest
from click.testing import CliRunner
from github import Github
from github.Repository import Repository
from pytest_mock import MockerFixture

from my_github_toolbox.adapters.commands.repositories_commands import cli
from my_github_toolbox.core.configuration import GitHubConfiguration


MOCK_BASE_PACKAGE = "my_github_toolbox.adapters.commands.repositories_commands"


@pytest.fixture
def fake_github_configuration() -> GitHubConfiguration:
    """Mock the list command."""
    return GitHubConfiguration(access_token="fake_access_token")  # no


@pytest.fixture
def mock_github_client(mocker: MockerFixture) -> Mock:
    """Mock the list command."""
    return mocker.patch(MOCK_BASE_PACKAGE + ".Github", return_value=Mock(spec=Github))


@pytest.fixture
def mock_read_github_config(
    mocker: MockerFixture, fake_github_configuration: GitHubConfiguration
) -> Mock:
    """Mock the list command."""
    return mocker.patch(
        MOCK_BASE_PACKAGE + ".read_github_config",
        return_value=fake_github_configuration,
    )


FAKE_GITHUB_REPOSITORIES = [
    Mock(name="repo1", spec=Repository),
    Mock(name="repo2", spec=Repository),
]


@pytest.fixture
def mock_list_repositories(mocker: MockerFixture) -> Mock:
    """Mock the list command."""
    return mocker.patch(
        MOCK_BASE_PACKAGE + ".list_repositories", return_value=FAKE_GITHUB_REPOSITORIES
    )


def fake_serializer(data: Any) -> str:
    return str(data)


@pytest.fixture
def mock_get_serializer(mocker: MockerFixture) -> Mock:
    """Mock the list command."""
    return mocker.patch(MOCK_BASE_PACKAGE + ".get_serializer")


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_list_repositories_command(
    runner: CliRunner,
    mock_list_repositories: Mock,
    mock_github_client: Mock,
    mock_read_github_config: Mock,
    mock_get_serializer: Mock,
) -> None:
    mock_get_serializer.return_value = fake_serializer

    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0

    for repository in FAKE_GITHUB_REPOSITORIES:
        assert str(repository.name) in result.output

    mock_list_repositories.assert_called_once_with(mock_github_client.return_value)
