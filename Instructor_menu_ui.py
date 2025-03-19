# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Instructor_menu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 685)
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
        self.instructor_sched_btn = QPushButton(self.centralwidget)
        self.instructor_sched_btn.setObjectName(u"instructor_sched_btn")
        self.instructor_sched_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.instructor_sched_btn)

        self.instructor_info_btn = QPushButton(self.centralwidget)
        self.instructor_info_btn.setObjectName(u"instructor_info_btn")
        self.instructor_info_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.instructor_info_btn)

        self.instructor_inbox_btn = QPushButton(self.centralwidget)
        self.instructor_inbox_btn.setObjectName(u"instructor_inbox_btn")
        self.instructor_inbox_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.instructor_inbox_btn)


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
        self.instructor_menu_stackedwidget = QTabWidget(self.frame_2)
        self.instructor_menu_stackedwidget.setObjectName(u"instructor_menu_stackedwidget")
        self.instructor_menu_stackedwidget.tabBar().setVisible(False)
        self.instructor_menu_stackedwidgetPage1 = QWidget()
        self.instructor_menu_stackedwidgetPage1.setObjectName(u"instructor_menu_stackedwidgetPage1")
        self.gridLayout_2 = QGridLayout(self.instructor_menu_stackedwidgetPage1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.instructor_menu_stackedwidgetPage1)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setPointSize(10)
        self.tabWidget.setFont(font2)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.sched_table = QWidget()
        self.sched_table.setObjectName(u"sched_table")
        self.gridLayout_7 = QGridLayout(self.sched_table)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.instructor_room_sched_table = QTableWidget(self.sched_table)
        if (self.instructor_room_sched_table.columnCount() < 5):
            self.instructor_room_sched_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.instructor_room_sched_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.instructor_room_sched_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.instructor_room_sched_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.instructor_room_sched_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.instructor_room_sched_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.instructor_room_sched_table.rowCount() < 14):
            self.instructor_room_sched_table.setRowCount(14)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(12, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.instructor_room_sched_table.setVerticalHeaderItem(13, __qtablewidgetitem18)
        self.instructor_room_sched_table.setObjectName(u"instructor_room_sched_table")

        self.gridLayout_7.addWidget(self.instructor_room_sched_table, 0, 0, 1, 1)

        self.tabWidget.addTab(self.sched_table, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_55 = QLabel(self.tab_2)
        self.label_55.setObjectName(u"label_55")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_55.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_55)

        self.accessed_room_instructor = QLineEdit(self.tab_2)
        self.accessed_room_instructor.setObjectName(u"accessed_room_instructor")
        self.accessed_room_instructor.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.accessed_room_instructor)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout_8.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.list_registered_stdnt_instructor_sched = QTableWidget(self.tab_2)
        if (self.list_registered_stdnt_instructor_sched.columnCount() < 2):
            self.list_registered_stdnt_instructor_sched.setColumnCount(2)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.list_registered_stdnt_instructor_sched.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.list_registered_stdnt_instructor_sched.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        if (self.list_registered_stdnt_instructor_sched.rowCount() < 1):
            self.list_registered_stdnt_instructor_sched.setRowCount(1)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.list_registered_stdnt_instructor_sched.setVerticalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.list_registered_stdnt_instructor_sched.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.list_registered_stdnt_instructor_sched.setItem(0, 1, __qtablewidgetitem23)
        self.list_registered_stdnt_instructor_sched.setObjectName(u"list_registered_stdnt_instructor_sched")
        self.list_registered_stdnt_instructor_sched.setFont(font2)
        self.list_registered_stdnt_instructor_sched.setFrameShadow(QFrame.Plain)
        self.list_registered_stdnt_instructor_sched.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.list_registered_stdnt_instructor_sched.horizontalHeader().setDefaultSectionSize(130)

        self.verticalLayout_5.addWidget(self.list_registered_stdnt_instructor_sched)


        self.gridLayout_8.addLayout(self.verticalLayout_5, 2, 0, 1, 1)

        self.list_attendance = QTableWidget(self.tab_2)
        if (self.list_attendance.columnCount() < 2):
            self.list_attendance.setColumnCount(2)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.list_attendance.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.list_attendance.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        if (self.list_attendance.rowCount() < 1):
            self.list_attendance.setRowCount(1)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.list_attendance.setVerticalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.list_attendance.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.list_attendance.setItem(0, 1, __qtablewidgetitem28)
        self.list_attendance.setObjectName(u"list_attendance")
        self.list_attendance.setFont(font2)
        self.list_attendance.setFrameShadow(QFrame.Plain)
        self.list_attendance.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.list_attendance.horizontalHeader().setDefaultSectionSize(130)

        self.gridLayout_8.addWidget(self.list_attendance, 0, 1, 3, 1)

        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_8.addWidget(self.line_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.instructor_menu_stackedwidget.addTab(self.instructor_menu_stackedwidgetPage1, "")
        self.instructor_menu_stackedwidgetPage2 = QWidget()
        self.instructor_menu_stackedwidgetPage2.setObjectName(u"instructor_menu_stackedwidgetPage2")
        self.gridLayout_4 = QGridLayout(self.instructor_menu_stackedwidgetPage2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.instructor_menu_stackedwidgetPage2)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setPointSize(11)
        self.label_11.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.room_access_status_instructor = QLineEdit(self.instructor_menu_stackedwidgetPage2)
        self.room_access_status_instructor.setObjectName(u"room_access_status_instructor")
        self.room_access_status_instructor.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.room_access_status_instructor)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.label_10 = QLabel(self.instructor_menu_stackedwidgetPage2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_10, 0, Qt.AlignTop)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)

        self.line = QFrame(self.instructor_menu_stackedwidgetPage2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.instructor_menu_stackedwidgetPage2)
        self.label_13.setObjectName(u"label_13")
        font5 = QFont()
        font5.setPointSize(12)
        self.label_13.setFont(font5)

        self.verticalLayout_14.addWidget(self.label_13, 0, Qt.AlignLeft)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.first_name_lineedit_stdntinfo = QLineEdit(self.instructor_menu_stackedwidgetPage2)
        self.first_name_lineedit_stdntinfo.setObjectName(u"first_name_lineedit_stdntinfo")

        self.verticalLayout_13.addWidget(self.first_name_lineedit_stdntinfo)

        self.label_30 = QLabel(self.instructor_menu_stackedwidgetPage2)
        self.label_30.setObjectName(u"label_30")
        font6 = QFont()
        font6.setPointSize(9)
        self.label_30.setFont(font6)

        self.verticalLayout_13.addWidget(self.label_30)


        self.horizontalLayout_6.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.last_name_lineedit_stdntinfo = QLineEdit(self.instructor_menu_stackedwidgetPage2)
        self.last_name_lineedit_stdntinfo.setObjectName(u"last_name_lineedit_stdntinfo")

        self.verticalLayout_12.addWidget(self.last_name_lineedit_stdntinfo)

        self.label_12 = QLabel(self.instructor_menu_stackedwidgetPage2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font6)

        self.verticalLayout_12.addWidget(self.label_12)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)


        self.verticalLayout_19.addLayout(self.verticalLayout_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.instructor_menu_stackedwidgetPage2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)

        self.verticalLayout_15.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.email_stdnt_lineedit_info = QLineEdit(self.instructor_menu_stackedwidgetPage2)
        self.email_stdnt_lineedit_info.setObjectName(u"email_stdnt_lineedit_info")

        self.verticalLayout_15.addWidget(self.email_stdnt_lineedit_info, 0, Qt.AlignVCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)


        self.verticalLayout_19.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_15 = QLabel(self.instructor_menu_stackedwidgetPage2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)

        self.verticalLayout_6.addWidget(self.label_15)

        self.password_stdnt_info = QLineEdit(self.instructor_menu_stackedwidgetPage2)
        self.password_stdnt_info.setObjectName(u"password_stdnt_info")
        self.password_stdnt_info.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.password_stdnt_info)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_19.addLayout(self.horizontalLayout_4)

        self.change_pass = QPushButton(self.instructor_menu_stackedwidgetPage2)
        self.change_pass.setObjectName(u"change_pass")
        self.change_pass.setMinimumSize(QSize(100, 40))

        self.verticalLayout_19.addWidget(self.change_pass, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_19)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.instructor_menu_stackedwidget.addTab(self.instructor_menu_stackedwidgetPage2, "")
        self.instructor_menu_stackedwidgetPage3 = QWidget()
        self.instructor_menu_stackedwidgetPage3.setObjectName(u"instructor_menu_stackedwidgetPage3")
        self.gridLayout_6 = QGridLayout(self.instructor_menu_stackedwidgetPage3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_43 = QLabel(self.instructor_menu_stackedwidgetPage3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)

        self.verticalLayout_55.addWidget(self.label_43)

        self.listsent_received_inbox_instructor = QListWidget(self.instructor_menu_stackedwidgetPage3)
        QListWidgetItem(self.listsent_received_inbox_instructor)
        self.listsent_received_inbox_instructor.setObjectName(u"listsent_received_inbox_instructor")
        self.listsent_received_inbox_instructor.setFont(font5)
        self.listsent_received_inbox_instructor.setFrameShape(QFrame.Box)
        self.listsent_received_inbox_instructor.setFrameShadow(QFrame.Plain)

        self.verticalLayout_55.addWidget(self.listsent_received_inbox_instructor)


        self.gridLayout_18.addLayout(self.verticalLayout_55, 0, 0, 1, 1)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_44 = QLabel(self.instructor_menu_stackedwidgetPage3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.verticalLayout_54.addWidget(self.label_44)

        self.received_message_instructor = QPlainTextEdit(self.instructor_menu_stackedwidgetPage3)
        self.received_message_instructor.setObjectName(u"received_message_instructor")
        self.received_message_instructor.setFrameShape(QFrame.Box)
        self.received_message_instructor.setFrameShadow(QFrame.Plain)
        self.received_message_instructor.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_54.addWidget(self.received_message_instructor)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.del_messages_instructor = QPushButton(self.instructor_menu_stackedwidgetPage3)
        self.del_messages_instructor.setObjectName(u"del_messages_instructor")
        self.del_messages_instructor.setMinimumSize(QSize(120, 60))

        self.horizontalLayout_17.addWidget(self.del_messages_instructor)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_12)

        self.send_message_instructor_btn = QPushButton(self.instructor_menu_stackedwidgetPage3)
        self.send_message_instructor_btn.setObjectName(u"send_message_instructor_btn")
        self.send_message_instructor_btn.setMinimumSize(QSize(120, 60))

        self.horizontalLayout_17.addWidget(self.send_message_instructor_btn, 0, Qt.AlignRight)


        self.verticalLayout_54.addLayout(self.horizontalLayout_17)


        self.gridLayout_18.addLayout(self.verticalLayout_54, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.instructor_menu_stackedwidget.addTab(self.instructor_menu_stackedwidgetPage3, "")

        self.gridLayout_3.addWidget(self.instructor_menu_stackedwidget, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.instructor_menu_stackedwidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.instructor_sched_btn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.instructor_info_btn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.instructor_inbox_btn.setText(QCoreApplication.translate("MainWindow", u"Inbox", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        ___qtablewidgetitem = self.instructor_room_sched_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Monday", None));
        ___qtablewidgetitem1 = self.instructor_room_sched_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None));
        ___qtablewidgetitem2 = self.instructor_room_sched_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None));
        ___qtablewidgetitem3 = self.instructor_room_sched_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Thursday", None));
        ___qtablewidgetitem4 = self.instructor_room_sched_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Friday", None));
        ___qtablewidgetitem5 = self.instructor_room_sched_table.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"7:00", None));
        ___qtablewidgetitem6 = self.instructor_room_sched_table.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"8:00", None));
        ___qtablewidgetitem7 = self.instructor_room_sched_table.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"9:00", None));
        ___qtablewidgetitem8 = self.instructor_room_sched_table.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"10:00", None));
        ___qtablewidgetitem9 = self.instructor_room_sched_table.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"11:00", None));
        ___qtablewidgetitem10 = self.instructor_room_sched_table.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"12:00", None));
        ___qtablewidgetitem11 = self.instructor_room_sched_table.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1:00", None));
        ___qtablewidgetitem12 = self.instructor_room_sched_table.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2:00", None));
        ___qtablewidgetitem13 = self.instructor_room_sched_table.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"3:00", None));
        ___qtablewidgetitem14 = self.instructor_room_sched_table.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"4:00", None));
        ___qtablewidgetitem15 = self.instructor_room_sched_table.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"5:00", None));
        ___qtablewidgetitem16 = self.instructor_room_sched_table.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"6:00", None));
        ___qtablewidgetitem17 = self.instructor_room_sched_table.verticalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"7:00", None));
        ___qtablewidgetitem18 = self.instructor_room_sched_table.verticalHeaderItem(13)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"8:00", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sched_table), QCoreApplication.translate("MainWindow", u"Schedules", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Accessed Room:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Registered Students", None))
        ___qtablewidgetitem19 = self.list_registered_stdnt_instructor_sched.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Student Name", None));
        ___qtablewidgetitem20 = self.list_registered_stdnt_instructor_sched.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem21 = self.list_registered_stdnt_instructor_sched.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1.", None));

        __sortingEnabled = self.list_registered_stdnt_instructor_sched.isSortingEnabled()
        self.list_registered_stdnt_instructor_sched.setSortingEnabled(False)
        ___qtablewidgetitem22 = self.list_registered_stdnt_instructor_sched.item(0, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Jonathan", None));
        ___qtablewidgetitem23 = self.list_registered_stdnt_instructor_sched.item(0, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"23-XXX", None));
        self.list_registered_stdnt_instructor_sched.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem24 = self.list_attendance.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Student Name", None));
        ___qtablewidgetitem25 = self.list_attendance.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem26 = self.list_attendance.verticalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"1.", None));

        __sortingEnabled1 = self.list_attendance.isSortingEnabled()
        self.list_attendance.setSortingEnabled(False)
        ___qtablewidgetitem27 = self.list_attendance.item(0, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Jonathan", None));
        ___qtablewidgetitem28 = self.list_attendance.item(0, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"23-XXX", None));
        self.list_attendance.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Room Access", None))
        self.instructor_menu_stackedwidget.setTabText(self.instructor_menu_stackedwidget.indexOf(self.instructor_menu_stackedwidgetPage1), "")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Room Access Status:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Instructor Information", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.change_pass.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.instructor_menu_stackedwidget.setTabText(self.instructor_menu_stackedwidget.indexOf(self.instructor_menu_stackedwidgetPage2), "")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Room Requests", None))

        __sortingEnabled2 = self.listsent_received_inbox_instructor.isSortingEnabled()
        self.listsent_received_inbox_instructor.setSortingEnabled(False)
        ___qlistwidgetitem = self.listsent_received_inbox_instructor.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Example of Received Messages", None));
        self.listsent_received_inbox_instructor.setSortingEnabled(__sortingEnabled2)

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Received Message", None))
        self.received_message_instructor.setPlainText(QCoreApplication.translate("MainWindow", u"Example Message\n"
"", None))
        self.del_messages_instructor.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.send_message_instructor_btn.setText(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.instructor_menu_stackedwidget.setTabText(self.instructor_menu_stackedwidget.indexOf(self.instructor_menu_stackedwidgetPage3), "")
    # retranslateUi

