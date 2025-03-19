# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Room_Request_Staff.ui'
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
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(572, 482)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.back_btn_request_staff = QPushButton(Form)
        self.back_btn_request_staff.setObjectName(u"back_btn_request_staff")

        self.verticalLayout.addWidget(self.back_btn_request_staff, 0, Qt.AlignLeft)

        self.label_47 = QLabel(Form)
        self.label_47.setObjectName(u"label_47")
        font = QFont()
        font.setPointSize(14)
        self.label_47.setFont(font)

        self.verticalLayout.addWidget(self.label_47)

        self.room_request_staff = QPlainTextEdit(Form)
        self.room_request_staff.setObjectName(u"room_request_staff")
        self.room_request_staff.setMinimumSize(QSize(262, 388))
        self.room_request_staff.setFrameShape(QFrame.Box)
        self.room_request_staff.setFrameShadow(QFrame.Plain)
        self.room_request_staff.setOverwriteMode(False)

        self.verticalLayout.addWidget(self.room_request_staff)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(277, 423))
        self.sched_view_for_request = QWidget()
        self.sched_view_for_request.setObjectName(u"sched_view_for_request")
        self.gridLayout = QGridLayout(self.sched_view_for_request)
        self.gridLayout.setObjectName(u"gridLayout")
        self.staff_room_sched_table_request = QTableWidget(self.sched_view_for_request)
        if (self.staff_room_sched_table_request.columnCount() < 6):
            self.staff_room_sched_table_request.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.staff_room_sched_table_request.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.staff_room_sched_table_request.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.staff_room_sched_table_request.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.staff_room_sched_table_request.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.staff_room_sched_table_request.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.staff_room_sched_table_request.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.staff_room_sched_table_request.setObjectName(u"staff_room_sched_table_request")

        self.gridLayout.addWidget(self.staff_room_sched_table_request, 1, 0, 1, 1)

        self.back_room_select_staff = QPushButton(self.sched_view_for_request)
        self.back_room_select_staff.setObjectName(u"back_room_select_staff")

        self.gridLayout.addWidget(self.back_room_select_staff, 0, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.sched_view_for_request)
        self.list_rooms_request_staff = QWidget()
        self.list_rooms_request_staff.setObjectName(u"list_rooms_request_staff")
        self.gridLayout_2 = QGridLayout(self.list_rooms_request_staff)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.room_list_request_staff = QListWidget(self.list_rooms_request_staff)
        font1 = QFont()
        font1.setPointSize(12)
        __qlistwidgetitem = QListWidgetItem(self.room_list_request_staff)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFont(font1);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.room_list_request_staff)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.room_list_request_staff)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.room_list_request_staff)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.room_list_request_staff.setObjectName(u"room_list_request_staff")

        self.gridLayout_2.addWidget(self.room_list_request_staff, 1, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.search_bar_room_request_staff = QLineEdit(self.list_rooms_request_staff)
        self.search_bar_room_request_staff.setObjectName(u"search_bar_room_request_staff")

        self.horizontalLayout_19.addWidget(self.search_bar_room_request_staff)

        self.search_room_request_staff_btn = QPushButton(self.list_rooms_request_staff)
        self.search_room_request_staff_btn.setObjectName(u"search_room_request_staff_btn")

        self.horizontalLayout_19.addWidget(self.search_room_request_staff_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.list_rooms_request_staff)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.send_btn_composed_request_instructor = QPushButton(Form)
        self.send_btn_composed_request_instructor.setObjectName(u"send_btn_composed_request_instructor")

        self.verticalLayout_2.addWidget(self.send_btn_composed_request_instructor, 0, Qt.AlignRight)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dialog", None))
        self.back_btn_request_staff.setText(QCoreApplication.translate("Form", u"Back", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Room Request:", None))
        self.room_request_staff.setPlainText(QCoreApplication.translate("Form", u"Example message to send\n"
"\n"
"", None))
        ___qtablewidgetitem = self.staff_room_sched_table_request.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Time Schedule", None));
        ___qtablewidgetitem1 = self.staff_room_sched_table_request.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Monday", None));
        ___qtablewidgetitem2 = self.staff_room_sched_table_request.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tuesday", None));
        ___qtablewidgetitem3 = self.staff_room_sched_table_request.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Wednesday", None));
        ___qtablewidgetitem4 = self.staff_room_sched_table_request.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Thursday", None));
        ___qtablewidgetitem5 = self.staff_room_sched_table_request.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Friday", None));
        self.back_room_select_staff.setText(QCoreApplication.translate("Form", u"Return", None))

        __sortingEnabled = self.room_list_request_staff.isSortingEnabled()
        self.room_list_request_staff.setSortingEnabled(False)
        ___qlistwidgetitem = self.room_list_request_staff.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Room 1", None));
        ___qlistwidgetitem1 = self.room_list_request_staff.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"rm 2", None));
        ___qlistwidgetitem2 = self.room_list_request_staff.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"rm 3", None));
        ___qlistwidgetitem3 = self.room_list_request_staff.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"rm 4", None));
        self.room_list_request_staff.setSortingEnabled(__sortingEnabled)

        self.search_room_request_staff_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.send_btn_composed_request_instructor.setText(QCoreApplication.translate("Form", u"Send", None))
    # retranslateUi

