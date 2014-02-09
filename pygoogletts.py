#!/usr/bin/python
# -*- coding: utf-8 -*-

#    The MIT License (MIT)
#    
#    Copyright (c) 2014 risedrag
#    
#    Permission is hereby granted, free of charge, to any person obtaining a copy of
#    this software and associated documentation files (the "Software"), to deal in
#    the Software without restriction, including without limitation the rights to
#    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
#    the Software, and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import urlparse
import urllib
import httplib

from urllib2 import urlopen, Request

class GoogleTTS:
    
    def get_sound_stream(self, text, language=None, ie=None):
        """Get sound stream data with provided parameters.
	
	:param text: this value will be converted to sound 
	:param language: defaults to "en"
	:param ie: defaults to "UTF-8"

	"""

	if not language:
	    language = "en"
	if not ie:
	    ie = "UTF-8"

	params = { 'ie': ie, 'q': text, 'tl': language }
	
	response = self.get_response(params)

	return response.read()

    def get_response(self, params):
        """Get connection response from Google Translate TTS Service."""
        
	url = 'http://translate.google.com/translate_tts'
	
	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0'

        data = urllib.urlencode(params)
	response = urlopen(Request(url, data = data, headers = headers))

	return response
