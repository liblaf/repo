export DEST_DIR ?= $(CURDIR)

export OWNER != git -C "$(DEST_DIR)" remote get-url origin | sed --regexp-extended 's|\.git$$||;s|.*github.com/([^/]+)/([^/]+)|\1|'
export REPO  != git -C "$(DEST_DIR)" remote get-url origin | sed --regexp-extended 's|\.git$$||;s|.*github.com/([^/]+)/([^/]+)|\2|'

export INSTALL := install -D --mode="u=rw,go=r" --no-target-directory --verbose

default:

define template
ifeq ($$(shell bash $(1)/detect.sh),true)
default: $(1)
.PHONY: $(1)
$(1):
	$(MAKE) --directory "$$@"
endif
endef
TEMPLATES := common
$(foreach t,$(TEMPLATES),$(eval $(call template,$(t))))
