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
    13, 26       # Bohlen-Pierce
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

def generate_tunings(tuning_group, **kwargs):
    for x in EDOs:
        tuning = f"{x}-EDO"
        make_dir(tuning_group, tuning)
        for template in templates:
            filename = str(template.name).replace(".jinja", f" ({tuning}).repatch")
            filepath = Path(tuning_group) / tuning / filename
            with open(filepath, "w") as f:
                repatch = template.render(x=x, **kwargs)
                f.write(repatch)

generate_tunings (
    tuning_group = "EDOs",
    tracking = (lambda x: (12 / x)),
    tracking_upper_half = (lambda x: (1 + (12 / x)) / 2),
)

for x in EDTs:
    make_dir("EDTs", f"{x}-EDT")
