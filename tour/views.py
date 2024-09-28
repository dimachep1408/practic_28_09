import flask
from .app import tour


def render_tour():
    return flask.render_template(template_name_or_list= "tour.html")