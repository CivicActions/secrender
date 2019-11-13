# Overview

Example tool to render a template using data loaded from a YAML
file.  One intended use case: load an OSCAL style YAML file and render
a Jinja2 template to produce the markdown for SSP front matter.

To better support the above intended use case, by default
the value of the key 'system_security_plan' in the input values YAML
is mapped to the template variable 'ssp'.

# Usage

```
$ secrender --in example-ssp.yaml --template example-ssp.md.j2 >ssp.md
```

# Installation:

```
$ pip install .    # until secrender is in the cheese shop
```

# TODO

- would be nice to validate input values against schema
- root element handling is simplistic
