# coding=utf-8
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

email_from_addr = '邮件来源地址'
password = '密码'
email_to_addr = '发送人'
smtp_server = '服务器'
# 邮件参数 抄送多人 则用‘,’ 隔开
mailto_list = '抄送人'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

'''
***发送邮件并添加附件***
to_list：收件人；
sub：主题；
content：邮件内容
'''

def send_mail(to_list, mail_sender, sub, file_path):
    msg = MIMEMultipart('mixed')
    msg['From'] = _format_addr(mail_sender + '<%s>' % email_from_addr)
    msg['To'] = email_to_addr
    msg['Cc'] = to_list
    msg['Subject'] = Header(sub, 'utf-8')

    to_receiver = email_to_addr.split(',') + to_list.split(',')
    mail_msg = '正文'
    msg.attach(MIMEText(mail_msg, 'plain', 'utf-8'))
    # 构造附件
    with open(file_path, 'rb') as fp:
        mail_body = fp.read()
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 附件中文名
    att.add_header("Content-Disposition", "attachment", filename=("utf-8", "", "测试文件.xlsx"))
    # 附件非中文名
    # att["Content-Disposition"] = 'attachment; filename={file_name}'.format(file_name=file_name)
    msg.attach(att)
    try:
        server = smtplib.SMTP(smtp_server)
        server.login(email_from_addr, password)
        # print(msg.as_string())
        server.sendmail(email_from_addr, to_receiver, msg.as_string())
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("邮件发送失败")


if __name__ == '__main__':
    path = 'E:\\datax_json\\测试文件.xlsx'
    mail_subject = '主题'
    mail_sender = ''
    send_mail(mailto_list, mail_sender, mail_subject, path)
