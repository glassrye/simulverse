#!/usr/bin/env python
import json
import os
from twitterlib.handlers import TwitterBase
from wtforms import Form
from wtforms import TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, url_for, redirect, sessions, session

app = Flask(__name__)
app.config['secret-key'] = 'jbk'

class Config(object):
    API_KEY = os.environ['MARION_API_KEY']
    API_SECRET = os.environ['MARION_API_SECRET']
    APP_SEC_KEY = os.environ['MARION_APP_SEC_KEY']


class MyBaseForm(Form):
    pass

class TwitForm(MyBaseForm):
    tweet_message = TextAreaField('')
    pass

def main():
    my_update = TwitterBase('https://api.twitter.com',
                            api_key=Config.API_KEY,
                            api_secret=Config.API_SECRET)

    my_status = [my_update.return_my_status().decode().replace("'", '"')]

    for index, data in enumerate(my_status):
        tweet_dict = json.loads(data)
        messages = [x['text'] for x in tweet_dict]
        for x in messages:
            print('Index: {} Tweet: {}'.format(index, x))


if __name__ == '__main__':
    main()