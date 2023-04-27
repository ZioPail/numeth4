.PHONY: generate profile clear

generate:
	@echo "Warning: build is not forced, some binaries may not be compiled in hardcore or profile mode."
	@python3 -m dummy_pkg.setup

force:
	@make clear
	@python3 -m dummy_pkg.setup --force_build

profile:
	@make clear
	@python3 -m dummy_pkg.setup --profile

hardcore:
	@make clear
	@python3 -m dummy_pkg.setup --hardcore

hardcoreprofile:
	@make clear
	@python3 -m dummy_pkg.setup --hardcore --profile

clear:
	@echo "Cleaning all.."
	@rm -f dummy_pkg/*.c
	@rm -f dummy_pkg/*.so
	@rm -f dummy_pkg/*.html
	@rm -R -f dummy_pkg/build
	@rm -R -f dummy_pkg/__pycache__
	@echo "Cleaned."