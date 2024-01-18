# Third Party
import torch


def set_device():
    if torch.cuda.device_count() >= 1:
        print(
            "Model pushed to {} GPU(s), type {}.".format(
                torch.cuda.device_count(), torch.cuda.get_device_name(0)
            )
        )
        torch.device("cuda")
    else:
        torch.device("cpu")
