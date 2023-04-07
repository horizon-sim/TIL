import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle() # 체크 박스의 상태를 채워진 상태로 시작
        
        # pressed() 체크 박스를 누를 때 신호를 발생
        # released() 체크 박스에서 뗄 때 신호를 발생
        # clicked() 체크 박스를 클릭할 때 신호를 발생
        cb.stateChanged.connect(self.changeTitle) # 체크 박스 상태가 바뀔 때 신호 발생
        
        print(cb.isChecked()) # Check여부 확인
        print(cb.text()) # text 확인, setText를 통해 라벨 텍스트를 수정할 수 있음
        print(cb.checkState()) # 체크 박스의 상태를 반환
        
        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        print(state)
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())