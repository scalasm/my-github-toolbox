"""Test cases for the repositories use case."""

from unittest.mock import Mock

import pytest
from github import AuthenticatedUser
from github import Github
from github.Repository import Repository
from pytest_mock import MockerFixture

from my_github_toolbox.core.usecases.repositories import list_repositories


MOCK_BASE_PACKAGE = "my_github_toolbox.core.usecases.repositories"


STUB_GITHUB_REPOSITORIES = [Mock(spec=Repository), Mock(spec=Repository)]


@pytest.fixture
def mock_authenticated_user(mocker: MockerFixture) -> Mock:
    """Mock the list command."""
    return Mock(spec=AuthenticatedUser)


@pytest.fixture
def github_client(mocker: MockerFixture) -> Mock:
    """Mock the list command."""
    return mocker.patch(MOCK_BASE_PACKAGE + ".Github", return_value=Mock(spec=Github()))


def test_list_repositories(github_client: Mock, mock_authenticated_user: Mock) -> None:
    """Test that list_repositories returns a list of repositories."""
    github_client.get_user().get_repos.return_value = STUB_GITHUB_REPOSITORIES

    repos = list_repositories(github_client)
    assert isinstance(repos, list)
    assert all(isinstance(repo, Repository) for repo in repos)
