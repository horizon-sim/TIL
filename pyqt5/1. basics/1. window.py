import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') # 창의 제목
        self.move(300, 300) # 켜졌을 때 시작 위치
        self.resize(400, 200) # 위젯 처음 크기
        self.show() # 위젯 보여주기


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())