.PHONY: scaffold setups push-all list

scaffold:
	python3 scripts/scaffold_cisco_workshop.py

setups:
	chmod +x scripts/build-track-setups.sh scripts/es3-setup-base.sh scripts/es3-setup-seed.sh
	./scripts/build-track-setups.sh

list:
	@ls -1 tracks/

push-all: setups
	@for t in tracks/cisco-w*; do \
	  echo "Push $$t: cd $$t && instruqt track push --force"; \
	done
