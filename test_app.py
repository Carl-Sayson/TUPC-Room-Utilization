from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QListWidgetItem, QPushButton, QLineEdit, QTableWidgetItem, QTableWidget, QComboBox, QListWidget, QAbstractItemView, QHeaderView
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QFont

from Log_in_ui import Ui_Log_In as login
from Admin_menu_ui import Ui_MainWindow as AdminUI
from Student_menu_ui import Ui_MainWindow as StudentUI
from Staff_menu_ui import Ui_MainWindow as StaffUI
from Instructor_menu_ui import Ui_MainWindow as InstructorUI

from Change_pass_ui import Ui_Dialog as ChangePassUi
from Room_Request_Instructor_ui import Ui_Form as RoomRequestInstructorUi
from Room_Request_Staff_ui import Ui_Form as RoomRequestStaffUi
from Compose_Message_staff_ui import Ui_Form as ComposeReportStaffUi
from Edit_students_ui import Ui_Form as EditStudentUi
from Force_change_Password_ui import Ui_Form as ForceChangePasswordUi
from staff_registration_ui import Ui_Form as StaffRegistrationUi
from student_registration_ui import Ui_Dialog as StudentRegistrationUi
from instructor_registration_ui import Ui_Form as InstructorRegistrationUi

import mysql.connector
from mysql.connector import errorcode
import sys
from datetime import time

class AdminMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = AdminUI()
        self.ui.setupUi(self)

        try: 
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="Group_F",
                password="CPET-8L-TUPCROOM",
                database="tupc-room_utilization"
            )
            
            self.mycursor = self.mydb.cursor()     
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)   

        self.student_table_widget = self.ui.stackedWidget.widget(1).findChild(QTableWidget, "list_registered_stdnt")
        self.instructor_table_widget = self.ui.stackedWidget.widget(4).findChild(QTableWidget, "list_registered_instructor")
        self.staff_table_widget = self.ui.stackedWidget.widget(2).findChild(QTableWidget, "list_registered_staff")

        self.student_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.instructor_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.staff_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.student_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.instructor_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.staff_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        student_tab = self.ui.stackedWidget.widget(1)
        self.sort_student = student_tab.findChild(QComboBox, "sort_student")
        self.search_student_btn = student_tab.findChild(QPushButton, "search_student_btn")
        self.search_bar_student = student_tab.findChild(QLineEdit, "search_bar_stdnt")
        self.student_table_widget = student_tab.findChild(QTableWidget, "list_registered_stdnt")

        self.sort_student.currentIndexChanged.connect(self.sort_students)
        self.search_student_btn.clicked.connect(self.search_students)
        self.search_bar_student.textChanged.connect(self.reset_student_search)

        self.ui.sort_instructor.clear()
        self.ui.sort_instructor.addItems(["ID", "First Name", "Last Name", "Email"])

        self.ui.sort_student.clear()
        self.ui.sort_student.addItems(["ID", "First Name", "Last Name", "Email", "Section", "Course", "Year"])

        self.ui.sort_staff.clear()
        self.ui.sort_staff.addItems(["ID", "First Name", "Last Name", "Email"])

        self.ui.sort_instructor.currentIndexChanged.connect(self.sort_instructors)
        self.ui.sort_staff.currentIndexChanged.connect(self.sort_staffs)

        self.ui.search_instructor_btn.clicked.connect(self.search_instructor)
        self.ui.search_bar_instructor.textChanged.connect(self.reset_instructor_search)

        self.ui.search_staff_btn.clicked.connect(self.search_staff)
        self.ui.search_bar_staff.textChanged.connect(self.reset_staff_search)

        self.search_staff_btn = self.ui.stackedWidget.widget(2).findChild(QTableWidget, "search_staff_btn")
        self.search_bar_staff = self.ui.stackedWidget.widget(2).findChild(QTableWidget, "search_bar_staff")
        self.sort_staff = self.ui.stackedWidget.widget(2).findChild(QTableWidget, "sort_staff")

        self.ui.add_rm.clicked.connect(self.add_room) 
        self.ui.del_rm.clicked.connect(self.delete_room)

        self.ui.start_time_instructor.setMinimumTime(QTime(7, 0))
        self.ui.start_time_instructor.setMaximumTime(QTime(20, 0))
        self.ui.start_time_instructor.timeChanged.connect(lambda: self.correct_time_minutes('start_instructor'))
        self.ui.final_time_instructor.setMinimumTime(QTime(8, 0))
        self.ui.final_time_instructor.setMaximumTime(QTime(20, 0))
        self.ui.final_time_instructor.timeChanged.connect(lambda: self.correct_time_minutes('end_instructor'))

        self.ui.start_time_staff.setMinimumTime(QTime(7, 0))
        self.ui.start_time_staff.setMaximumTime(QTime(20, 0))
        self.ui.start_time_staff.timeChanged.connect(lambda: self.correct_time_minutes('start_staff'))
        self.ui.final_time_staff.setMinimumTime(QTime(8, 0))
        self.ui.final_time_staff.setMaximumTime(QTime(20, 0))
        self.ui.final_time_staff.timeChanged.connect(lambda: self.correct_time_minutes('end_staff'))
        
        self.ui.room_btn.clicked.connect(lambda: self.open_page(0)) 
        self.ui.instructor_btn.clicked.connect(lambda: self.open_page(4)) 
        self.ui.student_btn.clicked.connect(lambda: self.open_page(1)) 
        self.ui.staff_btn.clicked.connect(lambda: self.open_page(2)) 
        self.ui.inbox_btn.clicked.connect(lambda: self.open_page(3))

        self.ui.log_rm.clicked.connect(lambda: self.handle_room_action(3))
        self.ui.edit_rm.clicked.connect(lambda: self.handle_room_action(2))
        self.ui.view_sched.clicked.connect(lambda: self.handle_room_action(1))

        self.bck_btn_editsched = self.ui.schedule_stackedwidget.widget(2).findChild(QPushButton, "back_2")
        self.bck_btn_display = self.ui.schedule_stackedwidget.widget(1).findChild(QPushButton, "back")
        self.bck_btn_logs = self.ui.schedule_stackedwidget.widget(3).findChild(QPushButton, "back_3")
        self.bck_btn_editsched.clicked.connect(self.return_roomview)
        self.bck_btn_display.clicked.connect(self.return_roomview)
        self.bck_btn_logs.clicked.connect(self.return_roomview)

        self.add_student = self.ui.schedule_stackedwidget.widget(2).findChild(QPushButton, "add_student")
        self.add_student.clicked.connect(self.open_add_student) 

        self.btn_manage_staff = self.ui.stackedWidget.widget(2).findChild(QPushButton, "manage_staff")
        self.btn_manage_student = self.ui.stackedWidget.widget(1).findChild(QPushButton, "manage_student")
        self.btn_manage_instructor = self.ui.stackedWidget.widget(4).findChild(QPushButton, "manage_instructor")
        self.btn_manage_staff.clicked.connect(self.open_manage_staff) 
        self.btn_manage_student.clicked.connect(self.open_manage_student) 
        self.btn_manage_instructor.clicked.connect(self.open_manage_instructor)
        self.ui.edit_room_sched_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.edit_room_sched_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.edit_room_sched_table.itemDoubleClicked.connect(self.edit_selected_schedule)
        self.ui.room_sched_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.room_sched_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.add_sched_instructor.clicked.connect(self.add_instructor_schedule)
        self.ui.add_sched_staff.clicked.connect(self.add_staff_schedule)
        self.setup_schedule_table()
        self.room_view()
        self.load_students_into_table()
        self.load_instructors_into_table()
        self.load_staffs_into_table()
        self.load_rooms_into_list()
        self.ui.room_list.itemChanged.connect(self.save_room_to_db)
        self.ui.room_list.itemChanged.connect(self.edit_room)
        # self.ui.logout_btn.clicked.connect(self.open_logout)  
        self.ui.change_instructor_sched.setDisabled(True)
        self.ui.change_staff_sched.setDisabled(True)
        self.ui.change_instructor_sched.clicked.connect(lambda: self.change_schedule('instructor'))
        self.ui.change_staff_sched.clicked.connect(lambda: self.change_schedule('staff'))

        self.ui.remove_instructor_sched.clicked.connect(self.remove_instructor_schedule)
        self.ui.remove_staff_sched.clicked.connect(self.remove_staff_schedule)

    def correct_time_minutes(self, timeedit):
        if timeedit == "start_instructor":
            time_edit = self.ui.start_time_instructor
        elif timeedit == "end_instructor":
            time_edit = self.ui.final_time_instructor
        elif timeedit == "start_staff":
            time_edit = self.ui.start_time_staff
        else:
            time_edit = self.ui.final_time_staff
        current_time = time_edit.time()
        corrected_time = QTime(current_time.hour(), 0)
        if current_time.minute() != 0:
            time_edit.setTime(corrected_time)

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(self, "Database Error", error_message)

    def load_rooms_into_list(self):
        try:
            self.ui.room_list.clear()
            self.mycursor.execute("SELECT room FROM tupc_rooms")
            for (room_name,) in self.mycursor.fetchall():
                item = QListWidgetItem(room_name)
                item.setTextAlignment(Qt.AlignCenter)
                font = QFont()
                font.setPointSize(12)
                item.setFont(font)

                item.setData(Qt.UserRole, room_name)  # Store original name
                self.ui.room_list.addItem(item)
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def save_room_to_db(self, item):
        room_name = item.text().strip()

        if not room_name:
            QMessageBox.warning(self, "Invalid Room Name", "Room name cannot be empty.")
            return

        try:
            # Check if the room already exists
            check_query = "SELECT COUNT(*) FROM tupc_rooms WHERE room = %s"
            self.mycursor.execute(check_query, (room_name,))
            (exists,) = self.mycursor.fetchone()

            if exists:
                return  # Room already exists, no need to insert again

            # Insert new room into database
            insert_query = "INSERT INTO tupc_rooms (room) VALUES (%s)"
            self.mycursor.execute(insert_query, (room_name,))
            self.mydb.commit()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def edit_room(self, item):
        new_name = item.text().strip()

        if not new_name:
            QMessageBox.warning(self, "Invalid Room Name", "Room name cannot be empty.")
            self.load_rooms_into_list()
            return

        # Get original name (before it was changed)
        old_name = item.data(Qt.UserRole)  # Stored when item was first added/loaded

        if not old_name or old_name == new_name:
            return  # No change, or missing original name

        try:
            # Check for duplicates
            check_query = "SELECT COUNT(*) FROM tupc_rooms WHERE room = %s"
            self.mycursor.execute(check_query, (new_name,))
            (exists,) = self.mycursor.fetchone()

            if exists:
                QMessageBox.warning(self, "Duplicate Room", f"'{new_name}' already exists.")
                self.load_rooms_into_list()
                return

            # Perform the update
            update_query = "UPDATE tupc_rooms SET room = %s WHERE room = %s"
            self.mycursor.execute(update_query, (new_name, old_name))
            self.mydb.commit()

            # Update stored original name
            item.setData(Qt.UserRole, new_name)

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def delete_room(self):
        selected_item = self.ui.room_list.currentItem()
        if selected_item:
            room_name = selected_item.text().strip()

            confirmation = QMessageBox.question(
                self, 
                "Confirm Deletion", 
                f"Are you sure you want to delete the room '{room_name}' and all associated schedules?",
                QMessageBox.Yes | QMessageBox.No
            )

            if confirmation == QMessageBox.Yes:
                try:
                    # Step 1: Get the room's ID
                    self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (room_name,))
                    result = self.mycursor.fetchone()
                    if not result:
                        QMessageBox.warning(self, "Error", "Room not found in database.")
                        return
                    room_id = result[0]

                    # Step 2: Delete all schedules associated with this room
                    self.mycursor.execute("DELETE FROM room_schedule WHERE selected_room_ID = %s", (room_id,))

                    # Step 3: Delete the room
                    self.mycursor.execute("DELETE FROM tupc_rooms WHERE room = %s", (room_name,))
                    self.mydb.commit()

                    # Step 4: Remove from the list widget
                    row = self.ui.room_list.row(selected_item)
                    self.ui.room_list.takeItem(row)

                    QMessageBox.information(self, "Success", f"Room '{room_name}' and its schedules were deleted.")

                except mysql.connector.Error as err:
                    self.errorDisplay(err.errno, err.sqlstate, err.msg)
        else:
            QMessageBox.warning(self, "Warning", "Please select a room to delete.")

    def convert_to_qtime(self, value):
        if isinstance(value, str):
            return QTime.fromString(value[:5], "HH:mm")
        elif hasattr(value, 'seconds'):
            # It's a timedelta (convert seconds to hours and minutes)
            total_minutes = value.seconds // 60
            return QTime(total_minutes // 60, total_minutes % 60)
        elif hasattr(value, 'hour'):
            # It's likely a datetime.time
            return QTime(value.hour, value.minute)
        else:
            return QTime()  # default invalid time

    def handle_room_action(self, page_index):
        selected_room = self.ui.room_list.currentItem()
        self.index = page_index
        if not selected_room:
            QMessageBox.warning(self, "No Room Selected", "Please select a room first.")
            return
        self.selected_room =  selected_room.text()
        if selected_room is not None:
            if self.index == 2:
                self.load_schedule()
            elif self.index == 1:
                self.view_schedule()
            else:
                self.room_logs()
        self.open_roompage(self.index)

    def view_schedule(self):
        self.ui.accessed_room_sched_lineedit.setText(self.selected_room)
        table = self.ui.room_sched_table
        # Clear all cells except the time column (column 0)
        for row in range(table.rowCount()):
            for col in range(1, table.columnCount()):
                table.setItem(row, col, QTableWidgetItem(""))
        try:
            # Get the room_nameID from tupc_rooms using the selected room name
            room_name_query = "SELECT idroom_names FROM tupc_rooms WHERE room = %s"
            self.mycursor.execute(room_name_query, (self.selected_room,))
            result = self.mycursor.fetchone()

            if not result:
                QMessageBox.warning(self, "Error", f"Room '{self.selected_room}' not found in database.")
                return

            selected_room_id = result[0]  # Foreign key for room_schedule

            # Retrieve schedule details along with user's full name
            schedule_query = """
                SELECT rs.selected_day, rs.start_schedule, rs.end_schedule,
                    CONCAT(ua.First_Name, ' ', ua.Last_Name) AS full_name,
                    rs.subject_code_purpose
                FROM room_schedule rs
                INNER JOIN user_accounts ua ON rs.user_room_ID = ua.real_ID
                WHERE rs.selected_room_ID = %s
            """
            self.mycursor.execute(schedule_query, (selected_room_id,))
            schedule_data = self.mycursor.fetchall()

            # Map days to columns
            day_column_map = {
                "Monday": 1,
                "Tuesday": 2,
                "Wednesday": 3,
                "Thursday": 4,
                "Friday": 5
            }
            for day, start_time_db, end_time_db, user_name, purpose in schedule_data:
                day_col = day_column_map.get(day)
                if day_col is None:
                    continue

                start_time = self.convert_to_qtime(start_time_db)
                end_time = self.convert_to_qtime(end_time_db)

                # Fill the table rows
                for row in range(table.rowCount()):
                    row_time_item = table.item(row, 0)
                    if not row_time_item:
                        continue

                    row_time = QTime.fromString(row_time_item.text(), "HH:mm")
                    if row_time.isValid() and start_time <= row_time < end_time:
                        item = QTableWidgetItem(f"{user_name}:\n{purpose}")
                        table.setItem(row, day_col, item)

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def load_schedule(self):
        table = self.ui.edit_room_sched_table
        # Clear all cells except the time column (column 0)
        for row in range(table.rowCount()):
            for col in range(1, table.columnCount()):
                table.setItem(row, col, QTableWidgetItem(""))
        try:
            # Get the room_nameID from tupc_rooms using the selected room name
            room_name_query = "SELECT idroom_names FROM tupc_rooms WHERE room = %s"
            self.mycursor.execute(room_name_query, (self.selected_room,))
            result = self.mycursor.fetchone()

            if not result:
                QMessageBox.warning(self, "Error", f"Room '{self.selected_room}' not found in database.")
                return

            selected_room_id = result[0]  # Foreign key for room_schedule

            # Retrieve schedule details along with user's full name
            schedule_query = """
                SELECT rs.selected_day, rs.start_schedule, rs.end_schedule,
                    CONCAT(ua.First_Name, ' ', ua.Last_Name) AS full_name,
                    rs.subject_code_purpose
                FROM room_schedule rs
                INNER JOIN user_accounts ua ON rs.user_room_ID = ua.real_ID
                WHERE rs.selected_room_ID = %s AND ua.user_type IN ('instructor', 'staff')
            """
            self.mycursor.execute(schedule_query, (selected_room_id,))
            schedule_data = self.mycursor.fetchall()

            # Map days to columns
            day_column_map = {
                "Monday": 1,
                "Tuesday": 2,
                "Wednesday": 3,
                "Thursday": 4,
                "Friday": 5
            }
            for day, start_time_db, end_time_db, user_name, purpose in schedule_data:
                day_col = day_column_map.get(day)
                if day_col is None:
                    continue

                start_time = self.convert_to_qtime(start_time_db)
                end_time = self.convert_to_qtime(end_time_db)

                # Fill the table rows
                for row in range(table.rowCount()):
                    row_time_item = table.item(row, 0)
                    if not row_time_item:
                        continue

                    row_time = QTime.fromString(row_time_item.text(), "HH:mm")
                    if row_time.isValid() and start_time <= row_time < end_time:
                        item = QTableWidgetItem(f"{user_name}:\n{purpose}")
                        table.setItem(row, day_col, item)

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def check_students_if_added(self):
        self.selected_day = self.ui.instructor_day_edit_comboBox.currentText().strip()
        self.selected_time_start = self.ui.start_time_instructor.time()

        try:
            # Step 1: Get Room ID
            self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.selected_room,))
            room_id_result = self.mycursor.fetchone()
            if not room_id_result:
                QMessageBox.warning(self, "Error", "Selected room not found in database.")
                return
            selected_room_id = room_id_result[0]

            # Step 2: Convert QTime to Python datetime.time
            start_time_py = time(
                self.selected_time_start.hour(),
                self.selected_time_start.minute(),
                self.selected_time_start.second()
            )

            # Step 3: Query to check for students (user_type = 'student') with section_ID (to avoid matching instructor)
            self.mycursor.execute("""
                SELECT rs.user_room_ID
                FROM room_schedule rs
                JOIN user_accounts ua ON rs.user_room_ID = ua.real_ID
                WHERE rs.selected_day = %s
                AND rs.selected_room_ID = %s
                AND rs.start_schedule = %s
                AND ua.user_type = 'student'
                AND rs.section_ID IS NOT NULL
                LIMIT 1
            """, (
                self.selected_day,
                selected_room_id,
                start_time_py
            ))

            result = self.mycursor.fetchone()

            if result:
                return True
            else:
                return False

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
            return False

    def add_instructor_schedule(self):
        self.assigned_instructor = self.ui.assign_instructor.text()
        self.subject_code = self.ui.assign_subject.text()
        self.selected_day = self.ui.instructor_day_edit_comboBox.currentText()
        self.selected_time_start = self.ui.start_time_instructor.time()
        self.selected_time_end = self.ui.final_time_instructor.time()

        if not (self.assigned_instructor and self.subject_code):
            QMessageBox.warning(self, "Missing Information", "Please fill in all required fields.")
            return
        elif not self.selected_day:
            QMessageBox.warning(self, "Missing Information", "Please select a day.")
            return
        elif self.selected_time_start >= self.selected_time_end:
            QMessageBox.warning(self, "Invalid Time", "Start time must be before end time.")
            return

        result = self.check_students_if_added()
        if result is True:
            try:
                # Get room ID
                self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.selected_room,))
                room_id_result = self.mycursor.fetchone()
                if not room_id_result:
                    QMessageBox.warning(self, "Error", "Selected room not found in database.")
                    return
                selected_room_id = room_id_result[0]

                # Conflict check for instructors
                self.mycursor.execute("""
                    SELECT COUNT(*) FROM room_schedule
                    WHERE selected_room_ID = %s AND selected_day = %s AND section_ID IS NULL
                    AND (start_schedule < %s AND end_schedule > %s)
                """, (
                    selected_room_id,
                    self.selected_day,
                    self.selected_time_end.toString("HH:mm:ss"),
                    self.selected_time_start.toString("HH:mm:ss")
                ))
                (conflict_count,) = self.mycursor.fetchone()
                if conflict_count > 0:
                    QMessageBox.warning(self, "Schedule Conflict", "This time slot is already occupied.")
                    return

                # Get instructor ID
                self.mycursor.execute("""
                    SELECT real_ID FROM user_accounts
                    WHERE CONCAT(First_Name, ' ', Last_Name) = %s
                """, (self.assigned_instructor,))
                instructor_id_result = self.mycursor.fetchone()
                if not instructor_id_result:
                    QMessageBox.warning(self, "Error", "Instructor not found.")
                    return
                instructor_id = instructor_id_result[0]

                self.mycursor.execute("""
                    SELECT section_ID
                    FROM room_schedule
                    WHERE selected_day = %s
                    AND start_schedule = %s
                    AND selected_room_ID = %s
                    AND section_ID IS NOT NULL
                """, (
                    self.selected_day,
                    self.selected_time_start.toString("HH:mm:ss"),
                    selected_room_id
                ))
                section_result = self.mycursor.fetchone()
                print(section_result)
                # Insert instructor schedule
                self.mycursor.execute("""
                    INSERT INTO room_schedule 
                    (subject_code_purpose, selected_day, start_schedule, end_schedule, user_room_ID, selected_room_ID, section_ID)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.subject_code,
                    self.selected_day,
                    self.selected_time_start.toString("HH:mm:ss"),
                    self.selected_time_end.toString("HH:mm:ss"),
                    instructor_id,
                    selected_room_id,
                    section_result[0] if section_result else None
                ))
                self.mydb.commit()

                QMessageBox.information(self, "Success", "Instructor schedule saved.")
                self.clear_instructor_fields()
                self.load_schedule()

            except mysql.connector.Error as err:
                self.errorDisplay(err.errno, err.sqlstate, err.msg)
        else:
            QMessageBox.warning(self, "Error", "Students must be added to schedule before adding the instructor.")
            return

    def room_view(self):
        table_view = self.ui.edit_room_sched_table
        table_view.setColumnCount(6)
        table_view.setRowCount(14)
        table_view.setHorizontalHeaderLabels(["Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        for i in range(14):  # From 07:00 to 20:00
            hour = 7 + i
            time_str = QTime(hour, 0).toString("HH:mm")
            table_view.setItem(i, 0, QTableWidgetItem(time_str))

    def setup_schedule_table(self):
        table = self.ui.room_sched_table      
        table.setColumnCount(6)
        table.setRowCount(14)
        table.setHorizontalHeaderLabels(["Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        for i in range(14):  # From 07:00 to 20:00
            hour = 7 + i
            time_str = QTime(hour, 0).toString("HH:mm")
            table.setItem(i, 0, QTableWidgetItem(time_str))

    def add_staff_schedule(self):
        self.assigned_staff = self.ui.assign_staff.text()
        self.purpose = self.ui.assign_maintenance.text()
        self.selected_day_staff = self.ui.day_edit_staff.currentText()
        self.selected_time_start_staff = self.ui.start_time_staff.time()
        self.selected_time_end_staff = self.ui.final_time_staff.time()
        if not (self.assigned_staff and self.purpose):
            QMessageBox.warning(self, "Missing Information", "Please fill in all required fields.")
            return
        elif not self.selected_day_staff:
            QMessageBox.warning(self, "Missing Information", "Please select a day.")
            return
        elif self.selected_time_start >= self.selected_time_end:
            QMessageBox.warning(self, "Invalid Time", "Start time must be before end time.")
            return

        try:
            # Get selected_room_ID
            self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.selected_room,))
            room_id_result = self.mycursor.fetchone()
            if not room_id_result:
                QMessageBox.warning(self, "Error", "Selected room not found in database.")
                return
            selected_room_id = room_id_result[0]

            # Conflict check
            conflict_query = """
                SELECT COUNT(*) FROM room_schedule
                WHERE selected_room_ID = %s AND selected_day = %s AND section_ID IS NULL
                AND (start_schedule < %s AND end_schedule > %s)
            """
            self.mycursor.execute(conflict_query, (
                selected_room_id,
                self.selected_day_staff,
                self.selected_time_start_staff.toString("HH:mm"),
                self.selected_time_end_staff.toString("HH:mm")
            ))
            (conflict_count,) = self.mycursor.fetchone()
            if conflict_count > 0:
                QMessageBox.warning(self, "Schedule Conflict", "This time slot is already occupied.")
                return

            # Get staff real_ID
            self.mycursor.execute("""
                SELECT real_ID FROM user_accounts
                WHERE CONCAT(First_Name, ' ', Last_Name) = %s
            """, (self.assigned_staff,))
            staff_id_result = self.mycursor.fetchone()
            if not staff_id_result:
                QMessageBox.warning(self, "Error", "Staff member not found.")
                return
            staff_id = staff_id_result[0]

            # Insert schedule
            insert_query = """
                INSERT INTO room_schedule 
                (subject_code_purpose, selected_day, start_schedule, end_schedule, user_room_ID, section_ID, selected_room_ID)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            self.mycursor.execute(insert_query, (
                self.purpose,
                self.selected_day_staff,
                self.selected_time_start_staff.toString("HH:mm"),
                self.selected_time_end_staff.toString("HH:mm"),
                staff_id,
                None,
                selected_room_id
            ))
            self.mydb.commit()
            QMessageBox.information(self, "Success", "Staff schedule saved.")
            self.clear_staff_fields()
            self.load_schedule()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def sort_students(self):
        """Sort students based on the selected category."""
        category = self.ui.sort_student.currentText()  # ✅ Get the selected text correctly

        sorting_map = {
            "ID": 0,
            "First Name": 1,
            "Last Name": 2,
            "Email": 3,
            "Section": 4,
            "Course": 5,  
            "Year": 6
        }

        if category in sorting_map:
            self.ui.list_registered_stdnt.sortItems(sorting_map[category], Qt.AscendingOrder)

    def room_logs(self):
        self.ui.accessed_room_logs_lineedit.setText(self.selected_room)

    def search_students(self):
        """Search students based on input in the search bar."""
        query = self.search_bar_student.text().strip().lower()

        for row in range(self.student_table_widget.rowCount()):
            match = False
            for col in range(self.student_table_widget.columnCount()):
                item = self.student_table_widget.item(row, col)
                if item and query in item.text().strip().lower():
                    match = True
                    break
            self.student_table_widget.setRowHidden(row, not match)

    def reset_student_search(self):
        """Reset search filter when search bar is cleared."""
        if not self.search_bar_student.text().strip():
            for row in range(self.student_table_widget.rowCount()):
                self.student_table_widget.setRowHidden(row, False)

    def reset_instructor_search(self):
        """Reset the instructor table when the search bar is cleared."""
        search_text = self.ui.search_bar_instructor.text().strip()
        if not search_text:
            for row in range(self.instructor_table_widget.rowCount()):
                self.instructor_table_widget.setRowHidden(row, False)

    def search_instructor(self):
        """Search for an instructor by ID, First Name, Last Name, or Email."""
        search_text = self.ui.search_bar_instructor.text().strip().lower()

        if not search_text:
            QMessageBox.warning(self, "Warning", "Please enter a search term.")
            return

        found = False
        for row in range(self.instructor_table_widget.rowCount()):
            match_found = False
            for col in range(self.instructor_table_widget.columnCount()):
                item = self.instructor_table_widget.item(row, col)
                if item and search_text in item.text().strip().lower():
                    match_found = True
                    break  # No need to check other columns if there's a match

            self.instructor_table_widget.setRowHidden(row, not match_found)
            if match_found:
                found = True

        if not found:
            QMessageBox.information(self, "No Results", "No matching instructor found.")

    def load_students_into_table(self):
        """Load all students into the table widget."""
        self.ui.list_registered_stdnt.setRowCount(0)
        try:
            query = """
                SELECT 
                    ua.First_Name, 
                    ua.Last_Name, 
                    ua.email, 
                    ua.real_ID, 
                    ua.user_type, 
                    ua.is_change_password, 
                    s.course,
                    s.year,
                    s.section                  
                FROM section_junction sj
                JOIN user_accounts ua ON sj.student_ID = ua.real_ID
                JOIN section s ON sj.section_ID = s.sections_id
                WHERE user_type = 'student'
            """

            # Execute the query
            self.mycursor.execute(query)

            # Fetch all results
            self.users_data = self.mycursor.fetchall()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
        self.ui.list_registered_stdnt.setRowCount(len(self.users_data))
        self.ui.list_registered_stdnt.setColumnCount(7)
        self.ui.list_registered_stdnt.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email", "Section", "Course", "Year"])

        for row_index, row_data in enumerate(self.users_data):
            display_data = [
                row_data[3], # ID 
                row_data[0], # First name
                row_data[1], # Last name
                row_data[2], # Email
                row_data[6], # Course
                row_data[7], # Year
                row_data[8]  # Section
            ]
            
            for col_index, value in enumerate(display_data):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.list_registered_stdnt.setItem(row_index, col_index, item)

        self.ui.list_registered_stdnt.sortItems(0, Qt.AscendingOrder)

    def load_instructors_into_table(self):
        self.instructor_table_widget.setRowCount(0)
        try:
            query = """
                SELECT 
                    First_Name, 
                    Last_Name, 
                    email, 
                    real_ID                  
                FROM user_accounts 
                WHERE user_type = 'instructor'
            """

            # Execute the query
            self.mycursor.execute(query)

            # Fetch all results
            self.users_data = self.mycursor.fetchall()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
        self.instructor_table_widget.setRowCount(len(self.users_data))
        self.instructor_table_widget.setColumnCount(4)
        self.instructor_table_widget.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email"])
        for row_index, row_data in enumerate(self.users_data):
            display_data = [
                row_data[3], # ID 
                row_data[0], # First name
                row_data[1], # Last name
                row_data[2]  # Email
            ]
            
            for col_index, value in enumerate(display_data):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.instructor_table_widget.setItem(row_index, col_index, item)
        self.instructor_table_widget.sortItems(0, Qt.AscendingOrder)

    def sort_instructors(self):
        """Sort instructors based on the selected category."""
        category = self.ui.sort_instructor.currentText()
        sorting_map = {
            "ID": 0,
            "First Name": 1,
            "Last Name": 2,
            "Email": 3
        }
        
        if category in sorting_map:
            self.ui.list_registered_instructor.sortItems(sorting_map[category], Qt.AscendingOrder)

    def load_staffs_into_table(self):
        self.staff_table_widget.setRowCount(0)
        try:
            query = """
                SELECT 
                    First_Name, 
                    Last_Name, 
                    email, 
                    real_ID                  
                FROM user_accounts 
                WHERE user_type = 'staff'
            """

            # Execute the query
            self.mycursor.execute(query)

            # Fetch all results
            self.users_data = self.mycursor.fetchall()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
        self.staff_table_widget.setRowCount(len(self.users_data))
        self.staff_table_widget.setColumnCount(4)
        self.staff_table_widget.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email"])
        for row_index, row_data in enumerate(self.users_data):
            display_data = [
                row_data[3], # ID 
                row_data[0], # First name
                row_data[1], # Last name
                row_data[2]  # Email
            ]
            
            for col_index, value in enumerate(display_data):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.staff_table_widget.setItem(row_index, col_index, item)
        self.staff_table_widget.sortItems(0, Qt.AscendingOrder)

    def sort_staffs(self):
        """Sort staff members based on the selected category."""
        staff_sort_combo = self.ui.stackedWidget.widget(2).findChild(QComboBox, "sort_staff")

        if not staff_sort_combo:
            return  # Exit if the combo box is not found

        category = staff_sort_combo.currentText()
        sorting_map = {
            "ID": 0,
            "First Name": 1,
            "Last Name": 2,
            "Email": 3
        }

        if category in sorting_map:
            self.staff_table_widget.sortItems(sorting_map[category], Qt.AscendingOrder)
    
    def reset_staff_search(self):
        """Reset the staff table when the search bar is cleared."""
        search_bar_staff = self.ui.stackedWidget.widget(2).findChild(QLineEdit, "search_bar_staff")

        if not search_bar_staff:
            return  # Exit if search bar is not found

        search_text = search_bar_staff.text().strip()
        if not search_text:
            for row in range(self.staff_table_widget.rowCount()):
                self.staff_table_widget.setRowHidden(row, False)

    def search_staff(self):
        """Search for a staff member by ID, First Name, Last Name, or Email."""
        search_bar_staff = self.ui.stackedWidget.widget(2).findChild(QLineEdit, "search_bar_staff")

        if not search_bar_staff:
            return  # Exit if search bar is not found

        search_text = search_bar_staff.text().strip().lower()

        if not search_text:
            QMessageBox.warning(self, "Warning", "Please enter a search term.")
            return

        found = False
        for row in range(self.staff_table_widget.rowCount()):
            match_found = False
            for col in range(self.staff_table_widget.columnCount()):
                item = self.staff_table_widget.item(row, col)
                if item and search_text in item.text().strip().lower():
                    match_found = True
                    break  # Stop checking other columns if match found

            self.staff_table_widget.setRowHidden(row, not match_found)
            if match_found:
                found = True

        if not found:
            QMessageBox.information(self, "No Results", "No matching staff member found.")

    def open_manage_staff(self):
        dialog = StaffRegistration(parent=self, db_connection=self.mydb, db_cursor=self.mycursor)   
        dialog.exec()
        self.load_staffs_into_table()

    def open_manage_student(self):
        dialog = StudentRegistration(parent=self, db_connection=self.mydb, db_cursor=self.mycursor)
        dialog.exec()
        self.load_students_into_table()

    def open_manage_instructor(self):
        dialog = InstructorRegistration(parent=self, db_connection=self.mydb, db_cursor=self.mycursor)
        dialog.exec()  
        self.load_instructors_into_table()

    def open_roompage(self, index):
        self.ui.schedule_stackedwidget.setCurrentIndex(index)

    def return_roomview(self):
        self.ui.schedule_stackedwidget.setCurrentIndex(0)
        self.clear_instructor_fields()
        self.clear_staff_fields()

    def add_room(self):
        item = QListWidgetItem()
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        item.setText("Enter Room Name")
        item.setTextAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(12)
        item.setFont(font)

        self.ui.room_list.addItem(item)
        self.ui.room_list.setCurrentItem(item)
        self.ui.room_list.editItem(item)

    def open_add_student(self):
        self.assigned_instructor = self.ui.assign_instructor.text()
        self.subject_code = self.ui.assign_subject.text()
        self.selected_day = self.ui.instructor_day_edit_comboBox.currentText()
        self.selected_time_start = self.ui.start_time_instructor.time()
        self.selected_time_end = self.ui.final_time_instructor.time()
        if not self.subject_code:
            QMessageBox.warning(self, "Missing Subject", "Please select or input a subject code before adding students.")
            return

        elif not self.selected_time_start or not self.selected_time_end:
            QMessageBox.warning(self, "Missing Time", "Please set both start and end times before adding students.")
            return

        elif not self.selected_day:
            QMessageBox.warning(self, "Missing Day", "Please select a day before adding students.")
            return
        
        else:
            dialog = EditStudent(
                    subject_code=self.subject_code,
                    start_time=self.selected_time_start,
                    end_time=self.selected_time_end,
                    selected_day=self.selected_day,
                    room_name=self.selected_room,
                    assigned_instructor=self.assigned_instructor,
                    db_connection=self.mydb,
                    db_cursor=self.mycursor
                )
            dialog.exec()

    def open_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        self.new_window = None
        
    def edit_selected_schedule(self):
        self.clear_instructor_fields()
        self.clear_staff_fields()
        print('I have been accessed')
        item = self.ui.edit_room_sched_table.currentItem()

        if not item:
            QMessageBox.warning(self, "Error", "No schedule item selected.")
            return
         
        clicked_text = item.text().strip()

        if clicked_text == "":
            self.ui.change_instructor_sched.setDisabled(True)
            self.ui.change_staff_sched.setDisabled(True)
            self.ui.add_sched_instructor.setDisabled(False)
            self.ui.add_sched_staff.setDisabled(False)
            return

        # Split into full_name and subject_code_purpose
        if ":\n" in clicked_text:
            full_name, subject_code = clicked_text.split(":\n", 1)
            full_name = full_name.strip()
            subject_code = subject_code.strip()
        else:
            QMessageBox.warning(self, "Error", "Invalid cell format.")
            return
        col = item.column() # gets the day
        # The first column (0) is time — skip if user clicked there
        if col == 0:
            return

        day_column_map = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday"
        }
        selected_day = day_column_map.get(col)
        if not selected_day:
            return

        try:
            self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.selected_room,))
            room_id_result = self.mycursor.fetchone()
            if not room_id_result:
                QMessageBox.warning(self, "Error", "Selected room not found in database.")
                return
            self.selected_room_id = room_id_result[0]
            # Use selected_room_id and selected_day + time to locate the schedule entry
            query = """
                SELECT rs.subject_code_purpose, rs.start_schedule, 
                    rs.end_schedule, ua.user_type, CONCAT(ua.First_Name, ' ', ua.Last_Name) AS full_name
                FROM room_schedule rs
                JOIN user_accounts ua ON rs.user_room_ID = ua.real_ID
                WHERE rs.selected_day = %s 
                AND rs.subject_code_purpose = %s 
                AND CONCAT(ua.First_Name, ' ', ua.Last_Name) = %s 
                AND rs.selected_room_ID = %s
            """
            self.mycursor.execute(query, (
                selected_day,
                subject_code,
                full_name,
                self.selected_room_id
            ))
            schedule = self.mycursor.fetchone()

            if not schedule:
                QMessageBox.warning(self, "Error", "Schedule not found in the database.")
                return

            # Unpack data
            subject_code, start_time, end_time, user_type, full_name = schedule

            start_time_seconds = start_time.total_seconds()

            # Get hours and minutes from total seconds
            start_hours = int(start_time_seconds // 3600)
            start_minutes = int((start_time_seconds % 3600) // 60)

            # Similarly for end_time
            end_time_seconds = end_time.total_seconds()
            end_hours = int(end_time_seconds // 3600)
            end_minutes = int((end_time_seconds % 3600) // 60)

            self.original_day = selected_day
            self.original_subject_code = subject_code

            if user_type == "instructor":
                self.ui.change_instructor_sched.setDisabled(False)
                self.ui.add_sched_instructor.setDisabled(True)
                self.ui.assign_instructor.setText(full_name)
                self.ui.assign_subject.setText(subject_code)
                self.ui.instructor_day_edit_comboBox.setCurrentText(selected_day)
                self.ui.start_time_instructor.setTime(QTime(start_hours, start_minutes))
                self.ui.final_time_instructor.setTime(QTime(end_hours, end_minutes))

            elif user_type == "staff":
                self.ui.change_staff_sched.setDisabled(False)
                self.ui.add_sched_staff.setDisabled(True)
                self.ui.assign_staff.setText(full_name)
                self.ui.assign_maintenance.setText(subject_code)
                self.ui.day_edit_staff.setCurrentText(selected_day)
                self.ui.start_time_staff.setTime(QTime(start_hours, start_minutes))
                self.ui.final_time_staff.setTime(QTime(end_hours, end_minutes))

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def clear_instructor_fields(self):
        self.ui.assign_instructor.clear()
        self.ui.assign_subject.clear()
        self.ui.instructor_day_edit_comboBox.setCurrentIndex(0)
        self.ui.start_time_instructor.setTime(QTime(0, 0))
        self.ui.final_time_instructor.setTime(QTime(0, 0))

    def clear_staff_fields(self):
        self.ui.assign_staff.clear()
        self.ui.assign_maintenance.clear()
        self.ui.day_edit_staff.setCurrentIndex(0)
        self.ui.start_time_staff.setTime(QTime(0, 0))
        self.ui.final_time_staff.setTime(QTime(0, 0))

    def timedelta_to_string(self, td):
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def change_schedule(self, user):
        try:
            if user == 'instructor':
                # Step 1: Get new values from the UI
                new_day = self.ui.instructor_day_edit_comboBox.currentText()
                new_start_qtime = self.ui.start_time_instructor.time()
                new_end_qtime = self.ui.final_time_instructor.time()
                stuff = self.ui.assign_subject.text().strip()
                full_name = self.ui.assign_instructor.text().strip()

                new_start_str = new_start_qtime.toString("HH:mm:ss")
                new_end_str = new_end_qtime.toString("HH:mm:ss")

            else:  # For staff
                new_day = self.ui.day_edit_staff.currentText()
                new_start_qtime = self.ui.start_time_staff.time()
                new_end_qtime = self.ui.final_time_staff.time()
                stuff = self.ui.assign_maintenance.text().strip()
                full_name = self.ui.assign_staff.text().strip()

                new_start_str = new_start_qtime.toString("HH:mm:ss")
                new_end_str = new_end_qtime.toString("HH:mm:ss")

            if new_start_qtime >= new_end_qtime:         
                QMessageBox.warning(self, "Invalid Time", "Start time must be before end time.")
                return

            # Step 2: Get user ID
            with self.mydb.cursor(buffered=True) as cursor_user:
                cursor_user.execute("""
                    SELECT real_ID FROM user_accounts 
                    WHERE CONCAT(First_Name, ' ', Last_Name) = %s
                """, (full_name,))
                result = cursor_user.fetchone()
            if not result:
                QMessageBox.warning(self, "Error", "User not found.")
                return
            user_id = result[0]

            with self.mydb.cursor(buffered=True) as cursor_original:
                cursor_original.execute("""
                    SELECT selected_day, subject_code_purpose, start_schedule, end_schedule
                    FROM room_schedule
                    WHERE selected_room_ID = %s AND user_room_ID = %s
                    LIMIT 1
                """, (self.selected_room_id, user_id))
                original_data = cursor_original.fetchone()

            if original_data:
                self.original_day = original_data[0]
                self.original_subject_code = original_data[1]
                self.original_start_time = self.timedelta_to_string(original_data[2])
                self.original_end_time = self.timedelta_to_string(original_data[3])

            original_start_str = self.original_start_time
            original_end_str = self.original_end_time
            # Step 3: Get section ID (for instructor only) from a scheduled student
            section_id = None
            if user == 'instructor':
                with self.mydb.cursor(buffered=True) as cursor_section:
                    cursor_section.execute("""
                        SELECT rs.section_ID 
                        FROM room_schedule rs
                        JOIN section_junction sj ON rs.user_room_ID = sj.student_ID
                        WHERE rs.selected_day = %s 
                        AND rs.subject_code_purpose = %s
                        AND rs.selected_room_ID = %s
                        AND rs.start_schedule = %s
                        AND rs.end_schedule = %s
                        LIMIT 1
                    """, (
                        self.original_day,
                        self.original_subject_code,
                        self.selected_room_id,
                        original_start_str,
                        original_end_str
                    ))
                    section_result = cursor_section.fetchone()
                    if section_result:
                        section_id = section_result[0]

            # Step 4: Update the instructor or staff's schedule
            with self.mydb.cursor() as cursor_update:
                cursor_update.execute("""
                    UPDATE room_schedule 
                    SET selected_day = %s, start_schedule = %s, end_schedule = %s, 
                        subject_code_purpose = %s, user_room_ID = %s 
                    WHERE selected_day = %s AND subject_code_purpose = %s 
                    AND selected_room_ID = %s AND user_room_ID = %s
                """, (
                    new_day, new_start_str, new_end_str, stuff, user_id,
                    self.original_day, self.original_subject_code,
                    self.selected_room_id, user_id
                ))

            # Step 5: Update all students tied to this section
            if user == 'instructor' and section_id is not None:
                with self.mydb.cursor() as cursor_update_students:
                    cursor_update_students.execute("""
                        UPDATE room_schedule rs
                        JOIN section_junction sj ON rs.user_room_ID = sj.student_ID
                        SET rs.selected_day = %s,
                            rs.start_schedule = %s,
                            rs.end_schedule = %s,
                            rs.subject_code_purpose = %s,
                            rs.selected_room_ID = %s
                        WHERE sj.section_ID = %s
                        AND rs.section_ID = sj.section_ID
                        AND rs.selected_day = %s
                        AND rs.start_schedule = %s
                        AND rs.end_schedule = %s
                        AND rs.subject_code_purpose = %s
                        AND rs.selected_room_ID = %s
                    """, (
                        new_day, new_start_str, new_end_str, stuff, self.selected_room_id,
                        section_id,
                        self.original_day, original_start_str, original_end_str,
                        self.original_subject_code,
                        self.selected_room_id
                    ))

            # Step 6: Commit and refresh
            self.mydb.commit()
            QMessageBox.information(self, "Success", "Schedule updated successfully.")

            self.load_schedule()
            self.clear_instructor_fields()
            self.clear_staff_fields()
            self.ui.change_instructor_sched.setDisabled(True)
            self.ui.change_staff_sched.setDisabled(True)
            self.ui.add_sched_instructor.setDisabled(False)
            self.ui.add_sched_staff.setDisabled(False)

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def remove_instructor_schedule(self):
        self.assigned_instructor = self.ui.assign_instructor.text()
        self.subject_code = self.ui.assign_subject.text()
        self.selected_day = self.ui.instructor_day_edit_comboBox.currentText()
        
        # Convert QTime to string (MySQL-compatible)
        self.selected_time_start = self.ui.start_time_instructor.time().toString("HH:mm:ss")
        self.selected_time_end = self.ui.final_time_instructor.time().toString("HH:mm:ss")

        if not (self.assigned_instructor and self.subject_code):
            QMessageBox.warning(self, "Missing Information", "Please fill in all required fields.")
            return
        elif not self.selected_day:
            QMessageBox.warning(self, "Missing Information", "Please select a day.")
            return

        try:
            # Check instructor
            self.mycursor.execute("""
                SELECT real_ID FROM user_accounts
                WHERE CONCAT(First_Name, ' ', Last_Name) = %s
            """, (self.assigned_instructor,))
            instructor_id_result = self.mycursor.fetchone()
            if not instructor_id_result:
                QMessageBox.warning(self, "Error", "Instructor not found.")
                return
            
            #Check if in schedule
            search_query = """
            SELECT room_id
            FROM room_schedule
            WHERE user_room_ID = %s AND start_schedule = %s AND end_schedule = %s AND selected_day = %s        
            """
            self.mycursor.execute(search_query, (instructor_id_result[0], 
                    self.selected_time_start, 
                    self.selected_time_end, 
                    self.selected_day))
            
            schedule = self.mycursor.fetchone()
            if not schedule:
                QMessageBox.warning(self, "Error", "Instructor is not scheduled for this time.")
                return

            # Get room ID
            self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.selected_room,))
            room_result = self.mycursor.fetchone()
            if not room_result:
                QMessageBox.warning(self, "Error", "Selected room not found.")
                return

            self.selected_room_id = room_result[0]

            # Delete everyone (instructor + students) with same room, day, and time
            delete_query = """
                DELETE FROM room_schedule 
                WHERE selected_day = %s AND start_schedule = %s AND end_schedule = %s AND selected_room_ID = %s
            """
            self.mycursor.execute(delete_query, (
                self.selected_day,
                self.selected_time_start,
                self.selected_time_end,
                self.selected_room_id
            ))
            self.mydb.commit()

            QMessageBox.information(self, "Success", "Instructor and associated students have been removed from the schedule.")

            # Optional: Clear fields and refresh views
            self.clear_instructor_fields()
            self.load_schedule()
            self.ui.add_sched_instructor.setDisabled(False)

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def remove_staff_schedule(self):
        self.staff_name = self.ui.assign_staff.text()
        self.staff_purpose = self.ui.assign_maintenance.text()
        self.selected_day = self.ui.day_edit_staff.currentText()
        self.start_staff = self.ui.start_time_staff.time().toString("HH:mm:ss")
        self.end_staff = self.ui.final_time_staff.time().toString("HH:mm:ss")

        if not (self.staff_name and self.staff_purpose):
            QMessageBox.warning(self, "Missing Information", "Please fill in all required fields.")
            return
        elif not self.selected_day:
            QMessageBox.warning(self, "Missing Information", "Please select a day.")
            return
 
        try:
            # Check staff
            self.mycursor.execute("""
                SELECT real_ID FROM user_accounts
                WHERE CONCAT(First_Name, ' ', Last_Name) = %s
            """, (self.staff_name,))
            staff_result = self.mycursor.fetchone()
            if not staff_result:
                QMessageBox.warning(self, "Error", "Instructor not found.")
                return

            # Get room ID
            self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.selected_room,))
            room_result = self.mycursor.fetchone()
            if not room_result:
                QMessageBox.warning(self, "Error", "Selected room not found.")
                return

            self.selected_room_id = room_result[0]

            # Delete staff
            delete_query = """
                DELETE FROM room_schedule 
                WHERE selected_day = %s AND start_schedule = %s AND end_schedule = %s AND selected_room_ID = %s
            """
            self.mycursor.execute(delete_query, (
                self.selected_day,
                self.start_staff,
                self.end_staff,
                self.selected_room_id
            ))
            self.mydb.commit()

            QMessageBox.information(self, "Success", "Staff has been removed from the schedule.")

            # Optional: Clear fields and refresh views
            self.clear_staff_fields()
            self.load_schedule()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    # def open_logout(self):
    #     self.switch_window(MainWindow)

    def switch_window(self, new_window_class):
        self.new_window = new_window_class()
        self.new_window.show()
        self.close()
    
    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(self, "Database Error", error_message)


class StaffRegistration(QDialog):
    def __init__(self, db_connection, db_cursor, parent=None):
        super().__init__(parent)  # Ensures it stays on top of the main window

        self.ui = StaffRegistrationUi()
        self.ui.setupUi(self)

        self.mydb = db_connection
        self.mycursor = db_cursor
        
        self.ui.sort_instructor.clear()
        self.ui.sort_instructor.addItems(["ID", "First Name", "Last Name", "Email"])

        self.ui.sort_instructor.currentIndexChanged.connect(self.sort_staff)

        self.staff_table_widget = self.ui.list_registered_staff
        self.ui.search_staff_btn.clicked.connect(self.search_staff)
        self.ui.search_bar_staff.textChanged.connect(self.reset_staff_search)

        self.ui.pass_generate_staff.clicked.connect(self.generate_default_password)
        self.ui.save_staff_btn.clicked.connect(self.register_staff)
    
        remove_tab = self.ui.tabWidget_instructor.widget(1)
        
        self.firstname = remove_tab.findChild(QLineEdit, "first_name_lineedit_remove_staff")
        self.lastname = remove_tab.findChild(QLineEdit, "last_name_lineedit_remove_staff")
        self.idnumber = remove_tab.findChild(QLineEdit, "ID_staff_remove")

        self.removestaff_btn = remove_tab.findChild(QPushButton, "del_staff_inlist")
        self.removestaff_btn.clicked.connect(self.remove_staff)

        # Initialize TableWidget
        self.setup_table()
        self.load_user_data()
        self.load_staffs_into_table()

    def load_user_data(self):
        try:
            query = """
                SELECT 
                    First_Name, 
                    Last_Name, 
                    email, 
                    real_ID                  
                FROM user_accounts 
                WHERE user_type = 'staff'
            """

            # Execute the query
            self.mycursor.execute(query)

            # Fetch all results
            self.users_data = self.mycursor.fetchall()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def reset_staff_search(self):
        """Reset the instructor table when the search bar is cleared."""
        search_text = self.ui.search_bar_instructor.text().strip()
        if not search_text:
            for row in range(self.staff_table_widget.rowCount()):
                self.staff_table_widget.setRowHidden(row, False)


    def search_staff(self):
        """Search for an instructor by ID, First Name, Last Name, or Email."""
        search_text = self.ui.search_bar_staff.text().strip().lower()

        if not search_text:
            QMessageBox.warning(self, "Warning", "Please enter a search term.")
            return

        found = False
        for row in range(self.staff_table_widget.rowCount()):
            match_found = False
            for col in range(self.staff_table_widget.columnCount()):
                item = self.staff_table_widget.item(row, col)
                if item and search_text in item.text().strip().lower():
                    match_found = True
                    break  # No need to check other columns if there's a match

            self.staff_table_widget.setRowHidden(row, not match_found)
            if match_found:
                found = True

        if not found:
            QMessageBox.information(self, "No Results", "No matching instructor found.")
            
    def sort_instructors(self):
        """Sort instructors based on the selected category."""
        category = self.ui.sort_instructor.currentText()
        sorting_map = {
            "ID": 0,
            "First Name": 1,
            "Last Name": 2,
            "Email": 3
        }
        
        if category in sorting_map:
            self.ui.list_registered_staff.sortItems(sorting_map[category], Qt.AscendingOrder)

    def setup_table(self):
        """Setup table columns."""
        self.ui.list_registered_staff.setColumnCount(4)
        self.ui.list_registered_staff.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email"])

    def load_staffs_into_table(self):
        """Load all instructors into the table widget."""
        self.ui.list_registered_staff.setRowCount(len(self.users_data))
        for row_index, row_data in enumerate(self.users_data):
            display_data = [
                row_data[3], # ID 
                row_data[0], # First name
                row_data[1], # Last name
                row_data[2]  # Email
            ]
            
            for col_index, value in enumerate(display_data):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.list_registered_staff.setItem(row_index, col_index, item)
        self.ui.list_registered_staff.sortItems(0, Qt.AscendingOrder)

    def generate_default_password(self):
        """Generate a default password."""
        default_password = "Staff123"
        self.ui.password_staff_reg.setText(default_password)

    def sort_staff(self):
        """Sort instructors based on the selected category."""
        category = self.ui.sort_instructor.currentText()
        sorting_map = {
            "ID": 0,
            "First Name": 1,
            "Last Name": 2,
            "Email": 3
        }
        
        if category in sorting_map:
            self.ui.list_registered_staff.sortItems(sorting_map[category], Qt.AscendingOrder)

    def register_staff(self):
        first_name = self.ui.first_name_lineedit_staff.text().strip()
        last_name = self.ui.lastname_lineedit_staff.text().strip()
        email = self.ui.email_staff_lineedit.text().strip()
        staff_id = self.ui.ID_staff.text().strip()
        password = self.ui.password_staff_reg.text().strip()

        if not (first_name and last_name and email and staff_id and password):
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return

        try:
            self.mycursor.execute("SELECT COUNT(*) FROM user_accounts WHERE real_ID = %s", (staff_id,))
            if self.mycursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Error", "Staff ID already exists!")
                return         
            
            sql_columns_inst = "INSERT INTO user_accounts (First_Name, Last_Name, email, password, real_ID, user_type, is_change_password) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = [first_name, last_name, email, password, staff_id, 'staff', 0]

            self.mycursor.execute(sql_columns_inst, values)
            self.mydb.commit()
           
            QMessageBox.information(self, "Success", "Staff registered successfully!")
            self.clear_fields()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

        # Refresh registration table
        self.load_user_data()
        self.load_staffs_into_table()

    def remove_staff(self):
        """Remove a student using First Name, Last Name, or ID"""
        first_name = self.firstname.text().strip()
        last_name = self.lastname.text().strip()
        id_number = self.idnumber.text().strip()

        if not first_name and not last_name and not id_number:
            QMessageBox.warning(self, "Error", "Please enter First Name, Last Name, or ID Number to remove.")
            return
        
        try:
            delete_section_sql = """
                DELETE FROM user_accounts WHERE First_Name = %s AND Last_Name = %s AND real_ID = %s
            """
            self.mycursor.execute(delete_section_sql, (first_name, last_name, id_number))

            self.mydb.commit()

            QMessageBox.information(self, "Success", "Staff removed successfully.")

            # Refresh UI
            self.load_user_data()
            self.load_staffs_into_table()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
        
        self.clear_remove_fields()

    def clear_remove_fields(self):
        """Clear input fields after removal"""
        self.firstname.clear()
        self.lastname.clear()
        self.idnumber.clear()

    def clear_fields(self):
        """Clear input fields after successful registration."""
        self.ui.first_name_lineedit_staff.clear()
        self.ui.lastname_lineedit_staff.clear()
        self.ui.email_staff_lineedit.clear()
        self.ui.ID_staff.clear()
        self.ui.password_staff_reg.clear()
    
    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(self, "Database Error", error_message)


class InstructorRegistration(QDialog):
    def __init__(self, db_connection, db_cursor, parent=None):
        super().__init__(parent)

        self.ui = InstructorRegistrationUi()
        self.ui.setupUi(self)
        
        self.mydb = db_connection
        self.mycursor = db_cursor

        self.ui.sort_instructor.currentIndexChanged.connect(self.sort_instructors)

        self.ui.sort_instructor.clear()
        self.ui.sort_instructor.addItems(["ID", "First Name", "Last Name", "Email"])

        self.ui.pass_generate_instructor.clicked.connect(self.generate_default_password)
        self.ui.save_instructor_btn.clicked.connect(self.register_instructor)

        self.instructor_table_widget = self.ui.list_registered_instructor
        self.ui.search_instructor_btn.clicked.connect(self.search_instructor)
        self.ui.search_bar_instructor.textChanged.connect(self.reset_instructor_search)

        remove_tab = self.ui.tabWidget_instructor.widget(1)

        # Find the correct QLineEdit widgets for instructor removal
        self.firstname = remove_tab.findChild(QLineEdit, "first_name_lineedit_remove_instructor_3")
        self.lastname = remove_tab.findChild(QLineEdit, "last_name_lineedit_remove_instructor_3")
        self.idnumber = remove_tab.findChild(QLineEdit, "ID_instructor_remove")

        # Find and connect remove button
        self.removeinstructor_btn = remove_tab.findChild(QPushButton, "del_instructor_inlist_3")
        self.removeinstructor_btn.clicked.connect(self.remove_instructor)

        self.setup_table()
        self.load_user_data()
        self.load_instructors_into_table()

    def load_user_data(self):
        try:
            query = """
                SELECT 
                    First_Name, 
                    Last_Name, 
                    email, 
                    real_ID                  
                FROM user_accounts 
                WHERE user_type = 'instructor'
            """

            # Execute the query
            self.mycursor.execute(query)

            # Fetch all results
            self.users_data = self.mycursor.fetchall()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def reset_instructor_search(self):
        """Reset the instructor table when the search bar is cleared."""
        search_text = self.ui.search_bar_instructor.text().strip()
        if not search_text:
            for row in range(self.instructor_table_widget.rowCount()):
                self.instructor_table_widget.setRowHidden(row, False)


    def search_instructor(self):
        """Search for an instructor by ID, First Name, Last Name, or Email."""
        search_text = self.ui.search_bar_instructor.text().strip().lower()

        if not search_text:
            QMessageBox.warning(self, "Warning", "Please enter a search term.")
            return

        found = False
        for row in range(self.instructor_table_widget.rowCount()):
            match_found = False
            for col in range(self.instructor_table_widget.columnCount()):
                item = self.instructor_table_widget.item(row, col)
                if item and search_text in item.text().strip().lower():
                    match_found = True
                    break  # No need to check other columns if there's a match

            self.instructor_table_widget.setRowHidden(row, not match_found)
            if match_found:
                found = True

        if not found:
            QMessageBox.information(self, "No Results", "No matching instructor found.")
            
    def sort_instructors(self):
        """Sort instructors based on the selected category."""
        category = self.ui.sort_instructor.currentText()
        sorting_map = {
            "ID": 0,
            "First Name": 1,
            "Last Name": 2,
            "Email": 3
        }
        
        if category in sorting_map:
            self.ui.list_registered_instructor.sortItems(sorting_map[category], Qt.AscendingOrder)

    def setup_table(self):
        """Setup table columns."""
        self.ui.list_registered_instructor.setColumnCount(4)
        self.ui.list_registered_instructor.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email"])

    def load_instructors_into_table(self):
        """Load all instructors into the table widget."""
        self.ui.list_registered_instructor.setRowCount(len(self.users_data))
        for row_index, row_data in enumerate(self.users_data):
            display_data = [
                row_data[3], # ID 
                row_data[0], # First name
                row_data[1], # Last name
                row_data[2]  # Email
            ]
            
            for col_index, value in enumerate(display_data):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.list_registered_instructor.setItem(row_index, col_index, item)
        self.ui.list_registered_instructor.sortItems(0, Qt.AscendingOrder)

    def generate_default_password(self):
        """Generate a default password."""
        default_password = "Instructor123"
        self.ui.password_instructor_reg.setText(default_password)

    def register_instructor(self):
        first_name = self.ui.first_name_lineedit_instructor.text().strip()
        last_name = self.ui.lastname_lineedit_instructor.text().strip()
        email = self.ui.email_instructor_lineedit.text().strip()
        instructor_id = self.ui.ID_instructor.text().strip()
        password = self.ui.password_instructor_reg.text().strip()

        if not (first_name and last_name and email and instructor_id and password):
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return

        try:
            self.mycursor.execute("SELECT COUNT(*) FROM user_accounts WHERE real_ID = %s", (instructor_id,))
            if self.mycursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Error", "Instructor ID already exists!")
                return         
            
            sql_columns_inst = "INSERT INTO user_accounts (First_Name, Last_Name, email, password, real_ID, user_type, is_change_password) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = [first_name, last_name, email, password, instructor_id, 'instructor', 0]

            self.mycursor.execute(sql_columns_inst, values)
            self.mydb.commit()
           
            QMessageBox.information(self, "Success", "Instructor registered successfully!")
            self.clear_fields()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

        # Refresh registration table
        self.load_user_data()
        self.load_instructors_into_table()

    def remove_instructor(self):
        """Remove a student using First Name, Last Name, or ID"""
        first_name = self.firstname.text().strip()
        last_name = self.lastname.text().strip()
        id_number = self.idnumber.text().strip()

        if not first_name and not last_name and not id_number:
            QMessageBox.warning(self, "Error", "Please enter First Name, Last Name, or ID Number to remove.")
            return
        
        try:
            delete_section_sql = """
                DELETE FROM user_accounts WHERE First_Name = %s AND Last_Name = %s AND real_ID = %s
            """
            self.mycursor.execute(delete_section_sql, (first_name, last_name, id_number))

            self.mydb.commit()

            QMessageBox.information(self, "Success", "Instructor removed successfully.")

            # Refresh UI
            self.load_user_data()
            self.load_instructors_into_table()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
        self.clear_fields()

    def clear_remove_fields(self):
        """Clear input fields after removal"""
        self.firstname.clear()
        self.lastname.clear()
        self.idnumber.clear()

    def clear_fields(self):
        """Clear input fields after successful registration."""
        self.ui.first_name_lineedit_instructor.clear()
        self.ui.lastname_lineedit_instructor.clear()
        self.ui.email_instructor_lineedit.clear()
        self.ui.ID_instructor.clear()
        self.ui.password_instructor_reg.clear()
    
    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(self, "Database Error", error_message)


class StudentRegistration(QDialog):
    def __init__(self, db_connection, db_cursor, parent=None):
        super().__init__(parent)

        self.ui = StudentRegistrationUi()
        self.ui.setupUi(self)

        self.mydb = db_connection
        self.mycursor = db_cursor
    
        self.ui.sort_student.clear()
        self.ui.sort_student.addItems(["ID", "First Name", "Last Name", "Email", "Section", "Course", "Year"])

        self.ui.sort_sections.clear()
        self.ui.sort_sections.addItems(["Section", "Course", "Year"])

        self.ui.sort_student.currentIndexChanged.connect(self.sort_students)

        student_tab = self.ui.edit_tab.widget(1)
        self.sort_student_combo = student_tab.findChild(QComboBox, "sort_student")
        self.search_student_btn = student_tab.findChild(QPushButton, "search_student_btn")
        self.search_bar_student = student_tab.findChild(QLineEdit, "search_bar_stdnt")
        self.student_table_widget = student_tab.findChild(QTableWidget, "list_registered_stdnt")

        self.search_student_btn.clicked.connect(self.search_students)
        self.search_bar_student.textChanged.connect(self.reset_student_search)

        section_tab = self.ui.edit_tab.widget(0)  # Get the first ta
        self.sort_sections_combo = section_tab.findChild(QComboBox, "sort_sections")
        self.search_sections_btn = section_tab.findChild(QPushButton, "search_sections_btn")
        self.list_sections = section_tab.findChild(QTableWidget, "list_sections")
        self.search_bar_sections = section_tab.findChild(QLineEdit, "search_bar_sections")  # ✅ Fix this

        self.ui.sort_sections.currentIndexChanged.connect(self.sort_sections)
        self.ui.search_sections_btn.clicked.connect(self.search_sections)
        self.ui.search_bar_sections.textChanged.connect(self.reset_section_search)


        self.stdnt_table_widget = self.ui.list_registered_stdnt

        self.ui.pass_generate_stdnt.clicked.connect(self.generate_default_password)
        self.ui.save_send_stdnt_cred.clicked.connect(self.register_student)

        remove_tab = self.ui.tabWidget_student.widget(1)
        self.firstname = remove_tab.findChild(QLineEdit, "first_name_lineedit_remove")
        self.lastname = remove_tab.findChild(QLineEdit, "last_name_lineedit_remove")
        self.idnumber = remove_tab.findChild(QLineEdit, "tupc_id_remove_lineedit")

        self.removestudent_btn = remove_tab.findChild(QPushButton, "del_student_inlist")
        self.removestudent_btn.clicked.connect(self.remove_student)

        self.list_sections_remove = remove_tab.findChild(QListWidget, "list_sections_register_3")
        self.remove_stdnts_in_section_from_system = remove_tab.findChild(QPushButton, "remove_stdnts_in_section_from_system")
        self.remove_stdnts_in_section_from_system.clicked.connect(self.remove_students_by_section)

        self.ui.remove_section.clicked.connect(self.remove_section)


        self.ui.add_section.clicked.connect(self.add_section)  # Connect button to method
        self.load_section_data()
        self.load_sections_into_list()

        # Initialize TableWidget
        self.load_user_data()
        self.setup_table()
        self.load_students_into_table() 

    def load_user_data(self):
        try:
            query = """
                SELECT 
                    ua.First_Name, 
                    ua.Last_Name, 
                    ua.email, 
                    ua.real_ID, 
                    ua.user_type, 
                    ua.is_change_password, 
                    s.course,
                    s.year,
                    s.section                  
                FROM section_junction sj
                JOIN user_accounts ua ON sj.student_ID = ua.real_ID
                JOIN section s ON sj.section_ID = s.sections_id
                WHERE user_type = 'student'
            """

            # Execute the query
            self.mycursor.execute(query)

            # Fetch all results
            self.users_data = self.mycursor.fetchall()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
        

    def load_sections_into_remove_list(self):
        """Load sections into the removal list."""
        sections = self.load_section_data()
        self.list_sections_remove.clear()
        self.list_sections_remove.addItems(sections)

    def load_sections_into_list(self):
        """Load and sort sections before displaying them."""
        self.ui.list_sections.clear()

        sections = self.load_section_data()
        sorted_sections = sorted(sections)  # Alphabetical sorting

        self.ui.list_sections.addItems(sorted_sections)


    def remove_section(self):
        """Remove a section and all associated students."""
        selected_section_item = self.ui.list_sections.currentItem()
        
        if not selected_section_item:
            QMessageBox.warning(self, "Error", "Please select a section to remove.")
            return

        section_text = selected_section_item.text().strip()  # Example: "BSIT - 1A"
        try:
            course, year_section = section_text.split(" - ")
            year = year_section[0]  # e.g. "1"
            section = year_section[1:]  # e.g. "A"
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid section format.")
            return

        confirm = QMessageBox.question(
            self, "Confirm Deletion", 
            f"Are you sure you want to remove section {section_text} and all associated students?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm != QMessageBox.Yes:
            return

        try:
            # Step 1: Get section_id
            self.mycursor.execute(
                "SELECT sections_id FROM section WHERE course = %s AND year = %s AND section = %s",
                (course, year, section)
            )
            result = self.mycursor.fetchone()

            if not result:
                QMessageBox.warning(self, "Error", "Section not found in the database.")
                return

            section_id = result[0]

            # Step 2: Get all student_ids associated with this section
            self.mycursor.execute(
                "SELECT student_ID FROM section_junction WHERE section_id = %s",
                (section_id,)
            )
            student_ids = self.mycursor.fetchall()
            student_ids_flat = [sid[0] for sid in student_ids]

            if student_ids_flat:
                # Step 3: Delete from student_section
                self.mycursor.execute(
                    "DELETE FROM section_junction WHERE section_ID = %s",
                    (section_id,)
                )

                # Step 4: Delete from user_accounts
                format_strings = ','.join(['%s'] * len(student_ids_flat))
                self.mycursor.execute(
                    f"DELETE FROM user_accounts WHERE real_ID IN ({format_strings})",
                    tuple(student_ids_flat)
                )

            # Step 5: Delete the section
            self.mycursor.execute(
                "DELETE FROM section WHERE sections_id = %s",
                (section_id,)
            )

            self.mydb.commit()

            QMessageBox.information(self, "Success", f"Section '{section_text}' and its students have been removed.")

            # Refresh UI
            self.load_section_data()
            self.load_sections_into_list()
            self.load_user_data()
            self.load_students_into_table()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def reset_section_search(self):
        section_tab = self.ui.edit_tab.widget(0)
        self.list_sections = section_tab.findChild(QTableWidget, "list_sections")
        self.search_bar_sections = section_tab.findChild(QLineEdit, "search_bar_sections")

        if not self.list_sections or not self.search_bar_sections:
            print("Error: list_sections or search_bar_sections not found!")
            return

        self.search_bar_sections.clear()

        for row in range(self.list_sections.rowCount()):
            self.list_sections.setRowHidden(row, False)

    def search_section(self):
        """Filter the section list based on search input."""
        search_text = self.ui.search_section_input.text().strip().lower()
        self.ui.list_sections.clear()

        sections = self.load_section_data()
        filtered_sections = [sec for sec in sections if search_text in sec.lower()]

        self.ui.list_sections.addItems(filtered_sections)

    def remove_students_by_section(self):
        """Remove all students in the selected section from the SQL database."""
        selected_section_item = self.ui.list_sections_register_3.currentItem()

        if not selected_section_item:
            QMessageBox.warning(self, "Error", "Please select a section to remove students from.")
            return

        section_text = selected_section_item.text().strip()  # e.g., "BET-COET - 2A"

        try:
            course, section_year = section_text.split(" - ")
            year = section_year[0]
            section = section_year[1]
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid section format. Please contact admin.")
            return

        try:
            # Step 1: Get section_id
            self.mycursor.execute(
                "SELECT sections_id FROM section WHERE course = %s AND year = %s AND section = %s",
                (course, year, section)
            )
            result = self.mycursor.fetchone()

            if not result:
                QMessageBox.information(self, "Info", "No such section found in the database.")
                return

            section_id = result[0]

            # Step 2: Get all student_ids in that section
            self.mycursor.execute(
                "SELECT student_ID FROM section_junction WHERE section_id = %s",
                (section_id,)
            )
            student_ids = self.mycursor.fetchall()

            if not student_ids:
                QMessageBox.information(self, "Info", "No students found in the selected section.")
                return

            # Step 3: Confirm deletion
            confirm = QMessageBox.question(
                self, "Confirm Deletion", 
                f"Are you sure you want to remove all students in {course}-{year}{section}?",
                QMessageBox.Yes | QMessageBox.No
            )

            if confirm == QMessageBox.Yes:
                student_ids_flat = [sid[0] for sid in student_ids]

                # Step 4: Delete from student_section first (foreign key constraint)
                self.mycursor.execute(
                    "DELETE FROM section_junction WHERE section_ID = %s",
                    (section_id,)
                )

                # Step 5: Delete the actual students in user_accounts
                format_strings = ','.join(['%s'] * len(student_ids_flat))
                self.mycursor.execute(
                    f"DELETE FROM user_accounts WHERE real_ID IN ({format_strings})",
                    tuple(student_ids_flat)
                )

                self.mydb.commit()

                QMessageBox.information(self, "Success", f"All students from {course}-{year}{section} have been removed.")

                self.load_user_data()
                self.load_students_into_table()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "SQL Error", f"Error: {err}")

    def sort_students(self):
        """Sort students based on the selected category."""
        category = self.ui.sort_student.currentText()  # ✅ Get the selected text correctly

        sorting_map = {
            "ID": 0,
            "First Name": 1,
            "Last Name": 2,
            "Email": 3,
            "Section": 4,
            "Course": 5,  
            "Year": 6
        }

        if category in sorting_map:
            self.ui.list_registered_stdnt.sortItems(sorting_map[category], Qt.AscendingOrder)

    def sort_sections(self):
        """Sort sections based on the selected category (Section, Course, or Year)."""
        category = self.ui.sort_sections.currentText()  # Get selected sorting category
        
        # Mapping category to index position
        sorting_map = {"Section": 0, "Course": 1, "Year": 2}

        if category in sorting_map:
            self.sort_section_list(sorting_map[category])

    def sort_section_list(self, category_index):
        """Sort sections by Section Name, Course, or Year."""
        section_items = []

        # Extract section text from QListWidget
        for i in range(self.ui.list_sections.count()):
            text = self.ui.list_sections.item(i).text().strip()
            parts = text.split(" - ")

            if len(parts) == 2:
                section_name = parts[0].strip()
                course_year = parts[1].strip("()").split()

                if len(course_year) == 2:
                    course = course_year[0].strip()
                    year = course_year[1].strip()
                else:
                    course = course_year[0].strip()
                    year = ""
            else:
                section_name = text
                course = ""
                year = ""

            section_items.append((section_name, course, year, text))

        # Sort by the selected category (Section Name, Course, or Year)
        section_items.sort(key=lambda item: item[category_index])

        # Update QListWidget with sorted sections
        self.ui.list_sections.clear()
        self.ui.list_sections.addItems([item[3] for item in section_items])

    def search_sections(self):
        """Search for sections based on input in the search bar."""
        search_text = self.ui.search_bar_sections.text().strip().lower()

        for i in range(self.ui.list_sections.count()):
            item = self.ui.list_sections.item(i)
            if item:
                item.setHidden(search_text not in item.text().strip().lower())  # Hide non-matching items

    def reset_section_search(self):
        """Reset search filter when search bar is cleared."""
        if not self.ui.search_bar_sections.text().strip():
            for i in range(self.ui.list_sections.count()):
                self.ui.list_sections.item(i).setHidden(False)  # Show all items again


    def search_students(self):
        """Search students based on input in the search bar."""
        query = self.search_bar_student.text().strip().lower()

        for row in range(self.student_table_widget.rowCount()):
            match = False
            for col in range(self.student_table_widget.columnCount()):
                item = self.student_table_widget.item(row, col)
                if item and query in item.text().strip().lower():
                    match = True
                    break
            self.student_table_widget.setRowHidden(row, not match)

    def reset_student_search(self):
        """Reset search filter when search bar is cleared."""
        if not self.search_bar_student.text().strip():
            for row in range(self.student_table_widget.rowCount()):
                self.student_table_widget.setRowHidden(row, False)

    def add_section(self):
        """Adds a new section to both list widgets"""
        section_name = self.ui.section.text().strip()
        course = self.ui.course_section.currentText()
        year_chosen = self.ui.year_level_section.currentText()
        year = "".join(y for y in year_chosen if y.isdecimal())

        if not section_name:
            QMessageBox.warning(self, "Error", "Section name cannot be empty!")
            return

        formatted_section = f"{course} - {year}{section_name}"

        # Prevent duplicate entries
        for i in range(self.ui.list_sections.count()):
            if self.ui.list_sections.item(i).text() == formatted_section:
                QMessageBox.warning(self, "Error", "Section already exists!")
                return

        # Add to both list widgets
        self.ui.list_sections.addItem(formatted_section)
        self.ui.list_sections_register_3.addItem(formatted_section)
        self.ui.list_sections_register.addItem(formatted_section)

        # Save to SQL 
        try:
            sql_columns = "INSERT INTO section (course, year, section) " \
            "VALUES (%s, %s, %s)"
            values = [course, year, section_name]

            self.mycursor.execute(sql_columns, values)
            self.mydb.commit()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

        # Clear input field
        self.ui.section.clear()

    def load_section_data(self):
        try:
            self.mycursor.execute("SELECT course, year, section FROM section")
            self.result_sections = self.mycursor.fetchall()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def load_sections_into_list(self):
        """Load stored sections into all list widgets"""
        self.sections = self.result_sections

        # Clear existing items first
        self.ui.list_sections.clear()
        self.ui.list_sections_register.clear()
        self.ui.list_sections_register_3.clear()

        for course, year, section in self.sections:
            display_text = f"{course} - {year}{section}"

            # Add to all relevant list widgets
            self.ui.list_sections.addItem(display_text)
            self.ui.list_sections_register.addItem(display_text)
            self.ui.list_sections_register_3.addItem(display_text)

    def setup_table(self):
        """Setup table columns."""
        self.ui.list_registered_stdnt.setColumnCount(7)
        self.ui.list_registered_stdnt.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email", "Section", "Course", "Year"])

    def load_students_into_table(self):
        """Load all students into the table widget."""
        self.ui.list_registered_stdnt.setRowCount(len(self.users_data))

        for row_index, row_data in enumerate(self.users_data):
            display_data = [
                row_data[3], # ID 
                row_data[0], # First name
                row_data[1], # Last name
                row_data[2], # Email
                row_data[6], # Course
                row_data[7], # Year
                row_data[8]  # Section
            ]
            
            for col_index, value in enumerate(display_data):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.list_registered_stdnt.setItem(row_index, col_index, item)

        self.ui.list_registered_stdnt.sortItems(0, Qt.AscendingOrder)

    def generate_default_password(self):
        """Generate a default password."""
        default_password = "Student123"
        self.ui.password_stdnt_reg.setText(default_password)

    def register_student(self):
        first_name = self.ui.first_name_lineedit.text().strip()
        last_name = self.ui.last_name_lineedit.text().strip()
        email = self.ui.email_stdnt_lineedit.text().strip()
        student_id = self.ui.tupc_id_lineedit.text().strip()
        password = self.ui.password_stdnt_reg.text().strip()
        
        # Get selected section from the list
        selected_section = self.ui.list_sections_register.currentItem()
        
        if not selected_section:
            QMessageBox.warning(self, "Error", "Please select a section!")
            return
        
        if not (first_name and last_name and email and student_id and password):
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return
        
        section_text = selected_section.text()
        
        try:
            course, section_year = section_text.split(" - ")  # Split into section and the rest
            year = ''.join([char for char in section_year if char.isdigit()])  
            section = ''.join([char for char in section_year if not char.isdigit()])         
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid section format! Contact admin.")
            return

        try:
            self.mycursor.execute("SELECT COUNT(*) FROM user_accounts WHERE real_ID = %s", (student_id,))
            if self.mycursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Error", "Student ID already exists!")
                return

            sql_columns_stdnt = "INSERT INTO user_accounts (First_Name, Last_Name, email, password, real_ID, user_type, is_change_password) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = [first_name, last_name, email, password, student_id, 'student', 0]

            self.mycursor.execute(sql_columns_stdnt, values)
            self.mydb.commit()

            self.query = "SELECT sections_id FROM section WHERE course = %s AND year = %s AND section = %s"
            self.mycursor.execute(self.query, (course, year, section))

            section_result = self.mycursor.fetchone()
            section_id = section_result[0]
            self.full_name = f"{first_name} {last_name}"

            # Insert into the section_junction table to link the student and the section
            self.mycursor.execute("""
                INSERT INTO section_junction (section_ID, student_ID, student_name)
                VALUES (%s, %s, %s)
            """, (section_id, student_id, self.full_name))

            # Commit the transaction
            self.mydb.commit()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

        self.clear_fields()
        self.load_user_data()
        self.load_students_into_table()

    def remove_student(self):
        """Remove a student using First Name, Last Name, or ID"""
        first_name = self.firstname.text().strip()
        last_name = self.lastname.text().strip()
        id_number = self.idnumber.text().strip()

        if not first_name and not last_name and not id_number:
            QMessageBox.warning(self, "Error", "Please enter First Name, Last Name, or ID Number to remove.")
            return
        
        try:
            delete_section_sql = """
                DELETE FROM user_accounts WHERE First_Name = %s AND Last_Name = %s AND real_ID = %s
            """
            self.mycursor.execute(delete_section_sql, (first_name, last_name, id_number))

            self.mydb.commit()

            QMessageBox.information(self, "Success", "Student removed successfully.")

            # Refresh UI
            self.load_user_data()
            self.load_students_into_table()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)
       
        self.clear_fields()

    def clear_remove_fields(self):
        """Clear input fields after removal"""
        self.firstname.clear()
        self.lastname.clear()
        self.idnumber.clear()

    def clear_fields(self):
        """Clear input fields after successful registration."""
        self.ui.first_name_lineedit.clear()
        self.ui.last_name_lineedit.clear()
        self.ui.email_stdnt_lineedit.clear()
        self.ui.tupc_id_lineedit.clear()
        self.ui.password_stdnt_reg.clear()

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(self, "Database Error", error_message)
        

class EditStudent(QDialog):
    def __init__(self, subject_code, start_time, end_time, selected_day, room_name, assigned_instructor, db_connection, db_cursor, parent=None):
        super().__init__(parent)

        self.mydb = db_connection
        self.mycursor = db_cursor
        self.ui = EditStudentUi()
        self.ui.setupUi(self)
        self.load_section_data()
        self.collect_sections()

        self.subject = subject_code
        self.start_time = start_time
        self.end_time = end_time
        self.selected_day = selected_day
        self.room_name = room_name
        self.assigned_instructor = assigned_instructor
        
        self.ui.sort_student_section.currentIndexChanged.connect(self.sort_students)
        self.ui.search_stdnt_insched_btn.clicked.connect(self.search_students)
        self.ui.search_bar_stdnt_insched.textChanged.connect(self.reset_student_search)

        self.ui.sort_student_section.clear()
        self.ui.sort_student_section.addItems(["A to Z", "Z to A"])

        self.ui.add_section_btn.clicked.connect(self.insert_students_to_schedule)
        self.ui.remove_section.clicked.connect(self.remove_students_section)
        self.display_students_in_section()

    def sort_students(self):
        """Sort students based on the selected category."""
        category = self.ui.sort_student_section.currentText()  # Get the selected sorting option

        sorting_map = {
            "A to Z": 0,  # Ascending order (A to Z)
            "Z to A": 1   # Descending order (Z to A)
        }

        if category in sorting_map:
            # Extract the items from the list
            rows = self.ui.list_students_schedule.count()
            students = []

            # Extract all items into a list for sorting
            for row in range(rows):
                item = self.ui.list_students_schedule.item(row)
                students.append(item.text())

            # Sort the list based on the selected option (A to Z or Z to A)
            if category == "A to Z":
                students.sort()  # Sort in ascending order (A to Z)
            elif category == "Z to A":
                students.sort(reverse=True)  # Sort in descending order (Z to A)

            # Clear the current list and re-add the sorted items
            self.ui.list_students_schedule.clear()
            for student in students:
                item = QListWidgetItem(student)
                self.ui.list_students_schedule.addItem(item)

    def search_students(self):
        """Search students based on input in the search bar."""
        query = self.ui.search_bar_stdnt_insched.text().strip().lower()

        for row in range(self.ui.list_students_schedule.count()):
            match = False
            item = self.ui.list_students_schedule.item(row)
            if item and query in item.text().strip().lower():
                match = True
            self.ui.list_students_schedule.setRowHidden(row, not match)

    def reset_student_search(self):
        """Reset search filter when search bar is cleared."""
        if not self.ui.search_bar_stdnt_insched.text().strip():
            for row in range(self.ui.list_students_schedule.count()):
                self.ui.list_students_schedule.setRowHidden(row, False)

    def load_section_data(self):
        try:
            self.mycursor.execute("SELECT course, year, section FROM section")
            self.result_sections = self.mycursor.fetchall()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def collect_sections(self):
        """Populate the list of sections in the list widget."""
        self.ui.list_sections_schedule.clear()  # Clear previous list if any
        self.sections = self.result_sections
        try:

            if not self.sections:
                self.ui.list_sections_schedule.addItem("No sections available")

            # Populate the list widget with sections
            for course, year, section in self.sections:
                display_text = f"{course} - {year}{section}"
                self.ui.list_sections_schedule.addItem(display_text)

        except mysql.connect.Error as err:
            self.show_error_message("Error", "sections.json is not formatted correctly.")

    def insert_students_to_schedule(self):
        selected_item = self.ui.list_sections_schedule.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Error", "Please select a section.")
            return
        list_text = self.ui.list_students_schedule.item(0).text()
        if list_text != "No students scheduled for this section.":
            QMessageBox.warning(self, "Error", "There is already a scheduled section")
            return
        self.section_text = selected_item.text().strip() 
        try:
            course, year_section = self.section_text.split(" - ")
            year = year_section[0]
            section = year_section[1:]
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid section format.")
            return

        try:
            # Step 1: Get section_id
            self.mycursor.execute(
                "SELECT sections_id FROM section WHERE course = %s AND year = %s AND section = %s",
                (course, year, section)
            )
            result = self.mycursor.fetchone()
            if not result:
                QMessageBox.warning(self, "Error", "Section not found in the database.")
                return
            self.section_id = result[0]

            # Step 2: Get student IDs from junction
            self.mycursor.execute("""
                SELECT sj.student_ID
                FROM section_junction sj
                JOIN user_accounts ua ON sj.student_ID = ua.real_ID
                JOIN section s ON sj.section_ID = s.sections_id
                WHERE sj.section_ID = %s AND ua.user_type = 'student'
            """, (self.section_id,))
            student_ids = self.mycursor.fetchall()

            if not student_ids:
                QMessageBox.information(self, "Info", "No students found in this section.")
                return

            # Step 3: Get room ID
            self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.room_name,))
            room_result = self.mycursor.fetchone()
            if not room_result:
                QMessageBox.warning(self, "Error", "Selected room not found.")
                return
            self.selected_room_id = room_result[0]

            self.mycursor.execute("""
                SELECT COUNT(*) FROM room_schedule
                WHERE section_ID = %s AND selected_day = %s AND start_schedule = %s AND selected_room_ID = %s
            """, (
                self.section_id,
                self.selected_day,
                self.start_time.toString("HH:mm:ss"),
                self.selected_room_id
            ))
            if self.mycursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Error", "This section is already scheduled for this time.")
                return

            # Step 4: Insert for each student
            insert_query = """
                INSERT INTO room_schedule 
                (subject_code_purpose, selected_day, start_schedule, end_schedule, user_room_ID, section_ID, selected_room_ID)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            for (student_id,) in student_ids:
                self.mycursor.execute(insert_query, (
                    self.subject,
                    self.selected_day,
                    self.start_time.toString("HH:mm:ss"),
                    self.end_time.toString("HH:mm:ss"),
                    student_id,
                    self.section_id,
                    self.selected_room_id
                ))
            self.mydb.commit()

            QMessageBox.information(self, "Success", "Student schedules added successfully.")
            self.display_students_in_section()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def display_students_in_section(self):
        self.ui.list_students_schedule.clear()  # Clear existing list
        try:
            self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.room_name,))
            room_result = self.mycursor.fetchone()
            if not room_result:
                QMessageBox.warning(self, "Error", "Selected room not found.")
                return
            self.selected_room_id = room_result[0]
            query = """
                SELECT ua.First_Name, ua.Last_Name
                FROM room_schedule rs
                JOIN user_accounts ua ON rs.user_room_ID = ua.real_ID
                WHERE rs.subject_code_purpose = %s
                AND rs.selected_day = %s
                AND rs.start_schedule = %s
                AND rs.end_schedule = %s
                AND rs.selected_room_ID = %s
                AND ua.user_type = 'student'
            """
            self.mycursor.execute(query, (
                self.subject,
                self.selected_day,
                self.start_time.toString("HH:mm:ss"),
                self.end_time.toString("HH:mm:ss"),
                self.selected_room_id,
            ))
            students = self.mycursor.fetchall()

            if not students:
                self.ui.list_students_schedule.addItem("No students scheduled for this section.")
                return

            for first_name, last_name in students:
                full_name = f"{last_name}, {first_name}"
                self.ui.list_students_schedule.addItem(QListWidgetItem(full_name))

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def show_error_message(self, title, message):
        """Show error message dialog."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec()

    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(self, "Database Error", error_message)

    def remove_students_section(self):
        selected_item = self.ui.list_sections_schedule.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Error", "Please select a section.")
            return

        self.section_text = selected_item.text().strip()
        try:
            course, year_section = self.section_text.split(" - ")
            year = year_section[0]
            section = year_section[1:]
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid section format.")
            return

        try:
            # Step 1: Get section_id
            self.mycursor.execute(
                "SELECT sections_id FROM section WHERE course = %s AND year = %s AND section = %s",
                (course, year, section)
            )
            result = self.mycursor.fetchone()
            if not result:
                QMessageBox.warning(self, "Error", "Section not found in the database.")
                return
            self.section_id = result[0]

            # Step 2: Optionally, get room ID if you want to delete based on room
            self.mycursor.execute("SELECT idroom_names FROM tupc_rooms WHERE room = %s", (self.room_name,))
            room_result = self.mycursor.fetchone()
            if not room_result:
                QMessageBox.warning(self, "Error", "Selected room not found.")
                return
            self.selected_room_id = room_result[0]

             # Get instructor ID
            self.mycursor.execute("""
                SELECT real_ID FROM user_accounts
                WHERE CONCAT(First_Name, ' ', Last_Name) = %s
            """, (self.assigned_instructor,))
            instructor_id_result = self.mycursor.fetchone()
            if not instructor_id_result:
                QMessageBox.warning(self, "Error", "Instructor not found.")
                return
            instructor_id = instructor_id_result[0]

            # Step 3: Delete only student schedules
            delete_query = """
                DELETE rs FROM room_schedule rs
                JOIN user_accounts ua ON rs.user_room_ID = ua.real_ID
                WHERE rs.section_ID = %s AND rs.selected_room_ID = %s AND ua.user_type = 'student'
            """
            self.mycursor.execute(delete_query, (self.section_id, self.selected_room_id))

            # just removes the section ID relation to the instructor
            self.mycursor.execute("""
                UPDATE room_schedule
                SET section_ID = NULL
                WHERE user_room_ID = %s
                AND selected_day = %s
                AND start_schedule = %s
                AND end_schedule = %s
                AND selected_room_ID = %s
            """, (
                instructor_id,
                self.selected_day,
                self.start_time.toString("HH:mm:ss"),
                self.end_time.toString("HH:mm:ss"),
                self.selected_room_id
            ))
            self.mydb.commit()

            QMessageBox.information(self, "Success", "Student schedules removed successfully.")
            self.display_students_in_section()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminMenu()
    window.show()
    sys.exit(app.exec())   