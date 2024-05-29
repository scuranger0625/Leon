import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 600)  #更改視窗大小
    w.move(0, 0)   #視窗開啟位置
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())
