SRC_DIR = src

DST_DIR = docs
MD_DIR = $(SRC_DIR)/md
MD_FILES = $(shell fd -t f ".md" $(SRC_DIR))
HTML_TREE = $(patsubst $(MD_DIR)/%, $(DST_DIR)/%, $(shell fd -t d . $(MD_DIR)))
HTML_FILES = $(patsubst $(MD_DIR)/%.md, $(DST_DIR)/%.html, $(MD_FILES))
TEMPLATE = $(SRC_DIR)/templates/main.html
CSS_SRC_DIR = $(SRC_DIR)/css
CSS_DST_DIR = $(DST_DIR)/css
CSS_SRC_FILES = $(shell fd -t f ".css" $(CSS_SRC_DIR))
CSS_DST_FILES = $(patsubst $(CSS_SRC_DIR)/%.css, $(CSS_DST_DIR)/%.css, $(CSS_SRC_FILES))

.PHONY : all
all : html css cname

.PHONY : css
css : $(CSS_DST_FILES)

$(CSS_DST_DIR) :
	mkdir -p $@

$(CSS_DST_DIR)/%.css : $(CSS_SRC_DIR)/%.css | $(CSS_DST_DIR)
	cp $< $@

.PHONY : html

html : $(HTML_FILES)

$(HTML_TREE) :
	mkdir -p $@

$(DST_DIR)/%.html : $(MD_DIR)/%.md $(TEMPLATE) | $(HTML_TREE)
	pandoc --template=$(TEMPLATE) $< $(<D)/nav.yml -o $@

.PHONY : cname

cname :
	cp src/CNAME docs/CNAME

.PHONY : clean

clean :
	rm -rf docs/*
