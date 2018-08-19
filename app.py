#!/usr/bin/env python
import json
import os
import sys
sys.path.append('/Users/james/marionwork/simulverse')
from twitterlib.handlers import TwitterBase
from wtforms import Form
from wtforms import TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, url_for, redirect, sessions, session

class Config(object):
    API_KEY = os.environ['MARION_API_KEY']
    API_SECRET = os.environ['MARION_API_SECRET']
    APP_SEC_KEY = os.environ['MARION_APP_SEC_KEY']


class MyBaseForm(Form):
    pass

class TwitForm(MyBaseForm):
    tweet_message = TextAreaField(label='WTF, eh?')

app = Flask(__name__)
app.config['secret-key'] = Config.APP_SEC_KEY

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/twitter')
def twitter():
    return_map = {}
    my_update = TwitterBase('https://api.twitter.com',
                            api_key=Config.API_KEY,
                            api_secret=Config.API_SECRET)

    my_status = [my_update.return_my_status().decode().replace("'", '"')]

    for index, data in enumerate(my_status):
        tweet_dict = json.loads(data)
        messages = [x['text'] for x in tweet_dict]
        for x in messages:
            print('Index: {} Tweet: {}'.format(index, x))
            return_map[index] = x
    return return_map

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry. Page Was Not Found...'

@app.errorhandler(500)
def internal_server_error(e):
    return 'Woops. Something serious went wrong...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)