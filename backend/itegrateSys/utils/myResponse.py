from rest_framework.response import Response


class myResponse:
    def __init__(self, data=[], code=200, msg='请求成功'):
        self.code = code
        self.data = data
        self.msg = msg

    def render(self):
        if not self.data:
            self.data = []
        if self.code == 1000:
            self.msg = '参数错误'

        return Response({'data': self.data, 'code': self.code, 'msg': self.msg})
