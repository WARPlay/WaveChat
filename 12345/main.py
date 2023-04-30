import flask


app = flask.Flask(__name__)


@app.route('/')
@app.route('/Entrance')
def entrance():
    return flask.render_template('entrance.html')
@app.route('/Profile')
def profile():
    return flask.render_template('Profile.html')
@app.route('/LoginorRegister')
def LoginorRegister():
    return flask.render_template('Login-or-Register.html')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')