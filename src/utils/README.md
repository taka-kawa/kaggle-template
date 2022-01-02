# utils

## file_uril

### save_npy/load_npy

```python
# Third Party
import numpy as np
from file_util import FileUtil

arr = np.zeros(100)

FileUtil.save_npy(arr, "zero.npy")
# >>> Saved zero.npy
arr = FileUtil.load_npy("zero.npy")
# >>> Loaded zero.npy
```

### save_pickle/load_pickle

```python
# Third Party
from file_util import FileUtil

zero = [0, 0, 0]

FileUtil.save_pickle(a, "zero.pkl")
# >>> Saved zero.pkl
a = FileUtil.load_pickle("zero.pkl")
# >>> Loaded zero.pkl
```

## kedro_util

### load_conf_catalog

```python
from kedro_util import KedroUtil

project_path = '../'
ku = KedroUtil(project_path)

print(ku.load_conf_catalog())
# >>> 'raw_data {'type': 'pandas.CSVDataSet',
# >>>  'filepath': 'data/01_raw/raw_data.csv',
# >>>  'load_args': {'encoding': 'utf-8'}},
# >>> ...
```

### load_datacatalog

```python
from kedro_util import KedroUtil

project_path = '../'
ku = KedroUtil(project_path)

io = ku.load_datacatalog()
type(io)
# >>> kedro.io.data_catalog.DataCatalog
```

### load_data_from_datacatalog

```python
from kedro_util import KedroUtil

project_path = '../'
ku = KedroUtil(project_path)

df = ku.load_data_from_datacatalog('raw_data')
```

## memory_util

### log_memory

```python
# Standard Library
import tracemalloc

# Third Party
from memory_util import MemoryUtil

tracemalloc.start()

MemoryUtil.log_memory()
# >>> current used memory: 3.494 MB

demo = [x for x in range(100000)]

MemoryUtil.log_memory()
# >>> current used memory: 6.953 MB
```

### reduce_df_mem_usuage

```python
import pandas as pd
df = pd.DataFrame([[i for i in range(1000)] for _ in range(1000)])

df = MemoryUtil.reduce_df_mem_usage(df)

# >>> Memory usage of dataframe is 7.63 MB
# >>> Memory usage after optimization is: 1.79 MB
# >>> Decreased by 76.6%
```

## metric_util

### search_threshold

```python
# Third Party
import numpy as np
from metric_util import MetricUtil
from sklearn.metrics import f1_score

y_true = np.array([0 for _ in range(500)] + [1 for _ in range(1000)])
y_pred = np.array([x * (1 / 1500) for x in range(1500)])
print(MetricUtil.search_threshold(y_true, y_pred, f1_score, is_higher_better=True))
# >>> {'threshold': 0.33, 'score': 0.998003992015968}
```



## seed_util

### seed_everything

```python
from seed_util import SeedUtil

seed = 1234
SeedUtil.seed_everything(seed)
```

## time_util

### timer

```python
# Standard Library
import time

# Third Party
from time_util import TimeUtil

with TimeUtil.timer("wait"):
    time.sleep(3)
# >>> [wait] done in 3.0018 s
```

### timer_wrapper

```python
# Standard Library
import time

# Third Party
from time_util import TimeUtil

@TimeUtil.timer_wrapper
def wait(wait_time):
    time.sleep(wait_time)

wait(5)
# >>> [wait] start
# >>> [wait] done in 5.0042 s

```

## visualization_util

### plot_confusion_matrix

```python
import numpy as np

from visualization_util import VisualizationUtil

class_name = np.array([0,1,2,3])
y_true = [np.random.choice(class_name, 1)[0] for _ in range(1000)]
y_pred = [np.random.choice(class_name, 1)[0] for _ in range(1000)]

VisualizationUtil.plot_confusion_matrix(y_true, y_pred, class_name, save_path='./cm.png')
# >>> Confusion matrix, without normalization
# >>> [[65 55 70 58]
# >>> [41 73 45 71]
# >>> [64 74 68 58]
# >>> [51 64 72 71]]
```

![test](https://media.ghe.rakuten-it.com/user/1428/files/389dac80-dfee-11eb-8b9a-3ad040e6a12f)

### plot_feature_importance

```python
import pandas as pd

from visualization_util import VisualizationUtil

importances = pd.DataFrame()
for fold_, model in enumerate(models):
    imp_df = pd.DataFrame()
    imp_df['feature'] = model.feature_name()
    imp_df['gain'] = model.feature_importance(importance_type="gain")
    imp_df['split'] = model.feature_importance(importance_type="split")
    imp_df['fold'] = fold_ + 1
    importances = pd.concat([importances, imp_df], axis=0, sort=False)

VisualizationUtil.plot_feature_importance(importances, 'gain', 'feature_importance.png')
```

![feature_importance](https://media.ghe.rakuten-it.com/user/1428/files/2f640e00-dff5-11eb-80bb-a9adda6cc284)

