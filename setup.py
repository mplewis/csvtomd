from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='csvtomd',
    version='0.3.0',
    description='Convert your CSV files into Markdown tables.',
    long_description=long_description,
    url='https://github.com/mplewis/csvtomd',
    license='MIT',
    author='Matthew Lewis',
    author_email='matt@mplewis.com',
    packages=['csvtomd'],
    entry_points={
        'console_scripts': [
            'csvtomd = csvtomd:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing :: Markup'
    ],
)
