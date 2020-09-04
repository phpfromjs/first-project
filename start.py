import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8080,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        info = ['python','php','java','c++','go']
        self.render('index.html',list=info)

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1',False)
        noun2 = self.get_argument('noun2',False)
        noun3 = self.get_argument('noun3',False)
        noun4 = self.get_argument('noun4',False)
        self.render('poem.html',road = nuno1,wood=noun2,made=noun3,difference=noun4)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/',IndexHandler),
        (r'/pome',PoemPageHandler)
    ])
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
