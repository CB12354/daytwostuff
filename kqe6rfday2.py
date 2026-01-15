# %%
# Name: Cameron Berryman
# Computing ID: kqe6rf

# %%
# Setup
# Path: @CB12354 -> /workspaces/daytwostuff (main)
# Path after venv: (.venv) @CB12354 -> /workspaces/daytwostuff (main)

# %%
# Imports
import numpy as np
import pandas as pd
# %%
# Viewing Data
penguins = pd.read_csv("penguins.csv")
penguins.head()

# The extensions menu has tons of different options which aren't always relevant to what you're working on.
# You can use tags to search for specific extensions ase well.
# 3 useful Data Wrangler functions:
# - Gives column summaries based on data type and scale
# - Usable with more than just CSV files (json, excel, etc.)
# - Directly integrates with Jupyter's saved variables

# %% 
# Package management
# Requirements files ensure that other users get the exact necessary packages needed to run the file.
# They may be missing a package or running the incorrect version of a package if they install everything on their own.
# pip freeze > requirements.txt