# Standard Library
import importlib
import os

# Third Party
import hydra
from omegaconf import DictConfig

# First Party
from utils.logger import get_logger

logger = get_logger(__name__)


def execute_mode(cfg: DictConfig):
    mode = cfg["mode"]
    module = importlib.import_module(f"pipelines.{mode}")
    run_func = getattr(module, "run")
    run_func(cfg)


@hydra.main(version_base=None, config_name="config", config_path="../../conf")
def main(cfg: DictConfig):
    os.environ["WANDB_SILENT"] = "true"
    logger.info(cfg)
    execute_mode(cfg)


if __name__ == "__main__":
    main()
