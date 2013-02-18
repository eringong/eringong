import os
from twisted.application import service, internet
from twisted.web import static, server

import cyclone.web
import cyclone.httpserver

from cyclone.web import StaticFileHandler

try:
    _port = int(os.environ["PORT"])
except:
    _port = 80

class DefaultHandler(cyclone.web.RequestHandler):
    def get(self):
        self.render('index.html')

class OpenTemplateHandler(cyclone.web.RequestHandler):
    def get(self, path):
        self.render(path)

class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
           (r"/", DefaultHandler),
#		   (r"/(.*?)", OpenTemplateHandler, {}),
		   (r"/(.*)", StaticFileHandler, {"path":"./"}),
         ]
        
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "html"),
            static_path=os.path.join(os.path.dirname(__file__), "html"),
#            debug=True,
            debug=False,
            autoescape=None,
            )

        cyclone.web.Application.__init__(self, handlers, **settings)


site = Application()
application = service.Application("PersonalResume")
internet.TCPServer(_port, site).setServiceParent(application)
