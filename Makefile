PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

help:
	@echo 'Makefile for a pelican Web site'
	@echo '  make html      build with dev settings'
	@echo '  make publish   build with publish settings'
	@echo '  make serve     serve output at http://localhost:8000'

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

serve:
	$(PY) -m http.server --directory $(OUTPUTDIR) 8000
