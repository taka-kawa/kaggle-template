# Standard Library
import tracemalloc

# Third Party
import numpy as np
import psutil
import torch

from .logger import get_logger

logger = get_logger(__name__)


def log_memory():
    def format_bytes(size: int):
        power = 2**10  # 2**10 = 1024
        n = 0
        power_labels = ["B", "KB", "MB", "GB", "TB"]
        while size > power and n <= len(power_labels):
            size /= power
            n += 1
        return "current used memory: {:.3f} {}".format(size, power_labels[n])

    snapshot = tracemalloc.take_snapshot()
    size = sum([stat.size for stat in snapshot.statistics("filename")])
    print(format_bytes(size))


def reduce_df_mem_usage(df):
    """iterate through all the columns of a dataframe and modify the data type
    to reduce memory usage.
    """
    start_mem = df.memory_usage().sum() / 1024**2
    print("Memory usage of dataframe is {:.2f} MB".format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    df[col] = df[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype("category")

    end_mem = df.memory_usage().sum() / 1024**2
    print("Memory usage after optimization is: {:.2f} MB".format(end_mem))
    print("Decreased by {:.1f}%".format(100 * (start_mem - end_mem) / start_mem))

    return df


def show_gpu_memory():
    if torch.cuda.is_available():
        allocated_memory = torch.cuda.memory_allocated()
        logger.info(f"Memory allocated on GPU: {allocated_memory} bytes")
        reserved_memory = torch.cuda.memory_reserved()
        logger.info(f"Memory reserved on GPU: {reserved_memory} bytes")


def display_memory_info():
    memory_info = psutil.virtual_memory()

    total_memory = memory_info.total / (1024**3)  # Convert bytes to GB
    used_memory = memory_info.used / (1024**3)
    available_memory = memory_info.available / (1024**3)
    percent_used = memory_info.percent

    logger.info(f"Total Memory: {total_memory:.2f} GB")
    logger.info(f"Used Memory: {used_memory:.2f} GB")
    logger.info(f"Available Memory: {available_memory:.2f} GB")
    logger.info(f"Percent Used: {percent_used}%")

    # Swap memory information
    swap_info = psutil.swap_memory()

    total_swap = swap_info.total / (1024**3)  # Convert bytes to GB
    used_swap = swap_info.used / (1024**3)
    free_swap = swap_info.free / (1024**3)
    percent_swap_used = swap_info.percent

    logger.info(f"Total Swap: {total_swap:.2f} GB")
    logger.info(f"Used Swap: {used_swap:.2f} GB")
    logger.info(f"Free Swap: {free_swap:.2f} GB")
    logger.info(f"Percent Swap Used: {percent_swap_used}%")