# coding: utf8
import web
import models



urls = (
    '/move', 'move',
    '/action', 'action',
)
app = web.application(urls, globals())


class forward:
    def GET(self):
        direction = web.ctx.query.split('=')[1]
        if direction.upper() == "F":
            models.m1.clockwise()
            models.m2.clockwise()
        elif direction.upper() == "B":
            models.m1.counter_clockwise()
            models.m2.counter_clockwise()
        elif direction.upper() == "R":
            models.m1.counter_clockwise()
            models.m2.clockwise()
        elif direction.upper() == "L":
            models.m1.clockwise()
            models.m2.counter_clockwise()
        elif direction.upper() == "S":
            models.m1.stop()
            models.m2.stop()
        else:
            print("movement non supporte")
        return 'OK'
    
class action:
    def GET(self):
        action = web.ctx.query.split('=')[1]
        if action == "1":
            models.u.getdistance()
       else:
            print("action non supportee")
        return 'OK'

if __name__ == "__main__":
    app.run()
