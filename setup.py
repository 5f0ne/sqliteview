from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="sqliteview",             # This name is used in: pip install hello-world
    version="1.0.1",
    author="5f0",
    url="https://github.com/5f0ne/sqliteview",
    description="Visualize SQLite files",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[
        "hash_calc"
    ],
     entry_points={
        "console_scripts": [
            "sqliteview = sqliteview.__main__:main"
        ]
    }
)
