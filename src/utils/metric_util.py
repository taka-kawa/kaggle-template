# Standard Library
from typing import Callable, Dict

# Third Party
import numpy as np


class MetricUtil:
    @staticmethod
    def search_threshold(
        y_true: np.ndarray,
        y_prob: np.ndarray,
        func: Callable[[np.ndarray, np.ndarray], float],
        is_higher_better: bool = True,
    ) -> Dict[str, float]:
        best_threshold = 0.0
        best_score = -np.inf if is_higher_better else np.inf

        for threshold in [i * 0.01 for i in range(100)]:
            score = func(y_true=y_true, y_pred=y_prob > threshold)
            if is_higher_better:
                if score > best_score:
                    best_threshold = threshold
                    best_score = score
            else:
                if score < best_score:
                    best_threshold = threshold
                    best_score = score

        search_result = {"threshold": best_threshold, "score": best_score}
        return search_result
