# Standard Library
from typing import Any

# Third Party
from kedro.config import ConfigLoader
from kedro.io import DataCatalog


class KedroUtil:
    def __init__(self, project_path: str):
        self.project_path = project_path

    def load_conf_catalog(self) -> dict:
        conf_catalog = ConfigLoader(
            [
                f"{self.project_path}/conf/base",
                f"{self.project_path}/conf/local",
            ]
        ).get("catalog*")

        return conf_catalog

    def load_datacatalog(self) -> DataCatalog:
        conf_catalog = self.load_conf_catalog()
        for k in conf_catalog.keys():
            conf_catalog[k][
                "filepath"
            ] = f"{self.project_path}/{conf_catalog[k]['filepath']}"

        catalog = DataCatalog.from_config(conf_catalog)

        return catalog

    def load_data_from_datacatalog(self, catalog_name: str) -> Any:
        catalog = self.load_datacatalog()
        data = catalog.load(catalog_name)

        return data
