from setuptools import setup, find_packages

setup(
    name="wisefrog",
    version="0.1",
    packages=find_packages(),
    package_data={
        '': ['*.pytorch'],  # All .pytorch files anywhere in the package
    },
    entry_points={
        'console_scripts': [
            'wisefrog = wisefrog.wisefrog:main',
        ],
    },
    install_requires=[
        'pandas==2.2.1',
        'torch==2.2.1',
        'requests==2.31.0',
        'argparse==1.1',
        'Bio',
    ], 
    python_requires='>=3.9',
)