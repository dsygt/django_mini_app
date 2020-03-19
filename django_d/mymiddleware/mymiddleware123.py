# 需要的模块:导入日志,time模块
import time
import logging

# 有了一个logging实例
logger_statistics = logging.getLogger('statistics')


class TestMiddle():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('before call在call之前')
        response = self.get_response(request)
        print('after call在call之后')
        return response


class StatisticsMiddle():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('before call在call之前')
        start_time = time.time()
        path = request.path
        response = self.get_response(request)
        end_time = time.time()

        # 将时间戳变成人类易读的方式
        log_dict={
            'start_time':start_time,
            'end_time':end_time,
            'used_time': end_time - start_time,
            'path':path
        }
        print('after call在call之后')
        logger_statistics.info(repr(log_dict))
        return response

