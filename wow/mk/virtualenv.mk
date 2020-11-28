.PHONY: venv clean-venv

$(VENV_DIR):
	python$(PYTHON_VERSION) -m venv $(VENV_DIR)
	$(PYTHON_BIN)/pip install --upgrade pip

$(call to_concrete, $(VENV_NAME)/req-%): $($(PROJ)_DIR)/%.txt | $(BUILD_DIR) $(VENV_DIR)
	$(PYTHON_BIN)/pip install --upgrade -r $<
	@mkdir -p $(dir $@)
	@date > $@

VENV_CONC := $(call to_concrete, $(VENV_NAME))
REQ_FILES := requirements dev_requirements
REQ_CONC  := $(REQ_FILES:%=$(call to_concrete,$(VENV_NAME)/req-%))
$(VENV_CONC): $(REQ_CONC)
	@date > $@

venv: $(VENV_CONC)

clean-venv:
	@rm -rf $($(PROJ)_DIR)/venv* $(BUILD_DIR)/venv*
