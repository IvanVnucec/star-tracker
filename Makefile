.PHONY: all download run

SCRIPTS_FOLDER = scripts
CATALOG_FOLDER = data
CATALOG = \
	data/catalog.dat \
	data/index.dat   \
	data/suppl_1.dat \
	data/suppl_2.dat \

all: run

run: $(CATALOG_FOLDER)
	@python3 parser.py

download: $(CATALOG)

$(CATALOG):
	@./$(SCRIPTS_FOLDER)/download_catalog.sh
