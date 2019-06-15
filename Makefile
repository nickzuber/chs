pprintf = @printf "\n\033[36m=-=-\033[39m \033[1m%s\033[0m \033[36m-=-=-=-=-=-=-=-=-=-=-=\033[39m 🚀\n" "$(1)"
p_update = @printf "\033[33m ↻\033[39m \033[89m%s\033[39m\n" "$(1)"
p_add = @printf "\033[32m ↗\033[39m \033[89m%s\033[39m\n" "$(1)"
p_remove = @printf "\033[31m ↘\033[39m \033[89m%s\033[39m\n" "$(1)"
p_dot = @printf "\033[32m ∗\033[39m \033[89m%s\033[39m\n" "$(1)"
p_dot_red = @printf "\033[31m ∗\033[39m \033[89m%s\033[39m\n" "$(1)"

.PHONY: run test build clean

run:
	$(call pprintf,Running app)
	@python3 chss.py

test:
	$(call pprintf,Running tests for project)
	$(call p_dot_red,Not implemented.)

build:
	$(call pprintf,Building project)
	pyinstaller ./chss.py --name=chss --onefile --add-binary=/Users/nick/projects/chss/app/engine/stockfish-10-64:/Users/nick/projects/chss/dist

clean:
	$(call pprintf,Cleaning project)
	rm ./chss.spec
	rm -rf ./build
	rm -rf ./dist
