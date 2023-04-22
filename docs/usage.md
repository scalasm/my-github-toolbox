# Usage

# Pre-requisites

Create the file `$HOME/.github_config.json` with the following structure

```json
{
    "access_token": "<YOUR GITHUB ACCESS TOKEN>"
}

where `access_token` contains your personal GitHub token with permissions for
accessing the GitHub repository metata (read-only - at this time we only collect
data, no changes will happen to your repositories!)

```

```{eval-rst}
.. click:: my_github_toolbox.__main__:main
    :prog: my-github-toolbox
    :nested: full
```
