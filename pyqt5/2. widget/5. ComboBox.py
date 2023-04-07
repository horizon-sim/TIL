import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        # activated[str]은 QComboBox의 옵션의 문자열을 받아 전달한다.
        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize() # 사이즈는 자동으로 조절하게 끔


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())