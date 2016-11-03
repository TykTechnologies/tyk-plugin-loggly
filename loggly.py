import json, requests

## Based on: https://www.loggly.com/docs/http-endpoint/

loggly_url = 'http://logs-01.loggly.com/inputs/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/tag/{0}/'

def log(tag, record):
    requests.post(loggly_url.format(tag), json=record)
