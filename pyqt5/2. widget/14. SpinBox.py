import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        # self.spinbox.setRange(-10, 30) # 위아래 합친것과 같음
        self.spinbox.setSingleStep(2) # step을 정하기 한번에 얼마나
        self.lbl2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())