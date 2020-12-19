import json
import jinja2
import os

template_file = "config.j2"
json_file = "params.json"
output_directory = "output"

config_params = json.load(open(json_file))

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."), trim_blocks=True, lstrip_blocks=True)

template = env.get_template(template_file)

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

print("Creating template...")
for param in config_params:
    result = template.render(param)
    f = open(os.path.join(output_directory, param['hostname'] + ".config"), "w")
    f.write(result)
    f.close()
    print("Configuration created")
print("Done,....")