from tour import tour, render_tour
from .setting import practic_app

tour.add_url_rule(rule = "/tour",view_func= render_tour)

practic_app.register_blueprint(blueprint= tour)