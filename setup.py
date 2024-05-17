from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    python_requires="3.12, <4",
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
    ],
    scripts=["app.py"]
)
