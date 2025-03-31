# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 659)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.student_sched_btn = QPushButton(self.centralwidget)
        self.student_sched_btn.setObjectName(u"student_sched_btn")
        self.student_sched_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.student_sched_btn)

        self.info_stdnt_btn = QPushButton(self.centralwidget)
        self.info_stdnt_btn.setObjectName(u"info_stdnt_btn")
        self.info_stdnt_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.info_stdnt_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout_3.addWidget(self.logout_btn)


        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(801, 637))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.student_menu_stackedwidget = QStackedWidget(self.frame_2)
        self.student_menu_stackedwidget.setObjectName(u"student_menu_stackedwidget")
        self.student_menu_stackedwidgetPage1_2 = QWidget()
        self.student_menu_stackedwidgetPage1_2.setObjectName(u"student_menu_stackedwidgetPage1_2")
        self.gridLayout_2 = QGridLayout(self.student_menu_stackedwidgetPage1_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.room_sched_table = QTableWidget(self.student_menu_stackedwidgetPage1_2)
        if (self.room_sched_table.columnCount() < 5):
            self.room_sched_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.room_sched_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.room_sched_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.room_sched_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.room_sched_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.room_sched_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.room_sched_table.rowCount() < 14):
            self.room_sched_table.setRowCount(14)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(12, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.room_sched_table.setVerticalHeaderItem(13, __qtablewidgetitem18)
        self.room_sched_table.setObjectName(u"room_sched_table")

        self.gridLayout_2.addWidget(self.room_sched_table, 0, 0, 1, 1)

        self.student_menu_stackedwidget.addWidget(self.student_menu_stackedwidgetPage1_2)
        self.student_menu_stackedwidgetPage2_2 = QWidget()
        self.student_menu_stackedwidgetPage2_2.setObjectName(u"student_menu_stackedwidgetPage2_2")
        self.gridLayout_4 = QGridLayout(self.student_menu_stackedwidgetPage2_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.student_menu_stackedwidgetPage2_2)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_11.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.room_status_stdnt_info = QLineEdit(self.student_menu_stackedwidgetPage2_2)
        self.room_status_stdnt_info.setObjectName(u"room_status_stdnt_info")
        self.room_status_stdnt_info.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.room_status_stdnt_info)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.label_10 = QLabel(self.student_menu_stackedwidgetPage2_2)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_10.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_10)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)

        self.line_2 = QFrame(self.student_menu_stackedwidgetPage2_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_2)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.student_menu_stackedwidgetPage2_2)
        self.label_13.setObjectName(u"label_13")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_13.setFont(font4)

        self.verticalLayout_14.addWidget(self.label_13, 0, Qt.AlignLeft)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.first_name_lineedit_stdntinfo = QLineEdit(self.student_menu_stackedwidgetPage2_2)
        self.first_name_lineedit_stdntinfo.setObjectName(u"first_name_lineedit_stdntinfo")

        self.verticalLayout_13.addWidget(self.first_name_lineedit_stdntinfo)

        self.label_30 = QLabel(self.student_menu_stackedwidgetPage2_2)
        self.label_30.setObjectName(u"label_30")
        font5 = QFont()
        font5.setPointSize(9)
        self.label_30.setFont(font5)

        self.verticalLayout_13.addWidget(self.label_30)


        self.horizontalLayout_6.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.last_name_lineedit_stdntinfo = QLineEdit(self.student_menu_stackedwidgetPage2_2)
        self.last_name_lineedit_stdntinfo.setObjectName(u"last_name_lineedit_stdntinfo")

        self.verticalLayout_12.addWidget(self.last_name_lineedit_stdntinfo)

        self.label_12 = QLabel(self.student_menu_stackedwidgetPage2_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)

        self.verticalLayout_12.addWidget(self.label_12)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)


        self.verticalLayout_19.addLayout(self.verticalLayout_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.student_menu_stackedwidgetPage2_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)

        self.verticalLayout_15.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.email_stdnt_lineedit_info = QLineEdit(self.student_menu_stackedwidgetPage2_2)
        self.email_stdnt_lineedit_info.setObjectName(u"email_stdnt_lineedit_info")

        self.verticalLayout_15.addWidget(self.email_stdnt_lineedit_info, 0, Qt.AlignVCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_16 = QLabel(self.student_menu_stackedwidgetPage2_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)

        self.verticalLayout_18.addWidget(self.label_16, 0, Qt.AlignLeft)

        self.tupc_id_lineedit_info = QLineEdit(self.student_menu_stackedwidgetPage2_2)
        self.tupc_id_lineedit_info.setObjectName(u"tupc_id_lineedit_info")

        self.verticalLayout_18.addWidget(self.tupc_id_lineedit_info, 0, Qt.AlignVCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_9)


        self.horizontalLayout_7.addLayout(self.verticalLayout_18)


        self.verticalLayout_19.addLayout(self.horizontalLayout_7)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_15 = QLabel(self.student_menu_stackedwidgetPage2_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.verticalLayout_5.addWidget(self.label_15)

        self.password_stdnt_info = QLineEdit(self.student_menu_stackedwidgetPage2_2)
        self.password_stdnt_info.setObjectName(u"password_stdnt_info")
        self.password_stdnt_info.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.password_stdnt_info)


        self.verticalLayout_17.addLayout(self.verticalLayout_5)


        self.verticalLayout_19.addLayout(self.verticalLayout_17)

        self.change_pass = QPushButton(self.student_menu_stackedwidgetPage2_2)
        self.change_pass.setObjectName(u"change_pass")
        self.change_pass.setMinimumSize(QSize(100, 40))

        self.verticalLayout_19.addWidget(self.change_pass, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_19)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.student_menu_stackedwidget.addWidget(self.student_menu_stackedwidgetPage2_2)

        self.gridLayout_3.addWidget(self.student_menu_stackedwidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.student_menu_stackedwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.student_sched_btn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.info_stdnt_btn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        ___qtablewidgetitem = self.room_sched_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Monday", None));
        ___qtablewidgetitem1 = self.room_sched_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None));
        ___qtablewidgetitem2 = self.room_sched_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None));
        ___qtablewidgetitem3 = self.room_sched_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Thursday", None));
        ___qtablewidgetitem4 = self.room_sched_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Friday", None));
        ___qtablewidgetitem5 = self.room_sched_table.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"7:00", None));
        ___qtablewidgetitem6 = self.room_sched_table.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"8:00", None));
        ___qtablewidgetitem7 = self.room_sched_table.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"9:00", None));
        ___qtablewidgetitem8 = self.room_sched_table.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"10:00", None));
        ___qtablewidgetitem9 = self.room_sched_table.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"11:00", None));
        ___qtablewidgetitem10 = self.room_sched_table.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"12:00", None));
        ___qtablewidgetitem11 = self.room_sched_table.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1:00", None));
        ___qtablewidgetitem12 = self.room_sched_table.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2:00", None));
        ___qtablewidgetitem13 = self.room_sched_table.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"3:00", None));
        ___qtablewidgetitem14 = self.room_sched_table.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"4:00", None));
        ___qtablewidgetitem15 = self.room_sched_table.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"5:00", None));
        ___qtablewidgetitem16 = self.room_sched_table.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"6:00", None));
        ___qtablewidgetitem17 = self.room_sched_table.verticalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"7:00", None));
        ___qtablewidgetitem18 = self.room_sched_table.verticalHeaderItem(13)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"8:00", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Attendance Status:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TUPC-ID:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.change_pass.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
    # retranslateUi

