import click
import sqlite_utils

from roam_to_sqlite import utils


@click.group()
@click.version_option()
def cli():
    """Create an SQLite database containing your Roam Research data"""


@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "json_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.option("-s", "--silent", is_flag=True, help="Print less output")
def convert(db_path, json_path, silent):
    "Save Roam Research data to a SQLite database"
    db = sqlite_utils.Database(db_path)
    with open(json_path) as json_file:
        utils.save_roam(db, json_file)
