"""
입력값의 형태에 따라 아래와 같이 다섯 개의 유용한 함수가 제공됩니다.


getText()
getMultiLineText()
getInt()
getDouble()
getItem()


예제에서는 getText() 메서드를 사용합니다.
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 35)

        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())