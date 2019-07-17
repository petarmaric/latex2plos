LATEX_MAINFILE = paper.tex

BUILD_DIR = build


.PHONY: .FORCE_MAKE build
build: .FORCE_MAKE
	latexmk -pdf -interaction=nonstopmode -aux-directory=$(BUILD_DIR) -output-directory=$(BUILD_DIR) $(LATEX_MAINFILE)


.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
