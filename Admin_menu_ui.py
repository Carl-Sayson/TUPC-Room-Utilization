# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 709)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionRoom = QAction(MainWindow)
        self.actionRoom.setObjectName(u"actionRoom")
        self.actionInstructor = QAction(MainWindow)
        self.actionInstructor.setObjectName(u"actionInstructor")
        self.actionStaff = QAction(MainWindow)
        self.actionStaff.setObjectName(u"actionStaff")
        self.actionStudent = QAction(MainWindow)
        self.actionStudent.setObjectName(u"actionStudent")
        self.actionInbox = QAction(MainWindow)
        self.actionInbox.setObjectName(u"actionInbox")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_14 = QGridLayout(self.centralwidget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.menu_admin_widget = QWidget(self.centralwidget)
        self.menu_admin_widget.setObjectName(u"menu_admin_widget")
        self.menu_admin_widget.setMinimumSize(QSize(801, 637))
        self.gridLayout_13 = QGridLayout(self.menu_admin_widget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.tabWidget = QTabWidget(self.menu_admin_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.gridLayout_2 = QGridLayout(self.tabWidgetPage1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.schedule_stackedwidget = QTabWidget(self.tabWidgetPage1)
        self.schedule_stackedwidget.setObjectName(u"schedule_stackedwidget")
        self.schedule_stackedwidget.setMinimumSize(QSize(579, 589))
        self.schedule_stackedwidget.tabBar().setVisible(False)
        self.schedule_stackedwidgetPage1 = QWidget()
        self.schedule_stackedwidgetPage1.setObjectName(u"schedule_stackedwidgetPage1")
        self.gridLayout_3 = QGridLayout(self.schedule_stackedwidgetPage1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.search_bar_room = QLineEdit(self.schedule_stackedwidgetPage1)
        self.search_bar_room.setObjectName(u"search_bar_room")

        self.horizontalLayout_19.addWidget(self.search_bar_room)

        self.search_room_btn = QPushButton(self.schedule_stackedwidgetPage1)
        self.search_room_btn.setObjectName(u"search_room_btn")

        self.horizontalLayout_19.addWidget(self.search_room_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_19, 0, 1, 1, 1)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.schedule_stackedwidgetPage1)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)

        self.verticalLayout_4.addWidget(self.label_3)


        self.verticalLayout_58.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.add_rm = QPushButton(self.schedule_stackedwidgetPage1)
        self.add_rm.setObjectName(u"add_rm")
        self.add_rm.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.add_rm)

        self.del_rm = QPushButton(self.schedule_stackedwidgetPage1)
        self.del_rm.setObjectName(u"del_rm")
        self.del_rm.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.del_rm)

        self.edit_rm = QPushButton(self.schedule_stackedwidgetPage1)
        self.edit_rm.setObjectName(u"edit_rm")
        self.edit_rm.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.edit_rm)

        self.view_sched = QPushButton(self.schedule_stackedwidgetPage1)
        self.view_sched.setObjectName(u"view_sched")
        self.view_sched.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.view_sched)

        self.log_rm = QPushButton(self.schedule_stackedwidgetPage1)
        self.log_rm.setObjectName(u"log_rm")
        self.log_rm.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.log_rm)


        self.verticalLayout_58.addLayout(self.verticalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 394, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addLayout(self.verticalLayout_58, 0, 0, 2, 1)

        self.horizontalSpacer_14 = QSpacerItem(276, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)

        self.room_list = QListWidget(self.schedule_stackedwidgetPage1)
        font1 = QFont()
        font1.setPointSize(12)
        __qlistwidgetitem = QListWidgetItem(self.room_list)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFont(font1);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.room_list.setObjectName(u"room_list")

        self.gridLayout_3.addWidget(self.room_list, 1, 1, 1, 2)

        self.schedule_stackedwidget.addTab(self.schedule_stackedwidgetPage1, "")
        self.schedule_stackedwidgetPage2 = QWidget()
        self.schedule_stackedwidgetPage2.setObjectName(u"schedule_stackedwidgetPage2")
        self.verticalLayout_64 = QVBoxLayout(self.schedule_stackedwidgetPage2)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.back = QPushButton(self.schedule_stackedwidgetPage2)
        self.back.setObjectName(u"back")

        self.horizontalLayout_15.addWidget(self.back)

        self.label_57 = QLabel(self.schedule_stackedwidgetPage2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_57)

        self.accessed_room_sched_lineedit = QLineEdit(self.schedule_stackedwidgetPage2)
        self.accessed_room_sched_lineedit.setObjectName(u"accessed_room_sched_lineedit")
        self.accessed_room_sched_lineedit.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.accessed_room_sched_lineedit)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_27)


        self.verticalLayout_64.addLayout(self.horizontalLayout_15)

        self.room_sched_table = QTableWidget(self.schedule_stackedwidgetPage2)
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

        self.verticalLayout_64.addWidget(self.room_sched_table)

        self.schedule_stackedwidget.addTab(self.schedule_stackedwidgetPage2, "")
        self.schedule_stackedwidgetPage3 = QWidget()
        self.schedule_stackedwidgetPage3.setObjectName(u"schedule_stackedwidgetPage3")
        self.gridLayout_4 = QGridLayout(self.schedule_stackedwidgetPage3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_4)

        self.label_56 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.verticalLayout_60.addWidget(self.label_56)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_19)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.assign_instructor = QLineEdit(self.schedule_stackedwidgetPage3)
        self.assign_instructor.setObjectName(u"assign_instructor")
        self.assign_instructor.setMaximumSize(QSize(600, 16777215))

        self.horizontalLayout_2.addWidget(self.assign_instructor)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout.addWidget(self.label_8)

        self.assign_subject = QLineEdit(self.schedule_stackedwidgetPage3)
        self.assign_subject.setObjectName(u"assign_subject")
        self.assign_subject.setMaximumSize(QSize(600, 16777215))

        self.horizontalLayout.addWidget(self.assign_subject)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_17)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.instructor_day_edit_comboBox = QComboBox(self.schedule_stackedwidgetPage3)
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.addItem("")
        self.instructor_day_edit_comboBox.setObjectName(u"instructor_day_edit_comboBox")

        self.horizontalLayout_3.addWidget(self.instructor_day_edit_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_6)

        self.start_time_instructor = QTimeEdit(self.schedule_stackedwidgetPage3)
        self.start_time_instructor.setObjectName(u"start_time_instructor")

        self.verticalLayout_7.addWidget(self.start_time_instructor)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.label_9 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.final_time_instructor = QTimeEdit(self.schedule_stackedwidgetPage3)
        self.final_time_instructor.setObjectName(u"final_time_instructor")

        self.verticalLayout_6.addWidget(self.final_time_instructor)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.add_student = QPushButton(self.schedule_stackedwidgetPage3)
        self.add_student.setObjectName(u"add_student")
        self.add_student.setMinimumSize(QSize(100, 30))

        self.verticalLayout_8.addWidget(self.add_student, 0, Qt.AlignHCenter)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.remove_instructor_sched = QPushButton(self.schedule_stackedwidgetPage3)
        self.remove_instructor_sched.setObjectName(u"remove_instructor_sched")

        self.horizontalLayout_24.addWidget(self.remove_instructor_sched, 0, Qt.AlignLeft)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_28)

        self.change_instructor_sched = QPushButton(self.schedule_stackedwidgetPage3)
        self.change_instructor_sched.setObjectName(u"change_instructor_sched")

        self.horizontalLayout_24.addWidget(self.change_instructor_sched, 0, Qt.AlignRight)

        self.add_sched_instructor = QPushButton(self.schedule_stackedwidgetPage3)
        self.add_sched_instructor.setObjectName(u"add_sched_instructor")

        self.horizontalLayout_24.addWidget(self.add_sched_instructor, 0, Qt.AlignRight)


        self.verticalLayout_8.addLayout(self.horizontalLayout_24)


        self.verticalLayout_60.addLayout(self.verticalLayout_8)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_6)

        self.line_11 = QFrame(self.schedule_stackedwidgetPage3)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_60.addWidget(self.line_11)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_50 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_50)

        self.assign_staff = QLineEdit(self.schedule_stackedwidgetPage3)
        self.assign_staff.setObjectName(u"assign_staff")
        self.assign_staff.setMaximumSize(QSize(600, 16777215))

        self.horizontalLayout_21.addWidget(self.assign_staff)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_49 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_49)

        self.assign_maintenance = QLineEdit(self.schedule_stackedwidgetPage3)
        self.assign_maintenance.setObjectName(u"assign_maintenance")
        self.assign_maintenance.setMaximumSize(QSize(600, 16777215))

        self.horizontalLayout_20.addWidget(self.assign_maintenance)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_18)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_17)

        self.label_51 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_51)

        self.day_edit_staff = QComboBox(self.schedule_stackedwidgetPage3)
        self.day_edit_staff.addItem("")
        self.day_edit_staff.addItem("")
        self.day_edit_staff.addItem("")
        self.day_edit_staff.addItem("")
        self.day_edit_staff.addItem("")
        self.day_edit_staff.setObjectName(u"day_edit_staff")

        self.horizontalLayout_22.addWidget(self.day_edit_staff)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_18)


        self.verticalLayout_9.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_19)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_52 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_52)

        self.start_time_staff = QTimeEdit(self.schedule_stackedwidgetPage3)
        self.start_time_staff.setObjectName(u"start_time_staff")

        self.verticalLayout_10.addWidget(self.start_time_staff)


        self.horizontalLayout_23.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_20)

        self.label_53 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_53)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_21)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(7)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_54 = QLabel(self.schedule_stackedwidgetPage3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font1)

        self.verticalLayout_59.addWidget(self.label_54)

        self.final_time_staff = QTimeEdit(self.schedule_stackedwidgetPage3)
        self.final_time_staff.setObjectName(u"final_time_staff")

        self.verticalLayout_59.addWidget(self.final_time_staff)


        self.horizontalLayout_23.addLayout(self.verticalLayout_59)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_22)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_5 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.remove_staff_sched = QPushButton(self.schedule_stackedwidgetPage3)
        self.remove_staff_sched.setObjectName(u"remove_staff_sched")

        self.horizontalLayout_25.addWidget(self.remove_staff_sched, 0, Qt.AlignLeft)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_29)

        self.change_staff_sched = QPushButton(self.schedule_stackedwidgetPage3)
        self.change_staff_sched.setObjectName(u"change_staff_sched")

        self.horizontalLayout_25.addWidget(self.change_staff_sched, 0, Qt.AlignRight)

        self.add_sched_staff = QPushButton(self.schedule_stackedwidgetPage3)
        self.add_sched_staff.setObjectName(u"add_sched_staff")

        self.horizontalLayout_25.addWidget(self.add_sched_staff, 0, Qt.AlignRight)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)


        self.verticalLayout_60.addLayout(self.verticalLayout_9)

        self.back_2 = QPushButton(self.schedule_stackedwidgetPage3)
        self.back_2.setObjectName(u"back_2")

        self.verticalLayout_60.addWidget(self.back_2, 0, Qt.AlignLeft)


        self.gridLayout_4.addLayout(self.verticalLayout_60, 0, 0, 1, 1)

        self.line_9 = QFrame(self.schedule_stackedwidgetPage3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_9, 0, 1, 1, 1)

        self.edit_room_sched_table = QTableWidget(self.schedule_stackedwidgetPage3)
        if (self.edit_room_sched_table.columnCount() < 5):
            self.edit_room_sched_table.setColumnCount(5)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.edit_room_sched_table.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.edit_room_sched_table.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.edit_room_sched_table.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.edit_room_sched_table.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.edit_room_sched_table.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        if (self.edit_room_sched_table.rowCount() < 14):
            self.edit_room_sched_table.setRowCount(14)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(7, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(8, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(9, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(10, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(11, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(12, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.edit_room_sched_table.setVerticalHeaderItem(13, __qtablewidgetitem37)
        self.edit_room_sched_table.setObjectName(u"edit_room_sched_table")
        self.edit_room_sched_table.setMinimumSize(QSize(351, 593))
        self.edit_room_sched_table.setMaximumSize(QSize(900, 600))

        self.gridLayout_4.addWidget(self.edit_room_sched_table, 0, 2, 1, 1)

        self.schedule_stackedwidget.addTab(self.schedule_stackedwidgetPage3, "")
        self.schedule_stackedwidgetPage4 = QWidget()
        self.schedule_stackedwidgetPage4.setObjectName(u"schedule_stackedwidgetPage4")
        self.verticalLayout_61 = QVBoxLayout(self.schedule_stackedwidgetPage4)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.back_3 = QPushButton(self.schedule_stackedwidgetPage4)
        self.back_3.setObjectName(u"back_3")

        self.verticalLayout_61.addWidget(self.back_3, 0, Qt.AlignLeft)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_55 = QLabel(self.schedule_stackedwidgetPage4)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_55)

        self.accessed_room_logs_lineedit = QLineEdit(self.schedule_stackedwidgetPage4)
        self.accessed_room_logs_lineedit.setObjectName(u"accessed_room_logs_lineedit")
        self.accessed_room_logs_lineedit.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.accessed_room_logs_lineedit)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_25)


        self.verticalLayout_61.addLayout(self.horizontalLayout_10)

        self.selected_room_log = QTableWidget(self.schedule_stackedwidgetPage4)
        if (self.selected_room_log.columnCount() < 3):
            self.selected_room_log.setColumnCount(3)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.selected_room_log.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.selected_room_log.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.selected_room_log.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        self.selected_room_log.setObjectName(u"selected_room_log")

        self.verticalLayout_61.addWidget(self.selected_room_log)

        self.schedule_stackedwidget.addTab(self.schedule_stackedwidgetPage4, "")

        self.gridLayout_2.addWidget(self.schedule_stackedwidget, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.gridLayout_8 = QGridLayout(self.tabWidgetPage2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_10 = QLabel(self.tabWidgetPage2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_25.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.line_2 = QFrame(self.tabWidgetPage2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_25.addWidget(self.line_2)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.tabWidgetPage2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_13, 0, Qt.AlignLeft)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.first_name_lineedit = QLineEdit(self.tabWidgetPage2)
        self.first_name_lineedit.setObjectName(u"first_name_lineedit")
        self.first_name_lineedit.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_13.addWidget(self.first_name_lineedit)

        self.label_30 = QLabel(self.tabWidgetPage2)
        self.label_30.setObjectName(u"label_30")
        font2 = QFont()
        font2.setPointSize(9)
        self.label_30.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_30)


        self.horizontalLayout_6.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.last_name_lineedit = QLineEdit(self.tabWidgetPage2)
        self.last_name_lineedit.setObjectName(u"last_name_lineedit")
        self.last_name_lineedit.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_12.addWidget(self.last_name_lineedit)

        self.label_12 = QLabel(self.tabWidgetPage2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_12)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)


        self.verticalLayout_19.addLayout(self.verticalLayout_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.tabWidgetPage2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.email_stdnt_lineedit = QLineEdit(self.tabWidgetPage2)
        self.email_stdnt_lineedit.setObjectName(u"email_stdnt_lineedit")
        self.email_stdnt_lineedit.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_15.addWidget(self.email_stdnt_lineedit, 0, Qt.AlignVCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_16 = QLabel(self.tabWidgetPage2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_18.addWidget(self.label_16, 0, Qt.AlignLeft)

        self.tupc_id_lineedit = QLineEdit(self.tabWidgetPage2)
        self.tupc_id_lineedit.setObjectName(u"tupc_id_lineedit")
        self.tupc_id_lineedit.setMaximumSize(QSize(375, 16777215))

        self.verticalLayout_18.addWidget(self.tupc_id_lineedit, 0, Qt.AlignVCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_9)


        self.horizontalLayout_7.addLayout(self.verticalLayout_18)


        self.verticalLayout_19.addLayout(self.horizontalLayout_7)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_15 = QLabel(self.tabWidgetPage2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_15)

        self.password_stdnt_reg = QLineEdit(self.tabWidgetPage2)
        self.password_stdnt_reg.setObjectName(u"password_stdnt_reg")
        self.password_stdnt_reg.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_16.addWidget(self.password_stdnt_reg)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.pass_generate_stdnt = QPushButton(self.tabWidgetPage2)
        self.pass_generate_stdnt.setObjectName(u"pass_generate_stdnt")
        self.pass_generate_stdnt.setMinimumSize(QSize(100, 40))

        self.verticalLayout_17.addWidget(self.pass_generate_stdnt, 0, Qt.AlignLeft)


        self.verticalLayout_19.addLayout(self.verticalLayout_17)

        self.send_stdnt_cred = QPushButton(self.tabWidgetPage2)
        self.send_stdnt_cred.setObjectName(u"send_stdnt_cred")
        self.send_stdnt_cred.setMinimumSize(QSize(100, 40))

        self.verticalLayout_19.addWidget(self.send_stdnt_cred, 0, Qt.AlignRight)


        self.verticalLayout_25.addLayout(self.verticalLayout_19)

        self.label_11 = QLabel(self.tabWidgetPage2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_25.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_17 = QLabel(self.tabWidgetPage2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_17, 0, Qt.AlignLeft)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.first_name_lineedit_remove = QLineEdit(self.tabWidgetPage2)
        self.first_name_lineedit_remove.setObjectName(u"first_name_lineedit_remove")

        self.verticalLayout_21.addWidget(self.first_name_lineedit_remove)

        self.last_name_lineedit_remove = QLabel(self.tabWidgetPage2)
        self.last_name_lineedit_remove.setObjectName(u"last_name_lineedit_remove")
        self.last_name_lineedit_remove.setFont(font2)

        self.verticalLayout_21.addWidget(self.last_name_lineedit_remove)


        self.horizontalLayout_8.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lineEdit_7 = QLineEdit(self.tabWidgetPage2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_22.addWidget(self.lineEdit_7)

        self.label_18 = QLabel(self.tabWidgetPage2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.verticalLayout_22.addWidget(self.label_18)


        self.horizontalLayout_8.addLayout(self.verticalLayout_22)


        self.verticalLayout_20.addLayout(self.horizontalLayout_8)


        self.verticalLayout_24.addLayout(self.verticalLayout_20)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_19 = QLabel(self.tabWidgetPage2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_23.addWidget(self.label_19, 0, Qt.AlignLeft)

        self.tupc_id_remove_lineedit = QLineEdit(self.tabWidgetPage2)
        self.tupc_id_remove_lineedit.setObjectName(u"tupc_id_remove_lineedit")
        self.tupc_id_remove_lineedit.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_23.addWidget(self.tupc_id_remove_lineedit, 0, Qt.AlignVCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_23.addItem(self.verticalSpacer_10)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)

        self.del_student_inlist = QPushButton(self.tabWidgetPage2)
        self.del_student_inlist.setObjectName(u"del_student_inlist")
        self.del_student_inlist.setMinimumSize(QSize(100, 40))

        self.verticalLayout_24.addWidget(self.del_student_inlist, 0, Qt.AlignRight)


        self.verticalLayout_25.addLayout(self.verticalLayout_24)


        self.gridLayout_7.addLayout(self.verticalLayout_25, 0, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_26)

        self.search_bar_stdnt = QLineEdit(self.tabWidgetPage2)
        self.search_bar_stdnt.setObjectName(u"search_bar_stdnt")

        self.horizontalLayout_5.addWidget(self.search_bar_stdnt)

        self.search_student_btn = QPushButton(self.tabWidgetPage2)
        self.search_student_btn.setObjectName(u"search_student_btn")

        self.horizontalLayout_5.addWidget(self.search_student_btn)


        self.gridLayout_6.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_6)

        self.list_registered_stdnt = QTableWidget(self.tabWidgetPage2)
        if (self.list_registered_stdnt.columnCount() < 3):
            self.list_registered_stdnt.setColumnCount(3)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        if (self.list_registered_stdnt.rowCount() < 1):
            self.list_registered_stdnt.setRowCount(1)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.list_registered_stdnt.setVerticalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 2, __qtablewidgetitem47)
        self.list_registered_stdnt.setObjectName(u"list_registered_stdnt")
        font3 = QFont()
        font3.setPointSize(10)
        self.list_registered_stdnt.setFont(font3)
        self.list_registered_stdnt.setFrameShadow(QFrame.Plain)
        self.list_registered_stdnt.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.list_registered_stdnt.horizontalHeader().setDefaultSectionSize(130)

        self.verticalLayout_11.addWidget(self.list_registered_stdnt)


        self.gridLayout_7.addLayout(self.verticalLayout_11, 0, 2, 1, 1)

        self.line = QFrame(self.tabWidgetPage2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(u"tabWidgetPage3")
        self.gridLayout_16 = QGridLayout(self.tabWidgetPage3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)

        self.search_bar_staff = QLineEdit(self.tabWidgetPage3)
        self.search_bar_staff.setObjectName(u"search_bar_staff")

        self.horizontalLayout_13.addWidget(self.search_bar_staff)

        self.search_staff_btn = QPushButton(self.tabWidgetPage3)
        self.search_staff_btn.setObjectName(u"search_staff_btn")

        self.horizontalLayout_13.addWidget(self.search_staff_btn, 0, Qt.AlignRight)


        self.gridLayout_15.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.verticalLayout_41.addLayout(self.gridLayout_15)

        self.list_registered_staff = QTableWidget(self.tabWidgetPage3)
        if (self.list_registered_staff.columnCount() < 2):
            self.list_registered_staff.setColumnCount(2)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.list_registered_staff.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.list_registered_staff.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        if (self.list_registered_staff.rowCount() < 1):
            self.list_registered_staff.setRowCount(1)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.list_registered_staff.setVerticalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.list_registered_staff.setItem(0, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.list_registered_staff.setItem(0, 1, __qtablewidgetitem52)
        self.list_registered_staff.setObjectName(u"list_registered_staff")
        self.list_registered_staff.setFont(font3)
        self.list_registered_staff.setFrameShadow(QFrame.Plain)
        self.list_registered_staff.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.verticalLayout_41.addWidget(self.list_registered_staff)


        self.gridLayout_16.addLayout(self.verticalLayout_41, 0, 2, 1, 1)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_32 = QLabel(self.tabWidgetPage3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.verticalLayout_32.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.line_4 = QFrame(self.tabWidgetPage3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_32.addWidget(self.line_4)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_33 = QLabel(self.tabWidgetPage3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.verticalLayout_43.addWidget(self.label_33, 0, Qt.AlignLeft)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.first_name_lineedit_staff = QLineEdit(self.tabWidgetPage3)
        self.first_name_lineedit_staff.setObjectName(u"first_name_lineedit_staff")
        self.first_name_lineedit_staff.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_44.addWidget(self.first_name_lineedit_staff)

        self.label_34 = QLabel(self.tabWidgetPage3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)

        self.verticalLayout_44.addWidget(self.label_34)


        self.horizontalLayout_14.addLayout(self.verticalLayout_44)

        self.horizontalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_10)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.lastname_lineedit_staff = QLineEdit(self.tabWidgetPage3)
        self.lastname_lineedit_staff.setObjectName(u"lastname_lineedit_staff")
        self.lastname_lineedit_staff.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_45.addWidget(self.lastname_lineedit_staff)

        self.label_35 = QLabel(self.tabWidgetPage3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.verticalLayout_45.addWidget(self.label_35)


        self.horizontalLayout_14.addLayout(self.verticalLayout_45)


        self.verticalLayout_43.addLayout(self.horizontalLayout_14)


        self.verticalLayout_42.addLayout(self.verticalLayout_43)

        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_36 = QLabel(self.tabWidgetPage3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)

        self.verticalLayout_46.addWidget(self.label_36, 0, Qt.AlignLeft)

        self.email_staff_lineedit = QLineEdit(self.tabWidgetPage3)
        self.email_staff_lineedit.setObjectName(u"email_staff_lineedit")
        self.email_staff_lineedit.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_46.addWidget(self.email_staff_lineedit, 0, Qt.AlignVCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_46.addItem(self.verticalSpacer_12)


        self.verticalLayout_62.addLayout(self.verticalLayout_46)


        self.verticalLayout_42.addLayout(self.verticalLayout_62)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_37 = QLabel(self.tabWidgetPage3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.verticalLayout_48.addWidget(self.label_37, 0, Qt.AlignLeft)

        self.password_staff_reg = QLineEdit(self.tabWidgetPage3)
        self.password_staff_reg.setObjectName(u"password_staff_reg")
        self.password_staff_reg.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_48.addWidget(self.password_staff_reg)

        self.verticalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_48.addItem(self.verticalSpacer_15)


        self.verticalLayout_47.addLayout(self.verticalLayout_48)

        self.pass_generate_staff = QPushButton(self.tabWidgetPage3)
        self.pass_generate_staff.setObjectName(u"pass_generate_staff")
        self.pass_generate_staff.setMinimumSize(QSize(100, 40))

        self.verticalLayout_47.addWidget(self.pass_generate_staff, 0, Qt.AlignLeft)


        self.verticalLayout_42.addLayout(self.verticalLayout_47)

        self.save_staff_btn = QPushButton(self.tabWidgetPage3)
        self.save_staff_btn.setObjectName(u"save_staff_btn")
        self.save_staff_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout_42.addWidget(self.save_staff_btn, 0, Qt.AlignRight)


        self.verticalLayout_32.addLayout(self.verticalLayout_42)

        self.label_38 = QLabel(self.tabWidgetPage3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.verticalLayout_32.addWidget(self.label_38, 0, Qt.AlignHCenter)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_39 = QLabel(self.tabWidgetPage3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.verticalLayout_50.addWidget(self.label_39, 0, Qt.AlignLeft)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.first_name_lineedit_remove_staff = QLineEdit(self.tabWidgetPage3)
        self.first_name_lineedit_remove_staff.setObjectName(u"first_name_lineedit_remove_staff")
        self.first_name_lineedit_remove_staff.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_51.addWidget(self.first_name_lineedit_remove_staff)

        self.label_40 = QLabel(self.tabWidgetPage3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)

        self.verticalLayout_51.addWidget(self.label_40)


        self.horizontalLayout_16.addLayout(self.verticalLayout_51)

        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_11)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.last_name_lineedit_remove_staff = QLineEdit(self.tabWidgetPage3)
        self.last_name_lineedit_remove_staff.setObjectName(u"last_name_lineedit_remove_staff")
        self.last_name_lineedit_remove_staff.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_52.addWidget(self.last_name_lineedit_remove_staff)

        self.label_41 = QLabel(self.tabWidgetPage3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font2)

        self.verticalLayout_52.addWidget(self.label_41)


        self.horizontalLayout_16.addLayout(self.verticalLayout_52)


        self.verticalLayout_50.addLayout(self.horizontalLayout_16)


        self.verticalLayout_49.addLayout(self.verticalLayout_50)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_42 = QLabel(self.tabWidgetPage3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)

        self.verticalLayout_53.addWidget(self.label_42, 0, Qt.AlignLeft)

        self.email_instructor_staff = QLineEdit(self.tabWidgetPage3)
        self.email_instructor_staff.setObjectName(u"email_instructor_staff")
        self.email_instructor_staff.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_53.addWidget(self.email_instructor_staff, 0, Qt.AlignVCenter)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_53.addItem(self.verticalSpacer_16)


        self.verticalLayout_49.addLayout(self.verticalLayout_53)

        self.del_instructor_inlist_2 = QPushButton(self.tabWidgetPage3)
        self.del_instructor_inlist_2.setObjectName(u"del_instructor_inlist_2")
        self.del_instructor_inlist_2.setMinimumSize(QSize(100, 40))

        self.verticalLayout_49.addWidget(self.del_instructor_inlist_2, 0, Qt.AlignRight)


        self.verticalLayout_32.addLayout(self.verticalLayout_49)


        self.gridLayout_16.addLayout(self.verticalLayout_32, 0, 0, 1, 1)

        self.line_3 = QFrame(self.tabWidgetPage3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_16.addWidget(self.line_3, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QWidget()
        self.tabWidgetPage4.setObjectName(u"tabWidgetPage4")
        self.gridLayout_17 = QGridLayout(self.tabWidgetPage4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabWidget1 = QTabWidget(self.tabWidgetPage4)
        self.tabWidget1.setObjectName(u"tabWidget1")
        self.tabWidget1.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(11)
        self.tabWidget1.setFont(font4)
        self.tabWidget1.setFocusPolicy(Qt.TabFocus)
        self.tabWidget1.setTabPosition(QTabWidget.North)
        self.tabWidget1.setTabShape(QTabWidget.Triangular)
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
        self.label_43.setFont(font)

        self.verticalLayout_55.addWidget(self.label_43)

        self.listWidget_2 = QListWidget(self.Roomrequest_tab)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setFont(font1)
        self.listWidget_2.setFrameShape(QFrame.Box)
        self.listWidget_2.setFrameShadow(QFrame.Plain)

        self.verticalLayout_55.addWidget(self.listWidget_2)


        self.gridLayout_18.addLayout(self.verticalLayout_55, 0, 0, 1, 1)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_44 = QLabel(self.Roomrequest_tab)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)

        self.verticalLayout_54.addWidget(self.label_44)

        self.received_request = QPlainTextEdit(self.Roomrequest_tab)
        self.received_request.setObjectName(u"received_request")
        self.received_request.setFrameShape(QFrame.Box)
        self.received_request.setFrameShadow(QFrame.Plain)
        self.received_request.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_54.addWidget(self.received_request)

        self.line_5 = QFrame(self.Roomrequest_tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_54.addWidget(self.line_5)

        self.label_45 = QLabel(self.Roomrequest_tab)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)

        self.verticalLayout_54.addWidget(self.label_45)

        self.reply_requests = QPlainTextEdit(self.Roomrequest_tab)
        self.reply_requests.setObjectName(u"reply_requests")
        self.reply_requests.setFrameShape(QFrame.Box)
        self.reply_requests.setFrameShadow(QFrame.Plain)
        self.reply_requests.setOverwriteMode(False)

        self.verticalLayout_54.addWidget(self.reply_requests)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.del_request = QPushButton(self.Roomrequest_tab)
        self.del_request.setObjectName(u"del_request")
        self.del_request.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_17.addWidget(self.del_request)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_12)

        self.send_message_requests_btn = QPushButton(self.Roomrequest_tab)
        self.send_message_requests_btn.setObjectName(u"send_message_requests_btn")
        self.send_message_requests_btn.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_17.addWidget(self.send_message_requests_btn, 0, Qt.AlignRight)


        self.verticalLayout_54.addLayout(self.horizontalLayout_17)


        self.gridLayout_18.addLayout(self.verticalLayout_54, 0, 1, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.tabWidget1.addTab(self.Roomrequest_tab, "")
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
        self.label_48.setFont(font)

        self.verticalLayout_57.addWidget(self.label_48)

        self.listWidget_3 = QListWidget(self.tab_2)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setFont(font1)
        self.listWidget_3.setFrameShape(QFrame.Box)
        self.listWidget_3.setFrameShadow(QFrame.Plain)

        self.verticalLayout_57.addWidget(self.listWidget_3)


        self.gridLayout_20.addLayout(self.verticalLayout_57, 0, 0, 1, 1)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_46 = QLabel(self.tab_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.verticalLayout_56.addWidget(self.label_46)

        self.received_report = QPlainTextEdit(self.tab_2)
        self.received_report.setObjectName(u"received_report")
        self.received_report.setFrameShape(QFrame.Box)
        self.received_report.setFrameShadow(QFrame.Plain)
        self.received_report.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_56.addWidget(self.received_report)

        self.line_6 = QFrame(self.tab_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_56.addWidget(self.line_6)

        self.label_47 = QLabel(self.tab_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)

        self.verticalLayout_56.addWidget(self.label_47)

        self.reply_report = QPlainTextEdit(self.tab_2)
        self.reply_report.setObjectName(u"reply_report")
        self.reply_report.setFrameShape(QFrame.Box)
        self.reply_report.setFrameShadow(QFrame.Plain)
        self.reply_report.setOverwriteMode(False)

        self.verticalLayout_56.addWidget(self.reply_report)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.del_report = QPushButton(self.tab_2)
        self.del_report.setObjectName(u"del_report")
        self.del_report.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_18.addWidget(self.del_report)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)

        self.send_message_report_btn = QPushButton(self.tab_2)
        self.send_message_report_btn.setObjectName(u"send_message_report_btn")
        self.send_message_report_btn.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_18.addWidget(self.send_message_report_btn, 0, Qt.AlignRight)


        self.verticalLayout_56.addLayout(self.horizontalLayout_18)


        self.gridLayout_20.addLayout(self.verticalLayout_56, 0, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)

        self.tabWidget1.addTab(self.tab_2, "")

        self.gridLayout_17.addWidget(self.tabWidget1, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.tabWidgetPage5 = QWidget()
        self.tabWidgetPage5.setObjectName(u"tabWidgetPage5")
        self.gridLayout_12 = QGridLayout(self.tabWidgetPage5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_20 = QLabel(self.tabWidgetPage5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.verticalLayout_26.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.line_7 = QFrame(self.tabWidgetPage5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_26.addWidget(self.line_7)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_21 = QLabel(self.tabWidgetPage5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.verticalLayout_28.addWidget(self.label_21, 0, Qt.AlignLeft)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.first_name_lineedit_instructor = QLineEdit(self.tabWidgetPage5)
        self.first_name_lineedit_instructor.setObjectName(u"first_name_lineedit_instructor")
        self.first_name_lineedit_instructor.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_29.addWidget(self.first_name_lineedit_instructor)

        self.label_24 = QLabel(self.tabWidgetPage5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.verticalLayout_29.addWidget(self.label_24)


        self.horizontalLayout_9.addLayout(self.verticalLayout_29)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.lastname_lineedit_instructor = QLineEdit(self.tabWidgetPage5)
        self.lastname_lineedit_instructor.setObjectName(u"lastname_lineedit_instructor")
        self.lastname_lineedit_instructor.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_30.addWidget(self.lastname_lineedit_instructor)

        self.label_22 = QLabel(self.tabWidgetPage5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.verticalLayout_30.addWidget(self.label_22)


        self.horizontalLayout_9.addLayout(self.verticalLayout_30)


        self.verticalLayout_28.addLayout(self.horizontalLayout_9)


        self.verticalLayout_27.addLayout(self.verticalLayout_28)

        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_23 = QLabel(self.tabWidgetPage5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.verticalLayout_31.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.email_instructor_lineedit = QLineEdit(self.tabWidgetPage5)
        self.email_instructor_lineedit.setObjectName(u"email_instructor_lineedit")
        self.email_instructor_lineedit.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_31.addWidget(self.email_instructor_lineedit, 0, Qt.AlignVCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_31.addItem(self.verticalSpacer_11)


        self.verticalLayout_63.addLayout(self.verticalLayout_31)


        self.verticalLayout_27.addLayout(self.verticalLayout_63)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_25 = QLabel(self.tabWidgetPage5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.verticalLayout_34.addWidget(self.label_25)

        self.password_instructor_reg = QLineEdit(self.tabWidgetPage5)
        self.password_instructor_reg.setObjectName(u"password_instructor_reg")
        self.password_instructor_reg.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_34.addWidget(self.password_instructor_reg)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_34.addItem(self.verticalSpacer_13)


        self.verticalLayout_33.addLayout(self.verticalLayout_34)

        self.pass_generate_instructor = QPushButton(self.tabWidgetPage5)
        self.pass_generate_instructor.setObjectName(u"pass_generate_instructor")
        self.pass_generate_instructor.setMinimumSize(QSize(100, 40))

        self.verticalLayout_33.addWidget(self.pass_generate_instructor, 0, Qt.AlignLeft)


        self.verticalLayout_27.addLayout(self.verticalLayout_33)

        self.save_instructor_btn = QPushButton(self.tabWidgetPage5)
        self.save_instructor_btn.setObjectName(u"save_instructor_btn")
        self.save_instructor_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout_27.addWidget(self.save_instructor_btn, 0, Qt.AlignRight)


        self.verticalLayout_26.addLayout(self.verticalLayout_27)

        self.label_26 = QLabel(self.tabWidgetPage5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.verticalLayout_26.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_27 = QLabel(self.tabWidgetPage5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.verticalLayout_36.addWidget(self.label_27, 0, Qt.AlignLeft)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.first_name_lineedit_remove_instructor = QLineEdit(self.tabWidgetPage5)
        self.first_name_lineedit_remove_instructor.setObjectName(u"first_name_lineedit_remove_instructor")

        self.verticalLayout_37.addWidget(self.first_name_lineedit_remove_instructor)

        self.label_31 = QLabel(self.tabWidgetPage5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.verticalLayout_37.addWidget(self.label_31)


        self.horizontalLayout_11.addLayout(self.verticalLayout_37)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.last_name_lineedit_remove_instructor = QLineEdit(self.tabWidgetPage5)
        self.last_name_lineedit_remove_instructor.setObjectName(u"last_name_lineedit_remove_instructor")

        self.verticalLayout_38.addWidget(self.last_name_lineedit_remove_instructor)

        self.label_28 = QLabel(self.tabWidgetPage5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.verticalLayout_38.addWidget(self.label_28)


        self.horizontalLayout_11.addLayout(self.verticalLayout_38)


        self.verticalLayout_36.addLayout(self.horizontalLayout_11)


        self.verticalLayout_35.addLayout(self.verticalLayout_36)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_29 = QLabel(self.tabWidgetPage5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.verticalLayout_39.addWidget(self.label_29, 0, Qt.AlignLeft)

        self.email_instructor_remove = QLineEdit(self.tabWidgetPage5)
        self.email_instructor_remove.setObjectName(u"email_instructor_remove")
        self.email_instructor_remove.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_39.addWidget(self.email_instructor_remove, 0, Qt.AlignVCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_39.addItem(self.verticalSpacer_14)


        self.verticalLayout_35.addLayout(self.verticalLayout_39)

        self.del_instructor_inlist = QPushButton(self.tabWidgetPage5)
        self.del_instructor_inlist.setObjectName(u"del_instructor_inlist")
        self.del_instructor_inlist.setMinimumSize(QSize(100, 40))

        self.verticalLayout_35.addWidget(self.del_instructor_inlist, 0, Qt.AlignRight)


        self.verticalLayout_26.addLayout(self.verticalLayout_35)


        self.gridLayout_11.addLayout(self.verticalLayout_26, 0, 0, 1, 1)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)

        self.search_bar_instructor = QLineEdit(self.tabWidgetPage5)
        self.search_bar_instructor.setObjectName(u"search_bar_instructor")

        self.horizontalLayout_12.addWidget(self.search_bar_instructor)

        self.search_instructor_btn = QPushButton(self.tabWidgetPage5)
        self.search_instructor_btn.setObjectName(u"search_instructor_btn")

        self.horizontalLayout_12.addWidget(self.search_instructor_btn)


        self.gridLayout_10.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)


        self.verticalLayout_40.addLayout(self.gridLayout_10)

        self.list_registered_instructor = QTableWidget(self.tabWidgetPage5)
        if (self.list_registered_instructor.columnCount() < 2):
            self.list_registered_instructor.setColumnCount(2)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.list_registered_instructor.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.list_registered_instructor.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        if (self.list_registered_instructor.rowCount() < 1):
            self.list_registered_instructor.setRowCount(1)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.list_registered_instructor.setVerticalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.list_registered_instructor.setItem(0, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.list_registered_instructor.setItem(0, 1, __qtablewidgetitem57)
        self.list_registered_instructor.setObjectName(u"list_registered_instructor")
        self.list_registered_instructor.setFont(font3)
        self.list_registered_instructor.setFrameShadow(QFrame.Plain)
        self.list_registered_instructor.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.verticalLayout_40.addWidget(self.list_registered_instructor)


        self.gridLayout_11.addLayout(self.verticalLayout_40, 0, 2, 1, 1)

        self.line_8 = QFrame(self.tabWidgetPage5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_11.addWidget(self.line_8, 0, 1, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage5, "")

        self.gridLayout_13.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.menu_admin_widget, 0, 1, 1, 1)

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
        font5 = QFont()
        font5.setPointSize(20)
        self.label.setFont(font5)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setPointSize(16)
        self.label_2.setFont(font6)

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.room_btn = QPushButton(self.centralwidget)
        self.room_btn.setObjectName(u"room_btn")
        self.room_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.room_btn)

        self.instructor_btn = QPushButton(self.centralwidget)
        self.instructor_btn.setObjectName(u"instructor_btn")
        self.instructor_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.instructor_btn)

        self.student_btn = QPushButton(self.centralwidget)
        self.student_btn.setObjectName(u"student_btn")
        self.student_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.student_btn)

        self.staff_btn = QPushButton(self.centralwidget)
        self.staff_btn.setObjectName(u"staff_btn")
        self.staff_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.staff_btn)

        self.inbox_btn = QPushButton(self.centralwidget)
        self.inbox_btn.setObjectName(u"inbox_btn")
        self.inbox_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.inbox_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setMinimumSize(QSize(100, 40))

        self.verticalLayout_3.addWidget(self.logout_btn)


        self.gridLayout_14.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 991, 26))
        self.menuHello = QMenu(self.menubar)
        self.menuHello.setObjectName(u"menuHello")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuHello.menuAction())
        self.menuHello.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.schedule_stackedwidget.setCurrentIndex(0)
        self.tabWidget1.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"H", None))
#endif // QT_CONFIG(shortcut)
        self.actionRoom.setText(QCoreApplication.translate("MainWindow", u"Room", None))
        self.actionInstructor.setText(QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.actionStaff.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.actionStudent.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.actionInbox.setText(QCoreApplication.translate("MainWindow", u"Inbox", None))
        self.search_room_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Room Schedule", None))
        self.add_rm.setText(QCoreApplication.translate("MainWindow", u"Add Room", None))
        self.del_rm.setText(QCoreApplication.translate("MainWindow", u"Delete Room", None))
        self.edit_rm.setText(QCoreApplication.translate("MainWindow", u"Edit Room", None))
        self.view_sched.setText(QCoreApplication.translate("MainWindow", u"View Room Schedule", None))
        self.log_rm.setText(QCoreApplication.translate("MainWindow", u"History", None))

        __sortingEnabled = self.room_list.isSortingEnabled()
        self.room_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.room_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Room 1", None));
        self.room_list.setSortingEnabled(__sortingEnabled)

        self.schedule_stackedwidget.setTabText(self.schedule_stackedwidget.indexOf(self.schedule_stackedwidgetPage1), "")
        self.back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u" Room: ", None))
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
        self.schedule_stackedwidget.setTabText(self.schedule_stackedwidget.indexOf(self.schedule_stackedwidgetPage2), "")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Edit Room Schedule", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Assign Instructor:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Subject Code:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Choose Day:", None))
        self.instructor_day_edit_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Monday", None))
        self.instructor_day_edit_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.instructor_day_edit_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Wednesday", None))
        self.instructor_day_edit_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Thursday", None))
        self.instructor_day_edit_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Friday", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Start of Class", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"End of Class", None))
        self.add_student.setText(QCoreApplication.translate("MainWindow", u"Add Students", None))
        self.remove_instructor_sched.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.change_instructor_sched.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.add_sched_instructor.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Assign Staff:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Purpose:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Choose Day:", None))
        self.day_edit_staff.setItemText(0, QCoreApplication.translate("MainWindow", u"Monday", None))
        self.day_edit_staff.setItemText(1, QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.day_edit_staff.setItemText(2, QCoreApplication.translate("MainWindow", u"Wednesday", None))
        self.day_edit_staff.setItemText(3, QCoreApplication.translate("MainWindow", u"Thursday", None))
        self.day_edit_staff.setItemText(4, QCoreApplication.translate("MainWindow", u"Friday", None))

        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Start of Schedule", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"End of Schedule", None))
        self.remove_staff_sched.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.change_staff_sched.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.add_sched_staff.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.back_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        ___qtablewidgetitem19 = self.edit_room_sched_table.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Monday", None));
        ___qtablewidgetitem20 = self.edit_room_sched_table.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None));
        ___qtablewidgetitem21 = self.edit_room_sched_table.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None));
        ___qtablewidgetitem22 = self.edit_room_sched_table.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Thursday", None));
        ___qtablewidgetitem23 = self.edit_room_sched_table.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Friday", None));
        ___qtablewidgetitem24 = self.edit_room_sched_table.verticalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"7:00", None));
        ___qtablewidgetitem25 = self.edit_room_sched_table.verticalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"8:00", None));
        ___qtablewidgetitem26 = self.edit_room_sched_table.verticalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"9:00", None));
        ___qtablewidgetitem27 = self.edit_room_sched_table.verticalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"10:00", None));
        ___qtablewidgetitem28 = self.edit_room_sched_table.verticalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"11:00", None));
        ___qtablewidgetitem29 = self.edit_room_sched_table.verticalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"12:00", None));
        ___qtablewidgetitem30 = self.edit_room_sched_table.verticalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"1:00", None));
        ___qtablewidgetitem31 = self.edit_room_sched_table.verticalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"2:00", None));
        ___qtablewidgetitem32 = self.edit_room_sched_table.verticalHeaderItem(8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"3:00", None));
        ___qtablewidgetitem33 = self.edit_room_sched_table.verticalHeaderItem(9)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"4:00", None));
        ___qtablewidgetitem34 = self.edit_room_sched_table.verticalHeaderItem(10)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"5:00", None));
        ___qtablewidgetitem35 = self.edit_room_sched_table.verticalHeaderItem(11)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"6:00", None));
        ___qtablewidgetitem36 = self.edit_room_sched_table.verticalHeaderItem(12)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"7:00", None));
        ___qtablewidgetitem37 = self.edit_room_sched_table.verticalHeaderItem(13)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"8:00", None));
        self.schedule_stackedwidget.setTabText(self.schedule_stackedwidget.indexOf(self.schedule_stackedwidgetPage3), "")
        self.back_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Accessed Room: ", None))
        ___qtablewidgetitem38 = self.selected_room_log.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Date and Time", None));
        ___qtablewidgetitem39 = self.selected_room_log.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"User", None));
        ___qtablewidgetitem40 = self.selected_room_log.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Access Attempt", None));
        self.schedule_stackedwidget.setTabText(self.schedule_stackedwidget.indexOf(self.schedule_stackedwidgetPage4), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), "")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Register Student ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TUPC-ID:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.pass_generate_stdnt.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.send_stdnt_cred.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Remove Student ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.last_name_lineedit_remove.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TUPC-ID:", None))
        self.del_student_inlist.setText(QCoreApplication.translate("MainWindow", u"Remove ", None))
        self.search_student_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem41 = self.list_registered_stdnt.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Student Name", None));
        ___qtablewidgetitem42 = self.list_registered_stdnt.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem43 = self.list_registered_stdnt.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem44 = self.list_registered_stdnt.verticalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"1.", None));

        __sortingEnabled1 = self.list_registered_stdnt.isSortingEnabled()
        self.list_registered_stdnt.setSortingEnabled(False)
        ___qtablewidgetitem45 = self.list_registered_stdnt.item(0, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Jonathan", None));
        ___qtablewidgetitem46 = self.list_registered_stdnt.item(0, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"23-XXX", None));
        ___qtablewidgetitem47 = self.list_registered_stdnt.item(0, 2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"xxx@gsfe.com.ph", None));
        self.list_registered_stdnt.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), "")
        self.search_staff_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem48 = self.list_registered_staff.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem49 = self.list_registered_staff.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem50 = self.list_registered_staff.verticalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"1.", None));

        __sortingEnabled2 = self.list_registered_staff.isSortingEnabled()
        self.list_registered_staff.setSortingEnabled(False)
        ___qtablewidgetitem51 = self.list_registered_staff.item(0, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Mark", None));
        ___qtablewidgetitem52 = self.list_registered_staff.item(0, 1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"xxx@gmail.com", None));
        self.list_registered_staff.setSortingEnabled(__sortingEnabled2)

        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Register Staff", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.pass_generate_staff.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.save_staff_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Remove Staff", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.del_instructor_inlist_2.setText(QCoreApplication.translate("MainWindow", u"Remove ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), "")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Room Requests", None))

        __sortingEnabled3 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_2.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Example Received Request", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled3)

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Received Message", None))
        self.received_request.setPlainText(QCoreApplication.translate("MainWindow", u"Example Message\n"
"", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Reply / Message", None))
        self.reply_requests.setPlainText(QCoreApplication.translate("MainWindow", u"Example message to send\n"
"\n"
"", None))
        self.del_request.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.send_message_requests_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.Roomrequest_tab), QCoreApplication.translate("MainWindow", u"Room Request", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Reports", None))

        __sortingEnabled4 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_3.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Example Received Report", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled4)

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Received Message", None))
        self.received_report.setPlainText(QCoreApplication.translate("MainWindow", u"Example Message\n"
"", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Reply / Message", None))
        self.reply_report.setPlainText(QCoreApplication.translate("MainWindow", u"Example message to send\n"
"\n"
"", None))
        self.del_report.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.send_message_report_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Maintenance / Damage Report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), "")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Register Instructor", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.pass_generate_instructor.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.save_instructor_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Remove Instructor", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.del_instructor_inlist.setText(QCoreApplication.translate("MainWindow", u"Remove ", None))
        self.search_instructor_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem53 = self.list_registered_instructor.horizontalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem54 = self.list_registered_instructor.horizontalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem55 = self.list_registered_instructor.verticalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"1.", None));

        __sortingEnabled5 = self.list_registered_instructor.isSortingEnabled()
        self.list_registered_instructor.setSortingEnabled(False)
        ___qtablewidgetitem56 = self.list_registered_instructor.item(0, 0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Prof. Jani", None));
        ___qtablewidgetitem57 = self.list_registered_instructor.item(0, 1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"xxx@gmail.com", None));
        self.list_registered_instructor.setSortingEnabled(__sortingEnabled5)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage5), "")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.room_btn.setText(QCoreApplication.translate("MainWindow", u"Room", None))
        self.instructor_btn.setText(QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.student_btn.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.staff_btn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.inbox_btn.setText(QCoreApplication.translate("MainWindow", u"Inbox", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.menuHello.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

