.PHONY: validate register smoke phase0-verify joint-debug

CORE ?= ../web3-edu-platform-core
PLUGINS_DIR ?= ..

validate:
	@for m in plugins/*/plugin.manifest.yaml; do \
		echo "==> $$m"; \
		cd "$(CORE)" && MANIFEST="../global-social-edu-sandbox/$$m" make validate-plugin; \
	done

register:
	cd "$(CORE)" && make register-plugins PLUGINS_DIR="$(PLUGINS_DIR)"

smoke:
	bash scripts/verify-all.sh

phase0-verify:
	bash scripts/global-phase0-verify.sh

joint-debug:
	bash scripts/joint-debug-smoke.sh
