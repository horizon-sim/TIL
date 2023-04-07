import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self) # 캘린더 객체 생성
        cal.setGridVisible(True) # 날짜 사이에 그리드 표시 할건지
        cal.clicked[QDate].connect(self.showDate) # 클릭했을 때 show date 메소드 호출
        
        self.lbl = QLabel(self)
        date = cal.selectedDate() # 현재 선택된 날짜 정보를 가지고있음(디폴트는 현재 날짜)
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())