"""GitHub Repositories use cases."""

from github import Github
from github.Repository import Repository


def list_repositories(github_client: Github) -> list[Repository]:
    """List all accessible GitHub repositories for the current user.

    Args:
        github_client: GitHub client.

    Returns:
        List of GitHub repositories.
    """
    return [repository for repository in github_client.get_user().get_repos()]
