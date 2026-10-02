"""
13_packages / package_demo.py
Topic: Package Management and Virtual Environments (npm vs pip / venv)

NODE.JS / NPM vs PYTHON PIP & VENV:
-----------------------------------
Node.js / npm Ecosystem:
    - `package.json`        -> Lists project dependencies
    - `node_modules/`       -> Local folder containing installed packages
    - `npm install`         -> Installs packages into local node_modules
    - `npm install <pkg>`   -> Adds dependency to package.json

Python Ecosystem:
    - `requirements.txt`    -> Lists project dependencies (pinned versions)
    - `.venv/`              -> Virtual environment isolating dependencies
    - `pip install -r requirements.txt` -> Installs packages into active environment

WHY ARE VIRTUAL ENVIRONMENTS (.venv) CRITICAL IN PYTHON?
- In Node.js, `npm install` installs into the local `./node_modules` folder by default.
- In Python, `pip install` by default installs GLOBALLY across your entire operating system!
  This leads to dependency conflicts between different projects.
- Creating a `.venv` creates an isolated Python sandbox for your project.
"""

GUIDE = """
=== Step-by-Step Python Environment Setup for JS Developers ===

1. Create a virtual environment (.venv) inside your project root:
   python -m venv .venv

2. Activate the virtual environment:
   - Windows PowerShell:  .\.venv\Scripts\Activate.ps1
   - Windows CMD:         .\.venv\Scripts\activate.bat
   - macOS / Linux:       source .venv/bin/activate

   (Once activated, your terminal prompt will show `(.venv)` prefix)

3. Install project dependencies:
   pip install -r 13_packages/requirements.txt

4. Save newly installed packages to requirements.txt (like updating package.json):
   pip freeze > requirements.txt

5. Deactivate environment when finished:
   deactivate
"""

print(GUIDE)

import sys
print(f"Current Python Executable: {sys.executable}")
print(f"Current Python Version: {sys.version.split()[0]}")
