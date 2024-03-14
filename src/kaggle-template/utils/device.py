# Third Party
import torch
from type_hint import Tensors

from .logger import get_logger

logger = get_logger(__name__)


def get_device():
    if torch.cuda.device_count() >= 1:
        logger.info(
            "Model pushed to {} GPU(s), type {}.".format(
                torch.cuda.device_count(), torch.cuda.get_device_name(0)
            )
        )
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    return device


def to_device(tensors: Tensors, device: torch.device, *args, **kwargs):
    if isinstance(tensors, tuple):
        return (t.to(device, *args, **kwargs) for t in tensors)
    elif isinstance(tensors, dict):
        return {k: t.to(device, *args, **kwargs) for k, t in tensors.items()}
    else:
        return tensors.to(device, *args, **kwargs)