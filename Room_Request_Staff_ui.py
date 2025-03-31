# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Room_Request_Staff.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(952, 713)
        Form.setMaximumSize(QSize(952, 713))
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_47 = QLabel(Form)
        self.label_47.setObjectName(u"label_47")
        font = QFont()
        font.setPointSize(14)
        self.label_47.setFont(font)

        self.verticalLayout.addWidget(self.label_47)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.choose_rm_btn = QPushButton(Form)
        self.choose_rm_btn.setObjectName(u"choose_rm_btn")

        self.horizontalLayout_4.addWidget(self.choose_rm_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.instructor_day_edit_comboBox = QComboBox(Form)
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.setObjectName(u"instructor_day_edit_comboBox")

        self.horizontalLayout_3.addWidget(self.instructor_day_edit_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_52 = QLabel(Form)
        self.label_52.setObjectName(u"label_52")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_52.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_52)

        self.start_time_staff = QTimeEdit(Form)
        self.start_time_staff.setObjectName(u"start_time_staff")

        self.verticalLayout_10.addWidget(self.start_time_staff)


        self.horizontalLayout_23.addLayout(self.verticalLayout_10)

        self.label_53 = QLabel(Form)
        self.label_53.setObjectName(u"label_53")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        self.label_53.setFont(font1)
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_53)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(7)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_54 = QLabel(Form)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font1)

        self.verticalLayout_59.addWidget(self.label_54)

        self.final_time_staff = QTimeEdit(Form)
        self.final_time_staff.setObjectName(u"final_time_staff")

        self.verticalLayout_59.addWidget(self.final_time_staff)


        self.horizontalLayout_23.addLayout(self.verticalLayout_59)


        self.verticalLayout.addLayout(self.horizontalLayout_23)

        self.label_48 = QLabel(Form)
        self.label_48.setObjectName(u"label_48")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_48.setFont(font2)

        self.verticalLayout.addWidget(self.label_48)

        self.room_request_staff = QPlainTextEdit(Form)
        self.room_request_staff.setObjectName(u"room_request_staff")
        self.room_request_staff.setMinimumSize(QSize(262, 388))
        self.room_request_staff.setFrameShape(QFrame.Box)
        self.room_request_staff.setFrameShadow(QFrame.Plain)
        self.room_request_staff.setOverwriteMode(False)

        self.verticalLayout.addWidget(self.room_request_staff)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(277, 423))
        self.sched_view_for_request = QWidget()
        self.sched_view_for_request.setObjectName(u"sched_view_for_request")
        self.gridLayout = QGridLayout(self.sched_view_for_request)
        self.gridLayout.setObjectName(u"gridLayout")
        self.staff_room_sched_table_request = QTableWidget(self.sched_view_for_request)
        if (self.staff_room_sched_table_request.columnCount() < 5):
            self.staff_room_sched_table_request.setColumnCount(5)
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
        if (self.staff_room_sched_table_request.rowCount() < 14):
            self.staff_room_sched_table_request.setRowCount(14)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(12, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.staff_room_sched_table_request.setVerticalHeaderItem(13, __qtablewidgetitem18)
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
        __qlistwidgetitem = QListWidgetItem(self.room_list_request_staff)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFont(font1);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
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

        self.send_btn_composed_request_instructor = QPushButton(self.list_rooms_request_staff)
        self.send_btn_composed_request_instructor.setObjectName(u"send_btn_composed_request_instructor")

        self.gridLayout_2.addWidget(self.send_btn_composed_request_instructor, 2, 0, 1, 1, Qt.AlignRight)

        self.stackedWidget.addWidget(self.list_rooms_request_staff)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dialog", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Room Request:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Choose Room:", None))
        self.choose_rm_btn.setText(QCoreApplication.translate("Form", u"Choose", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Choose Day:", None))
        self.instructor_day_edit_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Monday", None))
        self.instructor_day_edit_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Tuesday", None))
        self.instructor_day_edit_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Wednesday", None))
        self.instructor_day_edit_comboBox.setItemText(3, QCoreApplication.translate("Form", u"Thursday", None))
        self.instructor_day_edit_comboBox.setItemText(4, QCoreApplication.translate("Form", u"Friday", None))

        self.label_52.setText(QCoreApplication.translate("Form", u"Start of Schedule", None))
        self.label_53.setText(QCoreApplication.translate("Form", u":", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"End of Schedule", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"Message:", None))
        self.room_request_staff.setPlainText(QCoreApplication.translate("Form", u"Example message to send\n"
"\n"
"", None))
        ___qtablewidgetitem = self.staff_room_sched_table_request.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Monday", None));
        ___qtablewidgetitem1 = self.staff_room_sched_table_request.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tuesday", None));
        ___qtablewidgetitem2 = self.staff_room_sched_table_request.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Wednesday", None));
        ___qtablewidgetitem3 = self.staff_room_sched_table_request.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Thursday", None));
        ___qtablewidgetitem4 = self.staff_room_sched_table_request.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Friday", None));
        ___qtablewidgetitem5 = self.staff_room_sched_table_request.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"7:00", None));
        ___qtablewidgetitem6 = self.staff_room_sched_table_request.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"8:00", None));
        ___qtablewidgetitem7 = self.staff_room_sched_table_request.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"9:00", None));
        ___qtablewidgetitem8 = self.staff_room_sched_table_request.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"10:00", None));
        ___qtablewidgetitem9 = self.staff_room_sched_table_request.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"11:00", None));
        ___qtablewidgetitem10 = self.staff_room_sched_table_request.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"12:00", None));
        ___qtablewidgetitem11 = self.staff_room_sched_table_request.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"1:00", None));
        ___qtablewidgetitem12 = self.staff_room_sched_table_request.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"2:00", None));
        ___qtablewidgetitem13 = self.staff_room_sched_table_request.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"3:00", None));
        ___qtablewidgetitem14 = self.staff_room_sched_table_request.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"4:00", None));
        ___qtablewidgetitem15 = self.staff_room_sched_table_request.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"5:00", None));
        ___qtablewidgetitem16 = self.staff_room_sched_table_request.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"6:00", None));
        ___qtablewidgetitem17 = self.staff_room_sched_table_request.verticalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"7:00", None));
        ___qtablewidgetitem18 = self.staff_room_sched_table_request.verticalHeaderItem(13)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"8:00", None));
        self.back_room_select_staff.setText(QCoreApplication.translate("Form", u"Return", None))

        __sortingEnabled = self.room_list_request_staff.isSortingEnabled()
        self.room_list_request_staff.setSortingEnabled(False)
        ___qlistwidgetitem = self.room_list_request_staff.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Room 1", None));
        self.room_list_request_staff.setSortingEnabled(__sortingEnabled)

        self.search_room_request_staff_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.send_btn_composed_request_instructor.setText(QCoreApplication.translate("Form", u"Send", None))
    # retranslateUi

