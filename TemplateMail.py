#from -*- coding:utf-8 -*-
from email import encoders
from email.mime.base import MIMEBase
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr(( \
        Header(name,'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr,unicode) else addr))
#from_addr = raw_input('From: ')
#password = raw_input('Password: ')
#to_addr = raw_input('To: ')
#smtp_server = raw_input('SMTP server: ')
from_addr = 'zhangwenjun@.net'
to_addr = '@'
password = ''
smtp_server = 'SMTP.'


msg = MIMEMultipart()
msg['From'] = _format_addr(u'com.cn邮箱管理员<%s>' % from_addr)
msg['To'] = _format_addr(u'<%s>'% to_addr)
msg['Subject'] = Header(u'密码重置结果反馈','utf-8').encode()
#邮件正文是MIMEText
#msg.attach(MIMEText('send with file...','plain','utf-8'))
msg.attach(MIMEText('你好：\n     你的密码已经重置：!@#123ABC\n     请及时登录网页版的邮箱，输入冒号后的九位字符串。\n  '
                    '   提示：先切换到英文输入法或者直接复制\n     详细更改流程见附件，如有问题请邮件反馈。','plain','utf-8'))
with open('D:/Documents and Settings/Desktop/外网邮箱工作记录/邮箱忘记密码重置操作流程.docx'.decode('utf-8'),'rb') as f:
    mime = MIMEBase('document','docx',filename='邮箱忘记密码重置操作流程.docx')
    #mime = MIMEApplication(open)
    mime.add_header('Content-Disposition','attachment',filename = '邮箱忘记密码重置操作流程.docx')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-ID','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server,25)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()