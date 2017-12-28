from flask import Flask, request, json, Response
from sites.zimuku import get_movie_list, get_zimu_list, get_download_url
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)


@app.route('/api/movielist', methods=['POST'])
def movielist():
    html = request.form['html']
    ret = get_movie_list(html)
    return Response(ret, mimetype='application/json')


@app.route('/api/zimus', methods=['POST'])
def zimus():
    html = request.form['html']
    ret = get_zimu_list(html)
    return Response(ret, mimetype='application/json')


@app.route('/api/zimu_download_url', methods=['POST'])
def zimu_download_url():
    html = request.form['html']
    ret = get_download_url(html)
    return Response(ret, mimetype='application/json')


@app.route('/')
def zimudog():
    ret = 'hello'
    return Response(ret, mimetype='application/json')


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
