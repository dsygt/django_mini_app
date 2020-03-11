import django
import os
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_dj.settings")
django.setup()


def log_demo():
    # 命名记录器
    logger = logging.getLogger('django')
    logger.info('我是 info log')
    logger.info('我是 info log dsy')
    # warning
    logger.warning('我是 warning log')
    logger.warning('我是 warning log dsy')
    # error
    logger.error('我是 error log')
    logger.error('我是 error log dsy')


if __name__ == '__main__':
    log_demo()
