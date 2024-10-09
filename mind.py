from flask import Flask
import webbrowser
app = Flask(__name__)
# 百度云盘下载链接
# 改变a内的值
a={}
for i in range(len(a['dlink'])):
    print(a['dlink'][i]['dlink'])
    webbrowser.open(a['dlink'][i]['dlink'])
if __name__ == '__main__':
    app.run()











