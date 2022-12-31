from setuptools import setup

setup(
    name='foodsearch',
    packages=['foodsearch'],
    include_package_data=True,
    install_requires=[
        'flask', 
        'requests',
    ],
)