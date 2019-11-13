from setuptools import setup

setup(
    name='secrender',
    description='Render Jinja2 templates using YAML file for substitutions.',
    version='0.1',
    author='Tom Wood',
    author_email='tom.wood@civicactions.com',
    license='CC',
    packages=['secrender'],
    zip_safe=False,
    install_requires=[
        'click',
        'pyyaml',
        'Jinja2'
    ],
    entry_points = {
        'console_scripts': ['secrender=secrender.secrender:main']
    }
)