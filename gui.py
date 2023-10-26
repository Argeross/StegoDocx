
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browseBtn.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 tutorials\Browse Files', 'Images (*.png, *.xmp *.jpg)')
        self.filename.setText(fname[0])

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
