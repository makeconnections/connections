import re
from docutils.core import publish_parts
from pyramid.compat import escape
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config


@view_config(route_name='view_seeds', renderer='../templates/seeds.jinja2')
def view_seeds(request):
    coll = request.db.get_collection('seeds')
    coll.insert({'seed_id': coll.find().count()})
    results = [x for x in coll.find()]
    return dict(results=results)


@view_config(route_name='view_seed', renderer='../templates/seed.jinja2')
def view_seed(request):
    return dict(result=request.context.seed)
