# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_students.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(786, 602)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(764, 580))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        font = QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)

        self.verticalLayout_20.addWidget(self.label_17, 0, Qt.AlignLeft)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.first_name_lineedit_editsched = QLineEdit(self.frame)
        self.first_name_lineedit_editsched.setObjectName(u"first_name_lineedit_editsched")

        self.verticalLayout_21.addWidget(self.first_name_lineedit_editsched)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)

        self.verticalLayout_21.addWidget(self.label)


        self.horizontalLayout_8.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.last_name_lineedit_editsched = QLineEdit(self.frame)
        self.last_name_lineedit_editsched.setObjectName(u"last_name_lineedit_editsched")

        self.verticalLayout_22.addWidget(self.last_name_lineedit_editsched)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_22.addWidget(self.label_18)


        self.horizontalLayout_8.addLayout(self.verticalLayout_22)


        self.verticalLayout_20.addLayout(self.horizontalLayout_8)


        self.verticalLayout_24.addLayout(self.verticalLayout_20)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.verticalLayout_23.addWidget(self.label_19, 0, Qt.AlignLeft)

        self.tupc_id_editsched_lineedit = QLineEdit(self.frame)
        self.tupc_id_editsched_lineedit.setObjectName(u"tupc_id_editsched_lineedit")

        self.verticalLayout_23.addWidget(self.tupc_id_editsched_lineedit, 0, Qt.AlignVCenter)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)


        self.verticalLayout_9.addLayout(self.verticalLayout_24)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_student_schedule = QPushButton(self.frame)
        self.add_student_schedule.setObjectName(u"add_student_schedule")
        self.add_student_schedule.setMinimumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.add_student_schedule, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.del_student_schedule = QPushButton(self.frame)
        self.del_student_schedule.setObjectName(u"del_student_schedule")
        self.del_student_schedule.setMinimumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.del_student_schedule, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_9.addLayout(self.horizontalLayout)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sort_student_section = QComboBox(self.frame)
        self.sort_student_section.addItem("")
        self.sort_student_section.addItem("")
        self.sort_student_section.setObjectName(u"sort_student_section")

        self.horizontalLayout_12.addWidget(self.sort_student_section)

        self.search_bar_stdnt_insched = QLineEdit(self.frame)
        self.search_bar_stdnt_insched.setObjectName(u"search_bar_stdnt_insched")

        self.horizontalLayout_12.addWidget(self.search_bar_stdnt_insched)

        self.search_stdnt_insched_btn = QPushButton(self.frame)
        self.search_stdnt_insched_btn.setObjectName(u"search_stdnt_insched_btn")

        self.horizontalLayout_12.addWidget(self.search_stdnt_insched_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.list_students_schedule = QListWidget(self.frame)
        self.list_students_schedule.setObjectName(u"list_students_schedule")
        self.list_students_schedule.setMinimumSize(QSize(360, 233))

        self.verticalLayout.addWidget(self.list_students_schedule)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 2, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_34 = QLabel(self.frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 109))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_34.setFont(font2)

        self.gridLayout_2.addWidget(self.label_34, 0, 0, 1, 2, Qt.AlignHCenter)

        self.list_sections_schedule = QListWidget(self.frame)
        self.list_sections_schedule.setObjectName(u"list_sections_schedule")

        self.gridLayout_2.addWidget(self.list_sections_schedule, 1, 0, 1, 2)

        self.add_section_btn = QPushButton(self.frame)
        self.add_section_btn.setObjectName(u"add_section_btn")
        self.add_section_btn.setMinimumSize(QSize(100, 40))

        self.gridLayout_2.addWidget(self.add_section_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.remove_section = QPushButton(self.frame)
        self.remove_section.setObjectName(u"remove_section")
        self.remove_section.setMinimumSize(QSize(100, 40))

        self.gridLayout_2.addWidget(self.remove_section, 2, 1, 1, 1, Qt.AlignRight)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dialog", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"TUPC-ID:", None))
        self.add_student_schedule.setText(QCoreApplication.translate("Form", u"Add Student", None))
        self.del_student_schedule.setText(QCoreApplication.translate("Form", u"Remove Student", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Edit Students:", None))
        self.sort_student_section.setItemText(0, QCoreApplication.translate("Form", u"A-Z", None))
        self.sort_student_section.setItemText(1, QCoreApplication.translate("Form", u"Z-A", None))

        self.sort_student_section.setCurrentText(QCoreApplication.translate("Form", u"A-Z", None))
        self.search_stdnt_insched_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Add / Remove Section", None))
        self.add_section_btn.setText(QCoreApplication.translate("Form", u"Add Section", None))
        self.remove_section.setText(QCoreApplication.translate("Form", u"Remove Section", None))
    # retranslateUi

