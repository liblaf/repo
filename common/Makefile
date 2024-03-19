DEST_DIR ?= $(error DEST_DIR is not set)

default: $(DEST_DIR)/.github/auto-label.yaml
default: $(DEST_DIR)/.github/blunderbuss.yml
default: $(DEST_DIR)/.github/renovate.json
default: $(DEST_DIR)/.github/sync-repo-settings.yaml
default: $(DEST_DIR)/.github/workflows/stale.yaml
default: $(DEST_DIR)/.pre-commit-config.yaml
default: deprecated
default: github
default: pre-commit

#####################
# Auxiliary Targets #
#####################

$(DEST_DIR)/.pre-commit-config.yaml: .pre-commit-config.yaml
	@ install -D --mode="u=rw,go=r" --no-target-directory --verbose "$<" "$@"
	cd "$(@D)" && pch filter

$(DEST_DIR)/%: %
	@ $(INSTALL) "$<" "$@"

deprecated: RM := rm --force --verbose
deprecated:
	@ $(RM) "$(DEST_DIR)/.github/dependabot.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/dependabot.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/merge.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/pre-commit.yaml"
	@ $(RM) "$(DEST_DIR)/.github/workflows/template.yaml"

github: github.sh
	bash "$<" "$(OWNER)/$(REPO)"

pre-commit:
	- pre-commit install --install-hooks
