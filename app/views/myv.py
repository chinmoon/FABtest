from flask_appbuilder import AppBuilder, expose, BaseView,has_access
from .. import appbuilder

class MyView1(BaseView):
    route_base = "/myview1"

    @expose('/method1/<string:param1>')
    @has_access
    def method1(self, param1):
        # do something with param1
        # and return it
        return param1

    @expose('/method2/<string:param1>')
    def method2(self, param1):
        # do something with param1
        # and render it
        param1 = 'Hello %s' % (param1)
        return param1