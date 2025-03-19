# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Log_in.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Log_In(object):
    def setupUi(self, Log_In):
        if not Log_In.objectName():
            Log_In.setObjectName(u"Log_In")
        Log_In.resize(900, 723)
        self.centralwidget = QWidget(Log_In)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_screen = QLabel(self.widget)
        self.title_screen.setObjectName(u"title_screen")
        font = QFont()
        font.setPointSize(26)
        self.title_screen.setFont(font)
        self.title_screen.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_screen)

        self.greetings = QLabel(self.widget)
        self.greetings.setObjectName(u"greetings")
        font1 = QFont()
        font1.setPointSize(18)
        self.greetings.setFont(font1)

        self.verticalLayout.addWidget(self.greetings, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(431, 550))
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Login_lbl = QLabel(self.frame_2)
        self.Login_lbl.setObjectName(u"Login_lbl")
        self.Login_lbl.setFont(font1)
        self.Login_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Login_lbl, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pass_lbl_2 = QLabel(self.frame_2)
        self.pass_lbl_2.setObjectName(u"pass_lbl_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.pass_lbl_2.setFont(font2)
        self.pass_lbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.pass_lbl_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.username = QLineEdit(self.frame_2)
        self.username.setObjectName(u"username")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy1)
        self.username.setMaximumSize(QSize(700, 16777215))
        self.username.setBaseSize(QSize(2, 0))

        self.horizontalLayout_2.addWidget(self.username)

        self.horizontalSpacer = QSpacerItem(88, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pass_lbl = QLabel(self.frame_2)
        self.pass_lbl.setObjectName(u"pass_lbl")
        self.pass_lbl.setFont(font2)
        self.pass_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.pass_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.password = QLineEdit(self.frame_2)
        self.password.setObjectName(u"password")
        self.password.setBaseSize(QSize(2, 0))
        self.password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.password)

        self.show_password = QPushButton(self.frame_2)
        self.show_password.setObjectName(u"show_password")

        self.horizontalLayout.addWidget(self.show_password)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.login = QPushButton(self.frame_2)
        self.login.setObjectName(u"login")
        self.login.setBaseSize(QSize(75, 75))

        self.gridLayout_2.addWidget(self.login, 1, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        Log_In.setCentralWidget(self.centralwidget)

        self.retranslateUi(Log_In)

        QMetaObject.connectSlotsByName(Log_In)
    # setupUi

    def retranslateUi(self, Log_In):
        Log_In.setWindowTitle(QCoreApplication.translate("Log_In", u"MainWindow", None))
        self.title_screen.setText(QCoreApplication.translate("Log_In", u"TUPC-ROOM UTILIZATION", None))
        self.greetings.setText(QCoreApplication.translate("Log_In", u"Greetings", None))
        self.Login_lbl.setText(QCoreApplication.translate("Log_In", u"Login into your Account", None))
        self.pass_lbl_2.setText(QCoreApplication.translate("Log_In", u"Username", None))
        self.pass_lbl.setText(QCoreApplication.translate("Log_In", u"Password", None))
        self.show_password.setText(QCoreApplication.translate("Log_In", u"Show", None))
        self.login.setText(QCoreApplication.translate("Log_In", u"Login", None))
    # retranslateUi

