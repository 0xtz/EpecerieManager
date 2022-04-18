# DO NOT TOUCH THIS FILE
# IF U DONT KNOW WHAT U DOING
# 

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget QWidget {\n"
"background: transparent;\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QLineEdit {\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    padding-left:10px;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:pressed {    \n"
"    background-color: rgb(27, 29, 35);\n"
"    \n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.wrapper_frame = QtWidgets.QFrame(self.centralwidget)
        self.wrapper_frame.setStyleSheet("QFrame{\n"
"border:none;\n"
"}")
        self.wrapper_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.wrapper_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.wrapper_frame.setLineWidth(0)
        self.wrapper_frame.setObjectName("wrapper_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wrapper_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.wrapper_frame)
        self.frame_top.setEnabled(True)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_top.setStyleSheet("background-color: rgba(33, 37, 43, 150);\n"
"border:none;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_welcome = QtWidgets.QPushButton(self.frame_top)
        self.btn_welcome.setMinimumSize(QtCore.QSize(71, 60))
        self.btn_welcome.setMaximumSize(QtCore.QSize(71, 60))
        self.btn_welcome.setStyleSheet("QPushButton {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-bottom: 1px solid  rgb(85, 170, 255);\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"\n"
"}")
        self.btn_welcome.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_welcome.setIcon(icon)
        self.btn_welcome.setIconSize(QtCore.QSize(48, 48))
        self.btn_welcome.setObjectName("btn_welcome")
        self.horizontalLayout_2.addWidget(self.btn_welcome)
        self.frame_right = QtWidgets.QFrame(self.frame_top)
        self.frame_right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_right.setObjectName("frame_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_right)
        self.frame_label_top_btns.setMinimumSize(QtCore.QSize(846, 30))
        self.frame_label_top_btns.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_top_btns.setStyleSheet("background-color: rgb(98, 103, 111);")
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"margin-left: 5px;")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.frame_btns = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_btns.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_btns.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns.setStyleSheet("background: transparent;\n"
"")
        self.frame_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/icons/cil-minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QtCore.QSize(16, 16))
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_maximize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximize.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/icons/cil-window-maximize.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_maximize.setIcon(icon2)
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_close.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/icons/cil-x.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.horizontalLayout_10.addWidget(self.frame_btns)
        self.verticalLayout_2.addWidget(self.frame_label_top_btns)
        self.frame_2 = QtWidgets.QFrame(self.frame_right)
        self.frame_2.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_top_info_1 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_top_info_1.setObjectName("label_top_info_1")
        self.horizontalLayout_7.addWidget(self.label_top_info_1)
        self.label_top_info_2 = QtWidgets.QLabel(self.frame_2)
        self.label_top_info_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_top_info_2.setFont(font)
        self.label_top_info_2.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_top_info_2.setObjectName("label_top_info_2")
        self.horizontalLayout_7.addWidget(self.label_top_info_2)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.frame_right)
        self.verticalLayout.addWidget(self.frame_top)
        self.main_frame = QtWidgets.QWidget(self.wrapper_frame)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_left = QtWidgets.QFrame(self.main_frame)
        self.frame_left.setMinimumSize(QtCore.QSize(71, 0))
        self.frame_left.setMaximumSize(QtCore.QSize(71, 16777215))
        self.frame_left.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"")
        self.frame_left.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_left.setObjectName("frame_left")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_left)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_gestion = QtWidgets.QPushButton(self.frame_left)
        self.btn_gestion.setMinimumSize(QtCore.QSize(71, 60))
        self.btn_gestion.setStyleSheet("QPushButton {\n"
"    background-position:  center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_gestion.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/icons/cil-folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_gestion.setIcon(icon4)
        self.btn_gestion.setIconSize(QtCore.QSize(24, 24))
        self.btn_gestion.setObjectName("btn_gestion")
        self.verticalLayout_4.addWidget(self.btn_gestion)
        self.btn_g_entree = QtWidgets.QPushButton(self.frame_left)
        self.btn_g_entree.setMinimumSize(QtCore.QSize(71, 60))
        self.btn_g_entree.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_g_entree.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/icons/cil-input.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_g_entree.setIcon(icon5)
        self.btn_g_entree.setIconSize(QtCore.QSize(24, 24))
        self.btn_g_entree.setObjectName("btn_g_entree")
        self.verticalLayout_4.addWidget(self.btn_g_entree)
        self.btn_g_produit = QtWidgets.QPushButton(self.frame_left)
        self.btn_g_produit.setMinimumSize(QtCore.QSize(71, 60))
        self.btn_g_produit.setStyleSheet("QPushButton {\n"
"    \n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_g_produit.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/icons/cil-briefcase.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_g_produit.setIcon(icon6)
        self.btn_g_produit.setIconSize(QtCore.QSize(24, 24))
        self.btn_g_produit.setObjectName("btn_g_produit")
        self.verticalLayout_4.addWidget(self.btn_g_produit)
        self.btn_ventes = QtWidgets.QPushButton(self.frame_left)
        self.btn_ventes.setMinimumSize(QtCore.QSize(71, 60))
        self.btn_ventes.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_ventes.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/icons/cil-chart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_ventes.setIcon(icon7)
        self.btn_ventes.setIconSize(QtCore.QSize(24, 24))
        self.btn_ventes.setObjectName("btn_ventes")
        self.verticalLayout_4.addWidget(self.btn_ventes)
        spacerItem = QtWidgets.QSpacerItem(20, 299, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.frame_left)
        self.frame_5 = QtWidgets.QFrame(self.main_frame)
        self.frame_5.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_welcome = QtWidgets.QWidget()
        self.page_welcome.setObjectName("page_welcome")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_welcome)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 210, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.page_welcome)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 209, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_welcome)
        self.page_g_produit = QtWidgets.QWidget()
        self.page_g_produit.setObjectName("page_g_produit")
        self.gridLayout = QtWidgets.QGridLayout(self.page_g_produit)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(282, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.page_g_produit)
        self.label.setMaximumSize(QtCore.QSize(501, 31))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.page_g_produit)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 2, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 0, 5, 11, 1)
        spacerItem7 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 7, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 0, 8, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem9, 1, 1, 2, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 1, 4, 2, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem11, 1, 6, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem12, 1, 8, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setMinimumSize(QtCore.QSize(141, 31))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setMinimumSize(QtCore.QSize(141, 31))
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setMinimumSize(QtCore.QSize(141, 31))
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setMinimumSize(QtCore.QSize(141, 31))
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.linedit_edit_reference = QtWidgets.QLineEdit(self.tab)
        self.linedit_edit_reference.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_edit_reference.setStyleSheet("")
        self.linedit_edit_reference.setObjectName("linedit_edit_reference")
        self.verticalLayout_7.addWidget(self.linedit_edit_reference)
        self.linedit_edit_des = QtWidgets.QLineEdit(self.tab)
        self.linedit_edit_des.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_edit_des.setObjectName("linedit_edit_des")
        self.verticalLayout_7.addWidget(self.linedit_edit_des)
        self.linedite_edit_prix = QtWidgets.QLineEdit(self.tab)
        self.linedite_edit_prix.setMinimumSize(QtCore.QSize(221, 35))
        self.linedite_edit_prix.setObjectName("linedite_edit_prix")
        self.verticalLayout_7.addWidget(self.linedite_edit_prix)
        self.btn_edite_p = QtWidgets.QPushButton(self.tab)
        self.btn_edite_p.setMinimumSize(QtCore.QSize(140, 41))
        self.btn_edite_p.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid #ffaa00;\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_edite_p.setObjectName("btn_edite_p")
        self.verticalLayout_7.addWidget(self.btn_edite_p)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 2, 6, 3, 3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setMinimumSize(QtCore.QSize(141, 31))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_12.addWidget(self.label_17)
        self.btn_create_p_csv = QtWidgets.QPushButton(self.tab)
        self.btn_create_p_csv.setMinimumSize(QtCore.QSize(140, 41))
        self.btn_create_p_csv.setMaximumSize(QtCore.QSize(140, 41))
        self.btn_create_p_csv.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_create_p_csv.setObjectName("btn_create_p_csv")
        self.horizontalLayout_12.addWidget(self.btn_create_p_csv)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 3, 0, 1, 5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setMinimumSize(QtCore.QSize(141, 31))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setMinimumSize(QtCore.QSize(141, 31))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setMinimumSize(QtCore.QSize(141, 31))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setMinimumSize(QtCore.QSize(141, 31))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 4, 0, 3, 3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.linedit_reference = QtWidgets.QLineEdit(self.tab)
        self.linedit_reference.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_reference.setStyleSheet("")
        self.linedit_reference.setObjectName("linedit_reference")
        self.verticalLayout_5.addWidget(self.linedit_reference)
        self.linedit_designation = QtWidgets.QLineEdit(self.tab)
        self.linedit_designation.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_designation.setObjectName("linedit_designation")
        self.verticalLayout_5.addWidget(self.linedit_designation)
        self.linedit_prix = QtWidgets.QLineEdit(self.tab)
        self.linedit_prix.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_prix.setObjectName("linedit_prix")
        self.verticalLayout_5.addWidget(self.linedit_prix)
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setMinimumSize(QtCore.QSize(141, 31))
        self.label_27.setObjectName("label_27")
        self.verticalLayout_5.addWidget(self.label_27)
        self.btn_create_p = QtWidgets.QPushButton(self.tab)
        self.btn_create_p.setMinimumSize(QtCore.QSize(140, 41))
        self.btn_create_p.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_create_p.setObjectName("btn_create_p")
        self.verticalLayout_5.addWidget(self.btn_create_p)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 4, 3, 5, 2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 82, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 5, 7, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 3))
        self.line_3.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 6, 6, 1, 3)
        spacerItem14 = QtWidgets.QSpacerItem(152, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem14, 7, 6, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 7, 7, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(151, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem15, 7, 8, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 179, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem16, 8, 0, 3, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem17, 8, 7, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 126, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem18, 9, 3, 2, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setMinimumSize(QtCore.QSize(189, 31))
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_5.addWidget(self.label_28)
        self.linedit_delete_p = QtWidgets.QLineEdit(self.tab)
        self.linedit_delete_p.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_delete_p.setStyleSheet("\n"
"QLineEdit {\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    padding-left:10px;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:pressed {    \n"
"    background-color: rgb(27, 29, 35);\n"
"    \n"
"}")
        self.linedit_delete_p.setObjectName("linedit_delete_p")
        self.horizontalLayout_5.addWidget(self.linedit_delete_p)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem19 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.btn_delete_p = QtWidgets.QPushButton(self.tab)
        self.btn_delete_p.setMinimumSize(QtCore.QSize(222, 35))
        self.btn_delete_p.setMaximumSize(QtCore.QSize(221, 35))
        self.btn_delete_p.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(255, 21, 0);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_delete_p.setObjectName("btn_delete_p")
        self.horizontalLayout_9.addWidget(self.btn_delete_p)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.gridLayout_4.addLayout(self.verticalLayout_11, 9, 6, 1, 3)
        spacerItem20 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem20, 10, 7, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 5, 1, 2)
        spacerItem21 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 1, 6, 1, 2)
        spacerItem22 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem22, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setMinimumSize(QtCore.QSize(141, 31))
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_4.addWidget(self.label_25)
        self.linedit_search_produit = QtWidgets.QLineEdit(self.tab_2)
        self.linedit_search_produit.setMinimumSize(QtCore.QSize(50, 35))
        self.linedit_search_produit.setStyleSheet("")
        self.linedit_search_produit.setObjectName("linedit_search_produit")
        self.horizontalLayout_4.addWidget(self.linedit_search_produit)
        self.btn_search_produit = QtWidgets.QPushButton(self.tab_2)
        self.btn_search_produit.setMinimumSize(QtCore.QSize(91, 35))
        self.btn_search_produit.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_search_produit.setObjectName("btn_search_produit")
        self.horizontalLayout_4.addWidget(self.btn_search_produit)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 3)
        spacerItem23 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem23, 0, 2, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)
        self.table_rupture_stock = QtWidgets.QTableWidget(self.tab_2)
        self.table_rupture_stock.setStyleSheet("border: 1px solid rgb(85, 170, 255);")
        self.table_rupture_stock.setObjectName("table_rupture_stock")
        self.table_rupture_stock.setColumnCount(4)
        self.table_rupture_stock.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_rupture_stock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_rupture_stock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_rupture_stock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_rupture_stock.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.table_rupture_stock, 2, 0, 1, 8)
        spacerItem24 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem24, 1, 3, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem25, 0, 7, 1, 1)
        self.btn_refrech_table_rupture_stock = QtWidgets.QPushButton(self.tab_2)
        self.btn_refrech_table_rupture_stock.setMinimumSize(QtCore.QSize(91, 35))
        self.btn_refrech_table_rupture_stock.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_refrech_table_rupture_stock.setObjectName("btn_refrech_table_rupture_stock")
        self.gridLayout_3.addWidget(self.btn_refrech_table_rupture_stock, 1, 4, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 3)
        self.stackedWidget.addWidget(self.page_g_produit)
        self.page_g_entre_p = QtWidgets.QWidget()
        self.page_g_entre_p.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.page_g_entre_p.setObjectName("page_g_entre_p")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_g_entre_p)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem26 = QtWidgets.QSpacerItem(297, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem26, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_g_entre_p)
        self.label_2.setMaximumSize(QtCore.QSize(501, 31))
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(297, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem27, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.page_g_entre_p)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem28 = QtWidgets.QSpacerItem(20, 142, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem28, 0, 2, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(227, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem29, 1, 0, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setMinimumSize(QtCore.QSize(141, 31))
        self.label_32.setMaximumSize(QtCore.QSize(141, 40))
        self.label_32.setObjectName("label_32")
        self.verticalLayout_13.addWidget(self.label_32)
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setMinimumSize(QtCore.QSize(141, 31))
        self.label_30.setMaximumSize(QtCore.QSize(141, 41))
        self.label_30.setObjectName("label_30")
        self.verticalLayout_13.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setMinimumSize(QtCore.QSize(141, 31))
        self.label_31.setMaximumSize(QtCore.QSize(141, 40))
        self.label_31.setObjectName("label_31")
        self.verticalLayout_13.addWidget(self.label_31)
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setMinimumSize(QtCore.QSize(141, 31))
        self.label_34.setMaximumSize(QtCore.QSize(141, 40))
        self.label_34.setObjectName("label_34")
        self.verticalLayout_13.addWidget(self.label_34)
        self.gridLayout_7.addLayout(self.verticalLayout_13, 1, 1, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setMinimumSize(QtCore.QSize(141, 31))
        self.label_33.setObjectName("label_33")
        self.verticalLayout_12.addWidget(self.label_33)
        self.linedit_reference_entres = QtWidgets.QLineEdit(self.frame)
        self.linedit_reference_entres.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_reference_entres.setStyleSheet("\n"
"QLineEdit {\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    padding-left:10px;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:pressed {    \n"
"    background-color: rgb(27, 29, 35);\n"
"    \n"
"}")
        self.linedit_reference_entres.setObjectName("linedit_reference_entres")
        self.verticalLayout_12.addWidget(self.linedit_reference_entres)
        self.linedit_quantite_entres = QtWidgets.QLineEdit(self.frame)
        self.linedit_quantite_entres.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_quantite_entres.setStyleSheet("\n"
"QLineEdit {\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    padding-left:10px;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:pressed {    \n"
"    background-color: rgb(27, 29, 35);\n"
"    \n"
"}")
        self.linedit_quantite_entres.setText("")
        self.linedit_quantite_entres.setObjectName("linedit_quantite_entres")
        self.verticalLayout_12.addWidget(self.linedit_quantite_entres)
        self.linedit_raison_entres = QtWidgets.QLineEdit(self.frame)
        self.linedit_raison_entres.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_raison_entres.setStyleSheet("\n"
"QLineEdit {\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    padding-left:10px;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:pressed {    \n"
"    background-color: rgb(27, 29, 35);\n"
"    \n"
"}")
        self.linedit_raison_entres.setObjectName("linedit_raison_entres")
        self.verticalLayout_12.addWidget(self.linedit_raison_entres)
        self.gridLayout_7.addLayout(self.verticalLayout_12, 1, 2, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(227, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem30, 1, 3, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem31 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem31)
        self.btn_create_entres = QtWidgets.QPushButton(self.frame)
        self.btn_create_entres.setMinimumSize(QtCore.QSize(228, 35))
        self.btn_create_entres.setMaximumSize(QtCore.QSize(221, 35))
        self.btn_create_entres.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_create_entres.setObjectName("btn_create_entres")
        self.horizontalLayout_11.addWidget(self.btn_create_entres)
        self.gridLayout_7.addLayout(self.horizontalLayout_11, 2, 1, 1, 2)
        spacerItem32 = QtWidgets.QSpacerItem(20, 141, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem32, 3, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 3)
        self.stackedWidget.addWidget(self.page_g_entre_p)
        self.page_ventes_p = QtWidgets.QWidget()
        self.page_ventes_p.setObjectName("page_ventes_p")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_ventes_p)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem33 = QtWidgets.QSpacerItem(302, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem33, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_ventes_p)
        self.label_3.setMaximumSize(QtCore.QSize(501, 31))
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(301, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem34, 0, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.page_ventes_p)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem35 = QtWidgets.QSpacerItem(20, 166, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_9.addItem(spacerItem35, 0, 2, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(227, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem36, 1, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_35 = QtWidgets.QLabel(self.frame_4)
        self.label_35.setMinimumSize(QtCore.QSize(141, 31))
        self.label_35.setMaximumSize(QtCore.QSize(141, 40))
        self.label_35.setObjectName("label_35")
        self.verticalLayout_10.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.frame_4)
        self.label_36.setMinimumSize(QtCore.QSize(141, 31))
        self.label_36.setMaximumSize(QtCore.QSize(141, 40))
        self.label_36.setObjectName("label_36")
        self.verticalLayout_10.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.frame_4)
        self.label_37.setMinimumSize(QtCore.QSize(141, 31))
        self.label_37.setMaximumSize(QtCore.QSize(141, 41))
        self.label_37.setObjectName("label_37")
        self.verticalLayout_10.addWidget(self.label_37)
        self.label_39 = QtWidgets.QLabel(self.frame_4)
        self.label_39.setMinimumSize(QtCore.QSize(141, 31))
        self.label_39.setMaximumSize(QtCore.QSize(141, 41))
        self.label_39.setObjectName("label_39")
        self.verticalLayout_10.addWidget(self.label_39)
        self.gridLayout_9.addLayout(self.verticalLayout_10, 1, 1, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_38 = QtWidgets.QLabel(self.frame_4)
        self.label_38.setMinimumSize(QtCore.QSize(141, 31))
        self.label_38.setMaximumSize(QtCore.QSize(141, 40))
        self.label_38.setObjectName("label_38")
        self.verticalLayout_9.addWidget(self.label_38)
        self.linedit_reference_ventes = QtWidgets.QLineEdit(self.frame_4)
        self.linedit_reference_ventes.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_reference_ventes.setStyleSheet("\n"
"QLineEdit {\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    padding-left:10px;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:pressed {    \n"
"    background-color: rgb(27, 29, 35);\n"
"    \n"
"}")
        self.linedit_reference_ventes.setObjectName("linedit_reference_ventes")
        self.verticalLayout_9.addWidget(self.linedit_reference_ventes)
        self.linedit_quantite_ventes = QtWidgets.QLineEdit(self.frame_4)
        self.linedit_quantite_ventes.setMinimumSize(QtCore.QSize(221, 35))
        self.linedit_quantite_ventes.setStyleSheet("\n"
"QLineEdit {\n"
"    border: none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    padding-left:10px;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:pressed {    \n"
"    background-color: rgb(27, 29, 35);\n"
"    \n"
"}")
        self.linedit_quantite_ventes.setObjectName("linedit_quantite_ventes")
        self.verticalLayout_9.addWidget(self.linedit_quantite_ventes)
        self.btn_vente = QtWidgets.QPushButton(self.frame_4)
        self.btn_vente.setMinimumSize(QtCore.QSize(228, 35))
        self.btn_vente.setMaximumSize(QtCore.QSize(221, 35))
        self.btn_vente.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_vente.setObjectName("btn_vente")
        self.verticalLayout_9.addWidget(self.btn_vente)
        self.gridLayout_9.addLayout(self.verticalLayout_9, 1, 2, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(227, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem37, 1, 3, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(20, 166, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_9.addItem(spacerItem38, 2, 2, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 1, 0, 1, 3)
        self.stackedWidget.addWidget(self.page_ventes_p)
        self.page_etat_ventes = QtWidgets.QWidget()
        self.page_etat_ventes.setObjectName("page_etat_ventes")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_etat_ventes)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem39 = QtWidgets.QSpacerItem(342, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_10.addItem(spacerItem39, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_etat_ventes)
        self.label_4.setMaximumSize(QtCore.QSize(501, 31))
        self.label_4.setObjectName("label_4")
        self.gridLayout_10.addWidget(self.label_4, 0, 1, 1, 1)
        spacerItem40 = QtWidgets.QSpacerItem(287, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_10.addItem(spacerItem40, 0, 2, 1, 2)
        self.table_ventes = QtWidgets.QTableWidget(self.page_etat_ventes)
        self.table_ventes.setMinimumSize(QtCore.QSize(852, 461))
        self.table_ventes.setStyleSheet("\n"
"border: 1px solid rgb(85, 170, 255);")
        self.table_ventes.setObjectName("table_ventes")
        self.table_ventes.setColumnCount(3)
        self.table_ventes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_ventes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ventes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ventes.setHorizontalHeaderItem(2, item)
        self.gridLayout_10.addWidget(self.table_ventes, 1, 0, 1, 4)
        spacerItem41 = QtWidgets.QSpacerItem(615, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_10.addItem(spacerItem41, 2, 0, 1, 3)
        self.btn_refrech_ventes = QtWidgets.QPushButton(self.page_etat_ventes)
        self.btn_refrech_ventes.setMinimumSize(QtCore.QSize(228, 35))
        self.btn_refrech_ventes.setMaximumSize(QtCore.QSize(221, 35))
        self.btn_refrech_ventes.setStyleSheet("QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border: 1px solid rgb(85, 170, 255);\n"
"    border-radius:16px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.btn_refrech_ventes.setObjectName("btn_refrech_ventes")
        self.gridLayout_10.addWidget(self.btn_refrech_ventes, 2, 3, 1, 1)
        self.stackedWidget.addWidget(self.page_etat_ventes)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 15))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 15))
        self.frame_3.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem42 = QtWidgets.QSpacerItem(804, 12, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem42)
        self.label_top_info_3 = QtWidgets.QLabel(self.frame_3)
        self.label_top_info_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_top_info_3.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_top_info_3.setFont(font)
        self.label_top_info_3.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_top_info_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_top_info_3.setObjectName("label_top_info_3")
        self.horizontalLayout_6.addWidget(self.label_top_info_3)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.main_frame)
        self.gridLayout_2.addWidget(self.wrapper_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "Mon Epicerie Gestion"))
        self.label_top_info_1.setText(_translate("MainWindow", "  La gestion des tâches"))
        self.label_top_info_2.setText(_translate("MainWindow", "| {v 0.1.2}  "))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Bienvenue à</span></p><p align=\"center\"><span style=\" font-size:20pt; color:#55aaff;\">Mon Epecerie de Gestion</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">La gestion des produits</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Créer &amp; Modifier un produit</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Editer un produit</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Reference</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Designation</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Prix</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Quantite</span></p></body></html>"))
        self.btn_edite_p.setText(_translate("MainWindow", "Edite"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">FILE : </span><span style=\" font-weight:700; font-style:italic; text-decoration: underline;\">NONE</span></p></body></html>"))
        self.btn_create_p_csv.setText(_translate("MainWindow", "load CSV"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Reference</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Designation</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Prix</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Quantite</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">0 default</span></p></body></html>"))
        self.btn_create_p.setText(_translate("MainWindow", "Create"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Editer un produit</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Reference</span></p></body></html>"))
        self.btn_delete_p.setText(_translate("MainWindow", "Suprimer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Cree Del Edit"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Afficher les produit en rupture de stock</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Search by Reference</span></p></body></html>"))
        self.btn_search_produit.setText(_translate("MainWindow", "Search"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Rechercher Un Produit</span></p></body></html>"))
        item = self.table_rupture_stock.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ReferencePro"))
        item = self.table_rupture_stock.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DesignationPro"))
        item = self.table_rupture_stock.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PrixPro"))
        item = self.table_rupture_stock.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "QuantiteStock"))
        self.btn_refrech_table_rupture_stock.setText(_translate("MainWindow", "Refrech"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Search rupture"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">La gestion des entrées</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Date d\'Entree</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Reference</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Quantite</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">RaisonSociale</span></p><p><span style=\" font-size:8pt; font-weight:700;\">Fournisseur</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">datetime.now()</span></p></body></html>"))
        self.btn_create_entres.setText(_translate("MainWindow", "Create"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">La gestion des Ventes</span></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Date Vente</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Reférence</span></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Quantite</span></p></body></html>"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">datetime.now()</span></p></body></html>"))
        self.btn_vente.setText(_translate("MainWindow", "Sell"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">L\'état des ventes</span></p></body></html>"))
        item = self.table_ventes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DateVente"))
        item = self.table_ventes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "produit"))
        item = self.table_ventes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DateVente"))
        self.btn_refrech_ventes.setText(_translate("MainWindow", "refrech"))
        self.label_top_info_3.setText(_translate("MainWindow", "| by 0xtz "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
