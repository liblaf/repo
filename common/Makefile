DEST_DIR ?= $(error DEST_DIR is not set)

default: $(DEST_DIR)/.github/auto-label.yaml
default: $(DEST_DIR)/.github/blunderbuss.yml
default: $(DEST_DIR)/.github/sync-repo-settings.yaml
default: $(DEST_DIR)/.pre-commit-config.yaml
default: deprecated
default: github

#####################
# Auxiliary Targets #
#####################

$(DEST_DIR)/.pre-commit-config.yaml: .pre-commit-config.yaml
	cd "$(@D)" && pch filter --output="$(abspath $@)" "$(abspath $<)"

$(DEST_DIR)/%: %
	@ $(INSTALL) "$<" "$@"

deprecated:
	@ rm --verbose "$(DEST_DIR)/.github/workflows/merge.yaml"
	@ rm --verbose "$(DEST_DIR)/.github/workflows/pre-commit.yaml"
	@ rm --verbose "$(DEST_DIR)/.github/workflows/template.yaml"

github: github.sh
	bash "$<" "$(OWNER)/$(REPO)"
