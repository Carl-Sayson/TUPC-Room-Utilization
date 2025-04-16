from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QListWidgetItem, QPushButton, QLineEdit, QTableWidgetItem, QTableWidget, QComboBox, QListWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
import mysql.connector.cursor

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

import sys
import json
import os
import mysql.connector
from mysql.connector import errorcode

USER_DATA_FILE = "users.json"
SCHEDULE_FILE = "schedules.json"

def load_user_data():
    """Load all users from JSON and ensure required keys exist."""
    try:
        with open(USER_DATA_FILE, "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}

    users.setdefault("students", {})
    users.setdefault("staff", {})
    users.setdefault("instructors", {})
    users.setdefault("admin", {})

    return users

def save_user_data(users):
    """Save updated user data to JSON."""
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

def load_schedules():
    """Load schedules from the JSON file."""
    if os.path.exists(SCHEDULE_FILE):
        with open(SCHEDULE_FILE, "r") as file:
            return json.load(file)
    return {}

def save_schedules(schedules):
    """Save the schedules back to the JSON file."""
    with open(SCHEDULE_FILE, "w") as file:
        json.dump(schedules, file, indent=4)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            self.ui = login()
            self.ui.setupUi(self)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load UI: {e}")
            sys.exit(1)

        self.ui.login.clicked.connect(self.handle_login)
        self.ui.show_password.clicked.connect(self.toggle_password_visibility)
        self.new_window = None

    def handle_login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        users = load_user_data()  # Load user data from JSON

        if username in users and users[username]["role"] == "admin" and users[username]["password"] == password:
            QMessageBox.information(self, "Login Successful", "Welcome, Admin!")
            self.switch_window(AdminMenu)
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password!")
 

    def toggle_password_visibility(self):
        if self.ui.password.echoMode() == QLineEdit.Password:
            self.ui.password.setEchoMode(QLineEdit.Normal)  # Show password
            self.ui.show_password.setText("Hide Password")
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)  # Hide password
            self.ui.show_password.setText("Show Password")  

    def switch_window(self, new_window_class):
        if self.new_window:
            self.new_window.close()
        self.new_window = new_window_class()
        self.new_window.show()
        self.close()

class StudentMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = StudentUI()
        self.ui.setupUi(self)
        
        self.ui.logout_btn.clicked.connect(self.open_logout)
        self.ui.change_pass.clicked.connect(self.open_change_pass)  
        self.ui.student_sched_btn.clicked.connect(lambda: self.open_page(0))  # Student view
        self.ui.info_stdnt_btn.clicked.connect(lambda: self.open_page(1))  # Instructor view
        self.new_window = None

    def open_page(self, index):
        self.ui.student_menu_stackedwidget.setCurrentIndex(index)
        self.new_window = None
        
    def open_change_pass(self):
        dialog = ChangePass(self)
        dialog.exec()

    def open_logout(self):
        self.switch_window(MainWindow)

    def switch_window(self, new_window_class):
        if self.new_window:
            self.new_window.close()
        self.new_window = new_window_class()
        self.new_window.show()
        self.close()

class InstructorMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = InstructorUI()
        self.ui.setupUi(self)

        self.ui.logout_btn.clicked.connect(self.open_logout)
        self.ui.change_pass.clicked.connect(self.open_change_pass)  
        self.ui.send_message_instructor_btn.clicked.connect(self.open_compose)  
        self.ui.instructor_sched_btn.clicked.connect(lambda: self.open_page(0))  # Student view
        self.ui.instructor_info_btn.clicked.connect(lambda: self.open_page(1))  # Instructor view
        self.ui.instructor_inbox_btn.clicked.connect(lambda: self.open_page(2))  # Instructor view
        self.new_window = None

    def open_page(self, index):
        self.ui.instructor_menu_stackedwidget.setCurrentIndex(index)
        self.new_window = None

    def open_change_pass(self):
        dialog = ChangePass(self)
        dialog.exec()

    def open_compose(self):
        dialog = RoomRequestInstructor(self)
        dialog.exec()

    def open_logout(self):
        self.switch_window(MainWindow)

    def switch_window(self, new_window_class):
        if self.new_window:
            self.new_window.close()
        self.new_window = new_window_class()
        self.new_window.show()
        self.close()

class StaffMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = StaffUI()
        self.ui.setupUi(self)

        self.ui.logout_btn.clicked.connect(self.open_logout)
        self.ui.change_pass.clicked.connect(self.open_change_pass)       
        self.ui.compose_staff.clicked.connect(self.open_composerequest)     
        self.ui.compose_message_report_btn.clicked.connect(self.open_composereport)  
        self.ui.staff_sched_btn.clicked.connect(lambda: self.open_page(0))  # Student view
        self.ui.staff_info_btn.clicked.connect(lambda: self.open_page(1))  # Instructor view
        self.ui.staff_inbox_btn.clicked.connect(lambda: self.open_page(2))  # Instructor view
        self.new_window = None

    def open_page(self, index):
        self.ui.staff_menu_stackedwidget.setCurrentIndex(index)
        self.new_window = None

    def open_change_pass(self):
        dialog = ChangePass(self)
        dialog.exec() 

    def open_composerequest(self):
        dialog = RoomRequestStaff(self)
        dialog.exec()

    def open_composereport(self):
        dialog = ComposeReport(self)
        dialog.exec()
        
    def open_logout(self):
        self.switch_window(MainWindow)

    def switch_window(self, new_window_class):
        if self.new_window:
            self.new_window.close()
        self.new_window = new_window_class()
        self.new_window.show()
        self.close()

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

        self.users = load_user_data()
        self.students = self.users.get("students", {})
        self.instructors = self.users.get("instructors", {})
        self.staffs = self.users.get("staffs", {})

        self.student_table_widget = self.ui.stackedWidget.widget(1).findChild(QTableWidget, "list_registered_stdnt")
        self.instructor_table_widget = self.ui.stackedWidget.widget(4).findChild(QTableWidget, "list_registered_instructor")
        self.staff_table_widget = self.ui.stackedWidget.widget(2).findChild(QTableWidget, "list_registered_staff")
        
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
        self.ui.room_list.itemDoubleClicked.connect(self.edit_room)
        self.ui.logout_btn.clicked.connect(self.open_logout)  

        self.ui.room_btn.clicked.connect(lambda: self.open_page(0)) 
        self.ui.instructor_btn.clicked.connect(lambda: self.open_page(4)) 
        self.ui.student_btn.clicked.connect(lambda: self.open_page(1)) 
        self.ui.staff_btn.clicked.connect(lambda: self.open_page(2)) 
        self.ui.inbox_btn.clicked.connect(lambda: self.open_page(3))

        self.ui.log_rm.clicked.connect(lambda: self.open_roompage(3))
        self.ui.edit_rm.clicked.connect(lambda: self.open_roompage(2))
        self.ui.view_sched.clicked.connect(lambda: self.open_roompage(1))

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

        self.load_students_into_table()
        self.load_instructors_into_table()
        self.load_staffs_into_table()

    





















































































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
        print("hi")
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
        dialog = StaffRegistration(self)   
        dialog.data_updated.connect(self.load_staffs_into_table)   
        dialog.exec()

    def open_manage_student(self):
        dialog = StudentRegistration(self)
        dialog.data_updated.connect(self.load_students_into_table)
        dialog.exec()
        
    def open_manage_instructor(self):
        dialog = InstructorRegistration(self)
        dialog.data_updated.connect(self.load_instructors_into_table)
        dialog.exec()  
        
    def open_roompage(self, index):
        self.ui.schedule_stackedwidget.setCurrentIndex(index)

    def return_roomview(self):
        self.ui.schedule_stackedwidget.setCurrentIndex(0)

    def add_room(self):
        item = QListWidgetItem("New Room...")
        item.setTextAlignment(Qt.AlignCenter) 
        font = QFont()
        font.setPointSize(12)
        item.setFont(font)

        self.ui.room_list.addItem(item)

    def edit_room(self, item):
        item.setFlags(item.flags() | Qt.ItemIsEditable)  # Enable editing
        self.ui.room_list.editItem(item)

    def delete_room(self):
        selected_item = self.ui.room_list.currentItem()  # Correct reference to room_list

        if selected_item:  # Check if an item is selected
            confirmation = QMessageBox.question(
                self, 
                "Confirm Deletion", 
                "Are you sure you want to delete this room?",
                QMessageBox.Yes | QMessageBox.No
            )

            if confirmation == QMessageBox.Yes:
                row = self.ui.room_list.row(selected_item)
                self.ui.room_list.takeItem(row)
        else:
            QMessageBox.warning(self, "Warning", "Please select a room to delete.")

    def open_add_student(self):
        dialog = EditStudent(self)
        dialog.exec()

    def open_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        self.new_window = None
        
    def open_logout(self):
        self.switch_window(MainWindow)

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
    data_updated = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)  # Ensures it stays on top of the main window

        self.ui = StaffRegistrationUi()
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
        finally:
            if self.mycursor:
                self.mycursor.close()
            if self.mydb:
                self.mydb.close()
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
    
    def closeEvent(self, event):
        self.data_updated.emit()
        if self.mycursor:
            self.mycursor.close()
        if self.mydb:
            self.mydb.close()
        super().closeEvent(event)
    
    def errorDisplay(self, errno, sqlstate, msg):
        """Displays detailed error information to the user."""
        # Construct the error message
        error_message = f"Error Code: {errno}\nSQLSTATE: {sqlstate}\nMessage: {msg}"

        # Create and show a critical error message box with the detailed error
        QMessageBox.critical(self, "Database Error", error_message)
    
class InstructorRegistration(QDialog):
    data_updated = Signal()

    def __init__(self, instructor_menu=None, parent=None):
        super().__init__(parent)

        self.ui = InstructorRegistrationUi()
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
        finally:
            if self.mycursor:
                self.mycursor.close()
            if self.mydb:
                self.mydb.close()
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

    def closeEvent(self, event):
        self.data_updated.emit()
        if self.mycursor:
            self.mycursor.close()
        if self.mydb:
            self.mydb.close()
        super().closeEvent(event)

class StudentRegistration(QDialog):
    data_updated = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = StudentRegistrationUi()
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
        
        self.data_updated.emit()
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
            self.data_updated.emit()

        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

        finally:
            if self.mycursor:
                self.mycursor.close()
            if self.mydb:
                self.mydb.close()

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
                self.data_updated.emit()

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
        self.data_updated.emit()

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
        finally:
            if self.mycursor:
                self.mycursor.close()
            if self.mydb:
                self.mydb.close()
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

    def closeEvent(self, event):
        self.data_updated.emit()
        if self.mycursor:
            self.mycursor.close()
        if self.mydb:
            self.mydb.close()
        super().closeEvent(event)
        
class EditStudent(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # Ensures it stays on top of the main window

        self.ui = EditStudentUi()
        self.ui.setupUi(self)

class ChangePass(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # Ensures it stays on top of the main window
        self.ui = ChangePassUi()
        self.ui.setupUi(self)

        self.ui.cancel.clicked.connect(self.close)

class RoomRequestInstructor(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = RoomRequestInstructorUi()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(lambda: self.open_page(1))
        self.ui.room_list_request_instructor.itemDoubleClicked.connect(lambda: self.open_page(0))

        # Safer way to locate the 'back' button
        self.back = None
        for i in range(self.ui.stackedWidget.count()):
            self.back = self.ui.stackedWidget.widget(i).findChild(QPushButton, "back")
            if self.back:
                self.back.clicked.connect(lambda: self.open_page(1))
                break

        if not self.back:
            QMessageBox.warning(self, "Warning", "Back button not found in the stacked widget.")

    def open_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

class RoomRequestStaff(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  
        self.ui = RoomRequestStaffUi()
        self.ui.setupUi(self)
        self.ui.room_list_request_staff.itemDoubleClicked.connect(lambda: self.open_page(0))
        self.back_room_select_staff = self.ui.stackedWidget.widget(0).findChild(QPushButton, "back_room_select_staff")
        self.back_room_select_staff.clicked.connect(lambda: self.open_page(1))

    def open_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        self.new_window = None

class ComposeReport(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  
        self.ui = ComposeReportStaffUi()
        self.ui.setupUi(self)

class ForceChangePassword(QDialog):
    def __init__(self, parent=None, username=""):
        super().__init__(parent)
        self.ui = ForceChangePasswordUi()
        self.ui.setupUi(self)
        self.username = username  # Store username
        self.new_password = None  # Variable to store new password
        
        self.ui.new_pass.setEchoMode(QLineEdit.Password)
        self.ui.confirm_pass.setEchoMode(QLineEdit.Password)
        
        # Connect buttons
        self.ui.change_pass_btn.clicked.connect(self.save_new_password)
        self.ui.show_new.clicked.connect(lambda: self.toggle_password_visibility(self.ui.new_pass))
        self.ui.show_new_2.clicked.connect(lambda: self.toggle_password_visibility(self.ui.confirm_pass))
    
    def toggle_password_visibility(self, field):
        if field.echoMode() == QLineEdit.Password:
            field.setEchoMode(QLineEdit.Normal)  # Show password
        else:
            field.setEchoMode(QLineEdit.Password)  # Hide password
    def save_new_password(self):
        new_pass = self.ui.new_pass.text()
        confirm_pass = self.ui.confirm_pass.text()
        
        if not new_pass or new_pass != confirm_pass:
            QMessageBox.warning(self, "Error", "Passwords do not match!")
            return
        
        self.new_password = new_pass  # Save new password
        MainWindow.user_data[self.username]['default_password'] = False  # Mark password as changed
        MainWindow.user_data[self.username]['password'] = new_pass  # Save new password in class-level user data
        
        QMessageBox.information(self, "Success", "Password changed successfully.")
        
        # Proceed to respective module
        self.parent().open_role_module(MainWindow.user_data[self.username]['role'])
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminMenu()
    window.show()
    sys.exit(app.exec())   

    