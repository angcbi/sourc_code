# socketserver



### RequestHandler
BaseRequestHandler ---> StreamRequestHandler ---> DatagramRequestHandler
每个连接到来的时候，实例化一个RequestHandler, 如果想要自定义RequestHandler, 继承StreamRequestHandler或DatagramRequestHandler
并重写handler方法
setup做一些设置相关
finish做一些收尾工作

#### BaseRequestHandler
```
    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()

    def setup(self):
        pass

    def handle(self):
        pass

    def finish(self):
        pass
```

#### StreamRequestHandler

setup()
socket，read只能读取指定大小的数据，
采用makefile来方便读取数据，可以readline
rfile是缓冲的，
wfile不是缓冲的，集成BufferedIOBase实现的类，避免了每次flush操作

handler()
**需要重写**

finish()
关闭文件rfile wfile

#### DatagramRequestHandler

setup()
rfile、wfile是两个ByteIO

handler()
**需要重写**

finsh()
发送数据给服务器


