# coding: utf8
import web

urls = (
    '/move', 'forward',
)
app = web.application(urls, globals())


class forward:
    def GET(self):
        direction = web.ctx.query.split('=')[1]
        print(repr(direction))
        return 'OK'


if __name__ == "__main__":
    app.run()
