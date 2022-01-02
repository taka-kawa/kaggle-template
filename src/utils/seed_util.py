# Standard Library
import os
import random

# Third Party
import numpy as np
import torch


class SeedUtil:
    @staticmethod
    def seed_everything(seed=1234):
        random.seed(seed)
        os.environ["PYTHONHASHSEED"] = str(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
