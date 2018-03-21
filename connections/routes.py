from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound,
)
from pyramid.security import (
    Allow,
    Everyone,
)


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    config.add_route('view_seeds', '/s')
    config.add_route('view_seed', '/s/{seed_id}', factory=seed_factory)

    config.add_route('view_nurtures', '/n')
    config.add_route('view_nurture', '/n/{nurture_id}', factory=nurture_factory)


def seed_factory(request):
    seed_id = int(request.matchdict['seed_id'])
    seed = request.db.get_collection('seeds').find_one({'seed_id': seed_id})
    if seed is None:
        raise HTTPNotFound
    return SeedResource(seed)


class SeedResource(object):
    def __init__(self, seed):
        self.seed = seed

    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
        ]


def nurture_factory(request):
    nurture_id = request.matchdict['nurture_id']
    nurture = request.dbsession.query(Nurture).filter_by(nurture_id=nurture_id).first()
    if nurture is None:
        raise HTTPNotFound
    return NurtureResource(nurture)


class NurtureResource(object):
    def __init__(self, nurture):
        self.nurture = nurture

    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
        ]
