from setuptools import setup


def read_requirements():
    with open("requirements.txt", "r") as f:
        return [i.strip() for i in f.readlines()]


setup(
    name="plateplot",
    version="0.1",
    url="https://github.com/FrancisCrickInstitute/plateplot",
    description="Microtitre plate plotting",
    author="Scott Warchal",
    author_email="scott.warchal@crick.ac.uk",
    python_requires=">=3.6",
    license="MIT",
    packages=["plateplot"],
    install_requires=read_requirements(),
    zip_safe=True,
)
