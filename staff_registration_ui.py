# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'staff_registration.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(886, 735)
        Form.setMinimumSize(QSize(886, 735))
        Form.setMaximumSize(QSize(1248, 735))
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.sort_instructor = QComboBox(Form)
        self.sort_instructor.addItem("")
        self.sort_instructor.addItem("")
        self.sort_instructor.addItem("")
        self.sort_instructor.setObjectName(u"sort_instructor")

        self.horizontalLayout_13.addWidget(self.sort_instructor)

        self.search_bar_staff = QLineEdit(Form)
        self.search_bar_staff.setObjectName(u"search_bar_staff")

        self.horizontalLayout_13.addWidget(self.search_bar_staff)

        self.search_staff_btn = QPushButton(Form)
        self.search_staff_btn.setObjectName(u"search_staff_btn")

        self.horizontalLayout_13.addWidget(self.search_staff_btn, 0, Qt.AlignRight)


        self.gridLayout_15.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.verticalLayout_41.addLayout(self.gridLayout_15)

        self.list_registered_staff = QTableWidget(Form)
        if (self.list_registered_staff.columnCount() < 3):
            self.list_registered_staff.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.list_registered_staff.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list_registered_staff.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list_registered_staff.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.list_registered_staff.rowCount() < 1):
            self.list_registered_staff.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.list_registered_staff.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.list_registered_staff.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.list_registered_staff.setItem(0, 2, __qtablewidgetitem5)
        self.list_registered_staff.setObjectName(u"list_registered_staff")
        font = QFont()
        font.setPointSize(10)
        self.list_registered_staff.setFont(font)
        self.list_registered_staff.setFrameShadow(QFrame.Plain)
        self.list_registered_staff.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.verticalLayout_41.addWidget(self.list_registered_staff)


        self.gridLayout_3.addLayout(self.verticalLayout_41, 0, 1, 1, 1)

        self.tabWidget_instructor = QTabWidget(Form)
        self.tabWidget_instructor.setObjectName(u"tabWidget_instructor")
        self.tabWidget_instructor.setMinimumSize(QSize(400, 500))
        self.tabWidget_instructor.setMaximumSize(QSize(600, 16777215))
        self.tabWidget_instructor.setFont(font)
        self.register_staff = QWidget()
        self.register_staff.setObjectName(u"register_staff")
        self.gridLayout_2 = QGridLayout(self.register_staff)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_33 = QLabel(self.register_staff)
        self.label_33.setObjectName(u"label_33")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_33.setFont(font1)

        self.verticalLayout_43.addWidget(self.label_33, 0, Qt.AlignLeft)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.first_name_lineedit_staff = QLineEdit(self.register_staff)
        self.first_name_lineedit_staff.setObjectName(u"first_name_lineedit_staff")
        self.first_name_lineedit_staff.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_44.addWidget(self.first_name_lineedit_staff)

        self.label_34 = QLabel(self.register_staff)
        self.label_34.setObjectName(u"label_34")
        font2 = QFont()
        font2.setPointSize(9)
        self.label_34.setFont(font2)

        self.verticalLayout_44.addWidget(self.label_34)


        self.horizontalLayout_14.addLayout(self.verticalLayout_44)

        self.horizontalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_10)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.lastname_lineedit_staff = QLineEdit(self.register_staff)
        self.lastname_lineedit_staff.setObjectName(u"lastname_lineedit_staff")
        self.lastname_lineedit_staff.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_45.addWidget(self.lastname_lineedit_staff)

        self.label_35 = QLabel(self.register_staff)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.verticalLayout_45.addWidget(self.label_35)


        self.horizontalLayout_14.addLayout(self.verticalLayout_45)


        self.verticalLayout_43.addLayout(self.horizontalLayout_14)


        self.verticalLayout_42.addLayout(self.verticalLayout_43)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_42.addItem(self.verticalSpacer_3)

        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_36 = QLabel(self.register_staff)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)

        self.verticalLayout_46.addWidget(self.label_36, 0, Qt.AlignLeft)

        self.email_staff_lineedit = QLineEdit(self.register_staff)
        self.email_staff_lineedit.setObjectName(u"email_staff_lineedit")
        self.email_staff_lineedit.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_46.addWidget(self.email_staff_lineedit, 0, Qt.AlignVCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_46.addItem(self.verticalSpacer_12)


        self.verticalLayout_62.addLayout(self.verticalLayout_46)


        self.verticalLayout_42.addLayout(self.verticalLayout_62)

        self.label_27 = QLabel(self.register_staff)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.verticalLayout_42.addWidget(self.label_27)

        self.ID_staff = QLineEdit(self.register_staff)
        self.ID_staff.setObjectName(u"ID_staff")
        self.ID_staff.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_42.addWidget(self.ID_staff)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_42.addItem(self.verticalSpacer_13)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_37 = QLabel(self.register_staff)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.verticalLayout_48.addWidget(self.label_37, 0, Qt.AlignLeft)

        self.password_staff_reg = QLineEdit(self.register_staff)
        self.password_staff_reg.setObjectName(u"password_staff_reg")
        self.password_staff_reg.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_48.addWidget(self.password_staff_reg)

        self.verticalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_48.addItem(self.verticalSpacer_15)


        self.verticalLayout_47.addLayout(self.verticalLayout_48)

        self.pass_generate_staff = QPushButton(self.register_staff)
        self.pass_generate_staff.setObjectName(u"pass_generate_staff")
        self.pass_generate_staff.setMinimumSize(QSize(100, 40))

        self.verticalLayout_47.addWidget(self.pass_generate_staff, 0, Qt.AlignLeft)


        self.verticalLayout_42.addLayout(self.verticalLayout_47)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer)

        self.save_staff_btn = QPushButton(self.register_staff)
        self.save_staff_btn.setObjectName(u"save_staff_btn")
        self.save_staff_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout_42.addWidget(self.save_staff_btn, 0, Qt.AlignRight)


        self.gridLayout_2.addLayout(self.verticalLayout_42, 2, 0, 1, 1)

        self.label_32 = QLabel(self.register_staff)
        self.label_32.setObjectName(u"label_32")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_32.setFont(font3)

        self.gridLayout_2.addWidget(self.label_32, 0, 0, 1, 1, Qt.AlignHCenter)

        self.line = QFrame(self.register_staff)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.tabWidget_instructor.addTab(self.register_staff, "")
        self.remove_staff = QWidget()
        self.remove_staff.setObjectName(u"remove_staff")
        self.gridLayout = QGridLayout(self.remove_staff)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_28 = QLabel(self.remove_staff)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.gridLayout.addWidget(self.label_28, 0, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_30 = QLabel(self.remove_staff)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.verticalLayout_50.addWidget(self.label_30, 0, Qt.AlignLeft)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.first_name_lineedit_remove_staff = QLineEdit(self.remove_staff)
        self.first_name_lineedit_remove_staff.setObjectName(u"first_name_lineedit_remove_staff")

        self.verticalLayout_51.addWidget(self.first_name_lineedit_remove_staff)

        self.label_38 = QLabel(self.remove_staff)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)

        self.verticalLayout_51.addWidget(self.label_38)


        self.horizontalLayout_15.addLayout(self.verticalLayout_51)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.last_name_lineedit_remove_staff = QLineEdit(self.remove_staff)
        self.last_name_lineedit_remove_staff.setObjectName(u"last_name_lineedit_remove_staff")

        self.verticalLayout_52.addWidget(self.last_name_lineedit_remove_staff)

        self.label_39 = QLabel(self.remove_staff)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.verticalLayout_52.addWidget(self.label_39)


        self.horizontalLayout_15.addLayout(self.verticalLayout_52)


        self.verticalLayout_50.addLayout(self.horizontalLayout_15)


        self.verticalLayout_49.addLayout(self.verticalLayout_50)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_49.addItem(self.verticalSpacer_5)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_40 = QLabel(self.remove_staff)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)

        self.verticalLayout_53.addWidget(self.label_40, 0, Qt.AlignLeft)

        self.ID_staff_remove = QLineEdit(self.remove_staff)
        self.ID_staff_remove.setObjectName(u"ID_staff_remove")
        self.ID_staff_remove.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_53.addWidget(self.ID_staff_remove, 0, Qt.AlignVCenter)

        self.verticalSpacer_18 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_53.addItem(self.verticalSpacer_18)


        self.verticalLayout_49.addLayout(self.verticalLayout_53)

        self.del_staff_inlist = QPushButton(self.remove_staff)
        self.del_staff_inlist.setObjectName(u"del_staff_inlist")
        self.del_staff_inlist.setMinimumSize(QSize(100, 40))

        self.verticalLayout_49.addWidget(self.del_staff_inlist, 0, Qt.AlignRight)

        self.verticalSpacer_4 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_49.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_49, 2, 0, 1, 1)

        self.tabWidget_instructor.addTab(self.remove_staff, "")

        self.gridLayout_3.addWidget(self.tabWidget_instructor, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget_instructor.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Sort by:", None))
        self.sort_instructor.setItemText(0, QCoreApplication.translate("Form", u"Name", None))
        self.sort_instructor.setItemText(1, QCoreApplication.translate("Form", u"Email", None))
        self.sort_instructor.setItemText(2, QCoreApplication.translate("Form", u"ID", None))

        self.sort_instructor.setCurrentText(QCoreApplication.translate("Form", u"Name", None))
        self.search_staff_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        ___qtablewidgetitem = self.list_registered_staff.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem1 = self.list_registered_staff.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID No.", None));
        ___qtablewidgetitem2 = self.list_registered_staff.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem3 = self.list_registered_staff.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"1.", None));

        __sortingEnabled = self.list_registered_staff.isSortingEnabled()
        self.list_registered_staff.setSortingEnabled(False)
        self.list_registered_staff.setSortingEnabled(__sortingEnabled)

        self.label_33.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"ID Number:", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.pass_generate_staff.setText(QCoreApplication.translate("Form", u"Generate Password", None))
        self.save_staff_btn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Register Staff", None))
        self.tabWidget_instructor.setTabText(self.tabWidget_instructor.indexOf(self.register_staff), QCoreApplication.translate("Form", u"Register", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Remove Staff", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"ID Number:", None))
        self.del_staff_inlist.setText(QCoreApplication.translate("Form", u"Remove ", None))
        self.tabWidget_instructor.setTabText(self.tabWidget_instructor.indexOf(self.remove_staff), QCoreApplication.translate("Form", u"Remove", None))
    # retranslateUi

