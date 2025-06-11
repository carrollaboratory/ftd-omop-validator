#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Requirements
collection_name = "omop_test_synthea"

# Optional
files = ['observation.tsv', 'conditions.tsv']


# In[2]:


import subprocess
import os
import pandas
from IPython.display import display, HTML

display(HTML("<style>.container { width:100% !important; }</style>"))

# https://support.terra.bio/hc/en-us/articles/360046617372-Accessing-data-from-the-workspace-Bucket-in-a-notebook#h_e2733953-ecfe-4ffe-86f6-bab3eb0cf4fc
BILLING_PROJECT_ID = os.environ['WORKSPACE_NAMESPACE']
WORKSPACE = os.environ['WORKSPACE_NAME']
bucket = os.environ['WORKSPACE_BUCKET']

# Copies the repo into an editable dir.
get_ipython().system("rsync -a --exclude='.git' /opt/ftd-omop-validator/ /home/jupyter/ftd-omop-validator/")
get_ipython().system('PYTHONPATH=home/jupyter/ftd-omop-validator/src')

# The custom img creates an env for python3.12 includes pip. Use these versions when running the validation script.
py39 = "/opt/py39_venv/bin/python"
pip39 = "/opt/py39_venv/bin/pip"
base = "/home/jupyter"

# Frequently used filepaths
fov = "/home/jupyter/ftd-omop-validator/src/ftd_omop_validator"
script_loc = "ftd-omop-validator/src/ftd_omop_validator/omop_file_validator.py"
csv_dir = f"/home/jupyter/uploads/{collection_name}"
results = "/home/jupyter/ftd-omop-validator/src/ftd_omop_validator/data/output/results.csv"
results_html = "/home/jupyter/ftd-omop-validator/src/ftd_omop_validator/data/output/results.html"


# In[3]:


# Copy all files from the workspace bucket to the notebook disk
get_ipython().system('mkdir -p {csv_dir}')
get_ipython().system('gcloud storage cp --recursive $bucket/* {base}')


# In[4]:


# Optional: Sanity check - Views the tables listed in the `files` variable
print('Available files')
get_ipython().system('ls {csv_dir}')


print('View files')
for table in files:
    view = f"{csv_dir}/{table}"
    e = pandas.read_csv(view)
    print(table)
    print(e.head(2))


# In[5]:


subprocess.run([py39, script_loc, "-c", csv_dir], cwd=base)


# In[6]:


pandas.read_csv(results)

print(f'To see the html version, click on the jupyter logo at the top of this notebook and navigate here:\n"{results_html}"')


# In[ ]:




