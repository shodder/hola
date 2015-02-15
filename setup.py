
from setuptools import setup, find_packages

setup(
    name='hola',
    version='0.1.0',
    author='Simon Hodder',
    author_email='hodder.simon@gmail.com',
    description='Demo Flask app running behind NGINX and UWSGI',
    packages=find_packages(),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': {
            'hola = hola.__main__:main'
        }
    },
    install_requires={
        'flask',
        'logbook',
    }
)
