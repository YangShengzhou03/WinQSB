import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow

"""pyinstaller Application.spec"""


def main():
    app = QtWidgets.QApplication(sys.argv)
    shared_memory = QtCore.QSharedMemory("WinQSB_SharedMemory")
    if shared_memory.attach():
        sys.exit(1)

    if not shared_memory.create(1):
        sys.exit(1)

    window = MainWindow()
    window.setWindowTitle("64位WinQSB安装程序")
    window.move(300, 150)
    window.show()
    start_application()
    sys.exit(app.exec())


def start_application():
    try:
        app = QApplication(sys.argv)
        sys.exit(app.exec())
    except SystemExit:
        raise
    except Exception:
        sys.exit(1)


if __name__ == '__main__':
    main()
