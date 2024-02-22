NAME := repo
HOST != rustc --version --verbose | sed --quiet 's/host: //p'

default: check clippy fmt

check:
	cargo check

clippy:
	cargo clippy --fix --allow-dirty --allow-staged

.PHONY: dist
dist: dist/$(NAME)-$(HOST)

fmt: cargo-fmt fmt/Cargo.toml

#####################
# Auxiliary Targets #
#####################

ALWAYS:

cargo-fmt:
	cargo fmt

dist/%-$(HOST): target/release/% ALWAYS
	cargo build --release
	@ install -D --no-target-directory --verbose "$<" "$@"

fmt/Cargo.toml: Cargo.toml
	toml-sort --in-place --all "$<"
	taplo format "$<"
