# GitHub User Activity CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This command-line tool allows you to quickly fetch and view the recent activity of any GitHub user. It retrieves event data from the GitHub API and presents it in a user-friendly format.

This is also sample solution for the [github-user-activity](https://roadmap.sh/projects/github-user-activity) challenge from [roadmap.sh](https://roadmap.sh/).

## How to run

Clone the repository:

```bash
git clone https://github.com/monok8i/github-user-activity.git
cd ./github-user-activity
```

Activate virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Install locally (for using `github-user-activity` command):

```bash
pip install -e .
```

After installation, you can use the `github-user-activity` command from your terminal:

```bash
github-user-activity --username <GITHUB_USERNAME>
```

