import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QInputDialog,QLineEdit,QLabel

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'youtube_downloader'
        self.left = 200
        self.top = 300
        self.width = 700
        self.height = 400
        self.initUI()
#=======================================================================================================================
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
#輸入框
        self.label_input = QLabel(self)
        self.label_input.setText('輸入關鍵字:')
        self.line = QLineEdit(self)
        self.line.move(60, 80)
        self.line.resize(600, 80)
        self.label_input.move(20, 20)
#功能按鍵
        button_mp3 = QPushButton('mp3下載', self)
        button_mp3.setToolTip('mp3下載')
        button_mp3.resize(200,100)
        button_mp3.move(100, 250)
        button_mp3.clicked.connect(self.feature_mp3)

        button_mp4 = QPushButton('mp4下載', self)
        button_mp4.setToolTip('mp4下載')
        button_mp4.resize(200,100)
        button_mp4.move(400, 250)
        button_mp4.clicked.connect(self.feature_mp4)

        self.show()


    def feature_mp3(self):
        print('mp3' + self.line.text())

    def feature_mp4(self):
        print('mp4' + self.line.text())

#=======================================================================================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())