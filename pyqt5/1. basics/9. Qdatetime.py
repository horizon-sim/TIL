# from PyQt5.QtCore import QDate, Qt

# now = QDate.currentDate() # 현재 날짜 반환
# print(now.toString()) # 날짜를 문자열로 출력

# # 날짜 형식 설정하기
# now = QDate.currentDate()
# print(now.toString('d.M.yy'))
# print(now.toString('dd.MM.yyyy'))
# print(now.toString('ddd.MMMM.yyyy'))
# print(now.toString(Qt.ISODate)) # iso 표준형식
# print(now.toString(Qt.DefaultLocaleLongDate)) # 기본설정에 맞게



# from PyQt5.QtCore import QTime, Qt

# # 현재 시간 출력
# time = QTime.currentTime()
# print(time.toString())

# time = QTime.currentTime()
# print(time.toString('h.m.s'))
# print(time.toString('hh.mm.ss'))
# print(time.toString('hh.mm.ss.zzz'))
# print(time.toString(Qt.DefaultLocaleLongDate))
# print(time.toString(Qt.DefaultLocaleShortDate))

# # 현재 날짜와 시간
# from PyQt5.QtCore import QDateTime

# datetime = QDateTime.currentDateTime()
# print(datetime.toString())

# datetime = QDateTime.currentDateTime()
# print(datetime.toString('d.M.yy hh:mm:ss'))
# print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
# print(datetime.toString(Qt.DefaultLocaleLongDate))
# print(datetime.toString(Qt.DefaultLocaleShortDate))


# 예시

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
    