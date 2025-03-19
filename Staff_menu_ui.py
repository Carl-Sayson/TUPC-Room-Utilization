# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Staff_menu.ui'
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
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.staff_sched_btn = QPushButton(self.centralwidget)
        self.staff_sched_btn.setObjectName(u"staff_sched_btn")
        self.staff_sched_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.staff_sched_btn)

        self.staff_info_btn = QPushButton(self.centralwidget)
        self.staff_info_btn.setObjectName(u"staff_info_btn")
        self.staff_info_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.staff_info_btn)

        self.staff_inbox_btn = QPushButton(self.centralwidget)
        self.staff_inbox_btn.setObjectName(u"staff_inbox_btn")
        self.staff_inbox_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.staff_inbox_btn)


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
        self.staff_menu_stackedwidget = QTabWidget(self.frame_2)
        self.staff_menu_stackedwidget.setObjectName(u"staff_menu_stackedwidget")
        self.staff_menu_stackedwidget.tabBar().setVisible(False)
        self.staff_menu_stackedwidgetPage1 = QWidget()
        self.staff_menu_stackedwidgetPage1.setObjectName(u"staff_menu_stackedwidgetPage1")
        self.gridLayout_2 = QGridLayout(self.staff_menu_stackedwidgetPage1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.staff_room_sched_table = QTableWidget(self.staff_menu_stackedwidgetPage1)
        if (self.staff_room_sched_table.columnCount() < 5):
            self.staff_room_sched_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.staff_room_sched_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.staff_room_sched_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.staff_room_sched_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.staff_room_sched_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.staff_room_sched_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.staff_room_sched_table.rowCount() < 14):
            self.staff_room_sched_table.setRowCount(14)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(12, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.staff_room_sched_table.setVerticalHeaderItem(13, __qtablewidgetitem18)
        self.staff_room_sched_table.setObjectName(u"staff_room_sched_table")

        self.gridLayout_2.addWidget(self.staff_room_sched_table, 0, 0, 1, 1)

        self.staff_menu_stackedwidget.addTab(self.staff_menu_stackedwidgetPage1, "")
        self.staff_menu_stackedwidgetPage2 = QWidget()
        self.staff_menu_stackedwidgetPage2.setObjectName(u"staff_menu_stackedwidgetPage2")
        self.gridLayout_4 = QGridLayout(self.staff_menu_stackedwidgetPage2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.staff_menu_stackedwidgetPage2)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_11.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.room_access_status_staff = QLineEdit(self.staff_menu_stackedwidgetPage2)
        self.room_access_status_staff.setObjectName(u"room_access_status_staff")
        self.room_access_status_staff.setMaximumSize(QSize(450, 16777215))
        self.room_access_status_staff.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.room_access_status_staff, 0, Qt.AlignTop)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.label_10 = QLabel(self.staff_menu_stackedwidgetPage2)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_10.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_10, 0, Qt.AlignTop)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)

        self.line = QFrame(self.staff_menu_stackedwidgetPage2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.staff_menu_stackedwidgetPage2)
        self.label_13.setObjectName(u"label_13")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_13.setFont(font4)

        self.verticalLayout_14.addWidget(self.label_13, 0, Qt.AlignLeft)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.first_name_lineedit_stdntinfo = QLineEdit(self.staff_menu_stackedwidgetPage2)
        self.first_name_lineedit_stdntinfo.setObjectName(u"first_name_lineedit_stdntinfo")

        self.verticalLayout_13.addWidget(self.first_name_lineedit_stdntinfo)

        self.label_30 = QLabel(self.staff_menu_stackedwidgetPage2)
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
        self.last_name_lineedit_stdntinfo = QLineEdit(self.staff_menu_stackedwidgetPage2)
        self.last_name_lineedit_stdntinfo.setObjectName(u"last_name_lineedit_stdntinfo")

        self.verticalLayout_12.addWidget(self.last_name_lineedit_stdntinfo)

        self.label_12 = QLabel(self.staff_menu_stackedwidgetPage2)
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
        self.label_14 = QLabel(self.staff_menu_stackedwidgetPage2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)

        self.verticalLayout_15.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.email_stdnt_lineedit_info = QLineEdit(self.staff_menu_stackedwidgetPage2)
        self.email_stdnt_lineedit_info.setObjectName(u"email_stdnt_lineedit_info")

        self.verticalLayout_15.addWidget(self.email_stdnt_lineedit_info, 0, Qt.AlignVCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)


        self.verticalLayout_19.addLayout(self.horizontalLayout_7)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_15 = QLabel(self.staff_menu_stackedwidgetPage2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.verticalLayout_5.addWidget(self.label_15)

        self.password_staff_info = QLineEdit(self.staff_menu_stackedwidgetPage2)
        self.password_staff_info.setObjectName(u"password_staff_info")
        self.password_staff_info.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.password_staff_info)


        self.verticalLayout_17.addLayout(self.verticalLayout_5)


        self.verticalLayout_19.addLayout(self.verticalLayout_17)

        self.change_pass = QPushButton(self.staff_menu_stackedwidgetPage2)
        self.change_pass.setObjectName(u"change_pass")
        self.change_pass.setMinimumSize(QSize(100, 40))

        self.verticalLayout_19.addWidget(self.change_pass, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_19)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.staff_menu_stackedwidget.addTab(self.staff_menu_stackedwidgetPage2, "")
        self.staff_menu_stackedwidgetPage3 = QWidget()
        self.staff_menu_stackedwidgetPage3.setObjectName(u"staff_menu_stackedwidgetPage3")
        self.gridLayout_6 = QGridLayout(self.staff_menu_stackedwidgetPage3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.staff_menu_stackedwidgetPage3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setFont(font2)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.Roomrequest_tab = QWidget()
        self.Roomrequest_tab.setObjectName(u"Roomrequest_tab")
        self.Roomrequest_tab.setMinimumSize(QSize(0, 0))
        self.Roomrequest_tab.setMouseTracking(False)
        self.Roomrequest_tab.setTabletTracking(False)
        self.Roomrequest_tab.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.gridLayout_19 = QGridLayout(self.Roomrequest_tab)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_43 = QLabel(self.Roomrequest_tab)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)

        self.verticalLayout_55.addWidget(self.label_43)

        self.listWidget_2 = QListWidget(self.Roomrequest_tab)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setFont(font4)
        self.listWidget_2.setFrameShape(QFrame.Box)
        self.listWidget_2.setFrameShadow(QFrame.Plain)

        self.verticalLayout_55.addWidget(self.listWidget_2)


        self.gridLayout_18.addLayout(self.verticalLayout_55, 0, 0, 1, 1)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_44 = QLabel(self.Roomrequest_tab)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.verticalLayout_54.addWidget(self.label_44)

        self.received_request = QPlainTextEdit(self.Roomrequest_tab)
        self.received_request.setObjectName(u"received_request")
        self.received_request.setFrameShape(QFrame.Box)
        self.received_request.setFrameShadow(QFrame.Plain)
        self.received_request.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_54.addWidget(self.received_request)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.del_request = QPushButton(self.Roomrequest_tab)
        self.del_request.setObjectName(u"del_request")
        self.del_request.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_17.addWidget(self.del_request)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_12)

        self.compose_staff = QPushButton(self.Roomrequest_tab)
        self.compose_staff.setObjectName(u"compose_staff")
        self.compose_staff.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_17.addWidget(self.compose_staff, 0, Qt.AlignRight)


        self.verticalLayout_54.addLayout(self.horizontalLayout_17)


        self.gridLayout_18.addLayout(self.verticalLayout_54, 0, 1, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Roomrequest_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_21 = QGridLayout(self.tab_2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_48 = QLabel(self.tab_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font3)

        self.verticalLayout_57.addWidget(self.label_48)

        self.listWidget_3 = QListWidget(self.tab_2)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setFont(font4)
        self.listWidget_3.setFrameShape(QFrame.Box)
        self.listWidget_3.setFrameShadow(QFrame.Plain)

        self.verticalLayout_57.addWidget(self.listWidget_3)


        self.gridLayout_20.addLayout(self.verticalLayout_57, 0, 0, 1, 1)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_46 = QLabel(self.tab_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.verticalLayout_56.addWidget(self.label_46)

        self.received_report = QPlainTextEdit(self.tab_2)
        self.received_report.setObjectName(u"received_report")
        self.received_report.setFrameShape(QFrame.Box)
        self.received_report.setFrameShadow(QFrame.Plain)
        self.received_report.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_56.addWidget(self.received_report)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.del_report = QPushButton(self.tab_2)
        self.del_report.setObjectName(u"del_report")
        self.del_report.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_18.addWidget(self.del_report)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)

        self.compose_message_report_btn = QPushButton(self.tab_2)
        self.compose_message_report_btn.setObjectName(u"compose_message_report_btn")
        self.compose_message_report_btn.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_18.addWidget(self.compose_message_report_btn, 0, Qt.AlignRight)


        self.verticalLayout_56.addLayout(self.horizontalLayout_18)


        self.gridLayout_20.addLayout(self.verticalLayout_56, 0, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.staff_menu_stackedwidget.addTab(self.staff_menu_stackedwidgetPage3, "")

        self.gridLayout_3.addWidget(self.staff_menu_stackedwidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.staff_menu_stackedwidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.staff_sched_btn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.staff_info_btn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.staff_inbox_btn.setText(QCoreApplication.translate("MainWindow", u"Inbox", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        ___qtablewidgetitem = self.staff_room_sched_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Monday", None));
        ___qtablewidgetitem1 = self.staff_room_sched_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None));
        ___qtablewidgetitem2 = self.staff_room_sched_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None));
        ___qtablewidgetitem3 = self.staff_room_sched_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Thursday", None));
        ___qtablewidgetitem4 = self.staff_room_sched_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Friday", None));
        ___qtablewidgetitem5 = self.staff_room_sched_table.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"7:00", None));
        ___qtablewidgetitem6 = self.staff_room_sched_table.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"8:00", None));
        ___qtablewidgetitem7 = self.staff_room_sched_table.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"9:00", None));
        ___qtablewidgetitem8 = self.staff_room_sched_table.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"10:00", None));
        ___qtablewidgetitem9 = self.staff_room_sched_table.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"11:00", None));
        ___qtablewidgetitem10 = self.staff_room_sched_table.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"12:00", None));
        ___qtablewidgetitem11 = self.staff_room_sched_table.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1:00", None));
        ___qtablewidgetitem12 = self.staff_room_sched_table.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2:00", None));
        ___qtablewidgetitem13 = self.staff_room_sched_table.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"3:00", None));
        ___qtablewidgetitem14 = self.staff_room_sched_table.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"4:00", None));
        ___qtablewidgetitem15 = self.staff_room_sched_table.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"5:00", None));
        ___qtablewidgetitem16 = self.staff_room_sched_table.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"6:00", None));
        ___qtablewidgetitem17 = self.staff_room_sched_table.verticalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"7:00", None));
        ___qtablewidgetitem18 = self.staff_room_sched_table.verticalHeaderItem(13)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"8:00", None));
        self.staff_menu_stackedwidget.setTabText(self.staff_menu_stackedwidget.indexOf(self.staff_menu_stackedwidgetPage1), "")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Room Access Status:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Staff Information", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.change_pass.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.staff_menu_stackedwidget.setTabText(self.staff_menu_stackedwidget.indexOf(self.staff_menu_stackedwidgetPage2), "")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Room Maintenance Requests", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Example Received Request", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Received Message", None))
        self.received_request.setPlainText(QCoreApplication.translate("MainWindow", u"Example Message\n"
"", None))
        self.del_request.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.compose_staff.setText(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Roomrequest_tab), QCoreApplication.translate("MainWindow", u"Room Request", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Reports", None))

        __sortingEnabled1 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_3.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Example Received Report", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled1)

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Received Message", None))
        self.received_report.setPlainText(QCoreApplication.translate("MainWindow", u"Example Message\n"
"", None))
        self.del_report.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.compose_message_report_btn.setText(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Maintenance / Damage Report", None))
        self.staff_menu_stackedwidget.setTabText(self.staff_menu_stackedwidget.indexOf(self.staff_menu_stackedwidgetPage3), "")
    # retranslateUi

