# %%
# Name: Cameron Berryman
# Computing ID: kqe6rf

# %%
# Setup
# Path: @CB12354 -> /workspaces/daytwostuff (main)


# %% Virtual environment setup
# python3 -m venv .venv
# source .venv/bin/activate
# pip3 install -r requirements.txt

# Don't include .venv in the repo, just commit the requirements.txt so that the user can install it on their own
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

# %% Codespaces for Dummies: Making a New Environment
# 
# Step 1: Create or fork a GitHub repo.
#   - If a different base than normal linux for the dev container is required, add the dev container json and dockerfile
#   - Make sure to set the .gitignore template to Python
# Step 2: On the main Code page of the repo, click the green Code button, then Codespaces, then make a new codespace
# Step 3: Go to VSCode Desktop, do >Codespaces: Connect to Codespace, log into your GitHub account and select that codespace you just made online
# Step 4: Install necessary extensions to run the project (ex. Python, Data wrangler, etc.)
# Step 5: Create and activate a virtual environment for Python projects
# Step 6: Install needed dependencies and freeze them into a requirements file
# Step 7: Add necessary ignored files or folders, like .venv, to a .gitignore file
# Step 8: Add all modified files, commit, and push to the remote repo to save all locally made changes