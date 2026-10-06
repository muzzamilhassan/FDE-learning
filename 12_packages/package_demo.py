r"""
=====================================================================
TOPIC: Virtual Environments, pip, and Packages
=====================================================================

SCENARIO
--------
You download a side project that needs an older library version,
while your main project needs the newest one. Installing both into
the same Python would break something. A virtual environment gives
each project its own private set of installed libraries.

TOPIC
-----
- A venv is a self-contained folder with its own interpreter link
  and its own installed packages.
- Create one per project:  python -m venv .venv
- Activate it, so installs go to .venv instead of global Python:
    Windows PowerShell:  .\.venv\Scripts\Activate.ps1
    macOS / Linux:       source .venv/bin/activate
- Install a library:      pip install requests
- Snapshot and restore versions:
    pip freeze > requirements.txt
    pip install -r requirements.txt
- Leave with `deactivate`. Name it .venv and never commit it to git.
- Second half of the topic: a PACKAGE is a folder of modules with an
  __init__.py inside -- see the runnable demo below.

QUESTIONS
---------
Q1. Your script raises ModuleNotFoundError for 'requests' although
    you installed it yesterday. Give the two most likely causes.
Q2. A teammate sends you their requirements.txt. Which commands
    recreate their exact environment from scratch?
Q3. In the demo below, what does __init__.py do, and why can we
    call textutils.shout(...) without importing cleaner.py directly?

Run: python 12_packages/package_demo.py
Answers: answers/12_packages.py
=====================================================================
"""

# The commands above belong in your terminal -- this file only
# DEMONSTRATES the package half of the topic, with no installs.

import shutil
import sys
import tempfile
from pathlib import Path


# ------------------------------------------------------------------
# TOPIC EXAMPLES: build a real mini-package, then import it
# ------------------------------------------------------------------

demo_dir = Path(tempfile.mkdtemp(prefix="pkg_demo_"))
pkg_dir = demo_dir / "textutils"
pkg_dir.mkdir()

# __init__.py marks the folder as a package. It runs on import and
# often re-exports names, so users get short, stable imports.
(pkg_dir / "__init__.py").write_text(
    "from textutils.cleaner import shout\n",
    encoding="utf-8",
)
(pkg_dir / "cleaner.py").write_text(
    "def shout(text: str) -> str:\n    return text.upper() + '!'\n",
    encoding="utf-8",
)

sys.path.insert(0, str(demo_dir))  # pretend demo_dir is importable
import textutils                   # runs __init__.py, which loads shout

print("Interpreter  :", sys.executable)  # which Python is running me?
print("Package demo :", textutils.shout("packages are folders"))

shutil.rmtree(demo_dir)            # tidy up the demo files


# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/12_packages.py
# ------------------------------------------------------------------
# Q1: You get ModuleNotFoundError for 'requests' even though you
#     installed it yesterday. Give the two most likely causes.
# Q2: A teammate emails you their requirements.txt. Which commands
#     recreate their environment from scratch?
# Q3: Look at the demo above: what does __init__.py do, and why does
#     textutils.shout(...) work without importing cleaner.py?
