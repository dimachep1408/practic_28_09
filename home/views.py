import flask

def view_home():
    return flask.render_template('home.html')