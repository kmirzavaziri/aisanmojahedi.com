.PHONY: cv
cv:
	cd cv && rendercv render Aisan_Mojahedi_CV.yaml
	mkdir -p public/assets/pdf
	cp cv/rendercv_output/Aisan_Mojahedi_CV.pdf public/assets/pdf/Aisan_Mojahedi_CV.pdf

.PHONY: public
public:
	python3 render_html.py