"""
Generates the Math 290 template
"""
import os
from dotenv import dotenv_values

generator_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(generator_dir, "..")

def load_file(path=os.path.join(generator_dir, "template.tex")):
    with open("template.tex", "r", encoding="UTF-8") as f:
        return f.read()


def define_vars():
    f = load_file()

    latex_vars = {
        "NAME": None,
        "CLASSNAME": "Math 290",
        "HWNUMBER": None,
        "DUEDATE": None,
        "PROFESSOR": None,
        "SECTION": None,
    }

    latex_vars.update(dotenv_values(dotenv_path=os.path.join(root_dir, ".env")))
    latex_vars.update(dotenv_values(dotenv_path=os.path.join(generator_dir, ".env")))

    template_vars = ""

    for k, v in latex_vars.items():
        if v is None:
            assignment = input(f'What would you like to assign to the variable "{k}"? ')
            latex_vars[k] = v = assignment
        match k:
            case "NAME":
                template_vars += f"\\newcommand{{\\authorName}}{{\\textbf{{{v}}}}}\n"
            case "CLASSNAME":
                template_vars += f"\\newcommand{{\\className}}{{{v}}}\n"
            case "HWNUMBER":
                template_vars += f"\\newcommand{{\\hwTitle}}{{Homework #{v}}}\n"
            case "DUEDATE":
                template_vars += f"\\newcommand{{\\dueDate}}{{{v}}}\n"
            case "PROFESSOR":
                template_vars += f"\\newcommand{{\\professor}}{{{v}}}\n"
            case "SECTION":
                template_vars += f"\\newcommand{{\\classSection}}{{{v}}}\n"
            case _:
                raise ValueError(f"Unrecognized variable {k} with value {v}")
    f.replace("%VARS%", template_vars)