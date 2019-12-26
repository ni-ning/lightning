# -*-coding:utf-8 -*-

import flask
from alpha.views import alpha
from epsilon.views import epsilon

app = flask.Flask('lightning')

prefix = '/api/v1'
app.register_blueprint(alpha, url_prefix=prefix + '/alpha')
app.register_blueprint(epsilon, url_prefix=prefix + '/epsilon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)



