import sys
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
    sys.exit(app.exec_())