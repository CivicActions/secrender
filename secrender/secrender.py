#! /usr/bin/env python

# Example tool to render a template using data loaded from a YAML
# file.  One intended use case: load an OSCAL style YAML file and render
# a Jinja2 template to produce the markdown for SSP front matter.
#
# To better support the above intended use case, by default
# the value of the key 'system_security_plan' in the input values YAML
# is mapped to the template variable 'ssp'.
# 
# # secrender --in ssp.yaml --template ssp.md.j2 >ssp.md

# TODO
# - would be nice to validate input values against schema
# - root element handling is simplistic

import click
from yaml import load, FullLoader
import jinja2
import os

@click.command()
@click.option('--in', '-i', 'in_',
              required=True,
              type=click.Path(exists=True, dir_okay=False, readable=True),
              help='values (YAML)')
@click.option('--template', '-t', 'template_path',
              type=click.Path(exists=True, dir_okay=False, readable=True),
              required=True,
              help='Output template (Jinja2)')
@click.option('--root', '-r',
              default='ssp:system_security_plan',
              help='Maps the root element -- key_in_template:key_in_yaml')
def main(in_, template_path, root):
    with open(in_, "r") as stream:
        yaml = load(stream, Loader=FullLoader)

    template = get_template(template_path)

    template_args = dict()
    template_key, yaml_key = root.split(':')

    if yaml_key not in yaml:
        raise click.ClickException('Key {0} not found in input values'.format(yaml_key))
    
    template_args[template_key] = yaml[yaml_key]
    output = template.render(**template_args)

    print(output)

def get_template(template_path):
    abs_path = os.path.abspath(template_path)
    template_dir, template_file = os.path.split(abs_path)
    templateLoader = jinja2.FileSystemLoader(searchpath=template_dir)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(template_file)

    return template

if __name__ == '__main__':
    main()

