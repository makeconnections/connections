from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
from pymongo import MongoClient


def add_mongo_db(event):
    settings = event.request.registry.settings
    url = settings['mongodb.url']
    db_name = settings['mongodb.db_name']
    db = settings['mongodb_conn'][db_name]
    event.request.db = db


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.include('.security')
    # Include Mongo
    config.registry.settings['mongodb_conn'] = MongoClient(settings['mongodb.url'])
    config.add_subscriber(add_mongo_db, NewRequest)
    #
    config.scan()
    return config.make_wsgi_app()
