from repo.external.gh.release import GhRelease


class Gh:
    def release(self, repo: str | None = None) -> GhRelease:
        return GhRelease(repo)
