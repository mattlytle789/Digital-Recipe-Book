from ctypes import windll
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGridLayout

"""******************** Class for the main window of the GUI ********************"""
class MainWindow(QDialog):
    # initialization of the MainWindow class
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup()

    def setup(self):
        self.setGeometry(100, 100, 500, 500) # sets the size of the window 
        self.setWindowTitle('Recipe Book') # sets the title of the window
        self.move(60, 15) # sets the windows location on the screen

        # creating label widget for window
        helloMsg = QLabel('<h1>Welcome to Matt\'s Recipe Book', parent=self) # creates an instance of the QLabel and assigns it to be a child of the window object

        # creating a grid layout for the window
        layout = QGridLayout() # creates a QGridLayout instance
        layout.addWidget(QWidget(), 0, 0) # adding a spacing widget
        layout.addWidget(helloMsg, 0, 1) # adding the label to the grid
        layout.addWidget(QWidget(), 0, 2) # adding a spacing widget
        layout.addWidget(QWidget(), 1, 0) # adding a spacing widget
        layout.addWidget(QWidget(), 1, 1) # adding a spacing widget
        layout.addWidget(QWidget(), 1, 2) # adding a spacing widget
        self.setLayout(layout) # setting the layout of the window to be the grid layout

    pass
"""******************** End MainWindow class ************************************"""


if __name__ == "__main__":
    # creating an instance of the QApplication
    app = QApplication(sys.argv)
    # creating an instance of the MainWindow class
    mainWindow = MainWindow()
    # show the applications GUI
    mainWindow.show()
    # run the applications event loop
    sys.exit(app.exec_())

