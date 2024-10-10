DEST_DIR ?= $(error DEST_DIR is not set)
OWNER    ?= $(error OWNER is not set)
REPO     ?= $(error REPO is not set)
INSTALL  := install -D --mode="u=rw,go=r" --no-target-directory --verbose

NO_OVERWRITE += $(DEST_DIR)/.cspell.json
NO_OVERWRITE += $(DEST_DIR)/.mega-linter.yaml

default: $(DEST_DIR)/.github/megalinter/.checkov.yml
default: $(DEST_DIR)/.github/megalinter/.devskim.json
default: $(DEST_DIR)/.github/megalinter/kics.config
default: $(DEST_DIR)/.github/workflows/megalinter.yaml
default: $(NO_OVERWRITE)

#####################
# Auxiliary Targets #
#####################

$(DEST_DIR)/%: %
	@ $(INSTALL) "$<" "$@"

$(NO_OVERWRITE): $(DEST_DIR)/%: %
	@ test -f "$@" || $(INSTALL) "$<" "$@"
