import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction('Exit', self) # 메뉴 바에 추가할 액션 추가 
        exitAction.setShortcut('Ctrl+Q') # 단축키 설정
        exitAction.setStatusTip('Exit application') # 스테이터스 툴팁
        exitAction.triggered.connect(qApp.quit) # 선택시 연결되어 적힌 함수 호출

        # exitAction.triggered.connect(QApplication.instance().quit)

        self.statusBar()

        menubar = self.menuBar() # 메뉴바 메소드 생성
        menubar.setNativeMenuBar(False) # 맥에는 메뉴바가 자동으로 붙는데 그걸 사용하지 않는코드
        filemenu = menubar.addMenu('&File') # 메뉴추가 (앞에 앰퍼센트를 붙이면 alt + f 로 실행할 수 있음 &i로 시작할경우 alt + i가 된다.)
        filemenu.addAction(exitAction) # 동작 추가

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())