import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('img/exit.png'), 'Exit', self) # QAction 객체 생성
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        
        saveAction = QAction(QIcon('img/save.png'), 'save', self) # QAction 객체 생성
        saveAction.setShortcut('Ctrl+W')
        saveAction.setStatusTip('save application')
        saveAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit') # 툴바 생성
        self.toolbar.addAction(exitAction) # 툴바 내 액션 추가 (객체 추가)
        self.toolbar.addAction(saveAction)
        

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())