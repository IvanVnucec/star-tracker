.PHONY: download run

SCRIPTS_FOLDER = scripts
DATA_FOLDER = data

download: $(DATA_FOLDER)

run: $(DATA_FOLDER)
	@python3 parser.py

$(DATA_FOLDER):
	@./$(SCRIPTS_FOLDER)/download_catalog.sh
