import re
from setuptools import setup, find_packages

with open("requirements.in", "r") as fd:
    requirements = fd.read().strip().split("\n")

with open("secrender/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

setup(
    name="secrender",
    description="Render Jinja2 templates using YAML file for substitutions.",
    version=version,
    author="Tom Wood",
    author_email="tom.wood@civicactions.com",
    url="http://github.com/CivicActions/secrender",
    license="CC",
    packages=find_packages(),
    zip_safe=False,
    install_requires=requirements,
    entry_points={"console_scripts": ["secrender=secrender.secrender:main"]},
)
