from math import log, sqrt

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
]
Carlos = [  # wendycarlos.com/resources/pitch.html
    ("Alpha", 15.385),
    ("Beta" , 18.809),
    ("Gamma", 34.188),
]



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

def generate_tunings(tuning_group, tuning_f, tracking):
    for x in eval(tuning_group):
        tuning = tuning_f(x)
        make_dir(tuning_group, tuning)
        for template in templates:
            filename = str(template.name).replace(".jinja", f" ({tuning}).repatch")
            filepath = Path(tuning_group) / tuning / filename
            with open(filepath, "w") as f:
                repatch = template.render(
                    x = x, tracking = tracking, sqrt = sqrt,
                    upper_half = (lambda x: (1 + x) / 2),
                )
                f.write(repatch)


# Generate patch files

generate_tunings (
    tuning_group = "EDOs",
    tuning_f = (lambda x: f"{x}-EDO"),
    tracking = (lambda x: (12 / x)),
)

generate_tunings (
    tuning_group = "EDTs",
    tuning_f = (lambda x: f"{x}-EDT"),
    tracking = (lambda x: ( (log(3) / log(2)) * (12 / x) )),
)

generate_tunings (
    tuning_group = "Carlos",
    tuning_f = (lambda t: t[0]),
    tracking = (lambda t: (12 / t[1])),
)
