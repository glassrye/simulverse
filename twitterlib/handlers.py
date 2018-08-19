import requests as rq
import oauth2 as oauth
import os
from urllib.parse import urlencode


class OauthHandler(object):

    def __init__(self, base_url, api_key, api_secret):
        """

        :param base_url:
        :param api_key:
        :param api_secret:
        """
        self.CONSUMER_SECRET = os.environ['CONSUMER_SECRET'].encode('utf-8')
        self.CONSUMER_KEY = os.environ['CONSUMER_KEY'].encode('utf-8')
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret

    def get_oauth_url(self):
        """

        :return:
        """
        _consumer = oauth.Consumer(key=self.CONSUMER_KEY, secret=self.CONSUMER_SECRET)
        _token = oauth.Token(key=self.api_key, secret=self.api_secret)
        _client = oauth.Client(_consumer, _token)
        _resp, _content = _client.request(self.base_url, method='GET', body="".encode('utf-8'), headers=None)
        return _content

    def post_oauth_url(self):
        _consumer = oauth.Consumer(key=self.CONSUMER_KEY, secret=self.CONSUMER_SECRET)
        _token = oauth.Token(key=self.api_key, secret=self.api_secret)
        _client = oauth.Client(_consumer, _token)
        _resp, _content = _client.request(self.base_url, method='POST', body="".encode('utf-8'), headers=None)
        return _content


class RequestHandler(object):

    def __init__(self, base_url, verify=False):
        """

        :param base_url:
        :param verify:
        """
        self.base_url = base_url
        self.verify = verify

    def connect(self, request_type, path, parameters=None, data=None, content_type=None, debug=False,):
        """

        :param request_type:
        :param path:
        :param parameters:
        :param data:
        :param content_type:
        :param debug:
        :return:
        """
        if content_type is None:
            common_headers = {
                "Content-Type": "application/json"
            }
        else:
            common_headers = {
                "Content-Type": "{}".format(content_type)
            }

        full_url = '{}/{}'.format(self.base_url, path)

        if request_type == 'GET':
            result = rq.get(full_url,
                            headers=common_headers,
                            params=parameters,
                            verify=self.verify,
                            timeout=(5, 60))
        if request_type == 'POST':
            raise NotImplementedError('POST method not implemented yet')

        if request_type == 'HEAD':
            raise NotImplementedError('HEAD method not implemented yet')

        if request_type == 'PATCH':
            raise NotImplementedError('PATH method not implemented yet')

        if result.status_code != 200 or result.status_code != 204 and content_type is None:
            raise Exception(result.status_code, result.reason, result, self.base_url, path, common_headers)
        elif result.status_code != 200 or result.status_code != 204 and content_type is not None:
            raise Exception(result.status_code, result.reason, result, self.base_url, path, common_headers)

        return result


class TwitterBase(object):

    def __init__(self, base_url, api_key, api_secret):
        """

        :param base_url:
        :param consumer_key:
        :param secret_key:
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def return_my_retweets(self):
        """

        :return:
        """
        path = self.base_url + '/1.1/statuses/retweets_of_me.json'
        request_handler = OauthHandler(path, self.api_key, self.api_secret)
        response = request_handler.get_oauth_url()
        return response

    def return_my_status(self):
        """

        :return:
        """
        path = self.base_url + '/1.1/statuses/home_timeline.json'
        request_handler = OauthHandler(path, self.api_key, self.api_secret)
        response = request_handler.get_oauth_url()
        return response

    def update_timeline(self, tweet_data):
        """

        :param tweet_data:
        :return:
        """
        encoded_data = urlencode({'status': str(tweet_data)})
        path = self.base_url + '/1.1/statuses/update.json?%s' % encoded_data
        request_handler = OauthHandler(path, self.api_key, self.api_secret)
        response = request_handler.post_oauth_url()
        return response

    def send_direct_message(self, dm_target, dm_data):
        """

        :param dm_target:
        :return:
        """
        # TODO: Update the actual parameters here
        encoded_data = urlencode({'status': str(dm_data)})
        # TODO: Update the actual URL and required parameters here
        path = self.base_url + '/1.1/direct_message_send/send.json?%s' % encoded_data
        raise NotImplementedError(path)

    def return_direct_messages(self):
        """

        :return:
        """
        raise NotImplementedError('Not Yet Implemented')

    def retweet_tweet(self):
        """

        :return:
        """
        raise NotImplementedError('Not Yet Implemented')

