import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='quality-match-homework',
    version='0.0.1',
    author='David Hoof',
    author_email='dhoof@gmx.de',
    description='Quality Match Homework',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/davidhoof/quality-match-homework.git',
    project_urls={
        "Bug Tracker": "https://github.com/davidhoof/quality-match-homework/issues"
    },
    license='MIT',
    packages=['quality-match-homework'],
    install_requires=[
        'matplotlib~=3.6.1',
        'imageio~=2.22.2',
        'pandas~=1.5.1',
        'setuptools~=60.2.0'
    ],
)
