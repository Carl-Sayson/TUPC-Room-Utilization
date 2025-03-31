# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_registration.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDialog, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(890, 735)
        Dialog.setMaximumSize(QSize(1248, 735))
        self.gridLayout_4 = QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.edit_tab = QTabWidget(Dialog)
        self.edit_tab.setObjectName(u"edit_tab")
        font = QFont()
        font.setPointSize(10)
        self.edit_tab.setFont(font)
        self.edit_section = QWidget()
        self.edit_section.setObjectName(u"edit_section")
        self.gridLayout_8 = QGridLayout(self.edit_section)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.section_menu = QStackedWidget(self.edit_section)
        self.section_menu.setObjectName(u"section_menu")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_13 = QGridLayout(self.page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalSpacer_8 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.label_33 = QLabel(self.page)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 109))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_33.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_12)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_70 = QLabel(self.page)
        self.label_70.setObjectName(u"label_70")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_70.setFont(font2)

        self.horizontalLayout_15.addWidget(self.label_70)

        self.section = QLineEdit(self.page)
        self.section.setObjectName(u"section")
        self.section.setMaximumSize(QSize(375, 16777215))

        self.horizontalLayout_15.addWidget(self.section)


        self.gridLayout_11.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_68 = QLabel(self.page)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font2)

        self.horizontalLayout_37.addWidget(self.label_68)

        self.course_section = QComboBox(self.page)
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.addItem("")
        self.course_section.setObjectName(u"course_section")

        self.horizontalLayout_37.addWidget(self.course_section)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_37)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_69 = QLabel(self.page)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font2)

        self.horizontalLayout_38.addWidget(self.label_69)

        self.year_level_section = QComboBox(self.page)
        self.year_level_section.addItem("")
        self.year_level_section.addItem("")
        self.year_level_section.addItem("")
        self.year_level_section.addItem("")
        self.year_level_section.setObjectName(u"year_level_section")

        self.horizontalLayout_38.addWidget(self.year_level_section)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_38)


        self.gridLayout_11.addLayout(self.horizontalLayout_36, 0, 0, 1, 1)

        self.add_section = QPushButton(self.page)
        self.add_section.setObjectName(u"add_section")
        self.add_section.setMinimumSize(QSize(100, 40))

        self.gridLayout_11.addWidget(self.add_section, 4, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_9, 5, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_11, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_11)


        self.gridLayout_13.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.remove_section = QPushButton(self.page)
        self.remove_section.setObjectName(u"remove_section")
        self.remove_section.setMinimumSize(QSize(35, 35))
        font3 = QFont()
        font3.setPointSize(8)
        self.remove_section.setFont(font3)

        self.horizontalLayout_3.addWidget(self.remove_section)

        self.view_section = QPushButton(self.page)
        self.view_section.setObjectName(u"view_section")
        self.view_section.setMinimumSize(QSize(35, 35))
        self.view_section.setFont(font3)

        self.horizontalLayout_3.addWidget(self.view_section)


        self.gridLayout_12.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_14 = QLabel(self.page)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_2.addWidget(self.label_14)

        self.sort_sections = QComboBox(self.page)
        self.sort_sections.addItem("")
        self.sort_sections.addItem("")
        self.sort_sections.setObjectName(u"sort_sections")

        self.horizontalLayout_2.addWidget(self.sort_sections)

        self.search_bar_sections = QLineEdit(self.page)
        self.search_bar_sections.setObjectName(u"search_bar_sections")
        self.search_bar_sections.setMinimumSize(QSize(10, 5))

        self.horizontalLayout_2.addWidget(self.search_bar_sections)

        self.search_sections_btn = QPushButton(self.page)
        self.search_sections_btn.setObjectName(u"search_sections_btn")

        self.horizontalLayout_2.addWidget(self.search_sections_btn)


        self.gridLayout_12.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.list_sections = QListWidget(self.page)
        __qlistwidgetitem = QListWidgetItem(self.list_sections)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        self.list_sections.setObjectName(u"list_sections")

        self.gridLayout_12.addWidget(self.list_sections, 1, 0, 1, 2)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 1, 1, 1)

        self.section_menu.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_17 = QGridLayout(self.page_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_17)

        self.label_40 = QLabel(self.page_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 109))
        self.label_40.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_40, 0, Qt.AlignHCenter)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_37 = QLabel(self.page_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)

        self.verticalLayout_39.addWidget(self.label_37, 0, Qt.AlignLeft)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.first_name_addsection = QLineEdit(self.page_2)
        self.first_name_addsection.setObjectName(u"first_name_addsection")

        self.verticalLayout_40.addWidget(self.first_name_addsection)

        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(9)
        self.label.setFont(font4)

        self.verticalLayout_40.addWidget(self.label)


        self.horizontalLayout_20.addLayout(self.verticalLayout_40)

        self.horizontalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.last_name_addsection = QLineEdit(self.page_2)
        self.last_name_addsection.setObjectName(u"last_name_addsection")

        self.verticalLayout_41.addWidget(self.last_name_addsection)

        self.label_38 = QLabel(self.page_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font4)

        self.verticalLayout_41.addWidget(self.label_38)


        self.horizontalLayout_20.addLayout(self.verticalLayout_41)


        self.verticalLayout_39.addLayout(self.horizontalLayout_20)


        self.verticalLayout_38.addLayout(self.verticalLayout_39)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_15)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_39 = QLabel(self.page_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_39, 0, Qt.AlignLeft)

        self.tupc_id_addsection = QLineEdit(self.page_2)
        self.tupc_id_addsection.setObjectName(u"tupc_id_addsection")
        self.tupc_id_addsection.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_42.addWidget(self.tupc_id_addsection, 0, Qt.AlignVCenter)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_42.addItem(self.verticalSpacer_16)


        self.verticalLayout_38.addLayout(self.verticalLayout_42)

        self.add_in_section_btn = QPushButton(self.page_2)
        self.add_in_section_btn.setObjectName(u"add_in_section_btn")
        self.add_in_section_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout_38.addWidget(self.add_in_section_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_18)


        self.verticalLayout_5.addLayout(self.verticalLayout_38)


        self.gridLayout_17.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.remove_stdnt_section = QPushButton(self.page_2)
        self.remove_stdnt_section.setObjectName(u"remove_stdnt_section")
        self.remove_stdnt_section.setMinimumSize(QSize(35, 35))
        self.remove_stdnt_section.setFont(font3)

        self.horizontalLayout_5.addWidget(self.remove_stdnt_section)

        self.clear_section = QPushButton(self.page_2)
        self.clear_section.setObjectName(u"clear_section")
        self.clear_section.setMinimumSize(QSize(35, 35))
        self.clear_section.setFont(font3)

        self.horizontalLayout_5.addWidget(self.clear_section)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.sort_student_section = QComboBox(self.page_2)
        self.sort_student_section.addItem("")
        self.sort_student_section.addItem("")
        self.sort_student_section.addItem("")
        self.sort_student_section.setObjectName(u"sort_student_section")

        self.horizontalLayout_4.addWidget(self.sort_student_section)

        self.search_bar_stdnt_section = QLineEdit(self.page_2)
        self.search_bar_stdnt_section.setObjectName(u"search_bar_stdnt_section")
        self.search_bar_stdnt_section.setMinimumSize(QSize(10, 5))

        self.horizontalLayout_4.addWidget(self.search_bar_stdnt_section)

        self.search_student_btn_section = QPushButton(self.page_2)
        self.search_student_btn_section.setObjectName(u"search_student_btn_section")

        self.horizontalLayout_4.addWidget(self.search_student_btn_section)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.list_stdnt_in_section = QTableWidget(self.page_2)
        if (self.list_stdnt_in_section.columnCount() < 3):
            self.list_stdnt_in_section.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.list_stdnt_in_section.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list_stdnt_in_section.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list_stdnt_in_section.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.list_stdnt_in_section.rowCount() < 1):
            self.list_stdnt_in_section.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.list_stdnt_in_section.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.list_stdnt_in_section.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.list_stdnt_in_section.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.list_stdnt_in_section.setItem(0, 2, __qtablewidgetitem6)
        self.list_stdnt_in_section.setObjectName(u"list_stdnt_in_section")
        self.list_stdnt_in_section.setMinimumSize(QSize(0, 0))
        self.list_stdnt_in_section.setFont(font)
        self.list_stdnt_in_section.setFrameShape(QFrame.StyledPanel)
        self.list_stdnt_in_section.setFrameShadow(QFrame.Plain)
        self.list_stdnt_in_section.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.list_stdnt_in_section.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.list_stdnt_in_section.setShowGrid(True)
        self.list_stdnt_in_section.setGridStyle(Qt.SolidLine)
        self.list_stdnt_in_section.horizontalHeader().setDefaultSectionSize(130)

        self.verticalLayout_6.addWidget(self.list_stdnt_in_section)


        self.gridLayout_17.addLayout(self.verticalLayout_6, 0, 1, 1, 1)

        self.section_menu.addWidget(self.page_2)

        self.gridLayout_8.addWidget(self.section_menu, 0, 0, 1, 1)

        self.edit_tab.addTab(self.edit_section, "")
        self.edit_student = QWidget()
        self.edit_student.setObjectName(u"edit_student")
        self.gridLayout = QGridLayout(self.edit_student)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_12 = QLabel(self.edit_student)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout.addWidget(self.label_12)

        self.sort_student = QComboBox(self.edit_student)
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.setObjectName(u"sort_student")

        self.horizontalLayout.addWidget(self.sort_student)

        self.search_bar_stdnt = QLineEdit(self.edit_student)
        self.search_bar_stdnt.setObjectName(u"search_bar_stdnt")
        self.search_bar_stdnt.setMinimumSize(QSize(10, 5))

        self.horizontalLayout.addWidget(self.search_bar_stdnt)

        self.search_student_btn = QPushButton(self.edit_student)
        self.search_student_btn.setObjectName(u"search_student_btn")

        self.horizontalLayout.addWidget(self.search_student_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.list_registered_stdnt = QTableWidget(self.edit_student)
        if (self.list_registered_stdnt.columnCount() < 6):
            self.list_registered_stdnt.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        if (self.list_registered_stdnt.rowCount() < 1):
            self.list_registered_stdnt.setRowCount(1)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.list_registered_stdnt.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 2, __qtablewidgetitem16)
        self.list_registered_stdnt.setObjectName(u"list_registered_stdnt")
        self.list_registered_stdnt.setMinimumSize(QSize(431, 615))
        self.list_registered_stdnt.setFont(font)
        self.list_registered_stdnt.setFrameShape(QFrame.StyledPanel)
        self.list_registered_stdnt.setFrameShadow(QFrame.Plain)
        self.list_registered_stdnt.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.list_registered_stdnt.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.list_registered_stdnt.setShowGrid(True)
        self.list_registered_stdnt.setGridStyle(Qt.SolidLine)
        self.list_registered_stdnt.horizontalHeader().setDefaultSectionSize(130)

        self.verticalLayout.addWidget(self.list_registered_stdnt)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.tabWidget_student = QTabWidget(self.edit_student)
        self.tabWidget_student.setObjectName(u"tabWidget_student")
        self.tabWidget_student.setMinimumSize(QSize(400, 500))
        self.tabWidget_student.setMaximumSize(QSize(600, 16777215))
        self.tabWidget_student.setFont(font4)
        self.register_stdnt = QWidget()
        self.register_stdnt.setObjectName(u"register_stdnt")
        self.verticalLayout_8 = QVBoxLayout(self.register_stdnt)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_22 = QLabel(self.register_stdnt)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 109))
        self.label_22.setFont(font1)

        self.gridLayout_9.addWidget(self.label_22, 0, 0, 1, 1, Qt.AlignHCenter)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_23 = QLabel(self.register_stdnt)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.verticalLayout_26.addWidget(self.label_23)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.first_name_lineedit = QLineEdit(self.register_stdnt)
        self.first_name_lineedit.setObjectName(u"first_name_lineedit")
        self.first_name_lineedit.setMinimumSize(QSize(150, 0))
        self.first_name_lineedit.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_27.addWidget(self.first_name_lineedit)

        self.label_32 = QLabel(self.register_stdnt)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font4)

        self.verticalLayout_27.addWidget(self.label_32)


        self.horizontalLayout_12.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.last_name_lineedit = QLineEdit(self.register_stdnt)
        self.last_name_lineedit.setObjectName(u"last_name_lineedit")
        self.last_name_lineedit.setMinimumSize(QSize(150, 0))
        self.last_name_lineedit.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_28.addWidget(self.last_name_lineedit)

        self.label_24 = QLabel(self.register_stdnt)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)

        self.verticalLayout_28.addWidget(self.label_24)


        self.horizontalLayout_12.addLayout(self.verticalLayout_28)


        self.verticalLayout_26.addLayout(self.horizontalLayout_12)


        self.gridLayout_9.addLayout(self.verticalLayout_26, 1, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_25 = QLabel(self.register_stdnt)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.verticalLayout_29.addWidget(self.label_25, 0, Qt.AlignLeft)

        self.email_stdnt_lineedit = QLineEdit(self.register_stdnt)
        self.email_stdnt_lineedit.setObjectName(u"email_stdnt_lineedit")
        self.email_stdnt_lineedit.setMinimumSize(QSize(150, 0))
        self.email_stdnt_lineedit.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_29.addWidget(self.email_stdnt_lineedit, 0, Qt.AlignVCenter)


        self.horizontalLayout_13.addLayout(self.verticalLayout_29)

        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_26 = QLabel(self.register_stdnt)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.verticalLayout_30.addWidget(self.label_26, 0, Qt.AlignLeft)

        self.tupc_id_lineedit = QLineEdit(self.register_stdnt)
        self.tupc_id_lineedit.setObjectName(u"tupc_id_lineedit")
        self.tupc_id_lineedit.setMinimumSize(QSize(150, 0))
        self.tupc_id_lineedit.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_30.addWidget(self.tupc_id_lineedit, 0, Qt.AlignVCenter)


        self.horizontalLayout_13.addLayout(self.verticalLayout_30)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_27 = QLabel(self.register_stdnt)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.verticalLayout_32.addWidget(self.label_27)

        self.password_stdnt_reg = QLineEdit(self.register_stdnt)
        self.password_stdnt_reg.setObjectName(u"password_stdnt_reg")
        self.password_stdnt_reg.setMinimumSize(QSize(300, 0))
        self.password_stdnt_reg.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_32.addWidget(self.password_stdnt_reg)

        self.verticalSpacer_3 = QSpacerItem(5, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_32.addItem(self.verticalSpacer_3)

        self.pass_generate_stdnt = QPushButton(self.register_stdnt)
        self.pass_generate_stdnt.setObjectName(u"pass_generate_stdnt")
        self.pass_generate_stdnt.setMinimumSize(QSize(100, 40))

        self.verticalLayout_32.addWidget(self.pass_generate_stdnt, 0, Qt.AlignLeft)


        self.verticalLayout_8.addLayout(self.verticalLayout_32)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_31 = QLabel(self.register_stdnt)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_31)

        self.list_sections_register = QListWidget(self.register_stdnt)
        __qlistwidgetitem1 = QListWidgetItem(self.list_sections_register)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.list_sections_register.setObjectName(u"list_sections_register")

        self.verticalLayout_7.addWidget(self.list_sections_register)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.save_send_stdnt_cred = QPushButton(self.register_stdnt)
        self.save_send_stdnt_cred.setObjectName(u"save_send_stdnt_cred")
        self.save_send_stdnt_cred.setMinimumSize(QSize(100, 40))

        self.verticalLayout_8.addWidget(self.save_send_stdnt_cred, 0, Qt.AlignHCenter)

        self.tabWidget_student.addTab(self.register_stdnt, "")
        self.remove_stdnt = QWidget()
        self.remove_stdnt.setObjectName(u"remove_stdnt")
        self.gridLayout_2 = QGridLayout(self.remove_stdnt)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_13 = QLabel(self.remove_stdnt)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_28 = QLabel(self.remove_stdnt)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.verticalLayout_33.addWidget(self.label_28, 0, Qt.AlignLeft)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.first_name_lineedit_remove = QLineEdit(self.remove_stdnt)
        self.first_name_lineedit_remove.setObjectName(u"first_name_lineedit_remove")

        self.verticalLayout_34.addWidget(self.first_name_lineedit_remove)

        self.lable = QLabel(self.remove_stdnt)
        self.lable.setObjectName(u"lable")
        self.lable.setFont(font4)

        self.verticalLayout_34.addWidget(self.lable)


        self.horizontalLayout_8.addLayout(self.verticalLayout_34)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.last_name_lineedit_remove = QLineEdit(self.remove_stdnt)
        self.last_name_lineedit_remove.setObjectName(u"last_name_lineedit_remove")

        self.verticalLayout_35.addWidget(self.last_name_lineedit_remove)

        self.label_29 = QLabel(self.remove_stdnt)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font4)

        self.verticalLayout_35.addWidget(self.label_29)


        self.horizontalLayout_8.addLayout(self.verticalLayout_35)


        self.verticalLayout_33.addLayout(self.horizontalLayout_8)


        self.verticalLayout_31.addLayout(self.verticalLayout_33)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_31.addItem(self.verticalSpacer_6)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_30 = QLabel(self.remove_stdnt)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.verticalLayout_36.addWidget(self.label_30, 0, Qt.AlignLeft)

        self.tupc_id_remove_lineedit = QLineEdit(self.remove_stdnt)
        self.tupc_id_remove_lineedit.setObjectName(u"tupc_id_remove_lineedit")
        self.tupc_id_remove_lineedit.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_36.addWidget(self.tupc_id_remove_lineedit, 0, Qt.AlignVCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_36.addItem(self.verticalSpacer_10)


        self.verticalLayout_31.addLayout(self.verticalLayout_36)

        self.del_student_inlist = QPushButton(self.remove_stdnt)
        self.del_student_inlist.setObjectName(u"del_student_inlist")
        self.del_student_inlist.setMinimumSize(QSize(100, 40))

        self.verticalLayout_31.addWidget(self.del_student_inlist, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_31)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_16 = QLabel(self.remove_stdnt)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.remove_stdnt)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_35 = QLabel(self.remove_stdnt)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_35)

        self.list_sections_register_3 = QListWidget(self.remove_stdnt)
        __qlistwidgetitem2 = QListWidgetItem(self.list_sections_register_3)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.list_sections_register_3.setObjectName(u"list_sections_register_3")

        self.verticalLayout_10.addWidget(self.list_sections_register_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_10)

        self.remove_stdnts_in_section_from_system = QPushButton(self.remove_stdnt)
        self.remove_stdnts_in_section_from_system.setObjectName(u"remove_stdnts_in_section_from_system")
        self.remove_stdnts_in_section_from_system.setMinimumSize(QSize(100, 40))

        self.verticalLayout_4.addWidget(self.remove_stdnts_in_section_from_system, 0, Qt.AlignHCenter)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 0, 1, 1)

        self.tabWidget_student.addTab(self.remove_stdnt, "")

        self.gridLayout.addWidget(self.tabWidget_student, 0, 0, 1, 1)

        self.edit_tab.addTab(self.edit_student, "")

        self.gridLayout_4.addWidget(self.edit_tab, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_70.setBuddy(self.section)
        self.label_32.setBuddy(self.first_name_lineedit)
        self.label_24.setBuddy(self.last_name_lineedit)
        self.label_25.setBuddy(self.email_stdnt_lineedit)
        self.label_26.setBuddy(self.tupc_id_lineedit)
        self.label_27.setBuddy(self.password_stdnt_reg)
        self.label_31.setBuddy(self.password_stdnt_reg)
        self.label_35.setBuddy(self.password_stdnt_reg)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)

        self.edit_tab.setCurrentIndex(0)
        self.section_menu.setCurrentIndex(0)
        self.tabWidget_student.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"Add Section", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Note: Add section first before registering ", None))
        self.label_70.setText(QCoreApplication.translate("Dialog", u"Section:", None))
        self.label_68.setText(QCoreApplication.translate("Dialog", u"Course:", None))
        self.course_section.setItemText(0, QCoreApplication.translate("Dialog", u"BET-ET", None))
        self.course_section.setItemText(1, QCoreApplication.translate("Dialog", u"BET-MT", None))
        self.course_section.setItemText(2, QCoreApplication.translate("Dialog", u"BET-COET", None))
        self.course_section.setItemText(3, QCoreApplication.translate("Dialog", u"BET-PPT", None))
        self.course_section.setItemText(4, QCoreApplication.translate("Dialog", u"BET-EST", None))
        self.course_section.setItemText(5, QCoreApplication.translate("Dialog", u"BET-CT", None))
        self.course_section.setItemText(6, QCoreApplication.translate("Dialog", u"BET-AT", None))
        self.course_section.setItemText(7, QCoreApplication.translate("Dialog", u"BTVTED-CP", None))
        self.course_section.setItemText(8, QCoreApplication.translate("Dialog", u"BTVTED-EL", None))
        self.course_section.setItemText(9, QCoreApplication.translate("Dialog", u"BTLED-HE", None))
        self.course_section.setItemText(10, QCoreApplication.translate("Dialog", u"BTLED-ICT", None))
        self.course_section.setItemText(11, QCoreApplication.translate("Dialog", u"BTLED-IA", None))
        self.course_section.setItemText(12, QCoreApplication.translate("Dialog", u"BSCE", None))
        self.course_section.setItemText(13, QCoreApplication.translate("Dialog", u"BSEE", None))
        self.course_section.setItemText(14, QCoreApplication.translate("Dialog", u"BSME", None))

        self.label_69.setText(QCoreApplication.translate("Dialog", u"Year:", None))
        self.year_level_section.setItemText(0, QCoreApplication.translate("Dialog", u"1st ", None))
        self.year_level_section.setItemText(1, QCoreApplication.translate("Dialog", u"2nd", None))
        self.year_level_section.setItemText(2, QCoreApplication.translate("Dialog", u"3rd", None))
        self.year_level_section.setItemText(3, QCoreApplication.translate("Dialog", u"4th", None))

        self.add_section.setText(QCoreApplication.translate("Dialog", u"Add Section", None))
        self.remove_section.setText(QCoreApplication.translate("Dialog", u"Remove", None))
        self.view_section.setText(QCoreApplication.translate("Dialog", u"Manage", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Sort by:", None))
        self.sort_sections.setItemText(0, QCoreApplication.translate("Dialog", u"Course", None))
        self.sort_sections.setItemText(1, QCoreApplication.translate("Dialog", u"Year", None))

        self.sort_sections.setCurrentText(QCoreApplication.translate("Dialog", u"Course", None))
        self.search_sections_btn.setText(QCoreApplication.translate("Dialog", u"Search", None))

        __sortingEnabled = self.list_sections.isSortingEnabled()
        self.list_sections.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_sections.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"COET-2A", None));
        self.list_sections.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.label_40.setText(QCoreApplication.translate("Dialog", u"Add Student ", None))
        self.label_37.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.label_38.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_39.setText(QCoreApplication.translate("Dialog", u"TUPC-ID:", None))
        self.add_in_section_btn.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.remove_stdnt_section.setText(QCoreApplication.translate("Dialog", u"Remove", None))
        self.clear_section.setText(QCoreApplication.translate("Dialog", u"Clear", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Sort by:", None))
        self.sort_student_section.setItemText(0, QCoreApplication.translate("Dialog", u"Name", None))
        self.sort_student_section.setItemText(1, QCoreApplication.translate("Dialog", u"Email", None))
        self.sort_student_section.setItemText(2, QCoreApplication.translate("Dialog", u"ID", None))

        self.sort_student_section.setCurrentText(QCoreApplication.translate("Dialog", u"Name", None))
        self.search_student_btn_section.setText(QCoreApplication.translate("Dialog", u"Search", None))
        ___qtablewidgetitem = self.list_stdnt_in_section.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Student Name", None));
        ___qtablewidgetitem1 = self.list_stdnt_in_section.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Student ID", None));
        ___qtablewidgetitem2 = self.list_stdnt_in_section.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Email", None));
        ___qtablewidgetitem3 = self.list_stdnt_in_section.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"1.", None));

        __sortingEnabled1 = self.list_stdnt_in_section.isSortingEnabled()
        self.list_stdnt_in_section.setSortingEnabled(False)
        self.list_stdnt_in_section.setSortingEnabled(__sortingEnabled1)

        self.edit_tab.setTabText(self.edit_tab.indexOf(self.edit_section), QCoreApplication.translate("Dialog", u"Edit Sections", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Sort by:", None))
        self.sort_student.setItemText(0, QCoreApplication.translate("Dialog", u"Name", None))
        self.sort_student.setItemText(1, QCoreApplication.translate("Dialog", u"Email", None))
        self.sort_student.setItemText(2, QCoreApplication.translate("Dialog", u"ID", None))
        self.sort_student.setItemText(3, QCoreApplication.translate("Dialog", u"Course", None))
        self.sort_student.setItemText(4, QCoreApplication.translate("Dialog", u"Year", None))
        self.sort_student.setItemText(5, QCoreApplication.translate("Dialog", u"Section", None))

        self.sort_student.setCurrentText(QCoreApplication.translate("Dialog", u"Name", None))
        self.search_student_btn.setText(QCoreApplication.translate("Dialog", u"Search", None))
        ___qtablewidgetitem4 = self.list_registered_stdnt.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Student Name", None));
        ___qtablewidgetitem5 = self.list_registered_stdnt.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Student ID", None));
        ___qtablewidgetitem6 = self.list_registered_stdnt.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Email", None));
        ___qtablewidgetitem7 = self.list_registered_stdnt.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Course", None));
        ___qtablewidgetitem8 = self.list_registered_stdnt.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Year", None));
        ___qtablewidgetitem9 = self.list_registered_stdnt.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Section", None));
        ___qtablewidgetitem10 = self.list_registered_stdnt.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"1.", None));

        __sortingEnabled2 = self.list_registered_stdnt.isSortingEnabled()
        self.list_registered_stdnt.setSortingEnabled(False)
        self.list_registered_stdnt.setSortingEnabled(__sortingEnabled2)

        self.label_22.setText(QCoreApplication.translate("Dialog", u"Register Student ", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"TUPC-ID:", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.pass_generate_stdnt.setText(QCoreApplication.translate("Dialog", u"Generate Password", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"Select Section:", None))

        __sortingEnabled3 = self.list_sections_register.isSortingEnabled()
        self.list_sections_register.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.list_sections_register.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"COET-2A", None));
        self.list_sections_register.setSortingEnabled(__sortingEnabled3)

        self.save_send_stdnt_cred.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.tabWidget_student.setTabText(self.tabWidget_student.indexOf(self.register_stdnt), QCoreApplication.translate("Dialog", u"Register", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Remove Student ", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.lable.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"TUPC-ID:", None))
        self.del_student_inlist.setText(QCoreApplication.translate("Dialog", u"Remove ", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Remove Section of Students", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Note: Will only remove students of selected section from system", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"Select Section:", None))

        __sortingEnabled4 = self.list_sections_register_3.isSortingEnabled()
        self.list_sections_register_3.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.list_sections_register_3.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"COET-2A", None));
        self.list_sections_register_3.setSortingEnabled(__sortingEnabled4)

        self.remove_stdnts_in_section_from_system.setText(QCoreApplication.translate("Dialog", u"Remove", None))
        self.tabWidget_student.setTabText(self.tabWidget_student.indexOf(self.remove_stdnt), QCoreApplication.translate("Dialog", u"Remove", None))
        self.edit_tab.setTabText(self.edit_tab.indexOf(self.edit_student), QCoreApplication.translate("Dialog", u"Edit Student", None))
    # retranslateUi

