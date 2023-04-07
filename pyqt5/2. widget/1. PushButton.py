import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self) # 앰퍼샌트 기호 뒤에오는 이름은 alt + 단축키로 변환된다.
        btn1.setCheckable(True)
        btn1.toggle() # 토글형태로 바꿈

        # 이런식으로도 가능
        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False) # 버튼을 사용할 수 없게 해준다.

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())