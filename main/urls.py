from tour import tour, render_tour
from home import home_app, view_home
from user import user_app, view_user


from .setting import practic_app




tour.add_url_rule(rule = "/tour",view_func= render_tour)
home_app.add_url_rule(rule = "/", view_func= view_home)
user_app.add_url_rule(rule = "/user", view_func= view_user)

practic_app.register_blueprint(blueprint= tour)
practic_app.register_blueprint(blueprint= home_app)
practic_app.register_blueprint(blueprint= user_app)