import flask

def view_user():
    return flask.render_template('user.html')