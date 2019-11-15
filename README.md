# Secrender

## Overview

Example tool to render a template using data loaded from a YAML
file.  One intended use case: load an [OSCAL style](https://pages.nist.gov/OSCAL/documentation/schema/ssp/) YAML file and render
a Jinja2 template to produce the markdown for SSP front matter.

To better support the above intended use case, by default
the value of the key 'system_security_plan' in the input values YAML
is mapped to the template variable 'ssp'.

## Installation

You can either run this in a self-contained Docker container (recommended) or installed locally using Python.

### Using Docker

Running _Secrender_ in a Docker container will allow you to use the tool without needing to install the required Python libraries, or, for that matter, Python.

_Secrender_ has been packaged to run using the [DrydockCloud](https://github.com/CivicActions/drydock#what-is-the-drydock-pattern) pattern.

#### Usage

```bash
docker pull drydockcloud/ci-secrender
docker run -v $PWD:/src drydockcloud/ci-secrender --in my-config.yaml --template my-template.md.j2
```

### Python

To run _Secrender_ natively, simply install the requirements using the command below.

```bash
pip install .    # until secrender is in the cheese shop
```

#### Usage

```bash
secrender --in example-ssp.yaml --template example-ssp.md.j2 >ssp.md
```

## Authors

* **Tom Wood** - *Initial work* - [Woodt](https://github.com/woodt)
* **Tom Camp** - [Tom-Camp](https://github.com/Tom-Camp)

## TODO

* would be nice to validate input values against schema
* root element handling is simplistic

## License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.
