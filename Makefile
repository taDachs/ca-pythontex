build:
	pdflatex -interaction=nonstopmode sem-aus.tex
	pythontex sem-aus.tex
	pdflatex -interaction=nonstopmode sem-aus.tex

clean:
	rm -rf sem-aus.aux sem-aus.bib sem-aus.listing sem-aus.log sem-aus.pdf pythontex-files-sem-aus
