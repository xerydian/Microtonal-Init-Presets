from math import log2  # noqa: I001
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from microtonal_init_presets.lib import TEMPATE_HELPERS, make_dir
from config import Carlos, EDOs, EDTs

_ = (EDOs, EDTs, Carlos)  # used in eval

env = Environment(
    loader = FileSystemLoader("templates")
)
templates = list(map(
    env.get_template, env.list_templates()
))


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
                    x = get_x(x), tracking = tracking(get_x(x)),
                    monopoly = monopoly, **TEMPATE_HELPERS
                )
                f.write(repatch)


def main() -> None:
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
