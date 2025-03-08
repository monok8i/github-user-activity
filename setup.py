from setuptools import setup, find_packages

setup(
    name="github-user-activity",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "github-user-activity=github_user_activity.cli:main",
        ],
    },
)
