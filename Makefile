# values: default, tabby_strategy_intern, edenred, 6th_street
TAILOR = default


.PHONY: cv
cv:
	cd cv && rendercv render ../tailors/$(TAILOR)/cv.yaml
	mkdir -p public/assets/pdf
	cp cv/rendercv_output/Aisan_Mojahedi_CV.pdf public/assets/pdf/Aisan_Mojahedi_CV.pdf

.PHONY: public
public:
	python3 render_html.py tailors/$(TAILOR)/cv.yaml tailors/$(TAILOR)/web.yaml templates/index.html.j2 public/index.html
