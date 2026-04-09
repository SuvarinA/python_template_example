from string import Template

with open("settings.yml.template", "r") as f:
        src = Template(f.read())

result = src.substitute(
          {
            "env" : "dev",
            "x1" : 101,
            "x2" : 102,
            "x3" : 103
          }
)

with open("settings.yml", "w") as f:
          f.write(result)

print(result)
