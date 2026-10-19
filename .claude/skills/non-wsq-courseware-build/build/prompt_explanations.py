"""
"What it does" text for every step prompt (EXPLAIN), the formulas Gemini should
write (FORMULAS) and the explanations of each lab's sample prompts
(SAMPLE_EXPLAIN), keyed by lab number and prompt letter.

The text lives beside each lab in data_domainN.py ("explain", "formulas",
"sample_explain"), so a prompt and its explanation are edited together. This
module only indexes it, and fails the build if a lab's explanations and prompts
are out of step.
"""
import glob
import importlib
import os
import re

from lab_prompts import LETTERS, prompt_rows

HERE = os.path.dirname(os.path.abspath(__file__))
_LABS = []
for _p in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    _m = importlib.import_module(os.path.basename(_p)[:-3])
    for _n in dir(_m):
        if re.fullmatch(r"DOMAIN\d+", _n):
            _LABS.extend(getattr(_m, _n))

EXPLAIN, FORMULAS, SAMPLE_EXPLAIN = {}, {}, {}
for _lab in _LABS:
    _n, _rows, _ex = _lab["num"], prompt_rows(_lab), _lab.get("explain", [])
    assert len(_ex) == len(_rows), (
        f"Lab {_n}: {len(_rows)} prompts but {len(_ex)} explanations - "
        + "; ".join(f"{r['letter']} step {r['step']}: {r['text'][:40]}" for r in _rows))
    EXPLAIN[_n] = dict(zip(LETTERS, _ex))
    FORMULAS[_n] = _lab.get("formulas", {})
    if _lab.get("sample_explain"):
        assert len(_lab["sample_explain"]) == len(_lab.get("sample_prompts", [])), f"Lab {_n}: sample_explain count"
        SAMPLE_EXPLAIN[_n] = _lab["sample_explain"]
