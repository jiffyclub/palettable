build:
	python -m urubu build
	touch _build/.nojekyll

compile:
	python gendocs.py

images:
	python gendocs.py --images

serve:
	tserve --prefix palettable _build

.PHONY: build, compile, images, serve
