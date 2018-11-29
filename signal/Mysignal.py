import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
 
 
class Example(QMainWindow):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
         
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
 
        exitAction = QAction(QIcon(sys.path[0]+'/exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QAction(QIcon(sys.path[0]+'/open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a File')
      #  openAction.triggered.connect(self.close)

 
        self.statusBar()
 
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) #MAC OS 需要特别增加这个语句
        fileMenu = menubar.addMenu('&File')
        baseMenu = menubar.addMenu('&Base Info')
        
        #
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)
        
 
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
         
        self.setGeometry(300, 300, 650, 250)
        self.setWindowTitle('Main window')   
        self.show()
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())