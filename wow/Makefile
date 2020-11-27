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
include $($(PROJ)_DIR)/mk/venv.mk

$(BUILD_DIR):
	@mkdir -p $@/$(VENV_NAME)

all: venv

clean:
	@rm -rf $(BUILD_DIR)
