from math import log2, sqrt

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
    29,          # good fifth
    34, 41, 53,  # approximate JI
]
EDTs = [
    26,  # Double Bohlen-Pierce
    30,  # Stretched 19EDO
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

def generate_tunings (
    tuning_group,  tuning_f,  tracking,
    get_x = lambda x: x,
    monopoly = lambda x: (8/x) - (1/6),
):
    for x in eval(tuning_group):
        tuning = tuning_f(x)
        make_dir(tuning_group, tuning)
        for template in templates:
            filename = str(template.name).replace(".jinja", f" ({tuning}).repatch")
            filepath = Path(tuning_group) / tuning / filename
            with open(filepath, "w") as f:
                repatch = template.render(
                    x = get_x(x),
                    tracking = tracking,
                    sqrt = sqrt,
                    upper_half = (lambda x: (1 + x) / 2),
                    monopoly = monopoly,
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
    tracking = (lambda x: log2(3) * 12 / x),
    monopoly = (lambda x: log2(3) * (8 / x) - (1/6)),
)

generate_tunings (
    tuning_group = "Carlos",
    tuning_f = (lambda t: t[0]),
    get_x = (lambda t: t[1]),
    tracking = (lambda x: (12 / x)),
)
