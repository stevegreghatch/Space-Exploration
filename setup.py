from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    author='mr_blender',
    python_requires='>=3.12, <4',
    include_package_data=True,
    install_requires=[
        'fastapi'
    ],
    scripts=["app.py"]
)
