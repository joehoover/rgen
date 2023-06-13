import os
import pkg_resources
from pkg_resources import resource_filename
import typer
import yaml
import re

app = typer.Typer()

def get_template(template_name: str) -> str:
    template_path = resource_filename(__name__, f"data/{template_name}")
    with open(template_path, 'r') as file:
        return file.read()
    
@app.command()
def extract(template_path1: str = 'cog_readme_template.md', template_path2: str = 'replicate_readme_template.md'):
    templates = [get_template(template_path1), get_template(template_path2)]
    template_vars = set()

    for template in templates:
        template_vars.update(re.findall("{(.*?)}", template))

    with open("readme.yaml", "w") as file:
        yaml.dump({key: "" for key in template_vars}, file)

@app.command()
def generate(input_yaml: str = 'readme.yaml', 
             template_path1: str = 'data/cog_readme_template.md', 
             template_path2: str = 'data/replicate_readme_template.md',
             output_file1: str = 'COG_README.md', 
             output_file2: str = 'REPLICATE_README.md'):

    with open(input_yaml, 'r') as yaml_file:
        replacement_values = yaml.load(yaml_file, Loader=yaml.FullLoader)

    for template_path, output_file in zip([template_path1, template_path2], [output_file1, output_file2]):
        template = get_template(template_path)
        output_from_parsed_template = template.format(**replacement_values)
        with open(output_file, "w") as fh:
            fh.write(output_from_parsed_template)