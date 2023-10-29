import colorBackground
import colorText
import spacing
import sys, os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browseBtn.clicked.connect(self.browsefiles)
        self.encodeBtn.clicked.connect(self.encode)
        self.decodeBtn.clicked.connect(self.decode)
        self.browseBtn_template.clicked.connect(self.browsefilestemplate)

    def browsefiles(self): # browse files and set file path to 'self.filename' edit
        fname=QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), 'Text files (*.txt, *.doc, *.docx)')
        self.filename.setText(fname[0])

    def browsefilestemplate(self): # browse files and set file path to 'self.filename' edit
        fname=QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), 'Text files (*.txt, *.doc, *.docx)')
        self.filename_template.setText(fname[0])

    def encode(self): # encoding supplied text
        userText = self.userInput.toPlainText()
        print(userText)
        templateFile = self.filename_template.text()
        if self.selectMethodEncode.currentText() == "Background Color":
            path = colorBackground.encode_to_bg(templateFile, userText)
        elif self.selectMethodEncode.currentText() == "Letter Color":
            path = colorText.encode_to_color(templateFile, userText)
        elif self.selectMethodEncode.currentText() == "Spacing":
            path = spacing.encode_in_spaces(templateFile, userText)
            

        self.fileSavedAtLabel.setText(f'File saved at {path}')

    def decode(self): # decoding uploaded textfile
        print(self.filename.text())
        if self.selectMethodDecode.currentText() == "Background Color":
            self.decodedMessage.setText(colorBackground.decode_from_bg(self.filename.text()))
        elif self.selectMethodEncode.currentText() == "Letter Color":
            self.decodedMessage.setText(colorText.decode_from_color(self.filename.text()))
        elif self.selectMethodEncode.currentText() == "Spacing":
            self.decodedMessage.setText(spacing.decode_from_spaces(self.filename.text()))

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
