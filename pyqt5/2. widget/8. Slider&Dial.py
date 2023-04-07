import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2) # 조절 가능한 최소 단위
        # self.slider.setNotchesVisible() 틱의 간격 조정
        
        # self.slider.setTickPosition() 값들
        """
        QSlider.NoTicks: 틱을 표시하지 않습니다.
        QSlider.TicksAbove: 틱을 (수평) 슬라이더 위쪽에 표시합니다.
        QSlider.TicksBelow : 틱을 (수평) 슬라이더 아래쪽에 표시합니다.
        QSlider.TicksBothSides : 틱을 (수평) 슬라이더 양쪽에 표시합니다.
        QSlider.TicksLeft : 틱을 (수직) 슬라이더 왼쪽에 표시합니다.
        QSlider.TicksRight : 틱을 (수직) 슬라이더 오른쪽에 표시합니다.
        """
        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)
        # self.dial.setNotchesVisible(True) # 노치를 표시할 수 있음
        btn = QPushButton('Default', self)
        btn.move(35, 160)

        # valueChanged 자주 사용하는 시그널
        """
        valueChanged() : 슬라이더의 값이 변할 때 발생합니다.
        sliderPressed() : 사용자가 슬라이더를 움직이기 시작할 때 발생합니다.
        sliderMoved() : 사용자가 슬라이더를 움직이면 발생합니다.
        sliderReleased() : 사용자가 슬라이더를 놓을 때 발생합니다.
        """
        self.slider.valueChanged.connect(self.dial.setValue) # setValue로 두개를 연결
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())