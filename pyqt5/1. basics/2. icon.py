import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon("img/web.png"))
      self.setGeometry(300, 300, 300, 200) # move와 resize를 합침
      self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())