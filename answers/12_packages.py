"""
Answers for 12_packages - try the questions first!
"""

import shutil
import sys
import tempfile
from pathlib import Path


# ------------------------------------------------------------------
# package_demo.py
# ------------------------------------------------------------------

# Q1: Two likely causes:
#     1) Wrong interpreter: requests went into global Python but your
#        project's .venv is active (or the reverse). Check where pip
#        put it with `pip show requests` and which python runs you
#        with `python -c "import sys; print(sys.executable)"`.
#     2) The venv was never activated in THIS terminal, so `python`
#        and `pip` point somewhere else. Activate, then install again.
#     (Also worth a glance: a typo in the import name.)

# Q2: From scratch, in order:
#     python -m venv .venv
#     .\.venv\Scripts\Activate.ps1      (Windows)
#     source .venv/bin/activate         (macOS / Linux)
#     pip install -r requirements.txt

# Q3: __init__.py marks a folder as a package: when you
#     `import textutils`, Python runs textutils/__init__.py first.
#     Ours re-exports shout from the cleaner module, so
#     textutils.shout(...) works and callers never need to know that
#     cleaner.py exists. It can hold imports, shared setup, or be
#     empty -- the folder counts as a package either way.


# Bonus: a condensed, runnable version of the lesson's demo.

def mini_package_demo() -> None:
    demo_dir = Path(tempfile.mkdtemp(prefix="answer_pkg_"))
    pkg = demo_dir / "mathpack"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("", encoding="utf-8")  # just marks the package
    (pkg / "ops.py").write_text(
        "def add(a: float, b: float) -> float:\n    return a + b\n",
        encoding="utf-8",
    )
    sys.path.insert(0, str(demo_dir))
    from mathpack.ops import add
    print("2 + 3 =", add(2, 3))
    sys.path.pop(0)
    shutil.rmtree(demo_dir)


if __name__ == "__main__":
    mini_package_demo()
