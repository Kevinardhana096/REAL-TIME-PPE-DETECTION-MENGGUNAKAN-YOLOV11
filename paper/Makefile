# Makefile untuk kompilasi LaTeX paper
# Usage: make          (compile paper)
#        make clean    (remove auxiliary files)
#        make view     (open PDF after compile)

MAIN = main
PDFLATEX = pdflatex
BIBTEX = bibtex
VIEWER = start  # Windows: start, Mac: open, Linux: xdg-open

.PHONY: all clean view help

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex references.bib
	@echo "=== First LaTeX pass ==="
	$(PDFLATEX) $(MAIN).tex
	@echo "=== Running BibTeX ==="
	$(BIBTEX) $(MAIN)
	@echo "=== Second LaTeX pass ==="
	$(PDFLATEX) $(MAIN).tex
	@echo "=== Final LaTeX pass ==="
	$(PDFLATEX) $(MAIN).tex
	@echo "=== PDF generated: $(MAIN).pdf ==="

view: $(MAIN).pdf
	$(VIEWER) $(MAIN).pdf

clean:
	rm -f *.aux *.log *.bbl *.blg *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz

cleanall: clean
	rm -f $(MAIN).pdf

help:
	@echo "LaTeX Paper Makefile"
	@echo "Commands:"
	@echo "  make       - Compile paper to PDF"
	@echo "  make view  - Open PDF after compiling"
	@echo "  make clean - Remove auxiliary files"
	@echo "  make cleanall - Remove all generated files including PDF"
