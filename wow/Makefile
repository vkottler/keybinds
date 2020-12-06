.PHONY: all venv clean run run-help

.DEFAULT_GOAL  := all
PROJ           := vbinds
$(PROJ)_DIR    := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
BUILD_DIR_NAME := build
BUILD_DIR      := $($(PROJ)_DIR)/$(BUILD_DIR_NAME)

include $($(PROJ)_DIR)/mk/functions.mk
include $($(PROJ)_DIR)/env.mk
include $($(PROJ)_DIR)/mk/venv.mk
include $($(PROJ)_DIR)/mk/python.mk

$(BUILD_DIR):
	@mkdir -p $@

PY_EXTRA_LINT_ARGS := $($(PROJ)_DIR)/dev.py
lint: $(PY_PREFIX)lint
sa: $(PY_PREFIX)sa
test: check-env $(PY_PREFIX)test
view: $(PY_PREFIX)view
host-coverage: $(PY_PREFIX)host-coverage

all: lint sa test todo

run: $(VENV_CONC) check-env
	@$(PYTHON_BIN)/python $($(PROJ)_DIR)/dev.py -o $(BUILD_DIR) -v

run-help: $(VENV_CONC)
	@$(PYTHON_BIN)/python $($(PROJ)_DIR)/dev.py -h

todo:
	-cd $($(PROJ)_DIR) && ack -i todo $(PROJ) tests

clean: $(PY_PREFIX)clean
	@rm -rf $(BUILD_DIR) $($(PROJ)_DIR)/.vbinds_cache
