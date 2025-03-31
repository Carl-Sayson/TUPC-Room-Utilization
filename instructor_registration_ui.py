# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instructor_registration.ui'
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
        Form.resize(887, 734)
        Form.setMinimumSize(QSize(887, 734))
        Form.setMaximumSize(QSize(1248, 735))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_24)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.sort_instructor = QComboBox(Form)
        self.sort_instructor.addItem("")
        self.sort_instructor.addItem("")
        self.sort_instructor.addItem("")
        self.sort_instructor.setObjectName(u"sort_instructor")

        self.horizontalLayout_14.addWidget(self.sort_instructor)

        self.search_bar_instructor = QLineEdit(Form)
        self.search_bar_instructor.setObjectName(u"search_bar_instructor")

        self.horizontalLayout_14.addWidget(self.search_bar_instructor)

        self.search_instructor_btn = QPushButton(Form)
        self.search_instructor_btn.setObjectName(u"search_instructor_btn")

        self.horizontalLayout_14.addWidget(self.search_instructor_btn)


        self.gridLayout_10.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)


        self.verticalLayout_40.addLayout(self.gridLayout_10)

        self.list_registered_instructor = QTableWidget(Form)
        if (self.list_registered_instructor.columnCount() < 3):
            self.list_registered_instructor.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.list_registered_instructor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list_registered_instructor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list_registered_instructor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.list_registered_instructor.rowCount() < 1):
            self.list_registered_instructor.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.list_registered_instructor.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.list_registered_instructor.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.list_registered_instructor.setItem(0, 2, __qtablewidgetitem5)
        self.list_registered_instructor.setObjectName(u"list_registered_instructor")
        font = QFont()
        font.setPointSize(10)
        self.list_registered_instructor.setFont(font)
        self.list_registered_instructor.setFrameShadow(QFrame.Plain)
        self.list_registered_instructor.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.verticalLayout_40.addWidget(self.list_registered_instructor)


        self.gridLayout_2.addLayout(self.verticalLayout_40, 0, 1, 1, 1)

        self.tabWidget_instructor = QTabWidget(Form)
        self.tabWidget_instructor.setObjectName(u"tabWidget_instructor")
        self.tabWidget_instructor.setMinimumSize(QSize(400, 500))
        self.tabWidget_instructor.setMaximumSize(QSize(600, 16777215))
        self.tabWidget_instructor.setFont(font)
        self.register_instructor = QWidget()
        self.register_instructor.setObjectName(u"register_instructor")
        self.gridLayout = QGridLayout(self.register_instructor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_20 = QLabel(self.register_instructor)
        self.label_20.setObjectName(u"label_20")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_20.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.verticalSpacer_19 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_26.addItem(self.verticalSpacer_19)

        self.line_7 = QFrame(self.register_instructor)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_26.addWidget(self.line_7)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_21 = QLabel(self.register_instructor)
        self.label_21.setObjectName(u"label_21")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_21.setFont(font2)

        self.verticalLayout_28.addWidget(self.label_21, 0, Qt.AlignLeft)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.first_name_lineedit_instructor = QLineEdit(self.register_instructor)
        self.first_name_lineedit_instructor.setObjectName(u"first_name_lineedit_instructor")
        self.first_name_lineedit_instructor.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_29.addWidget(self.first_name_lineedit_instructor)

        self.label_24 = QLabel(self.register_instructor)
        self.label_24.setObjectName(u"label_24")
        font3 = QFont()
        font3.setPointSize(9)
        self.label_24.setFont(font3)

        self.verticalLayout_29.addWidget(self.label_24)


        self.horizontalLayout_9.addLayout(self.verticalLayout_29)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.lastname_lineedit_instructor = QLineEdit(self.register_instructor)
        self.lastname_lineedit_instructor.setObjectName(u"lastname_lineedit_instructor")
        self.lastname_lineedit_instructor.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_30.addWidget(self.lastname_lineedit_instructor)

        self.label_22 = QLabel(self.register_instructor)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.verticalLayout_30.addWidget(self.label_22)


        self.horizontalLayout_9.addLayout(self.verticalLayout_30)


        self.verticalLayout_28.addLayout(self.horizontalLayout_9)


        self.verticalLayout_27.addLayout(self.verticalLayout_28)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_27.addItem(self.verticalSpacer_2)

        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_23 = QLabel(self.register_instructor)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.verticalLayout_32.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.email_instructor_lineedit = QLineEdit(self.register_instructor)
        self.email_instructor_lineedit.setObjectName(u"email_instructor_lineedit")
        self.email_instructor_lineedit.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_32.addWidget(self.email_instructor_lineedit, 0, Qt.AlignVCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_32.addItem(self.verticalSpacer_11)


        self.verticalLayout_63.addLayout(self.verticalLayout_32)


        self.verticalLayout_27.addLayout(self.verticalLayout_63)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_26 = QLabel(self.register_instructor)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.verticalLayout_38.addWidget(self.label_26)


        self.verticalLayout_37.addLayout(self.verticalLayout_38)

        self.ID_instructor = QLineEdit(self.register_instructor)
        self.ID_instructor.setObjectName(u"ID_instructor")
        self.ID_instructor.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_37.addWidget(self.ID_instructor)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_16)


        self.verticalLayout_27.addLayout(self.verticalLayout_37)

        self.label_25 = QLabel(self.register_instructor)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.verticalLayout_27.addWidget(self.label_25)

        self.password_instructor_reg = QLineEdit(self.register_instructor)
        self.password_instructor_reg.setObjectName(u"password_instructor_reg")
        self.password_instructor_reg.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_27.addWidget(self.password_instructor_reg)

        self.pass_generate_instructor = QPushButton(self.register_instructor)
        self.pass_generate_instructor.setObjectName(u"pass_generate_instructor")
        self.pass_generate_instructor.setMinimumSize(QSize(100, 40))

        self.verticalLayout_27.addWidget(self.pass_generate_instructor, 0, Qt.AlignLeft)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer)

        self.save_instructor_btn = QPushButton(self.register_instructor)
        self.save_instructor_btn.setObjectName(u"save_instructor_btn")
        self.save_instructor_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout_27.addWidget(self.save_instructor_btn, 0, Qt.AlignRight)


        self.verticalLayout_26.addLayout(self.verticalLayout_27)


        self.gridLayout.addLayout(self.verticalLayout_26, 0, 0, 1, 1)

        self.tabWidget_instructor.addTab(self.register_instructor, "")
        self.remove_instructor = QWidget()
        self.remove_instructor.setObjectName(u"remove_instructor")
        self.gridLayout_3 = QGridLayout(self.remove_instructor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_30 = QLabel(self.remove_instructor)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.verticalLayout_50.addWidget(self.label_30, 0, Qt.AlignLeft)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.first_name_lineedit_remove_instructor_3 = QLineEdit(self.remove_instructor)
        self.first_name_lineedit_remove_instructor_3.setObjectName(u"first_name_lineedit_remove_instructor_3")

        self.verticalLayout_51.addWidget(self.first_name_lineedit_remove_instructor_3)

        self.label_37 = QLabel(self.remove_instructor)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.verticalLayout_51.addWidget(self.label_37)


        self.horizontalLayout_13.addLayout(self.verticalLayout_51)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.last_name_lineedit_remove_instructor_3 = QLineEdit(self.remove_instructor)
        self.last_name_lineedit_remove_instructor_3.setObjectName(u"last_name_lineedit_remove_instructor_3")

        self.verticalLayout_52.addWidget(self.last_name_lineedit_remove_instructor_3)

        self.label_38 = QLabel(self.remove_instructor)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.verticalLayout_52.addWidget(self.label_38)


        self.horizontalLayout_13.addLayout(self.verticalLayout_52)


        self.verticalLayout_50.addLayout(self.horizontalLayout_13)


        self.verticalLayout_49.addLayout(self.verticalLayout_50)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_49.addItem(self.verticalSpacer_5)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_39 = QLabel(self.remove_instructor)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_39, 0, Qt.AlignLeft)

        self.ID_instructor_remove = QLineEdit(self.remove_instructor)
        self.ID_instructor_remove.setObjectName(u"ID_instructor_remove")
        self.ID_instructor_remove.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_53.addWidget(self.ID_instructor_remove, 0, Qt.AlignVCenter)

        self.verticalSpacer_18 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_53.addItem(self.verticalSpacer_18)


        self.verticalLayout_49.addLayout(self.verticalLayout_53)

        self.del_instructor_inlist_3 = QPushButton(self.remove_instructor)
        self.del_instructor_inlist_3.setObjectName(u"del_instructor_inlist_3")
        self.del_instructor_inlist_3.setMinimumSize(QSize(100, 40))

        self.verticalLayout_49.addWidget(self.del_instructor_inlist_3, 0, Qt.AlignRight)

        self.verticalSpacer_3 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_49.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addLayout(self.verticalLayout_49, 2, 0, 1, 1)

        self.label_28 = QLabel(self.remove_instructor)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_3.addWidget(self.label_28, 0, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.tabWidget_instructor.addTab(self.remove_instructor, "")

        self.gridLayout_2.addWidget(self.tabWidget_instructor, 0, 0, 1, 1)


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
        self.search_instructor_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        ___qtablewidgetitem = self.list_registered_instructor.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem1 = self.list_registered_instructor.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID No.", None));
        ___qtablewidgetitem2 = self.list_registered_instructor.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem3 = self.list_registered_instructor.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"1.", None));

        __sortingEnabled = self.list_registered_instructor.isSortingEnabled()
        self.list_registered_instructor.setSortingEnabled(False)
        self.list_registered_instructor.setSortingEnabled(__sortingEnabled)

        self.label_20.setText(QCoreApplication.translate("Form", u"Register Instructor", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"ID Number:", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.pass_generate_instructor.setText(QCoreApplication.translate("Form", u"Generate Password", None))
        self.save_instructor_btn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.tabWidget_instructor.setTabText(self.tabWidget_instructor.indexOf(self.register_instructor), QCoreApplication.translate("Form", u"Register", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"ID Number:", None))
        self.del_instructor_inlist_3.setText(QCoreApplication.translate("Form", u"Remove ", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Remove Instructor", None))
        self.tabWidget_instructor.setTabText(self.tabWidget_instructor.indexOf(self.remove_instructor), QCoreApplication.translate("Form", u"Remove", None))
    # retranslateUi

