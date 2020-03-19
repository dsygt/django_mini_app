# 分析日志
# 发送邮件(定时任务)

import os
from first_dj import settings
import logging
import os
import smtplib
from email.mime.text import MIMEText

# 写自己的
log_file = 'test_no/statistics.log'
logger = logging.getLogger('django')


def log_analyse():
    log_file_path = os.path.join(settings.BASE_DIR, log_file)
    # print(log_file_path,666666666)
    if not os.path.exists(log_file_path):
        print('日志问及那不存在,log file not exist....')
        return

    result = {}
    with open(log_file_path, 'r', encoding='utf8')as f:
        # f.readline()
        for line in f:
            line = line.strip()
            line_dict = eval(line)
            # print(77777, line_dict)

            # 记录数据
            # xxx接口1    平均耗时    最高耗时    最低耗时    出现次数
            # xxx接口2    平均耗时    最高耗时    最低耗时    出现次数

            # 如果path存在,count+1
            # 如果path不存在,count==1
            # result[count] = '记录接口访问次数',
            # result[min] = '最少',
            # result[max] ='最多',
            # result[avg] ='总耗时/次数'

            key = line_dict['path']
            if key in result:
                result[key][0] += 1  # 第0位标识次数
                if line_dict['used_time'] < result[key][1]:
                    result[key][1] = line_dict['used_time']
                if line_dict['used_time'] > result[key][1]:
                    result[key][2] = line_dict['used_time']
                result[key][3] += line_dict['used_time']

            # 第一次
            else:
                result[key] = ['次数', '最小值', '最大值', '总时间']
                result[key][0] = 1
                result[key][1] = line_dict['used_time']
                result[key][2] = line_dict['used_time']
                result[key][3] = line_dict['used_time']
        return result


def analyse():
    res = log_analyse()
    for key in res:
        res[key].append(res[key][3] / res[key][0])
    return res


def send_email():
    msg = MIMEText(repr(analyse()), "plain", "utf-8")
    # 发件人
    msg['FROM'] = "dsy"
    # 主题
    msg['Subject'] = "【端口统计dsy】"
    # 接收人
    receivers = ['2210755345@qq.com']  # list,可添加多个联系人
    # 不加密or加密
    # server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()


if __name__ == '__main__':
    send_email()
    # print(analyse())
    # print(log_analyse())