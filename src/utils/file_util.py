# Standard Library
import pickle
from pathlib import Path
from typing import Any, Union

# Third Party
import numpy as np


class FileUtil:
    @staticmethod
    def save_npy(arr: np.ndarray, filepath: Union[str, Path]):
        with open(filepath, "wb") as f:
            np.save(f, arr)
        print(f"Saved {str(filepath)}")

    @staticmethod
    def load_npy(filepath: Union[str, Path]) -> np.ndarray:
        with open(filepath, "rb") as f:
            arr = np.load(f)
        print(f"Loaded {str(filepath)}")
        return arr

    @staticmethod
    def save_pickle(obj: Any, filepath: Union[str, Path]):
        with open(filepath, "wb") as f:
            pickle.dump(obj, f)
        print(f"Saved {str(filepath)}")

    @staticmethod
    def load_pickle(filepath: Union[str, Path]) -> Any:
        with open(filepath, "rb") as f:
            obj = pickle.load(f)
        print(f"Loaded {str(filepath)}")
        return obj
