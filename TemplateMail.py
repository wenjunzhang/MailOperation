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
msg['From'] = _format_addr(u'com.cn�������Ա<%s>' % from_addr)
msg['To'] = _format_addr(u'<%s>'% to_addr)
msg['Subject'] = Header(u'�������ý������','utf-8').encode()
#�ʼ�������MIMEText
#msg.attach(MIMEText('send with file...','plain','utf-8'))
msg.attach(MIMEText('��ã�\n     ��������Ѿ����ã�!@#123ABC\n     �뼰ʱ��¼��ҳ������䣬����ð�ź�ľ�λ�ַ�����\n  '
                    '   ��ʾ�����л���Ӣ�����뷨����ֱ�Ӹ���\n     ��ϸ�������̼������������������ʼ�������','plain','utf-8'))
with open('D:/Documents and Settings/Desktop/�������乤����¼/���������������ò�������.docx'.decode('utf-8'),'rb') as f:
    mime = MIMEBase('document','docx',filename='���������������ò�������.docx')
    #mime = MIMEApplication(open)
    mime.add_header('Content-Disposition','attachment',filename = '���������������ò�������.docx')
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