import click
import ckanext.likes.model as model



# def init_db():
#     import ckan.model as model
#     from ckanext.likes.utils_db import init_tables
#     init_tables(model.meta.engine)



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
    model.init_db()
    click.echo("DB tables added.")



likes.add_command(init)
    

# ckan -c /etc/ckan/dov/ckan.ini likes init -- init tables for likes in dov database
# ckan -c test.ini likes init -- init tables for likes in test db
# ckan -c 
