.PHONY: download

SCRIPTS_FOLDER = scripts
DATA_FOLDER = data

download: $(DATA_FOLDER)

$(DATA_FOLDER):
	@./$(SCRIPTS_FOLDER)/download_catalog.sh
