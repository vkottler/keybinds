.PHONY: all venv clean

.DEFAULT_GOAL  := all
PYTHON_VERSION := 3.8
PROJ           := vbinds
$(PROJ)_DIR    := .
BUILD_DIR      := $($(PROJ)_DIR)/build
VENV_NAME      := venv$(PYTHON_VERSION)
VENV_DIR       := $($(PROJ)_DIR)/$(VENV_NAME)
PYTHON_BIN     := $(VENV_DIR)/bin

include $($(PROJ)_DIR)/mk/functions.mk
include $($(PROJ)_DIR)/mk/virtualenv.mk
include $($(PROJ)_DIR)/mk/env.mk

$(BUILD_DIR):
	@mkdir -p $@/$(VENV_NAME)

lint-%: $(VENV_CONC) check-env
	$(PYTHON_BIN)/$* $(PROJ) tests

lint: lint-flake8 lint-pylint

sa: lint-mypy

test: $(VENV_CONC) check-env
	$(PYTHON_BIN)/pytest -x --log-cli-level=10 --cov=$(PROJ) --cov-report html

view:
	@$(BROWSER) htmlcov/index.html

host-coverage:
	cd $($(PROJ)_DIR)/htmlcov && python$(PYTHON_VERSION) -m http.server 8080

all: lint sa test todo

clean:
	@find -iname '*.pyc' -delete
	@find -iname '__pycache__' -delete
	@rm -rf $(BUILD_DIR) $($(PROJ)_DIR)/.vbinds_cache $($(PROJ)_DIR)/.mypy_cache
	@rm -rf $($(PROJ)_DIR)/cover $($(PROJ)_DIR)/.coverage dist \
		$($(PROJ)_DIR)/*.egg-info $($(PROJ)_DIR)/htmlcov \
		$($(PROJ)_DIR)/.pytest_cache
