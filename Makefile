build:
	pdflatex -interaction=nonstopmode sem-aus.tex
	pythontex sem-aus.tex
	bibtex sem-aus
	pdflatex -interaction=nonstopmode sem-aus.tex
	pdflatex -interaction=nonstopmode sem-aus.tex

clean:
	rm -rf sem-aus.bbl sem-aus.blg sem-aus.aux sem-aus.listing sem-aus.log sem-aus.pdf pythontex-files-sem-aus
