import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 위젯 객체 생성
        tab1 = QWidget()
        tab2 = QWidget()

        # 탭을 만들고 탭안에 위젯 추가
        tabs = QTabWidget()
        tabs.addTab(tab1, '탭1')
        tabs.addTab(tab2, '탭2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())