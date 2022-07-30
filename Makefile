MAIN ?= p
DIFF ?= HEAD^
CODE := $(addsuffix .tex,$(filter-out %.tex,$(wildcard code/*)))
FIGS := $(patsubst %.svg,%.pdf,$(wildcard fig/*.svg))
PPTX := $(patsubst pptx/%.pdf,fig/%-crop.pdf,$(wildcard pptx/*.pdf))
PLOT := $(patsubst %.gp,%.tex,$(wildcard data/*.gp))
DEPS := rev.tex code/fmt.tex abstract.txt $(CODE) $(FIGS) $(PPTX) $(PLOT)
BTEX := --bibtex-args="-min-crossrefs=99"
LTEX := --latex-args="-interaction=nonstopmode -synctex=4"
SHELL:= $(shell echo $$SHELL)

all: $(DEPS) ## generate a pdf
	@TEXINPUTS="sty:" python3 bin/latexrun.py $(BTEX) $(LTEX) $(MAIN)
	@cp latex.out/p.synctex.gz p.synctex.gz

submit: $(DEPS) ## proposal function
	@python bin/nsf-submit.py $(MAIN).pdf $(CURDIR)/nsf-submit

diff: $(DEPS) ## generate diff-highlighed pdf
	@sh bin/diff.sh $(DIFF)

help: ## print help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

rev.tex: FORCE
	@printf '\\gdef\\therev{%s}\n\\gdef\\thedate{%s}\n' \
	   "$(shell git rev-parse --short HEAD)"            \
	   "$(shell git log -1 --format='%ci' HEAD)" > $@

code/%.tex: code/% ## build highlighted tex code from source code
	pygmentize -P tabsize=4 -P mathescape -f latex $^ | mark.py > $@

code/fmt.tex: ## generate color table
	pygmentize -f latex -S default > $@

fig/%.pdf: fig/%.svg ## generate pdf from svg
	inkscape --without-gui -f $^ -D -A $@

fig/%-crop.pdf: pptx/%.pdf
	pdfcrop --margin=1 $^ $@

data/%.tex: data/%.gp ## generate plot
	gnuplot $^

draft: $(DEPS) ## generate pdf with a draft info
	echo -e '\\newcommand*{\\DRAFT}{}' >> rev.tex
	@TEXINPUTS="sty:" python3 bin/latexrun.py $(BTEX) $(MAIN)

watermark: $(DEPS) ## generate pdf with a watermark
	echo -e '\\usepackage[firstpage]{draftwatermark}' >> rev.tex
	@TEXINPUTS="sty:" python3 bin/latexrun.py $(BTEX) $(MAIN)

spell: ## run a spell check
	@for i in *.tex fig/*.tex; do sh bin/aspell.sh $$i; done
	@for i in *.tex; do bin/double.pl $$i; done
	@for i in *.tex; do bin/abbrv.pl  $$i; done
	@sh bin/hyphens.sh *.tex
	@pdftotext $(MAIN).pdf /dev/stdout | grep '??'

clean: ## clean up
	@python3 bin/latexrun.py --clean
	rm -f abstract.txt
	rm -f p.synctex.gz

distclean: clean ## clean up completely
	rm -f code/*.tex

init: ## init writing (discarding example)
	rm -f {code,fig,data}/ex-*
	perl -pi -e 's/^\\input{ex}/% \\input{ex}/g' $(MAIN).tex

abstract.txt: abstract.tex $(MAIN).tex ## generate abstract.txt
	@python3 bin/mkabstract.py $(MAIN).tex $< | fmt -w72 > $@

.PHONY: all help FORCE draft clean spell distclean init
