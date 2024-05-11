DESTDIR ?= $(error DESTDIR is not set)

default: $(DESTDIR)/.github/auto-label.yaml
default: $(DESTDIR)/.github/blunderbuss.yml
default: $(DESTDIR)/.github/renovate.json
default: $(DESTDIR)/.github/sync-repo-settings.yaml
default: $(DESTDIR)/.pre-commit-config.yaml
default: deprecated
default: github
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

github: github.sh
	bash "$<" "$(OWNER)/$(REPO)"

pre-commit:
	- pre-commit install --install-hooks
