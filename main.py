import webapp2
import json
import urllib
import random
import logging
from google.appengine.api import urlfetch
import jinja2
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env=jinja2.Environment(loader=template_loader)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        beg_template = template_env.get_template('index.html')
        self.response.write(beg_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug = True)
