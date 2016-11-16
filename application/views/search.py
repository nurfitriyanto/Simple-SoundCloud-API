#! /application/views/search.py

# project : Soundcloud API
# creator : https://github.com/nurfitriyanto
# endpoint : http://0.0.0.0:6969/api/v1_2/search?q=simple&genres=metal&limit=1&offset=1

import json
import urllib
import requests
from application import app
from config.general import CLIENT_ID
from flask import request, render_template, redirect, jsonify

@app.route('/api/v1_2/search')
def search():
    try:
        #begin : get parameter
        query       = request.args.get('q')
        genres      = request.args.get('genres')
        if request.args.get('limit'):
            limit = int(request.args.get('limit'))
        else:
            limit = 10
        if request.args.get('offset'):
            offset = int(request.args.get('offset'))
        else:
            offset = 1
        #end : get parameter

        #begin : request from api soundcloud
        url = 'http://api.soundcloud.com/tracks.json?client_id=%s&limit=%s&offset=%s' % (CLIENT_ID, limit, offset)
        if query:
            url += "&q=%s" % query
        if genres:
            url += "&genres=%s" % genres
        req = requests.get(url)
        results = json.loads(req.text)
        #end : request from api soundcloud
        rows = {}
        if results:
            if len(results) >= limit:
                pageNext = int(offset+1)
                pagePrev = int(pageNext-2)
            else:
                pageNext = 0
                pagePrev = 0
            rows['meta'] = {
                'code'      : 200,
                'message'   : 'OK'
            }
            rows['attribute'] = {
                'query'     : query,
                'genres'    : genres
            }
            rows['pagination'] = {
                'offset'    : offset,
                'limit'     : limit,
                'pageNext'  : pageNext,
                'pagePrev'  : pagePrev
            }
            rows['data'] = results
        else:
            rows['meta'] = {
                'code'      : 404,
                'message'   : 'error : data is empty'
            }
            rows['data'] = 0
    except:
        rows = {}
        rows['meta'] = {
            'code'      : 500,
            'message'   : 'error 500'
        }
        rows['data'] = 0
    return jsonify(rows)
