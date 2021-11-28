
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        top = 100
        left = 100
        width = 600
        height = 600

        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(width,height)
        

# ---------- sets image ----------
        self.image = QImage(self.size(), QImage.Format_RGBA64)
        self.image.fill(QColor('#2c2f33'))

# ---------- init drawing state ----------
        self.drawing = False
        self.brushSize = 2
        self.brushColor = QColor('#7757e0')
        self.lastPoint = QPoint()
        self.frame()

    def frame(self):
        self.f1 = QFrame()
        self.f1.setStyleSheet('background-color: #08050f;')
        self.f1.setFixedHeight(30)

        wid = QWidget(self)
        self.setCentralWidget(wid)

        layout=QVBoxLayout()
        layout.addWidget(self.f1)


# ---------- Catch Mouse Down --------

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

# ---------- Catch Mouse Move --------
    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

# ---------- Catch Mouse Up --------
    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

# ---------- Paint --------
    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

# ---------- Save Action ----------
    

# ---------- Clear Frame Action ----------
    def clearFrame(self):
        self.image.fill(QColor())
        self.update(QColor('#2c2f33'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Window()
    Window.show()
    sys.exit(app.exec_())