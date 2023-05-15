import click
import ckanext.likes.model as model


def get_commands():
    return [likes]

@click.group()
def likes():
    """Likes extension for CKAN
    
    Usage: 

        ckan -c <path to CKAN config file> likes init
            - Creates the database tables that the ckanext-likes uses

        The commands should be run from the ckanext-lies directory and expect
        a development.ini file to be present. Most of the time you will
        specify the config explicitly.

    """

@likes.command()
def init():
    model.setup()
    click.echo("DB tables added.")



likes.add_command(init)
    


