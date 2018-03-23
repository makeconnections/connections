import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
]

_req = """
    'bcrypt',
    'docutils',
    'gunicorn',
    'plaster_pastedeploy',
    'pyramid >= 1.9a',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_retry',
    'pyramid_tm',
    'transaction',
    'waitress',
    'webtest',
"""

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='connections',
    version='0.0',
    description='connections',
    long_description=README,
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = connections:main',
        ],
        'console_scripts': [
            'connections_demo = connections.scripts.demo:main',
        ],
    },
)
