# code utf-8
import json
import os
import sys
import urllib.parse
import urllib.request

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

hostUrl = "http://zasellaid.njshangka.com"


def login(username, password):
    post_data = urllib.parse.urlencode({'phone': username, 'password': password})
    post_data = post_data.encode('utf-8')
    res = urllib.request.urlopen(hostUrl + "/c/u/login", post_data)
    response_json = res.read().decode('utf-8')
    print(res.status, response_json)
    json_string = json.loads(response_json)['data']['token']
    print(json_string)
    return json_string


def dailyRequest(token, yesterday, today):
    post_data = urllib.parse.urlencode({'token': token, 'yesterday_summary': yesterday, 'today_goal': today})
    post_data = post_data.encode('utf-8')
    res = urllib.request.urlopen(hostUrl + "/c/dailyreport/writetoday", post_data)
    response_json = res.read().decode('utf-8')
    print(res.status, response_json)
    json_result = json.loads(response_json)
    json_code = json_result['code']
    json_message = json_result['codeMsg']
    if json_code == 0:
        return "日报提交成功"
    else:
        return json_message


class CallHandle(QObject):
    # @pyqtSlot(str, result=int)
    # def myHello(self, sss):
    #     print("js call py :" + sss)
    #     self.result.emit(8888)
    #     return 123
    result = pyqtSignal(int)

    @pyqtSlot(str, str, str, str, result=str)  # 要与方法中的参数一一对应
    def getUserName(self, username, password, yesterday, today):
        # username = os.path.dirname(os.path.abspath(__file__))
        print('call received :::', username, password, yesterday, today)
        token = login(username, password)
        dailyResult = dailyRequest(token, yesterday, today)
        self.result.emit(8888)
        return dailyResult


def _LoadFinish(self, *args, **kwargs):
    ret = view.page().runJavaScript("window.show()")
    print("load finish", ret)


if __name__ == "__main__":
    # os.system("pause")
    app = QApplication(sys.argv)
    view = QWebEngineView()
    channel = QWebChannel()
    handler = CallHandle()
    channel.registerObject('pyjs', handler)
    view.page().setWebChannel(channel)
    view.loadFinished.connect(_LoadFinish)
    htmlUrl = './daily/dailyPython.html'  # htmlUrl = 'D:/python/daily/dailyPython.html'
    # aa = open(htmlUrl, encoding="utf-8")
    # print(os.getcwd())
    qurl = QUrl.fromLocalFile(os.getcwd() + "/dailyPython.html")  # os.getcwd() + "/dailyPython.html"
    view.load(qurl)
    view.show()
    sys.exit(app.exec_())
