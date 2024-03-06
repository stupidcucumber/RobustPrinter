from setuptools import find_packages, setup

with open('README.md') as desc_f:
    long_description = desc_f.read()

setup(
    name='robustprinter',
    version='0.0.10',
    description='Package for easy printing and logging to the terminal/console.',
    package_dir={'': 'main'},
    packages=find_packages('main'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/stupidcucumber/RobustPrinter.git',
    author='Ihor Kostiuk',
    author_email='sk.companymail@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent'
    ],
    install_requires=[],
    extras_require={
        'dev' : ['twine>=4.0.2']
    },
    python_requires='>=3.10'
)