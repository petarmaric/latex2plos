LATEX_MAINFILE = paper.tex

BUILD_DIR = build
EXPORT_DIR = export


.PHONY: .FORCE_MAKE build
build: .FORCE_MAKE
	latexmk -pdf -interaction=nonstopmode -aux-directory=$(BUILD_DIR) -output-directory=$(BUILD_DIR) $(LATEX_MAINFILE)


.PHONY: clean
clean:
	rm -rf $(BUILD_DIR) $(EXPORT_DIR)

.PHONY: export
export: build
	rm -rf $(EXPORT_DIR)
	latex2plos --build-dir $(BUILD_DIR) --export-dir $(EXPORT_DIR) --quiet $(LATEX_MAINFILE)
	make -C $(EXPORT_DIR) -f ../Makefile build
