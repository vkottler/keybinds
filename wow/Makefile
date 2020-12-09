.PHONY: all venv clean run run-help

.DEFAULT_GOAL  := all

PY_EXTRA_LINT_ARGS := $($(PROJ)_DIR)/dev.py $($(PROJ)_DIR)/setup.py
include $($(PROJ)_DIR)/env.mk

lint: $(PY_PREFIX)lint
sa: $(PY_PREFIX)sa
test: check-env $(PY_PREFIX)test
upload: check-env $(PYPI_PREFIX)upload
view: $(PY_PREFIX)view
host-coverage: $(PY_PREFIX)host-coverage
dist: $(PY_PREFIX)dist

all: lint sa test todo

run: $(VENV_CONC) check-env
	@$(PYTHON_BIN)/python $($(PROJ)_DIR)/dev.py -o $(BUILD_DIR) -v

run-help: $(VENV_CONC)
	@$(PYTHON_BIN)/python $($(PROJ)_DIR)/dev.py -h

todo:
	-cd $($(PROJ)_DIR) && ack -i todo $(PROJ) tests

clean: $(PY_PREFIX)clean
	@rm -rf $(BUILD_DIR) $($(PROJ)_DIR)/.vbinds_cache
