from setuptools import setup, find_packages

setup(
    name="edsimchecker",
    version="0.1.0",
    packages=find_packages(where='src'),
    install_requires=[],
    author="Eddy Lecoña",
    author_email="crew0eddy@gmail.com",
    description=" A tool for analyzing code snippets and detecting similarities",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/EdsonEddy/edsimchecker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ],
    keywords="code analysis, similarity detection, plagiarism detection, code snippets, code comparison",
    project_urls={
        "Bug Tracker": "https://github.com/EdsonEddy/edsimchecker/issues",
        "Documentation": "https://github.com/EdsonEddy/edsimchecker/wiki",
        "Source Code": "https://github.com/EdsonEddy/edsimchecker",
    },
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'edsimchecker=src.__main__:main',
        ],
    },
)