import sys
from math import sqrt
from pathlib import Path

# This gives us access to the top-level config.py
root_dir = Path(__file__).resolve().parent.parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from config import HALVE_FILTER_KT, SHOULD_KEYTRACK_EXTRA, SHOULD_KEYTRACK_FILTER


def make_dir(*args) -> None:
    Path(*args).mkdir(parents=True, exist_ok=True)


def if_keytrack_filter(keytrack, default = 0) -> float:
    if SHOULD_KEYTRACK_FILTER:
        return keytrack * (0.5 if HALVE_FILTER_KT else 1)
    return default


def if_keytrack_extra(keytrack, default = 0) -> float:
    return keytrack if SHOULD_KEYTRACK_EXTRA else default


TEMPATE_HELPERS = {
    'sqrt': sqrt,
    'if_keytrack_extra': if_keytrack_extra,
    'if_keytrack_filter': if_keytrack_filter,
    'remap': (lambda x, min, max: x*(max-min) + min),
}
