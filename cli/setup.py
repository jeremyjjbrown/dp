from setuptools import find_packages, setup
import sys

if sys.version_info < (3, 7):
    sys.exit('Sorry, Python < 3.7 is not supported')

setup(
    name='dpctl',
    version='0.0.1',
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    license='Properitary unless otherwise stated',
    install_requires=[
        'PyYAML==5.3.1',
        'click>=8.0.3',
        'flake8==3.8.4',
        'pathlib2>=2.3.5',
        'pytest>=6.2.1',
        'requests>=2.25.1',
    ],
    entry_points={
        'console_scripts': [
            'dpctl = dpctl.cli:cli',
        ],
    },
)
