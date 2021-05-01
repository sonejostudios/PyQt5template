import sys
from PyQt5 import QtWidgets

# import mainwindow.py as module and it's main class
from mainwindow import Ui_MainWindow



# in PyCharm:
# in Run Configuration, Run Before Launch, add External Tool
# Command: pyuic5
# Arguments: mainwindow.ui -o mainwindow.py
# Folder: $ProjectFileDir$
# or in terminal: pyuic5 mainwindow.ui -o mainwindow.py




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # print available styles
        print(QtWidgets.QStyleFactory.keys())


        # Signals
        self.ui.my_button.clicked.connect(self.test)



    def test(self):
        print("test!")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # set qt style
    style = QtWidgets.QStyleFactory.create('Fusion')
    app.setStyle(style)


    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
