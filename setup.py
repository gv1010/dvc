from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="gv1010",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gv1010/dvc",
    author_email="gv281093@gmail.com",
    packages=["src"],
    python_requires=">=3.8",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)