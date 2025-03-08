import requests
import click
from json.decoder import JSONDecodeError

URL = "https://api.github.com/users/{}/events"


def get_data(username: str) -> list[dict] | None:
    try:
        response = requests.get(URL.format(username))
        status_code = response.status_code
        
        try:
            data = response.json()
        except JSONDecodeError:
            click.secho(f"Failed to parse JSON response for user {username}", fg='red', err=True)
            return None

        match status_code:
            case 200:
                if len(data):
                    return data
                click.secho(f"({status_code}) Data for user {username} is empty", fg='yellow', err=True)
            case 403:
                message = data.get('message', 'Unknown Error')
                click.secho(f"({status_code}) Rate limit exceeded: {message}", fg='red', err=True)
            case 404:
                click.secho(f"({status_code}) User {username} not found", fg='yellow', err=True)
            case _:
                message = data.get('message', 'Unknown Error')
                click.secho(f"({status_code}) Failed to fetch data: {message}", fg='red', err=True)
        return None

    except requests.exceptions.RequestException as e:
        click.secho(f"Request failed: {e}", fg='red', err=True)
        return None



def get_activity(data: list[dict]) -> None:
    if data:
        for event in data:
            click.secho(f"Event: {event['type']}, Repo: {event['repo']['name']}", fg='green')


@click.command()
@click.option("--username", '-u', required=True, help="GitHub username")
def main(username: str) -> None:
    data = get_data(username)
    if data is None:
        click.get_current_context().exit(1)
    get_activity(data)
