# Standard Library
import pickle
from pathlib import Path
from typing import Any, Union

# Third Party
import numpy as np
import yaml

from .logger import get_logger

logger = get_logger(__name__)


def save_npy(arr: np.ndarray, filepath: Union[str, Path]):
    with open(filepath, "wb") as f:
        np.save(f, arr)
    logger.info(f"Saved {str(filepath)}")


def load_npy(filepath: Union[str, Path]) -> np.ndarray:
    with open(filepath, "rb") as f:
        arr = np.load(f)
    logger.info(f"Loaded {str(filepath)}")
    return arr


def save_pickle(obj: Any, filepath: Union[str, Path]):
    with open(filepath, "wb") as f:
        pickle.dump(obj, f)
    logger.info(f"Saved {str(filepath)}")


def load_pickle(filepath: Union[str, Path]) -> Any:
    with open(filepath, "rb") as f:
        obj = pickle.load(f)
    logger.info(f"Loaded {str(filepath)}")
    return obj


def load_yaml(file_path: str, verbose: bool = True) -> dict:
    with open(file_path) as f:
        if verbose:
            logger.info(f"load {file_path}")
        return yaml.safe_load(f)
