import urlparse
import urllib
import httplib

from urllib2 import urlopen, Request

class pygoogletts:
    def get_sound_stream(self, text, language, ie="UTF-8"):
        url = 'http://translate.google.com/translate_tts'
	params = { 'ie': ie, 'q': text, 'tl': language }

	request_url = self.get_request_url(url, params)

	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0'
	
	response = self.get_response(url, params, headers)

	return response.read()

    def get_response(self, url, params, headers):
        data = urllib.urlencode(params)
	response = urlopen(Request(url, data = data, headers = headers))

	return response
