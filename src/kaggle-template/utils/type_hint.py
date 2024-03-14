# Third Party
import numpy as np
import torch
from pytorch_lightning.callbacks import Callback

Tensors = tuple[torch.Tensor] | dict[str, torch.Tensor]
Callbacks = list[Callback]