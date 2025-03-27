import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from bs4 import BeautifulSoup

from Ui_NoticeDialog import Ui_NoticeDialog
from Common import get_resource_path

key_value = []


def visit_notice_url():
    notice_url = 'https://www.cnblogs.com/YangShengzhou/p/18461572'
    try:
        response = requests.get(notice_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title_element = soup.find('a', class_='postTitle2')
        post_body = soup.find('div', class_='postBody')

        if not title_element or not post_body:
            return 1

        title = title_element.text.strip()
        blog_content = post_body.get_text().strip()
        blog_parts = blog_content.split('==')

        if len(blog_parts) != 2:
            return 1

        key, notice_content = blog_parts
        global key_value
        key_value = key.split(',')

        dialog = NoticeDialog(title=title, content=notice_content)
        dialog.exec()
    except Exception:
        return 1


def get_key():
    return key_value


class NoticeDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, title=None, content=None):
        super(NoticeDialog, self).__init__(parent)
        self.ui = Ui_NoticeDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("WinQSB安装提示")
        self.setWindowIcon(QtGui.QIcon(get_resource_path('resources/img/ui/icon.ico')))
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.dialogTitle = title
        self.content = content
        self.ui.label_title.setText(self.dialogTitle)
        self.ui.label_content.setText(self.content)
        self.ui.pushButton_cancel.clicked.connect(self.reject)
