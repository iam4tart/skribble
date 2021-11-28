import sys
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
#--------
from instructor import NewWindow

        
        #color for buttons -> #7757e0

class Ui_Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vibrancy Window")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.setGeometry(200,100,1000,570)
        #self.setFixedWidth(1000)
        #self.setFixedHeight(570)

        self.setStyleSheet('''

                       QScrollBar:vertical {
     border: 2px solid grey;
     background: #32CC99;
     width: 15px;
     margin: 22px 0 22px 0;
 }
 QScrollBar::handle:vertical {
     background: white;
     min-height: 20px;
 }
 QScrollBar::add-line:vertical {
     border: 2px solid grey;
     background: #32CC99;
     height: 20px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }

 QScrollBar::sub-line:vertical {
     border: 2px solid grey;
     background: #2c2f33;
     height: 20px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }
 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
     border: 2px solid #7757e0;
     width: 3px;
     height: 3px;
     background: #7757e0;
 }

 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: #7289da;
 }

 QToolTip {
    border: 1px solid #7757e0; 
    
}


                      ''')

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
     	self.mainframe.setStyleSheet('background-color: #14111a; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

     	wid = QWidget(self)
     	self.setCentralWidget(wid)

     	layout=QVBoxLayout()
     	layout.addWidget(self.btnframe)
     	layout.addWidget(self.transframe)
     	layout.addWidget(self.mainframe)

     	wid.setLayout(layout)

    def main_wid_frame(self):
        main_wid_width = 319
        var_name = 'Meijing'
        score_fixed_width = 75
        score_fixed_height = 25
        #-------------------
        player1_name = 'kawaguchi'
        player1_score_now = '25'
        player2_name = 'tamako'
        player2_score_now = '52'


        player1 = QLabel()
        player1.setFont(QFont('Saira-ExtraLight', 9)) 
        player1.setText("  "+ player1_name)
        player1.setFixedWidth(score_fixed_width)
        player1.setFixedHeight(score_fixed_height)
        player1.setStyleSheet('background-color: #7757e0; color:#f6f6f6;')

        player1_score = QLabel()
        player1_score.setFont(QFont('Saira-ExtraLight', 9)) 
        player1_score.setText(" "+ player1_score_now)
        player1_score.setFixedWidth(score_fixed_width)
        player1_score.setFixedHeight(score_fixed_height)
        player1_score.setStyleSheet('background-color: #14111a; color:#7757e0; border: 1px solid #7757e0;')

        player2 = QLabel()
        player2.setFont(QFont('Saira-ExtraLight', 9)) 
        player2.setText("  "+ player2_name)
        player2.setFixedWidth(score_fixed_width)
        player2.setFixedHeight(score_fixed_height)
        player2.setStyleSheet('background-color: #7757e0; color:#f6f6f6;')

        player2_score = QLabel()
        player2_score.setFont(QFont('Saira-ExtraLight', 9)) 
        player2_score.setText(" "+ player2_score_now)
        player2_score.setFixedWidth(score_fixed_width)
        player2_score.setFixedHeight(score_fixed_height)
        player2_score.setStyleSheet('background-color: #14111a; color:#7757e0; border: 1px solid #7757e0;')

        _chat_show = QPlainTextEdit()
        _chat_show.setFixedWidth(main_wid_width)
        _chat_show.setFont(QFont('Saira-ExtraLight', 10)) 
        _chat_show.setFixedHeight(310)
        _chat_show.setStyleSheet('background-color: #14111a; color:#7757e0; border: 1px solid #7757e0;')

        _username = QLabel()
        _username.setFont(QFont('Saira-ExtraLight', 11)) 
        _username.setText("  Your Name : "+ var_name)
        _username.setFixedWidth(main_wid_width)
        _username.setFixedHeight(25)
        _username.setStyleSheet('background-color: #7757e0; color:#f6f6f6;')

        _chat_type = QPlainTextEdit()
        _chat_type.setFixedWidth(main_wid_width)
        _chat_type.setFont(QFont('Saira-ExtraLight', 11))
        _chat_type.setFixedHeight(75)
        _chat_type.setStyleSheet('background-color: #14111a; color:#7757e0; border: 1px solid #7757e0;')

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

        main_layout.addWidget(canvas_set, 1, 1, 4, 4)

        #main_layout.addWidget(self.image, 1, 1, 4, 4)

        main_layout.addWidget(_sep, 1, 5, 4, 1)

        main_layout.addWidget(player1, 1, 7, 1, 1)
        main_layout.addWidget(player1_score, 1, 8, 1, 1)
        main_layout.addWidget(player2, 1, 9, 1, 1)
        main_layout.addWidget(player2_score, 1, 10, 1, 1)

        main_layout.addWidget(_chat_show, 2, 7, 1, 4)
        main_layout.addWidget(_username, 3, 7, 1, 4)
        main_layout.addWidget(_chat_type, 4, 7, 1, 4)


        main_wid.setLayout(main_layout)

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
        _min.setGeometry(896,5,30, 8)
        _min.setText(" ___ ")
        _min.clicked.connect(lambda: self.showMinimized())
        _min.setStyleSheet('background-color: #08050f; color: #7757e0; font-family: "Saira-ExtraBold"; min-width: 36px; min-height: 36px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')


        close = QPushButton(self)
        close.setGeometry(942,5,30, 8)
        close.clicked.connect(QApplication.instance().quit)
        close.setStyleSheet('background-color: #08050f; color: #7757e0; qproperty-text: "r"; font-family: "Webdings"; min-width: 36px; min-height: 36px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        inst = QPushButton(self)
        inst.setGeometry(21,5,30, 8)
        #inst.clicked.connect(#self.instruct())
        inst.setStyleSheet('background-color: #08050f; color: #7757e0; qproperty-text: "s"; font-family: "Webdings"; min-width: 36px; min-height: 36px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;')

        skr_text = QLabel(self)
        skr_text.setFont(QFont('Saira-ExtraLight', 11)) 
        skr_text.setGeometry(450,18,95, 25)
        skr_text.setText('SkribbleX')
        skr_text.setToolTip('DRAW AS YOU <b> LIKE<b>')
        skr_text.setAlignment(Qt.AlignCenter)
        skr_text.setStyleSheet('background-color: #08050f; color: #7757e0; min-width: 36px; min-height: 10px; border-top-left-radius: 3px; border-top-right-radius: 3px; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;')

        edge = QWidget(self)

        tile_layout = QHBoxLayout()
        tile_layout.addWidget(_min)
        tile_layout.addWidget(close)
        tile_layout.addWidget(inst)
        tile_layout.addWidget(skr_text)

    def instruct(self):
        self.inst_event = NewWindow()
        self.inst_event.show()


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




