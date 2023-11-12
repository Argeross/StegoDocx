import colorBackground
import colorText
import spacing
import sys, os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt6.uic import loadUi
from docx.shared import RGBColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browseBtn.clicked.connect(self.browsefiles)
        self.encodeBtn.clicked.connect(self.encode)
        self.decodeBtn.clicked.connect(self.decode)
        self.browseBtn_template.clicked.connect(self.browsefilestemplate)
        self.help_text.setText('''Methods:
Background Color - changes a color of the secret text to white (default) or selected one (RGB selector). The secret text is then appended to the text of a input .docx file.
                               
Letter Color - encodes secret text as RGB values of the shades of a black color and changes accordingly the font color of letters in template file. The length of the text in a input .docx file has to be greater than the length of the secret text.

 
''')

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
            # print(type(self.Rvalue.value()), type(self.Gvalue.value()), type(self.Bvalue.value()))
            try:
                path = colorBackground.encode_to_bg(templateFile, userText, RGBColor(self.Rvalue.value(), self.Gvalue.value(), self.Bvalue.value()))
                self.fileSavedAtLabel.setText(f'File saved at {path}')
            except:
                self.fileSavedAtLabel.setText("No template file was selected. Please select template file.")
        elif self.selectMethodEncode.currentText() == "Letter Color":
            try:
                path = colorText.encode_to_color(templateFile, userText)
                if path == "Too short template file or too long message.":
                    self.fileSavedAtLabel.setText(path)
                else:                
                    self.fileSavedAtLabel.setText(f'File saved at {path}')
            except:
                self.fileSavedAtLabel.setText("No template file was selected. Please select template file.")
        elif self.selectMethodEncode.currentText() == "Spacing":
            try:
                path = spacing.encode_in_spaces(templateFile, userText)
                if path == "Too short template file or too long message.":
                    self.fileSavedAtLabel.setText(path)
                else:
                    self.fileSavedAtLabel.setText(f'File saved at {path}')
            except:
                self.fileSavedAtLabel.setText("No template file was selected. Please select template file.")            
            

    def decode(self): # decoding uploaded textfile
        print(self.filename.text())
        if self.selectMethodDecode.currentText() == "Background Color":
            try:
                self.decodedMessage.setText(colorBackground.decode_from_bg(self.filename.text()))
            except:
                self.decodedMessage.setText("No file to decode!")
        elif self.selectMethodEncode.currentText() == "Letter Color":
            try:
                self.decodedMessage.setText(colorText.decode_from_color(self.filename.text()))
            except:
                self.decodedMessage.setText("No file to decode!")           
        elif self.selectMethodEncode.currentText() == "Spacing":
            try:
                self.decodedMessage.setText(spacing.decode_from_spaces(self.filename.text()))
            except:
                self.decodedMessage.setText("No file to decode!")      
            

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
