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
    try:
        module = importlib.import_module(f"pipelines.{mode}")
        run_func = getattr(module, "run")
        run_func(cfg)
    except ImportError:
        logger.error(
            f"Mode '{mode}' is not implemented. No module named 'pipelines.{mode}'"
        )
    except AttributeError:
        logger.error(
            f"Mode '{mode}' is implemented, but 'run' function is missing in 'pipelines.{mode}'"
        )
    except Exception as e:
        logger.error(f"An error occurred while executing mode '{mode}': {str(e)}")


@hydra.main(version_base=None, config_name="config", config_path="../../conf")
def main(cfg: DictConfig):
    os.environ["WANDB_SILENT"] = "true"
    logger.info(cfg)
    execute_mode(cfg)


if __name__ == "__main__":
    main()
