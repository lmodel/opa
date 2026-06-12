"""Data test."""

import os
import glob
import pytest
from pathlib import Path

import opa.datamodel.opa
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"
DATA_DIR_CONTRIB_VALID = Path(__file__).parent / "data" / "contrib" / "valid"
DATA_DIR_CONTRIB_INVALID = Path(__file__).parent / "data" / "contrib" / "invalid"

VALID_EXAMPLE_FILES = sorted(
    glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
    + glob.glob(os.path.join(DATA_DIR_CONTRIB_VALID, "*.yaml"))
)
INVALID_EXAMPLE_FILES = sorted(
    glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))
    + glob.glob(os.path.join(DATA_DIR_CONTRIB_INVALID, "*.yaml"))
)


def _target_class_for_filepath(filepath: str):
    """Resolve fixture filename prefix to datamodel class."""
    target_class_name = Path(filepath).stem.split("-")[0]
    return getattr(opa.datamodel.opa, target_class_name)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    tgt_class = _target_class_for_filepath(filepath)
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test loading of invalid fixtures raises an error."""
    tgt_class = _target_class_for_filepath(filepath)
    with pytest.raises(Exception):
        yaml_loader.load(filepath, target_class=tgt_class)
