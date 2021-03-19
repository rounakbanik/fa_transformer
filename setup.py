from setuptools import setup

setup(
    name='fa_transformer',
    version='0.1.2',    
    description='A package containing custom Factor Analysis Transformers',
    url='https://github.com/rounakbanik/fa_transformer',
    author='Rounak Banik',
    author_email='rounakbanik@gmail.com',
    license='MIT',
    packages=['fa_transformer'],
    install_requires=['numpy',
                      'sklearn',
                      'pandas',
                      'factor_analyzer',                   
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',       
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)