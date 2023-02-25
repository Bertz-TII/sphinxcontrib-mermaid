from setuptools import find_packages, setup

readme = open("README.rst", encoding="utf-8").read()
changes = open("CHANGELOG.rst", encoding="utf-8").read()
version = "0.8.1"


def long_description():
    """
    return readme + changes, removing directive blocks that are only valid in the context
    of sphinx doc"""

    def remove_block(text, token, margin=0):
        input_lines = text.splitlines()
        for i, l in enumerate(input_lines):
            if l.startswith(token):
                break
        start = i
        end = input_lines.index("", start + margin)
        return "\n".join(input_lines[:start] + input_lines[end:])

    readme_ = remove_block(readme, ".. mermaid::", margin=2)
    readme_ = remove_block(readme_, ".. autoclasstree::")
    readme_ = remove_block(readme_, ".. autoclasstree::")
    readme_ = remove_block(readme_, ".. versionchanged::")
    return f"{readme_}\n\n{changes}"


setup(
    name="sphinxcontrib-mermaid",
    version=version,
    url="https://github.com/mgaitan/sphinxcontrib-mermaid",
    download_url="https://pypi.python.org/pypi/sphinxcontrib-mermaid",
    license="BSD",
    author="Martín Gaitán",
    author_email="gaitan@gmail.com",
    description="Mermaid diagrams in yours Sphinx powered docs",
    long_description=long_description(),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    platforms="any",
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=["sphinxcontrib"],
)
