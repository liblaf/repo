DEST_DIR ?= $(error DEST_DIR is not set)
OWNER    ?= $(error OWNER is not set)
REPO     ?= $(error REPO is not set)
INSTALL  := install -D --mode="u=rw,go=r" --no-target-directory --verbose

default: $(DEST_DIR)/.github/auto-label.yaml
default: $(DEST_DIR)/.github/blunderbuss.yml
default: $(DEST_DIR)/.github/renovate.json
default: $(DEST_DIR)/.github/sync-repo-settings.yaml
default: $(DEST_DIR)/.pre-commit-config.yaml
default: deprecated
default: github
default: label-sync
default: pre-commit

#####################
# Auxiliary Targets #
#####################

$(DEST_DIR)/.pre-commit-config.yaml: .pre-commit-config.yaml
	@ $(INSTALL) "$<" "$@"
	cd "$(@D)" && pch filter

$(DEST_DIR)/%: %
	@ $(INSTALL) "$<" "$@"

deprecated: RM := rm --force --verbose
deprecated:
	@ $(RM) "$(DEST_DIR)/.github/dependabot.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/dependabot.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/merge.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/pre-commit.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/stale.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/template.yaml"

github: scripts/github.sh
	@ bash "$<" "$(OWNER)/$(REPO)"

label-sync: scripts/label-sync.sh
	@ bash "$<" "$(OWNER)/$(REPO)"

pre-commit:
	- pre-commit install --install-hooks
