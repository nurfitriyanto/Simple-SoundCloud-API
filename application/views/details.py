#! /application/views/details.py

# project : Soundcloud API
# creator : https://github.com/nurfitriyanto
# endpoint : http://0.0.0.0:6969/api/v1_2/details?id=236143578

import json
import urllib
import requests
import lxml.html
import re
from application import app
from config.general import CLIENT_ID
from flask import request, render_template, url_for, redirect, jsonify
from string import digits
from utils.helper import first_words

@app.route('/api/v1_2/details')
def details():
    try:
        id_file = request.args.get('id')
        url     = 'http://api.soundcloud.com/tracks/%s.json?client_id=%s' % (id_file, CLIENT_ID)
        req     = requests.get(url)
        results = json.loads(req.text)

        rows = {}
        if results:
            #begin : query name for recomended file
            titleString = re.sub('\W+',' ', results['title'])
            cleanString = str(titleString.replace('_', ' '))
            name_html   = lxml.html.document_fromstring(cleanString.translate(None, digits))
            queryName   = first_words(name_html.cssselect('body')[0].text_content()[:25], 1)
            #end : query name for recomended file

            #begin : request recomended file from soundcloud api
            url_recomended      = "http://api.soundcloud.com/tracks.json?client_id=%s&limit=10&offset=1&q=%s" % (CLIENT_ID, queryName)
            req_recomended      = requests.get(url_recomended)
            results_recomended  = json.loads(req_recomended.text)
            #end : request recomended file from soundcloud api

            rows['meta'] = {
                'code'      : 200,
                'message'   : 'OK'
            }
            rows['data'] = results
            rows['recomended'] = results_recomended
        else:
            rows['meta'] = {
                'code'      : 404,
                'message'   : 'error : data not found'
            }
            rows['data'] = 0
            rows['recomended'] = 0
    except:
        rows['meta'] = {
            'code'      : 500,
            'message'   : 'error 500'
        }
        rows['data'] = 0
        rows['recomended'] = 0
    return jsonify(rows)
