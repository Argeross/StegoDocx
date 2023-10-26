
import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browseBtn.clicked.connect(self.browsefiles)
        self.encodeBtn.clicked.connect(self.encode)
        self.decodeBtn.clicked.connect(self.decode)

    def browsefiles(self): # browse files and set file path to 'self.filename' edit
        fname=QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), 'Text files (*.txt, *.doc, *.docx)')
        self.filename.setText(fname[0])

    def encode(self): # encoding supplied text
        userText = self.userInput.toPlainText()
        print(userText)

    def decode(self): # decoding uploaded textfile
        print(self.filename.text())

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
