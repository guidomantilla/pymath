.PHONY: phony
phony-goal: ; @echo $@

validate:
	#black . && flake8 . && mypy .
	black . && mypy .

prepare:
	pip install pandas-stubs black flake8 mypy