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
import os, datetime

@click.command()
@click.option('--in', '-i', 'in_',
              required=True,
              type=click.Path(exists=True, dir_okay=False, readable=True),
              help='values (YAML)')
@click.option('--template', '-t', 'template_path',
              type=click.Path(exists=True, dir_okay=False, readable=True),
              required=True,
              help='Template (Jinja2)')
@click.option('--rename', '-r', nargs=2,
              multiple=True,
              help='-r YKEY VAR will define a Jinja2 variable VAR based on the value of YKEY in the YAML file.')
@click.option('--root', '-R',
              help='If supplied, names a Jinja2 variable that will hold all the top-level YAML values.')
@click.option('--set', '-s', 'set_', nargs=2,
              multiple=True,
              help='Set a value.  E.g., -s var value')
@click.option('--output', '-o',
              type=click.File('w'),
              default='-',
              help='Output file (or - for stdout)')
def main(in_, template_path, rename, root, set_, output):
    with open(in_, "r") as stream:
        yaml = load(stream, Loader=FullLoader)

    template = get_template(template_path)

    template_args = dict()

    if root:
        target = dict()
        template_args[root] = target
    else:
        target = template_args
        
    rename_dict = dict((k, v) for (k, v) in rename)

    for key, value in yaml.items():
        key = rename_dict.get(key, key)
        target[key] = value
        
    for (key, value) in set_:
        template_args[key] = value
        
    template_args['current_date'] = datetime.datetime.today()
    rendered = template.render(**template_args)

    print(rendered, file=output)

def get_template(template_path):
    abs_path = os.path.abspath(template_path)
    template_dir, template_file = os.path.split(abs_path)
    templateLoader = jinja2.FileSystemLoader(searchpath=template_dir)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(template_file)

    return template

if __name__ == '__main__':
    main()

