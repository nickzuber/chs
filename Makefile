pprintf = @printf "\n\033[36m=-=-\033[39m \033[1m%s\033[0m \033[36m-=-=-=-=-=-=-=-=-=-=-=\033[39m 🚀\n" "$(1)"
p_update = @printf "\033[33m ↻\033[39m \033[89m%s\033[39m\n" "$(1)"
p_add = @printf "\033[32m ↗\033[39m \033[89m%s\033[39m\n" "$(1)"
p_remove = @printf "\033[31m ↘\033[39m \033[89m%s\033[39m\n" "$(1)"
p_dot = @printf "\033[32m ∗\033[39m \033[89m%s\033[39m\n" "$(1)"
p_dot_red = @printf "\033[31m ∗\033[39m \033[89m%s\033[39m\n" "$(1)"

.PHONY: run test build rebuild release build-exe clean-exe clean

run:
	$(call pprintf,Running app)
	@python3 chs.py

test:
	$(call pprintf,Running tests for project)
	python3 -m "nose"

test-nocapture:
	$(call pprintf,Running tests for project)
	python3 -m "nose" --nocapture

build:
	$(call pprintf,Building project)
	python3 setup.py sdist

rebuild:
	make clean
	make build

release-major:
	$(call pprintf,Releasing project w/ major revision)
	python3 upgrade.py major
	make rebuild
	make release

release-minor:
	$(call pprintf,Releasing project w/ minor revision)
	python3 upgrade.py minor
	make rebuild
	make release

release-patch:
	$(call pprintf,Releasing project w/ patch revision)
	python3 upgrade.py patch
	make rebuild
	make release

release:
	twine upload dist/* --verbose

build-exe:
	$(call pprintf,Building project)
	pyinstaller ./chs.py --name=chs --onefile --add-binary=/Users/nick/projects/chs/chs/engine/stockfish-10-64:/Users/nick/projects/chs/dist

clean-exe:
	$(call pprintf,Cleaning project)
	rm ./chs.spec
	rm -rf ./build
	rm -rf ./dist

clean:
	$(call pprintf,Cleaning project)
	rm -rf ./dist
