import tornado.web  # web框架模块
import tornado.ioloop  # 核心IO循环模块,封装了linux的epoll和BSD的kqueue，是tornado高效的基础


#   业务处理类
class IndexHandler(tornado.web.RequestHandler):
    #   处理get请求，不能处理post请求
    def get(self):
        #   对应http请求方法
        #   给浏览器响应信息
        self.write("Hello Python!!!!")

class TextHandler(tornado.web.RequestHandler):
    def get(self):
        url = self.get_argument("n",'python good')
        self.write(url)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])
        self.write(input[::])
if __name__ == "__main__":
    #   实例化一个app对象
    #   Application: tornado.web框架的核心应用类.是与服务器对应的接口
    #   里面保存了路由映射表，有一个listen方法用来创建一个http服务器的实例绑定了端口
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/res", TextHandler),
        (r"/reverse/(\w+)",ReverseHandler)
    ])
    '''
        IOLoop.current()    返回当前线程的IOLoop实例
        IOLoop.start()  启动IOLoop实例的I/O循环，开启监听
    '''
    app.listen(8080)  # 端口号8080
    '''
	    HttpServer = tornado.httpserver.HTTPServer(app)
	    httpServer.bind(8888)
	    httpServer.start(5) #   默认开启1个线程

	    HttpServer = tornado.httpserver.HTTPServer(app)
	    httpServer.listen(8888) 
    '''
    tornado.ioloop.IOLoop.current().start()