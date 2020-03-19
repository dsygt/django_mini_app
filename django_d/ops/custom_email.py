import os
import django
import smtplib
from first_dj import settings
from email.mime.text import MIMEText

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_dj.settings')
django.setup()


def send_mail():
    msg = MIMEText("邮件通道测试我是苏鑫涛", "plain", "utf-8")
    msg['FROM'] = "Mail Test"
    msg['Subject'] = "【猜猜老子是谁???真的不是我】"
    receivers = ['2210755345@qq.com','1040493047@qq.com']
    # 不加密
    # server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()
    pass


if __name__ == '__main__':
    send_mail()
