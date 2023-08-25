from setuptools import setup, find_packages

setup(
    name='image_format_converter',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ]
    },
    entry_points={
        'console_scripts': [
            'image-format-converter=image_format_converter.converter:main',
        ],
    },
    author="Carlos Aponte",
    author_email="carlos@caponte.io",
    description="A lightweight Python package that converts images in a directory from one format to another while "
                "preserving their dimensions.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/0xCaponte/image_format_converter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)