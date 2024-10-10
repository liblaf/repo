DESTDIR ?= $(error DESTDIR is not set)
OWNER   ?= $(error OWNER is not set)
REPO    ?= $(error REPO is not set)
INSTALL := install -D --mode="u=rw,go=r" --no-target-directory --verbose

default: $(DESTDIR)/.github/auto-label.yaml
default: $(DESTDIR)/.github/blunderbuss.yml
default: $(DESTDIR)/.github/renovate.json
default: $(DESTDIR)/.github/sync-repo-settings.yaml
default: $(DESTDIR)/.pre-commit-config.yaml
default: deprecated
default: github
default: label-sync
default: pre-commit

#####################
# Auxiliary Targets #
#####################

$(DESTDIR)/.pre-commit-config.yaml: .pre-commit-config.yaml
	@ $(INSTALL) "$<" "$@"
	cd "$(@D)" && pch filter

$(DESTDIR)/%: %
	@ $(INSTALL) "$<" "$@"

deprecated: RM := rm --force --verbose
deprecated:
	@ $(RM) "$(DESTDIR)/.github/dependabot.yaml"
	@ $(RM) "$(DESTDIR)/.github/workflows/dependabot.yaml"
	@ $(RM) "$(DESTDIR)/.github/workflows/merge.yaml"
	@ $(RM) "$(DESTDIR)/.github/workflows/pre-commit.yaml"
	@ $(RM) "$(DESTDIR)/.github/workflows/stale.yaml"
	@ $(RM) "$(DESTDIR)/.github/workflows/template.yaml"

github: scripts/github.sh
	@ bash "$<" "$(OWNER)/$(REPO)"

label-sync: scripts/label-sync.sh
	@ bash "$<" "$(OWNER)/$(REPO)"

pre-commit:
	- pre-commit install --install-hooks
