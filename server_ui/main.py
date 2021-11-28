import sys
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
#--------


        
        #color for buttons -> #7757e0

class Ui_Main(QMainWindow):

    def __init__(self):
        super().__init__()

        screen_resolution = app.desktop().screenGeometry()
        width_pos, height_pos = screen_resolution.width(), screen_resolution.height()
        print("System Resolution --> " + f'{width_pos}' + " X " + f'{height_pos}')

        self.setWindowTitle("Vibrancy Window")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setAttribute(Qt.WA_TranslucentBackground)
        
        
        #self.setGeometry(1250,510,295,370)
        self.setGeometry(int(width_pos/2 + width_pos/4), int(height_pos/2 + 50), 295, 370)

        self.framer()
        self.blur_frame()
        self.get_font()
        self.btn_frame_btns()
        self.main_wid_frame()

        self.show()

    def framer(self):

        self.btnframe = QFrame()
        self.btnframe.setStyleSheet('background-color: #08050f; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')
        self.btnframe.setFixedHeight(30)

        self.transframe = QFrame()
        self.transframe.setFixedHeight(2)

        self.mainframe = QFrame()
        self.mainframe.setStyleSheet('background-color: #08050f; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')
        self.mainframe.setFixedWidth(200)

        self.transframe_2 = QFrame()
        self.transframe_2.setFixedHeight(2)

        self.btnframe_2 = QFrame()
        self.btnframe_2.setStyleSheet('background-color: #08050f; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')
        self.btnframe_2.setFixedHeight(30)

        


        wid = QWidget(self)
        self.setCentralWidget(wid)

        layout=QVBoxLayout()
        layout.addWidget(self.btnframe)
        layout.addWidget(self.transframe)
        layout.addWidget(self.mainframe)
        layout.addWidget(self.transframe_2)
        layout.addWidget(self.btnframe_2)


        wid.setLayout(layout)


    def blur_frame(self): #translucency FX
         op=QGraphicsOpacityEffect(self)
         op.setOpacity(0.2)
         self.transframe.setGraphicsEffect(op) # ON or OFF doesn't make any difference

    def get_font(self):
        font_db = QFontDatabase()
        saira1 = font_db.addApplicationFont("saira/Saira-ExtraLight.otf")
        saira2 = font_db.addApplicationFont("saira/Saira-ExtraBold.otf")
        saira3 = font_db.addApplicationFont("saira/Saira-Medium.otf")

    def btn_frame_btns(self): ####-- edit button positions for QHBox

        _min = QPushButton(self)
        _min.setGeometry(200,130,30, 8)
        _min.setText(" ___ ")
        _min.clicked.connect(lambda: self.showMinimized())
        _min.setStyleSheet('background-color: #08050f; color: #7757e0; font-family: "Saira-ExtraBold"; min-width: 36px; min-height: 36px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')


        close = QPushButton(self)
        close.setGeometry(200,65,30, 8)
        close.clicked.connect(QApplication.instance().quit)
        close.setStyleSheet('background-color: #08050f; color: #7757e0; qproperty-text: "r"; font-family: "Webdings"; min-width: 36px; min-height: 36px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        inst = QLabel(self)
        inst.setGeometry(21,5,30, 360)
        #inst.clicked.connect(#self.instruct())
        inst.setStyleSheet('background-color: #08050f; color: #7757e0; min-width: 36px; min-height: 36px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        inst_2 = QLabel(self)
        inst_2.setGeometry(240,5,30, 360)
        #inst.clicked.connect(#self.instruct())
        inst_2.setStyleSheet('background-color: #08050f; color: #7757e0; min-width: 36px; min-height: 36px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        skr_text = QLabel(self)
        skr_text.setFont(QFont('Saira-ExtraLight', 11)) 
        skr_text.setGeometry(100,20,95, 25)
        skr_text.setText('SkribbleX')
        skr_text.setToolTip('To Play <b> Start Server & Client<b>')
        skr_text.setAlignment(Qt.AlignCenter)
        skr_text.setStyleSheet('background-color: #08050f; color: #7757e0; min-width: 36px; min-height: 10px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;')

        serv = QLabel(self)
        serv.setFont(QFont('Saira-ExtraLight', 11)) 
        serv.setGeometry(40,90,95, 25)
        serv.setText('SERVER')
        serv.setAlignment(Qt.AlignCenter)
        serv.setStyleSheet('background-color: #08050f; color: #eb565a; min-width: 36px; min-height: 10px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;')

        cl_1 = QLabel(self)
        cl_1.setFont(QFont('Saira-ExtraLight', 11)) 
        cl_1.setGeometry(40,150,95, 25)
        cl_1.setText('CLIENT 1')
        cl_1.setAlignment(Qt.AlignCenter)
        cl_1.setStyleSheet('background-color: #08050f; color: #7757e0; min-width: 36px; min-height: 10px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;')

        cl_2 = QLabel(self)
        cl_2.setFont(QFont('Saira-ExtraLight', 11)) 
        cl_2.setGeometry(40,210,95, 25)
        cl_2.setText('CLIENT 2')
        cl_2.setAlignment(Qt.AlignCenter)
        cl_2.setStyleSheet('background-color: #08050f; color: #7757e0; min-width: 36px; min-height: 10px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        s_check = QCheckBox(self)
        s_check.setGeometry(150,90,0, 25)
        s_check.stateChanged.connect(self.server_check)
        s_check.setStyleSheet('background-color: #08050f; color: #eb565a; min-width: 36px; min-height: 10px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        cl1_check = QCheckBox(self)
        cl1_check.setGeometry(150,150,5, 25)
        cl1_check.stateChanged.connect(self.client_1_check)
        cl1_check.setStyleSheet('background-color: #08050f; color: #7757e0; min-width: 36px; min-height: 10px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        cl2_check = QCheckBox(self)
        cl2_check.setGeometry(150,210,5, 25)
        cl2_check.stateChanged.connect(self.client_2_check)
        cl2_check.setStyleSheet('background-color: #08050f; color: #7757e0; min-width: 36px; min-height: 10px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        edge = QWidget(self)

        tile_layout = QHBoxLayout()
        tile_layout.addWidget(_min)
        tile_layout.addWidget(close)
        tile_layout.addWidget(inst)
        tile_layout.addWidget(inst_2)
        tile_layout.addWidget(skr_text)

    def server_check(self, checked):

        if checked:
            print('SERVER is ON')
        else:
            print('SERVER is OFF')

    def client_1_check(self, checked):

        if checked:
            print('CLIENT 1 is ON')
        else:
            print('CLIENT 1 is OFF')

    def client_2_check(self, checked):

        if checked:
            print('CLIENT 2 is ON')
        else:
            print('CLIENT 2 is OFF')


        


    def main_wid_frame(self):
        main_wid_width = 319
        var_name = 'Meijing'
        score_fixed_width = 75
        score_fixed_height = 25
       
        _sep = QLabel()
        _sep.setFixedWidth(6)
        _sep.setFixedHeight(460)
        _sep.setStyleSheet('background-color: #14111a; border: 1px solid #2c2f33;')

        canvas_set = QLabel()
        canvas = QPixmap(565,450)
        #canvas_set.setPixmap(canvas)
        canvas_set.setFixedWidth(570)
        canvas_set.setFixedHeight(460)
        canvas_set.setStyleSheet('background-color: #14111a; color:#7757e0; border: 1px solid #7757e0;')

        #self.image = QImage(self.size(), QImage.Format_RGBA64)
        #self.image.fill(QColor('#2c2f33'))

        main_wid = QWidget(self.mainframe)

        main_layout = QGridLayout()
        main_layout.setContentsMargins(35,30,15,15)

        #main_layout.addWidget(canvas_set, 1, 1, 4, 4)

        #main_layout.addWidget(self.image, 1, 1, 4, 4)

        #main_layout.addWidget(_sep, 1, 5, 4, 1)


        main_wid.setLayout(main_layout)

    def mousePressEvent(self, event):

        self.btnframe.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.btnframe.offset.x()
        y_w = self.btnframe.offset.y()
        self.move(x-x_w, y-y_w) # comment out if you want to stop draggability

if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = Ui_Main()
    sys.exit(app.exec_())




