def simple_middleware(get_response):
    """
    simple_middleware 外层函数，在请求阶段执行
    get_response 视图本身
    """

    def middleware(request):
        """
        middleware 内层函数  ，会在视图调用前执行
        """
        print("函数中间件 视图执行前A")
        response = get_response(request)  # response 就是视图执行的结果
        print("函数中间件 视图执行后B")

        return response

    return middleware


from django.utils.deprecation import MiddlewareMixin  # 表示当前是一个混入类，扩展类，混入类的作用就是保存一些类的公共方法


# 类中间件提供了5个基本的hook方法，方法名固定，一旦实现了这些方法，会在请求与响应过程中按指定顺序分别执行
class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):  # 不需要return
        print("类中间件 视图执行前")

    def process_view(self, request, view_func, view_args, view_kwargs):  # 不需要return
        print("类中间件 视图接收参数后，执行代码前，会自动执行process_view")  # 可以返回response对象，若返回，则视图不会执行

    def process_response(self, request, response):
        print("类中间件 视图执行后")
        return response

    def process_exception(self, request, exception):
        print(exception)
        print("类中间件 视图执行中发生异常,自动执行，否则不执行")

    def process_template_renponse(self, request, response):
        print("类中间件 建立静态页面缓存") # 视图执行过程中如果调用了模板 则自动执行
