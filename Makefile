.PHONY: phony
phony-goal: ; @echo $@

validate:
	black . && isort . && flake8 . && mypy .

prepare:
	pip install pandas-stubs black flake8 mypy