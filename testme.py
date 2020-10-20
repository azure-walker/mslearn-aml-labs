# %% This is going to be an interactive python script

import azureml.core
from azureml.core import Workspace, Datastore, Dataset

ws = Workspace.from_config()

# %%
default_ds = ws.get_default_datastore()


# %%
datastore_paths = [(default_ds, 'data')]
DS = Dataset.File.from_files(path=datastore_paths)

# %%

import os
import pandas as pd
import xlrd

# Access Data using Mount Point instead of Download
with DS.mount() as mount_context:
    print(os.listdir(mount_context.mount_point))
    excel = pd.read_excel(mount_context.mount_point +'/bi_dimensions.xlsx', sheet_name='product', header=0)
# %%
