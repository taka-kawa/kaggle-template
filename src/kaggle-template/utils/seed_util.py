# Standard Library
import os
import random

# Third Party
import numpy as np
import pytorch_lightning as pl
import torch


def seed_torch(seed=1234):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    pl.seed_everything(seed, workers=True)


def seed_everything(seed=1234):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    seed_torch(seed)