DEST_DIR ?= $(error DEST_DIR is not set)
OWNER    ?= $(error OWNER is not set)
REPO     ?= $(error REPO is not set)
INSTALL  := install -D --mode="u=rw,go=r" --no-target-directory --verbose

default: $(DEST_DIR)/.github/workflows/megalinter.yaml
default: $(DEST_DIR)/.jscpd.json
default: $(DEST_DIR)/.mega-linter.yaml
default: | $(DEST_DIR)/.cspell.json

#####################
# Auxiliary Targets #
#####################

$(DEST_DIR)/%: %
	@ $(INSTALL) "$<" "$@"
