#!/usr/bin/env python
import json
from twitterlib.handlers import TwitterBase
from flask import Flask, url_for, redirect, sessions, session

app = Flask(__name__)
app.config['secret-key'] = 'jbk'


def main():
    # TODO: Move this to a configuration or environment file (pref environment)
    API_KEY = config.state
    API_SECRET = config.state

    my_update = TwitterBase('https://api.twitter.com',
                            api_key=API_KEY,
                            api_secret=API_SECRET)

    my_status = [my_update.return_my_status().decode().replace("'", '"')]

    for index, data in enumerate(my_status):
        tweet_dict = json.loads(data)
        messages = [x['text'] for x in tweet_dict]
        for x in messages:
            print('Index: {} Tweet: {}'.format(index, x))


if __name__ == '__main__':
    main()