from setuptools import setup

setup(
    name='data-faker',
    version='1.0',
    url='https://github.com/subinsoman/data-faker.git',
    license='MIT',
    author='subin.soman',
    author_email='tosubins@gmail.com',
    description='Generate synthetic datasets for Pandas using their definitions',
    packages=['data_faker', 'data_faker.examples'],
    package_dir={'data_faker': 'data_faker',
                 'data_faker.examples': 'data_faker/examples'},
    install_requires=['numpy', 'faker', 'ruamel.yaml', 'pandas'],
    entry_points={
        'console_scripts': [
            'datafaker=data_faker.generator:main',
        ],
    },
)
