# -*- coding: utf-8 -*-

""" Pocket specific utils """

import requests

import pokuz.exceptions


def get_request_token(consumer_key):
    """ get request token from api """
    data = {'consumer_key': consumer_key, 'redirect_uri': 'getpocket.com'}
    headers = {'x-accept': 'application/json'}
    r = requests.post('https://getpocket.com/v3/oauth/request',
                      data=data, headers=headers)

    if r.ok:
        return r.json()['code']
    else:
        exception_msg = 'An error occured while requesting request token'
        raise pokuz.exceptions.PocketGetRequestTokenException(exception_msg)


def generate_auth_url(request_token):
    """ return auth url for user to authorize application """
    url = ('https://getpocket.com/auth/authorize'
           '?request_token={0}'
           '&redirect_uri=https://getpocket.com').format(request_token)

    return url


def get_access_token(consumer_key, request_token):
    """ get access token from api """
    data = {'consumer_key': consumer_key, 'code': request_token}
    headers = {'x-accept': 'application/json'}
    r = requests.post('https://getpocket.com/v3/oauth/authorize', data=data, headers=headers)

    if r.ok:
        return r.json()['access_token']
    else:
        exception_msg = 'An error occured while requesting access token'
        raise pokuz.exceptions.PocketGetAccessTokenException(exception_msg)


def get_items(consumer_key, access_token):
    """ get a list pocket items from api """
    data = {
        'consumer_key': consumer_key,
        'access_token': access_token,
        'detailType': 'complete'
    }
    r = requests.post('https://getpocket.com/v3/get', data=data)

    if r.ok:
        return [i for i in r.json()['list'].values()]
    else:
        exception_msg = 'An error occured while retrieving pocket items'
        raise pokuz.exceptions.PocketGetItemsException(exception_msg)


def item_to_dict(p_item):
    """ convert pocket item to universal dict 
        tags: list

        About Types:
        e.g.
         tags as dict: 
         { 
            'download': {'item_id': '1953283945', 'tag': 'download'}, 
            'game': {'item_id': '1953283945', 'tag': 'game'}
         }
         OR
         tags as array:
            [{'item_id': '207570641', 'tag': '0'}]
         So,
         >>> dict([{'item_id': '207570641', 'tag': '0'}])
        {'item_id': 'tag'}
    """
    out = {
        'url': p_item.get('resolved_url') or p_item.get('given_url'),
        'title': p_item.get('resolved_title') or p_item.get('given_title'),
        'tags': list(
            dict(p_item.get('tags', dict())).keys()
        ),
        'timestamp': int(p_item.get('time_updated'))
    }

    return out
