from setuptools import setup, find_packages


setup(
    name="my_library",
    version="1.0",
    packages=find_packages(),
        entry_points = {
        'console_scripts': ['hello=main3:main']}
)
