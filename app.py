# -*-coding:utf-8 -*-

import flask
from alpha.views import alpha

app = flask.Flask('alpha')

prefix = '/api/v1'
app.register_blueprint(alpha, url_prefix=prefix + '/alpha')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)



