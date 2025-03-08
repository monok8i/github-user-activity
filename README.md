# GitHub User Activity CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This command-line tool allows you to quickly fetch and view the recent activity of any GitHub user. It retrieves event data from the GitHub API and presents it in a user-friendly format.

## Features

*   **Fetch User Events:** Retrieves a list of recent events (e.g., commits, pull requests, issues) for a given GitHub username.
*   **Clear Output:** Displays the event type and the repository name for each event in an easy-to-read format.
*   **Error Handling:** Gracefully handles various API errors, such as rate limiting, user not found, and network issues.
*   **Informative Messages:** Provides helpful error messages and warnings when problems occur.
*   **Command-Line Interface:** Uses `click` to create an intuitive command-line interface.

## Installation

1.  **Prerequisites:**
    *   Python 3.7+

2.  **Installation:**
    ```bash
    git clone https://github.com/monok8i/github-user-activity.git
    cd ./github-user-activity
    
     # activate venv
    
    pip install -e . # install locally for using `github-user-activity` cli
    ```

## Usage

After installation, you can use the `github-user-activity` command from your terminal:

```bash
github-user-activity --username <GITHUB_USERNAME>
