import sys
<<<<<<< HEAD
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
=======
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QFormLayout
class MainWindow(QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi()
        self.show()
#===================================================================================
    def setupUi(self):                                     #物件
        self.setWindowTitle("yt_downloader")
        self.line_text = QLineEdit()
        self.button_mp3 = QPushButton()
        self.button_mp3.setText("下載mp3")
        self.button_mp4 = QPushButton()
        self.button_mp4.setText("下載mp4")
        self.button_cancel = QPushButton()
        self.button_cancel.setText("cancel")

        form_layout = QFormLayout()  #輸出
        form_layout.addRow(self.button_mp3, self.line_text)
        form_layout.addRow(self.button_mp4, self.line_text)
        form_layout.addRow(self.button_cancel)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        self.setLayout(layout)

#按鈕觸發
        self.button_mp3.clicked.connect(self.mp3_download)
        self.button_mp4.clicked.connect(self.mp4_download)
        self.button_cancel.clicked.connect(self.cancel)
    def mp3_download(self):
        self.line_text.setText("mp3")
    def mp4_download(self):
        self.line_text.setText("mp4")
    def cancel(self):
        self.line_text.setText("")

#===================================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
>>>>>>> b4fd5fcbe62d9c0c62386b832ae88f1fa6f58f77
    sys.exit(app.exec_())