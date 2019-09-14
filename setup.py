# from setuptools import setup, find_packages
from setuptools import find_packages, setup

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='devsunkylogger',
    version='0.2.3',
    description='Useful tools to work with Elastic stack in Python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Ilesanmi Omoniyi',
    author_email='omoniyi24@gmail.com',
    keywords=['Elastic', 'ElasticSearch', 'Elastic Stack', 'Python 3', 'Elastic 7'],
    url='https://github.com/omoniyi24/dev-sunky-logger'
)

install_requires = [
    'elasticsearch>=7.0.2',
    'jinja2'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
