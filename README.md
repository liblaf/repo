# Repo

Repo Automation and Config Files

## Config Files

### Common

- [auto-label](https://github.com/googleapis/repo-automation-bots/tree/main/packages/auto-label)
  - `.github/auto-label.yaml`
- [blunderbuss](https://github.com/googleapis/repo-automation-bots/tree/main/packages/blunderbuss)
  - `.github/blunderbuss.yml`
- [pre-commit.ci](https://pre-commit.ci/)
  - `.pre-commit-config.yaml`
- [release-please](https://github.com/googleapis/repo-automation-bots/tree/main/packages/release-please)
  - `.github/release-please.yml`
  - `.release-please-manifest.json`
  - `release-please-config.json`
- [Renovate](https://docs.renovatebot.com/)
  - `.github/renovate.json`
- [sync-repo-settings](https://github.com/googleapis/repo-automation-bots/tree/main/packages/sync-repo-settings)
  - `.github/sync-repo-settings.yaml`

### latexindent

- [latexindent](https://latexindentpl.readthedocs.io/)
  - `.latexindent.yaml`

### Python

- [Ruff](https://docs.astral.sh/ruff/)
  - `.ruff.toml`
- [MyPy](https://mypy.readthedocs.io/en/stable/config_file.html)
  - `.mypy.ini`

## GitHub Apps

- [pre-commit.ci](https://github.com/apps/pre-commit-ci): a continuous integration service for the [pre-commit](https://pre-commit.com) framework
- [Repo Automation Bots](https://github.com/googleapis/repo-automation-bots): A collection of bots, based on [probot](https://github.com/probot/probot), for performing common maintenance tasks across the open-source repos managed by Google on GitHub.
  - [auto-label](https://github.com/apps/product-auto-label): Automatically labels issues and PRs with product, language, or directory based labels
  - [blunderbuss](https://github.com/apps/blunderbuss-gcf): Assigns issues and PRs randomly to a specific list of users
  - [conventional-commit-lint](https://github.com/apps/conventional-commit-lint-gcf): PR checker that ensures that the commit messages follow conventionalcommits.org style
  - [do-not-merge](https://github.com/apps/do-not-merge-gcf): PR checker that ensures the `do not merge` label is not present
  - [merge-on-green](https://github.com/apps/gcf-merge-on-green): Merge a pull-request when all required checks have passed
  - [release-please](https://github.com/apps/release-please): Proposes releases based on semantic version commits
  - [sync-repo-settings](https://github.com/apps/sync-repo-settings): Synchronize repository settings from a centralized config
