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
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QStatusBar
from GUISignals import *


""" Class for the main window of the GUI """
class MainWindow(QMainWindow):
    # initialization of the MainWindow class
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup()
        pass
    # method to setup the Main Window
    def setup(self):
        self.setGeometry(100, 100, 700, 500) # sets the size of the window 
        self.setWindowTitle('Recipe Book') # sets the title of the window
        self.move(60, 15) # sets the windows location on the screen

        # creating label widget for window
        self.helloMsg = QLabel('<h1>Welcome to Matt\'s Recipe Book') # creates an instance of the QLabel and assigns it to be a child of the window object
        self.setCentralWidget(self.helloMsg)

        # calling setup method for New Recipe Button
        self.setupNewRecipeButton()
        # calling setup method for Browse Recipes Button
        self.setupBrowseRecipesButton()
        # calling setup method for Menu Bar
        self.setupMenuBar()
        # calling setup method for Tool Bar
        self.setupToolBar()
        # calling setup method for Status Bar
        self.setupStatusBar()
        pass
    # method to setup the New Recipe Button
    def setupNewRecipeButton(self):
        # creating an instance of the QPushButton
        self.newRecipeBtn = QPushButton("New Recipe")
        pass
    # method to setup the Browse Recipes Button
    def setupBrowseRecipesButton(self):
        self.browseRecipesBtn = QPushButton("Browse Recipes")
        pass
    # method to setup the Menu Bar
    def setupMenuBar(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Browse Recipes', browseRecipesSelected) # Adding a Browse Recipes option to the menu
        self.menu.addAction('&Add New Recipe', newRecipeSelected) # Adding an Add New Recipe option to the menu
        self.menu.addAction('&Exit', self.close)
        pass
    # method to setup the Tool Bar
    def setupToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('&Exit', self.close)
        pass
    # method to setup the Status Bar
    def setupStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)
        pass
pass
""" End MainWindow class """


if __name__ == "__main__":
    # creating an instance of the QApplication
    app = QApplication(sys.argv)
    # creating an instance of the MainWindow class
    mainWindow = MainWindow()
    # show the applications GUI
    mainWindow.show()
    # run the applications event loop
    sys.exit(app.exec_())

