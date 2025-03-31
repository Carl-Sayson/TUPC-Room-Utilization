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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 793)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon = QIcon()
        iconThemeName = u"A"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionAbout.setIcon(icon)
        self.actionAbout.setShortcutContext(Qt.WindowShortcut)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
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


        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(832, 720))
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.gridLayout_2 = QGridLayout(self.stackedWidgetPage1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.schedule_stackedwidget = QStackedWidget(self.stackedWidgetPage1)
        self.schedule_stackedwidget.setObjectName(u"schedule_stackedwidget")
        self.schedule_stackedwidget.setMinimumSize(QSize(579, 589))
        self.schedule_stackedwidgetPage1_2 = QWidget()
        self.schedule_stackedwidgetPage1_2.setObjectName(u"schedule_stackedwidgetPage1_2")
        self.gridLayout_3 = QGridLayout(self.schedule_stackedwidgetPage1_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.schedule_stackedwidgetPage1_2)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_3.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_3)


        self.verticalLayout_58.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.add_rm = QPushButton(self.schedule_stackedwidgetPage1_2)
        self.add_rm.setObjectName(u"add_rm")
        self.add_rm.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.add_rm)

        self.del_rm = QPushButton(self.schedule_stackedwidgetPage1_2)
        self.del_rm.setObjectName(u"del_rm")
        self.del_rm.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.del_rm)

        self.edit_rm = QPushButton(self.schedule_stackedwidgetPage1_2)
        self.edit_rm.setObjectName(u"edit_rm")
        self.edit_rm.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.edit_rm)

        self.view_sched = QPushButton(self.schedule_stackedwidgetPage1_2)
        self.view_sched.setObjectName(u"view_sched")
        self.view_sched.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.view_sched)

        self.log_rm = QPushButton(self.schedule_stackedwidgetPage1_2)
        self.log_rm.setObjectName(u"log_rm")
        self.log_rm.setMinimumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.log_rm)


        self.verticalLayout_58.addLayout(self.verticalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 394, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addLayout(self.verticalLayout_58, 0, 0, 2, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_14 = QSpacerItem(276, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_14)

        self.sort_room = QComboBox(self.schedule_stackedwidgetPage1_2)
        self.sort_room.addItem("")
        self.sort_room.addItem("")
        self.sort_room.setObjectName(u"sort_room")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort_room.sizePolicy().hasHeightForWidth())
        self.sort_room.setSizePolicy(sizePolicy)
        self.sort_room.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_19.addWidget(self.sort_room)

        self.search_bar_room = QLineEdit(self.schedule_stackedwidgetPage1_2)
        self.search_bar_room.setObjectName(u"search_bar_room")

        self.horizontalLayout_19.addWidget(self.search_bar_room)

        self.search_room_btn = QPushButton(self.schedule_stackedwidgetPage1_2)
        self.search_room_btn.setObjectName(u"search_room_btn")

        self.horizontalLayout_19.addWidget(self.search_room_btn)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_19)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.room_list = QListWidget(self.schedule_stackedwidgetPage1_2)
        font3 = QFont()
        font3.setPointSize(12)
        __qlistwidgetitem = QListWidgetItem(self.room_list)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFont(font3);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.room_list.setObjectName(u"room_list")
        self.room_list.setMinimumSize(QSize(621, 637))

        self.gridLayout_3.addWidget(self.room_list, 1, 1, 1, 1)

        self.schedule_stackedwidget.addWidget(self.schedule_stackedwidgetPage1_2)
        self.schedule_stackedwidgetPage2_2 = QWidget()
        self.schedule_stackedwidgetPage2_2.setObjectName(u"schedule_stackedwidgetPage2_2")
        self.verticalLayout_64 = QVBoxLayout(self.schedule_stackedwidgetPage2_2)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.back = QPushButton(self.schedule_stackedwidgetPage2_2)
        self.back.setObjectName(u"back")

        self.horizontalLayout_15.addWidget(self.back)

        self.label_57 = QLabel(self.schedule_stackedwidgetPage2_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font2)

        self.horizontalLayout_15.addWidget(self.label_57)

        self.accessed_room_sched_lineedit = QLineEdit(self.schedule_stackedwidgetPage2_2)
        self.accessed_room_sched_lineedit.setObjectName(u"accessed_room_sched_lineedit")
        self.accessed_room_sched_lineedit.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.accessed_room_sched_lineedit)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_27)


        self.verticalLayout_64.addLayout(self.horizontalLayout_15)

        self.room_sched_table = QTableWidget(self.schedule_stackedwidgetPage2_2)
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

        self.schedule_stackedwidget.addWidget(self.schedule_stackedwidgetPage2_2)
        self.schedule_stackedwidgetPage3_2 = QWidget()
        self.schedule_stackedwidgetPage3_2.setObjectName(u"schedule_stackedwidgetPage3_2")
        self.gridLayout_4 = QGridLayout(self.schedule_stackedwidgetPage3_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_4)

        self.label_56 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font2)

        self.verticalLayout_60.addWidget(self.label_56)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_19)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.assign_instructor = QLineEdit(self.schedule_stackedwidgetPage3_2)
        self.assign_instructor.setObjectName(u"assign_instructor")
        self.assign_instructor.setMaximumSize(QSize(600, 16777215))

        self.horizontalLayout_2.addWidget(self.assign_instructor)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout.addWidget(self.label_8)

        self.assign_subject = QLineEdit(self.schedule_stackedwidgetPage3_2)
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

        self.label_5 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.instructor_day_edit_comboBox = QComboBox(self.schedule_stackedwidgetPage3_2)
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
        self.label_6 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_6)

        self.start_time_instructor = QTimeEdit(self.schedule_stackedwidgetPage3_2)
        self.start_time_instructor.setObjectName(u"start_time_instructor")

        self.verticalLayout_7.addWidget(self.start_time_instructor)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.label_9 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_7)

        self.final_time_instructor = QTimeEdit(self.schedule_stackedwidgetPage3_2)
        self.final_time_instructor.setObjectName(u"final_time_instructor")

        self.verticalLayout_6.addWidget(self.final_time_instructor)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.add_student = QPushButton(self.schedule_stackedwidgetPage3_2)
        self.add_student.setObjectName(u"add_student")
        self.add_student.setMinimumSize(QSize(100, 30))

        self.verticalLayout_8.addWidget(self.add_student, 0, Qt.AlignHCenter)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.remove_instructor_sched = QPushButton(self.schedule_stackedwidgetPage3_2)
        self.remove_instructor_sched.setObjectName(u"remove_instructor_sched")

        self.horizontalLayout_24.addWidget(self.remove_instructor_sched, 0, Qt.AlignLeft)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_28)

        self.change_instructor_sched = QPushButton(self.schedule_stackedwidgetPage3_2)
        self.change_instructor_sched.setObjectName(u"change_instructor_sched")

        self.horizontalLayout_24.addWidget(self.change_instructor_sched, 0, Qt.AlignRight)

        self.add_sched_instructor = QPushButton(self.schedule_stackedwidgetPage3_2)
        self.add_sched_instructor.setObjectName(u"add_sched_instructor")

        self.horizontalLayout_24.addWidget(self.add_sched_instructor, 0, Qt.AlignRight)


        self.verticalLayout_8.addLayout(self.horizontalLayout_24)


        self.verticalLayout_60.addLayout(self.verticalLayout_8)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_6)

        self.line_11 = QFrame(self.schedule_stackedwidgetPage3_2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_60.addWidget(self.line_11)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_50 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font2)

        self.horizontalLayout_21.addWidget(self.label_50)

        self.assign_staff = QLineEdit(self.schedule_stackedwidgetPage3_2)
        self.assign_staff.setObjectName(u"assign_staff")
        self.assign_staff.setMaximumSize(QSize(600, 16777215))

        self.horizontalLayout_21.addWidget(self.assign_staff)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_49 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label_49)

        self.assign_maintenance = QLineEdit(self.schedule_stackedwidgetPage3_2)
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

        self.label_51 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label_51)

        self.day_edit_staff = QComboBox(self.schedule_stackedwidgetPage3_2)
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
        self.label_52 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_52)

        self.start_time_staff = QTimeEdit(self.schedule_stackedwidgetPage3_2)
        self.start_time_staff.setObjectName(u"start_time_staff")

        self.verticalLayout_10.addWidget(self.start_time_staff)


        self.horizontalLayout_23.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_20)

        self.label_53 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_53)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_21)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(7)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_54 = QLabel(self.schedule_stackedwidgetPage3_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.verticalLayout_59.addWidget(self.label_54)

        self.final_time_staff = QTimeEdit(self.schedule_stackedwidgetPage3_2)
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
        self.remove_staff_sched = QPushButton(self.schedule_stackedwidgetPage3_2)
        self.remove_staff_sched.setObjectName(u"remove_staff_sched")

        self.horizontalLayout_25.addWidget(self.remove_staff_sched, 0, Qt.AlignLeft)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_29)

        self.change_staff_sched = QPushButton(self.schedule_stackedwidgetPage3_2)
        self.change_staff_sched.setObjectName(u"change_staff_sched")

        self.horizontalLayout_25.addWidget(self.change_staff_sched, 0, Qt.AlignRight)

        self.add_sched_staff = QPushButton(self.schedule_stackedwidgetPage3_2)
        self.add_sched_staff.setObjectName(u"add_sched_staff")

        self.horizontalLayout_25.addWidget(self.add_sched_staff, 0, Qt.AlignRight)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)


        self.verticalLayout_60.addLayout(self.verticalLayout_9)

        self.back_2 = QPushButton(self.schedule_stackedwidgetPage3_2)
        self.back_2.setObjectName(u"back_2")

        self.verticalLayout_60.addWidget(self.back_2, 0, Qt.AlignLeft)


        self.gridLayout_4.addLayout(self.verticalLayout_60, 0, 0, 1, 1)

        self.edit_room_sched_table = QTableWidget(self.schedule_stackedwidgetPage3_2)
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
        self.edit_room_sched_table.setMinimumSize(QSize(351, 676))
        self.edit_room_sched_table.setMaximumSize(QSize(90000, 90000))

        self.gridLayout_4.addWidget(self.edit_room_sched_table, 0, 2, 1, 1)

        self.line_9 = QFrame(self.schedule_stackedwidgetPage3_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_9, 0, 1, 1, 1)

        self.schedule_stackedwidget.addWidget(self.schedule_stackedwidgetPage3_2)
        self.schedule_stackedwidgetPage4_2 = QWidget()
        self.schedule_stackedwidgetPage4_2.setObjectName(u"schedule_stackedwidgetPage4_2")
        self.verticalLayout_61 = QVBoxLayout(self.schedule_stackedwidgetPage4_2)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.back_3 = QPushButton(self.schedule_stackedwidgetPage4_2)
        self.back_3.setObjectName(u"back_3")

        self.verticalLayout_61.addWidget(self.back_3, 0, Qt.AlignLeft)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_55 = QLabel(self.schedule_stackedwidgetPage4_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_55)

        self.accessed_room_logs_lineedit = QLineEdit(self.schedule_stackedwidgetPage4_2)
        self.accessed_room_logs_lineedit.setObjectName(u"accessed_room_logs_lineedit")
        self.accessed_room_logs_lineedit.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.accessed_room_logs_lineedit)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_25)


        self.verticalLayout_61.addLayout(self.horizontalLayout_10)

        self.selected_room_log = QTableWidget(self.schedule_stackedwidgetPage4_2)
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

        self.schedule_stackedwidget.addWidget(self.schedule_stackedwidgetPage4_2)

        self.gridLayout_2.addWidget(self.schedule_stackedwidget, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.gridLayout_6 = QGridLayout(self.stackedWidgetPage2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.stackedWidgetPage2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 109))
        self.label_10.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.manage_student = QPushButton(self.stackedWidgetPage2)
        self.manage_student.setObjectName(u"manage_student")
        self.manage_student.setMinimumSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.manage_student)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_26)

        self.label_11 = QLabel(self.stackedWidgetPage2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.sort_student = QComboBox(self.stackedWidgetPage2)
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.addItem("")
        self.sort_student.setObjectName(u"sort_student")

        self.horizontalLayout_5.addWidget(self.sort_student)

        self.search_bar_stdnt = QLineEdit(self.stackedWidgetPage2)
        self.search_bar_stdnt.setObjectName(u"search_bar_stdnt")
        self.search_bar_stdnt.setMinimumSize(QSize(10, 5))

        self.horizontalLayout_5.addWidget(self.search_bar_stdnt)

        self.search_student_btn = QPushButton(self.stackedWidgetPage2)
        self.search_student_btn.setObjectName(u"search_student_btn")

        self.horizontalLayout_5.addWidget(self.search_student_btn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)


        self.gridLayout_5.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.list_registered_stdnt = QTableWidget(self.stackedWidgetPage2)
        if (self.list_registered_stdnt.columnCount() < 6):
            self.list_registered_stdnt.setColumnCount(6)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.list_registered_stdnt.setHorizontalHeaderItem(5, __qtablewidgetitem46)
        if (self.list_registered_stdnt.rowCount() < 1):
            self.list_registered_stdnt.setRowCount(1)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.list_registered_stdnt.setVerticalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.list_registered_stdnt.setItem(0, 2, __qtablewidgetitem50)
        self.list_registered_stdnt.setObjectName(u"list_registered_stdnt")
        self.list_registered_stdnt.setMinimumSize(QSize(808, 513))
        font4 = QFont()
        font4.setPointSize(10)
        self.list_registered_stdnt.setFont(font4)
        self.list_registered_stdnt.setFrameShape(QFrame.StyledPanel)
        self.list_registered_stdnt.setFrameShadow(QFrame.Plain)
        self.list_registered_stdnt.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.list_registered_stdnt.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.list_registered_stdnt.setShowGrid(True)
        self.list_registered_stdnt.setGridStyle(Qt.SolidLine)
        self.list_registered_stdnt.horizontalHeader().setDefaultSectionSize(130)

        self.gridLayout_5.addWidget(self.list_registered_stdnt, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage3.setObjectName(u"stackedWidgetPage3")
        self.gridLayout_23 = QGridLayout(self.stackedWidgetPage3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_13 = QLabel(self.stackedWidgetPage3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 109))
        self.label_13.setFont(font2)

        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.manage_staff = QPushButton(self.stackedWidgetPage3)
        self.manage_staff.setObjectName(u"manage_staff")
        self.manage_staff.setMinimumSize(QSize(35, 35))

        self.horizontalLayout_13.addWidget(self.manage_staff)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_30)

        self.label_12 = QLabel(self.stackedWidgetPage3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.sort_staff = QComboBox(self.stackedWidgetPage3)
        self.sort_staff.addItem("")
        self.sort_staff.addItem("")
        self.sort_staff.addItem("")
        self.sort_staff.setObjectName(u"sort_staff")

        self.horizontalLayout_13.addWidget(self.sort_staff)

        self.search_bar_staff = QLineEdit(self.stackedWidgetPage3)
        self.search_bar_staff.setObjectName(u"search_bar_staff")

        self.horizontalLayout_13.addWidget(self.search_bar_staff)

        self.search_staff_btn = QPushButton(self.stackedWidgetPage3)
        self.search_staff_btn.setObjectName(u"search_staff_btn")

        self.horizontalLayout_13.addWidget(self.search_staff_btn, 0, Qt.AlignRight)


        self.gridLayout_15.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_15, 1, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.list_registered_staff = QTableWidget(self.stackedWidgetPage3)
        if (self.list_registered_staff.columnCount() < 3):
            self.list_registered_staff.setColumnCount(3)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.list_registered_staff.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.list_registered_staff.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.list_registered_staff.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        if (self.list_registered_staff.rowCount() < 1):
            self.list_registered_staff.setRowCount(1)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.list_registered_staff.setVerticalHeaderItem(0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.list_registered_staff.setItem(0, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.list_registered_staff.setItem(0, 1, __qtablewidgetitem56)
        self.list_registered_staff.setObjectName(u"list_registered_staff")
        self.list_registered_staff.setFont(font4)
        self.list_registered_staff.setFrameShadow(QFrame.Plain)
        self.list_registered_staff.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.gridLayout_9.addWidget(self.list_registered_staff, 1, 0, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage3)
        self.stackedWidgetPage4 = QWidget()
        self.stackedWidgetPage4.setObjectName(u"stackedWidgetPage4")
        self.gridLayout_17 = QGridLayout(self.stackedWidgetPage4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabWidget = QTabWidget(self.stackedWidgetPage4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(11)
        self.tabWidget.setFont(font5)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
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
        self.label_43.setFont(font2)

        self.verticalLayout_55.addWidget(self.label_43)

        self.list_requests = QListWidget(self.Roomrequest_tab)
        QListWidgetItem(self.list_requests)
        self.list_requests.setObjectName(u"list_requests")
        self.list_requests.setFont(font3)
        self.list_requests.setFrameShape(QFrame.Box)
        self.list_requests.setFrameShadow(QFrame.Plain)

        self.verticalLayout_55.addWidget(self.list_requests)


        self.gridLayout_18.addLayout(self.verticalLayout_55, 0, 0, 1, 1)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_44 = QLabel(self.Roomrequest_tab)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font2)

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
        self.label_45.setFont(font2)

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
        self.label_48.setFont(font2)

        self.verticalLayout_57.addWidget(self.label_48)

        self.list_reports = QListWidget(self.tab_2)
        QListWidgetItem(self.list_reports)
        self.list_reports.setObjectName(u"list_reports")
        self.list_reports.setFont(font3)
        self.list_reports.setFrameShape(QFrame.Box)
        self.list_reports.setFrameShadow(QFrame.Plain)

        self.verticalLayout_57.addWidget(self.list_reports)


        self.gridLayout_20.addLayout(self.verticalLayout_57, 0, 0, 1, 1)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_46 = QLabel(self.tab_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font2)

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
        self.label_47.setFont(font2)

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

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_17.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage4)
        self.stackedWidgetPage5 = QWidget()
        self.stackedWidgetPage5.setObjectName(u"stackedWidgetPage5")
        self.gridLayout_14 = QGridLayout(self.stackedWidgetPage5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_16 = QLabel(self.stackedWidgetPage5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 109))
        self.label_16.setFont(font2)

        self.gridLayout_12.addWidget(self.label_16, 0, 0, 1, 1)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.manage_instructor = QPushButton(self.stackedWidgetPage5)
        self.manage_instructor.setObjectName(u"manage_instructor")
        self.manage_instructor.setMinimumSize(QSize(35, 35))

        self.horizontalLayout_16.addWidget(self.manage_instructor)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_32)

        self.label_17 = QLabel(self.stackedWidgetPage5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_16.addWidget(self.label_17)

        self.sort_instructor = QComboBox(self.stackedWidgetPage5)
        self.sort_instructor.addItem("")
        self.sort_instructor.addItem("")
        self.sort_instructor.addItem("")
        self.sort_instructor.setObjectName(u"sort_instructor")

        self.horizontalLayout_16.addWidget(self.sort_instructor)

        self.search_bar_instructor = QLineEdit(self.stackedWidgetPage5)
        self.search_bar_instructor.setObjectName(u"search_bar_instructor")

        self.horizontalLayout_16.addWidget(self.search_bar_instructor)

        self.search_instructor_btn = QPushButton(self.stackedWidgetPage5)
        self.search_instructor_btn.setObjectName(u"search_instructor_btn")

        self.horizontalLayout_16.addWidget(self.search_instructor_btn, 0, Qt.AlignRight)


        self.gridLayout_22.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_22, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.list_registered_instructor = QTableWidget(self.stackedWidgetPage5)
        if (self.list_registered_instructor.columnCount() < 3):
            self.list_registered_instructor.setColumnCount(3)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.list_registered_instructor.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.list_registered_instructor.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.list_registered_instructor.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        if (self.list_registered_instructor.rowCount() < 1):
            self.list_registered_instructor.setRowCount(1)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.list_registered_instructor.setVerticalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.list_registered_instructor.setItem(0, 0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.list_registered_instructor.setItem(0, 1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.list_registered_instructor.setItem(0, 2, __qtablewidgetitem63)
        self.list_registered_instructor.setObjectName(u"list_registered_instructor")
        self.list_registered_instructor.setFont(font4)
        self.list_registered_instructor.setFrameShadow(QFrame.Plain)
        self.list_registered_instructor.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.gridLayout_13.addWidget(self.list_registered_instructor, 1, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage5)

        self.gridLayout_7.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1022, 26))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.schedule_stackedwidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.room_btn.setText(QCoreApplication.translate("MainWindow", u"Room", None))
        self.instructor_btn.setText(QCoreApplication.translate("MainWindow", u"Instructor", None))
        self.student_btn.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.staff_btn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.inbox_btn.setText(QCoreApplication.translate("MainWindow", u"Inbox", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Room Schedule", None))
        self.add_rm.setText(QCoreApplication.translate("MainWindow", u"Add Room", None))
        self.del_rm.setText(QCoreApplication.translate("MainWindow", u"Delete Room", None))
        self.edit_rm.setText(QCoreApplication.translate("MainWindow", u"Edit Room", None))
        self.view_sched.setText(QCoreApplication.translate("MainWindow", u"View Room Schedule", None))
        self.log_rm.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.sort_room.setItemText(0, QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.sort_room.setItemText(1, QCoreApplication.translate("MainWindow", u"Z-A", None))

        self.search_room_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))

        __sortingEnabled = self.room_list.isSortingEnabled()
        self.room_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.room_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Room 1", None));
        self.room_list.setSortingEnabled(__sortingEnabled)

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
        self.back_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Accessed Room: ", None))
        ___qtablewidgetitem38 = self.selected_room_log.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Date and Time", None));
        ___qtablewidgetitem39 = self.selected_room_log.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"User", None));
        ___qtablewidgetitem40 = self.selected_room_log.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Access Attempt", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Accounts", None))
        self.manage_student.setText(QCoreApplication.translate("MainWindow", u"Manage Student", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sort by:", None))
        self.sort_student.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.sort_student.setItemText(1, QCoreApplication.translate("MainWindow", u"Email", None))
        self.sort_student.setItemText(2, QCoreApplication.translate("MainWindow", u"ID", None))
        self.sort_student.setItemText(3, QCoreApplication.translate("MainWindow", u"Course", None))
        self.sort_student.setItemText(4, QCoreApplication.translate("MainWindow", u"Year", None))
        self.sort_student.setItemText(5, QCoreApplication.translate("MainWindow", u"Section", None))

        self.sort_student.setCurrentText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_student_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem41 = self.list_registered_stdnt.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Student Name", None));
        ___qtablewidgetitem42 = self.list_registered_stdnt.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem43 = self.list_registered_stdnt.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem44 = self.list_registered_stdnt.horizontalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        ___qtablewidgetitem45 = self.list_registered_stdnt.horizontalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Year", None));
        ___qtablewidgetitem46 = self.list_registered_stdnt.horizontalHeaderItem(5)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem47 = self.list_registered_stdnt.verticalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"1.", None));

        __sortingEnabled1 = self.list_registered_stdnt.isSortingEnabled()
        self.list_registered_stdnt.setSortingEnabled(False)
        self.list_registered_stdnt.setSortingEnabled(__sortingEnabled1)

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Staff Accounts", None))
        self.manage_staff.setText(QCoreApplication.translate("MainWindow", u"Manage Staff", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Sort by:", None))
        self.sort_staff.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.sort_staff.setItemText(1, QCoreApplication.translate("MainWindow", u"Email", None))
        self.sort_staff.setItemText(2, QCoreApplication.translate("MainWindow", u"ID", None))

        self.sort_staff.setCurrentText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_staff_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem48 = self.list_registered_staff.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem49 = self.list_registered_staff.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"ID No.", None));
        ___qtablewidgetitem50 = self.list_registered_staff.horizontalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem51 = self.list_registered_staff.verticalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"1.", None));

        __sortingEnabled2 = self.list_registered_staff.isSortingEnabled()
        self.list_registered_staff.setSortingEnabled(False)
        self.list_registered_staff.setSortingEnabled(__sortingEnabled2)

        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Room Requests", None))

        __sortingEnabled3 = self.list_requests.isSortingEnabled()
        self.list_requests.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.list_requests.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Example Received Request", None));
        self.list_requests.setSortingEnabled(__sortingEnabled3)

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Received Message", None))
        self.received_request.setPlainText(QCoreApplication.translate("MainWindow", u"Example Message\n"
"", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Reply / Message", None))
        self.reply_requests.setPlainText(QCoreApplication.translate("MainWindow", u"Example message to send\n"
"\n"
"", None))
        self.del_request.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.send_message_requests_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Roomrequest_tab), QCoreApplication.translate("MainWindow", u"Room Request", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Reports", None))

        __sortingEnabled4 = self.list_reports.isSortingEnabled()
        self.list_reports.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.list_reports.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Example Received Report", None));
        self.list_reports.setSortingEnabled(__sortingEnabled4)

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Received Message", None))
        self.received_report.setPlainText(QCoreApplication.translate("MainWindow", u"Example Message\n"
"", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Reply / Message", None))
        self.reply_report.setPlainText(QCoreApplication.translate("MainWindow", u"Example message to send\n"
"\n"
"", None))
        self.del_report.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.send_message_report_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Maintenance / Damage Report", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Instructor Accounts", None))
        self.manage_instructor.setText(QCoreApplication.translate("MainWindow", u"Manage Instructor", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sort by:", None))
        self.sort_instructor.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.sort_instructor.setItemText(1, QCoreApplication.translate("MainWindow", u"Email", None))
        self.sort_instructor.setItemText(2, QCoreApplication.translate("MainWindow", u"ID", None))

        self.sort_instructor.setCurrentText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_instructor_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem52 = self.list_registered_instructor.horizontalHeaderItem(0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem53 = self.list_registered_instructor.horizontalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"ID No.", None));
        ___qtablewidgetitem54 = self.list_registered_instructor.horizontalHeaderItem(2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem55 = self.list_registered_instructor.verticalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"1.", None));

        __sortingEnabled5 = self.list_registered_instructor.isSortingEnabled()
        self.list_registered_instructor.setSortingEnabled(False)
        self.list_registered_instructor.setSortingEnabled(__sortingEnabled5)

        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

