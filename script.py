from math import sqrt

import pygit2
import os

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

## Tunings

EDOs = [
    24, 36,      # extended 12TET
    14, 15, 16,  # xenharmonic
    17, 22, 27,  # superpyth
    19, 31, 43,  # meantone
    34, 41, 53,  # approximate JI
]
EDTs = [
    26       # Double Bohlen-Pierce
],
Carlos = {
    "Alpha": 78.0,
    "Beta": 63.8,
    "Gamma": 35.1,
}


# Basic Setup
# repo = pygit2.Repository(".")
# walker = repo.walk(repo.head.target)
env = Environment(
    loader = FileSystemLoader("templates")
)
templates = list(map(
    env.get_template, env.list_templates()
))


def make_dir(*args):
    Path(*args).mkdir(parents=True, exist_ok=True)


# Create tunings

def generate_tunings(tuning_group, tuning_f, **kwargs):
    for x in EDOs:
        tuning = tuning_f(x)
        make_dir(tuning_group, tuning)
        for template in templates:
            filename = str(template.name).replace(".jinja", f" ({tuning}).repatch")
            filepath = Path(tuning_group) / tuning / filename
            with open(filepath, "w") as f:
                repatch = template.render(x=x, **kwargs)
                f.write(repatch)

generate_tunings (
    tuning_group = "EDOs",
    tuning_f = (lambda x: f"{x}-EDO"),
    tracking = (lambda x: (12 / x)),
    tracking_upper_half = (lambda x: (1 + (12 / x)) / 2),
    tracking_sqrt = (lambda x: sqrt(12 / x)),
)

for x in EDTs:
    make_dir("EDTs", f"{x}-EDT")
