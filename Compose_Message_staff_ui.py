# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Compose_Message_staff.ui'
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
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(942, 697)
        Form.setMaximumSize(QSize(942, 697))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(551, 479))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.send_btn_composed_msg = QPushButton(self.frame)
        self.send_btn_composed_msg.setObjectName(u"send_btn_composed_msg")

        self.gridLayout_2.addWidget(self.send_btn_composed_msg, 3, 2, 1, 1, Qt.AlignRight)

        self.label_47 = QLabel(self.frame)
        self.label_47.setObjectName(u"label_47")
        font = QFont()
        font.setPointSize(14)
        self.label_47.setFont(font)

        self.gridLayout_2.addWidget(self.label_47, 0, 0, 2, 2, Qt.AlignLeft)

        self.type_report = QComboBox(self.frame)
        self.type_report.addItem("")
        self.type_report.addItem("")
        self.type_report.setObjectName(u"type_report")

        self.gridLayout_2.addWidget(self.type_report, 1, 2, 1, 1)

        self.message_report = QPlainTextEdit(self.frame)
        self.message_report.setObjectName(u"message_report")
        self.message_report.setFrameShape(QFrame.Box)
        self.message_report.setFrameShadow(QFrame.Plain)
        self.message_report.setOverwriteMode(False)

        self.gridLayout_2.addWidget(self.message_report, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dialog", None))
        self.send_btn_composed_msg.setText(QCoreApplication.translate("Form", u"Send", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Staff Report:", None))
        self.type_report.setItemText(0, QCoreApplication.translate("Form", u"Damage Report", None))
        self.type_report.setItemText(1, QCoreApplication.translate("Form", u"Maintenance Report", None))

        self.message_report.setPlainText(QCoreApplication.translate("Form", u"Example message to send\n"
"\n"
"", None))
    # retranslateUi

