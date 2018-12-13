#from Histgram import *
from hist import *
import sys 
#from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QDialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
 
 
class Example(QMainWindow):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
         
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

    #各个子菜单
        #file
        exitAction = QAction(QIcon(sys.path[0]+'/exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

    #base info
        HistAction = QAction(QIcon(sys.path[0]+'/Hist.png'), 'Hist', self)
        HistAction.setShortcut('Ctrl+H')
        HistAction.setStatusTip('Image Histgram')
        HistAction.triggered.connect(self.hist)
 
        self.statusBar()
 
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) #MAC OS 需要特别增加这个语句
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        BaseInfoMenu = menubar.addMenu('&Base Info')
        BaseInfoMenu.addAction(HistAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
         
        self.setGeometry(200, 200, 900, 600)
        self.setWindowTitle('Main window')   
    def hist(self): 
        #下面的self必须要加上
        self.child=childWindow()
        self.child.show()

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        #self.child = HistgramUI()
        self.child = HistDlg()
        self.child.setupUi(self)
       # Form.show()
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
 
    #widget = QWidget(None)
    #Ui_Hist().setupUi(widget)
    ex = Example()
    ex.show()
    app.exec_()
    #sys.exit(app.exec_())