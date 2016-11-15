#! /application/views/detail.py

# project : Soundcloud API
# creator : https://github.com/nurfitriyanto
# endpoint : http://0.0.0.0:6969/api/v1_2/download?id=236143578

import json
import requests
from application import app
from config.general import CLIENT_ID
from flask import request, url_for, redirect, jsonify

@app.route('/api/v1_2/download')
def download():
    try:
        id_file     = request.args.get('id')
        url         = 'http://api.soundcloud.com/tracks/%s/streams?client_id=%s' % (id_file, CLIENT_ID)
        req         = requests.get(url)
        results     = json.loads(req.text)

        rows = {}
        if results:
            rows['meta'] = {
                'code'      : 200,
                'message'   : 'OK'
            }
            rows['data'] = {
                'url_file'      : results['http_mp3_128_url'].replace('\u0026', '&'),
                'url_preview'   : results['preview_mp3_128_url']
            }
        else:
            rows['meta'] = {
                'code'      : 404,
                'message'   : 'error : data not found'
            }
            rows['data'] = 0
    except:
        rows['meta'] = {
            'code'      : 500,
            'message'   : 'error 500'
        }
        rows['data'] = 0
    return jsonify(rows)
