from setuptools import setup, find_packages

setup(
    name='research-base',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # dependencies
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.11',
    ],
    author='Florian Rascoussier (0nyr), Clément Lahoche (Fitz35)',
    author_email='darkvoldorious@gmail.com',
    description='A python package for easy python programming for research projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
