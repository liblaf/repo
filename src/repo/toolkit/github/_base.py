import githubkit
from githubkit.versions.rest import RestVersionSwitcher


class GitHubBase:
    owner: str
    repo: str
    _gh: githubkit.GitHub

    def __init__(self, repo: str) -> None:
        self._gh = githubkit.GitHub(githubkit.ActionAuthStrategy())
        self.owner, _, self.repo = repo.partition("/")

    @property
    def rest(self) -> RestVersionSwitcher:
        return self._gh.rest
