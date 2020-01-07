# -*-coding:utf-8 -*-

import flask
from epsilon.views import epsilon
from omega.views import omega

app = flask.Flask('lightning')

prefix = '/api/v1'
app.register_blueprint(epsilon, url_prefix=prefix + '/epsilon')
app.register_blueprint(omega, url_prefix=prefix + '/omega')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)



