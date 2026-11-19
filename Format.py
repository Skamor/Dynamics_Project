from Calculations import create_table, calc_all
from jinja2 import Template

heights = calc_all()
table = create_table(heights)
print(table)

with open("template.txt", "r") as file:
    temp = file.read()

print(temp)

def generate_template(temp, attempt):
    template = Template(temp)
    output = template.render(mass=attempt[0], real=attempt[1], calculated=attempt[2], error=attempt[3])
    return output

with open("output.md", "w") as out:
    out.write("|mass (kg)|experimental (m)|theoretical (m)|error deviation (\%)|\n")
    out.write("|---|---|---|---|\n")
    for attempt in table:
        out.write(generate_template(temp, attempt) + "\n")
