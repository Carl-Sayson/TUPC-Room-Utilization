from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QListWidgetItem, QPushButton, QLineEdit, QTableWidgetItem, QTableWidget, QComboBox, QListWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from Log_in_ui import Ui_Log_In as login
from Admin_menu_ui import Ui_MainWindow as AdminUI
from Student_menu_ui import Ui_MainWindow as StudentUI
from Staff_menu_ui import Ui_MainWindow as StaffUI
from Instructor_menu_ui import Ui_MainWindow as InstructorUI

from Change_pass_ui import Ui_Dialog as ChangePassUi
from Room_Request_Instructor_ui import Ui_Form as RoomRequestInstructorUi
from Room_Request_Staff_ui import Ui_Form as RoomRequestStaffUi
from Compose_Message_staff_ui import Ui_Dialog as ComposeReportStaffUi
from Edit_students_ui import Ui_Form as EditStudentUi
from Force_change_Password_ui import Ui_Form as ForceChangePasswordUi
from staff_registration_ui import Ui_Form as StaffRegistrationUi
from student_registration_ui import Ui_Dialog as StudentRegistrationUi
from instructor_registration_ui import Ui_Form as InstructorRegistrationUi

import sys
import json
import os

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

        self.users = load_user_data()
        self.students = self.users.get("students", {})
        self.instructors = self.users.get("instructors", {})
        self.staffs = self.users.get("staffs", {})

        self.student_table_widget = self.ui.stackedWidget.widget(1).findChild(QTableWidget, "list_registered_stdnt")
        self.instructor_table_widget = self.ui.stackedWidget.widget(4).findChild(QTableWidget, "list_registered_instructor")
        self.staff_table_widget = self.ui.stackedWidget.widget(2).findChild(QTableWidget, "list_registered_staff")

        self.load_students_into_table()
        self.load_instructors_into_table()
        self.load_staffs_into_table()
        
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
        users = load_user_data()
        students = users.get("students", {})

        self.student_table_widget.setRowCount(len(students))
        self.student_table_widget.setColumnCount(7)
        self.student_table_widget.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email", "Section", "Course", "Year"])

        for row, (student_id, data) in enumerate(students.items()):
            self.student_table_widget.setItem(row, 0, QTableWidgetItem(student_id))
            self.student_table_widget.setItem(row, 1, QTableWidgetItem(data["first_name"]))
            self.student_table_widget.setItem(row, 2, QTableWidgetItem(data["last_name"]))
            self.student_table_widget.setItem(row, 3, QTableWidgetItem(data["email"]))
            self.student_table_widget.setItem(row, 4, QTableWidgetItem(data["section"]))
            self.student_table_widget.setItem(row, 5, QTableWidgetItem(data["course"]))
            self.student_table_widget.setItem(row, 6, QTableWidgetItem(data["year"]))

    def load_instructors_into_table(self):
        users = load_user_data()
        instructors = users.get("instructors", {})

        self.instructor_table_widget.setRowCount(len(instructors))
        self.instructor_table_widget.setColumnCount(4)
        self.instructor_table_widget.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email"])

        for row, (instructor_id, data) in enumerate(instructors.items()):
            self.instructor_table_widget.setItem(row, 0, QTableWidgetItem(instructor_id))
            self.instructor_table_widget.setItem(row, 1, QTableWidgetItem(data["first_name"]))
            self.instructor_table_widget.setItem(row, 2, QTableWidgetItem(data["last_name"]))
            self.instructor_table_widget.setItem(row, 3, QTableWidgetItem(data["email"]))

        self.ui.list_registered_instructor.sortItems(0, Qt.AscendingOrder)

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
        users = load_user_data()
        staffs = users.get("staffs", {})

        self.staff_table_widget.setRowCount(len(staffs))
        self.staff_table_widget.setColumnCount(4)
        self.staff_table_widget.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email"])

        for row, (staff_id, data) in enumerate(staffs.items()):
            self.staff_table_widget.setItem(row, 0, QTableWidgetItem(staff_id))
            self.staff_table_widget.setItem(row, 1, QTableWidgetItem(data["first_name"]))
            self.staff_table_widget.setItem(row, 2, QTableWidgetItem(data["last_name"]))
            self.staff_table_widget.setItem(row, 3, QTableWidgetItem(data["email"]))

        self.ui.list_registered_staff.sortItems(0, Qt.AscendingOrder)

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
        dialog.exec()
        self.load_staffs_into_table()
        
    def open_manage_student(self):
        dialog = StudentRegistration(self)
        dialog.exec()
        self.load_students_into_table() 

    def open_manage_instructor(self):
        dialog = InstructorRegistration(self)
        dialog.exec()
        self.load_instructors_into_table()

        
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


class StaffRegistration(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # Ensures it stays on top of the main window

        self.ui = StaffRegistrationUi()
        self.ui.setupUi(self)

        self.users = load_user_data()
        self.staffs = self.users.get("staffs", {})
        
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
        self.load_staff_into_table()

    def load_user_data(self):
        """Load user data from JSON"""
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"staffs": {}}

    def save_user_data(self):
        """Save user data to JSON"""
        with open("users.json", "w") as file:
            json.dump(self.users, file, indent=4)

    def reset_staff_search(self):
        """Reset the instructor table when the search bar is cleared."""
        search_text = self.ui.search_bar_staff.text().strip()
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

    def setup_table(self):
        """Setup table columns."""
        self.ui.list_registered_staff.setColumnCount(5)
        self.ui.list_registered_staff.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email", "Password"])

    def load_staff_into_table(self):
        """Load all staff into the table widget."""
        self.ui.list_registered_staff.setRowCount(len(self.staffs))

        for row, (staff_id, data) in enumerate(self.staffs.items()):
            self.ui.list_registered_staff.setItem(row, 0, QTableWidgetItem(staff_id))
            self.ui.list_registered_staff.setItem(row, 1, QTableWidgetItem(data["first_name"]))
            self.ui.list_registered_staff.setItem(row, 2, QTableWidgetItem(data["last_name"]))
            self.ui.list_registered_staff.setItem(row, 3, QTableWidgetItem(data["email"]))

        self.ui.list_registered_staff.sortItems(0, Qt.AscendingOrder)

    def generate_default_password(self):
        """Generate a default password."""
        default_password = "Staff123"
        self.ui.password_staff_reg.setText(default_password)

    def register_staff(self):
        """Save staff details to a JSON file."""
        first_name = self.ui.first_name_lineedit_staff.text().strip()
        last_name = self.ui.lastname_lineedit_staff.text().strip()
        email = self.ui.email_staff_lineedit.text().strip()
        staff_id = self.ui.ID_staff.text().strip()
        password = self.ui.password_staff_reg.text().strip()

        if not (first_name and last_name and email and staff_id and password):
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return

        if staff_id in self.staffs:
            QMessageBox.warning(self, "Error", "Staff ID already exists!")
            return

        self.staffs[staff_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }

        self.users["staffs"] = self.staffs
        save_user_data(self.users)

        QMessageBox.information(self, "Success", "Staff registered successfully!")
        self.clear_fields()

        # Refresh table with new staff member
        self.load_staff_into_table()
    
    def remove_staff(self):
        """Remove a staff member using First Name, Last Name, or ID"""
        first_name = self.firstname.text().strip()
        last_name = self.lastname.text().strip()
        id_number = self.idnumber.text().strip()

        if not first_name and not last_name and not id_number:
            QMessageBox.warning(self, "Error", "Please enter First Name, Last Name, or ID Number to remove.")
            return

        staff_list = self.users.get("staffs", {})

        staff_to_remove = None
        for key, staff in staff_list.items():
            if (
                (first_name and staff.get("first_name") == first_name) or
                (last_name and staff.get("last_name") == last_name) or
                (id_number and key == id_number)  # Match staff ID directly
            ):
                staff_to_remove = key
                break

        if staff_to_remove:
            del self.users["staffs"][staff_to_remove]
            self.save_user_data()
            QMessageBox.information(self, "Success", "Staff member removed successfully.")
            self.clear_remove_fields()
            self.load_staff_into_table()  # Refresh staff list in the table
        else:
            QMessageBox.warning(self, "Error", "No matching staff found.")

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

class StudentRegistration(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = StudentRegistrationUi()
        self.ui.setupUi(self)

        self.users = load_user_data()
        self.students = self.users.get("students", {})

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
        self.load_sections_into_list()

        # Initialize TableWidget
        self.setup_table()
        self.load_students_into_table()
        
    def load_user_data(self):
        """Load user data from JSON"""
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"students": {}}

    def save_user_data(self):
        """Save user data to JSON"""
        with open("users.json", "w") as file:
            json.dump(self.users, file, indent=4) 

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

        section_text = selected_section_item.text().strip()  # Example: "A1 - BSIT (1st Year)"
        section_name = section_text.split(" - ")[0].strip()  # Extract section name

        # Confirmation dialog
        confirm = QMessageBox.question(
            self, "Confirm Deletion", 
            f"Are you sure you want to remove section {section_name} and all associated students?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            # Remove students in this section
            students_to_remove = [sid for sid, data in self.students.items() if data["section"] == section_name]
            for sid in students_to_remove:
                del self.students[sid]  

            self.users["students"] = self.students
            self.save_user_data()

            # Remove section from the section list
            sections = self.load_section_data()
            sections = [sec for sec in sections if not sec.startswith(section_name)]
            with open("sections.json", "w") as file:
                json.dump({"sections": sections}, file, indent=4)

            QMessageBox.information(self, "Success", f"Section '{section_name}' and its students have been removed.")

            # Refresh UI
            self.load_sections_into_list()
            self.load_students_into_table()

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
        """Remove all students in the selected section."""
        selected_section_item = self.list_sections_remove.currentItem()

        if not selected_section_item:
            QMessageBox.warning(self, "Error", "Please select a section to remove students from.")
            return

        section_text = selected_section_item.text().strip()
        section_name = section_text.split(" - ")[0].strip()

        students_to_remove = [sid for sid, data in self.students.items() if data["section"] == section_name]

        if not students_to_remove:
            QMessageBox.information(self, "Info", "No students found in the selected section.")
            return

        # Confirm deletion
        confirm = QMessageBox.question(
            self, "Confirm Deletion", 
            f"Are you sure you want to remove all students in {section_name}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            for sid in students_to_remove:
                del self.students[sid]  # Delete student

            self.users["students"] = self.students  # Update main data
            self.save_user_data()  # Save changes

            QMessageBox.information(self, "Success", f"All students from {section_name} have been removed.")
            
            self.load_students_into_table()  # Refresh student list

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
        year = self.ui.year_level_section.currentText()

        if not section_name:
            QMessageBox.warning(self, "Error", "Section name cannot be empty!")
            return

        formatted_section = f"{section_name} - {course} ({year})"

        # Prevent duplicate entries
        for i in range(self.ui.list_sections.count()):
            if self.ui.list_sections.item(i).text() == formatted_section:
                QMessageBox.warning(self, "Error", "Section already exists!")
                return

        # Add to both list widgets
        self.ui.list_sections.addItem(formatted_section)
        self.ui.list_sections_register_3.addItem(formatted_section)
        self.ui.list_sections_register.addItem(formatted_section)

        # Save to JSON file
        self.save_section_data(formatted_section)

        # Clear input field
        self.ui.section.clear()


    def load_section_data(self):
        """Load existing sections from JSON"""
        try:
            with open("sections.json", "r") as file:
                data = json.load(file)
                if isinstance(data, dict):  # Ensure it's a dictionary
                    return data.get("sections", [])
                return []  # If it's not a dictionary, return an empty list
        except FileNotFoundError:
            return []


    def save_section_data(self, new_section):
        """Save sections to JSON file"""
        sections = self.load_section_data()
        sections.append(new_section)
        with open("sections.json", "w") as file:
            json.dump({"sections": sections}, file, indent=4)

    def load_sections_into_list(self):
        """Load stored sections into both list widgets"""
        sections = self.load_section_data()
        
        # Clear existing items
        self.ui.list_sections.clear()
        self.ui.list_sections_register.clear()
        self.ui.list_sections_register_3.clear()

        # Add all sections properly
        self.ui.list_sections.addItems(sections)
        self.ui.list_sections_register.addItems(sections)
        self.ui.list_sections_register_3.addItems(sections)


    def setup_table(self):
        """Setup table columns."""
        self.ui.list_registered_stdnt.setColumnCount(7)
        self.ui.list_registered_stdnt.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email", "Section", "Course", "Year"])

    def load_students_into_table(self):
        """Load all students into the table widget."""
        self.ui.list_registered_stdnt.setRowCount(len(self.students))

        for row, (student_id, data) in enumerate(self.students.items()):
            self.ui.list_registered_stdnt.setItem(row, 0, QTableWidgetItem(student_id))
            self.ui.list_registered_stdnt.setItem(row, 1, QTableWidgetItem(data["first_name"]))
            self.ui.list_registered_stdnt.setItem(row, 2, QTableWidgetItem(data["last_name"]))
            self.ui.list_registered_stdnt.setItem(row, 3, QTableWidgetItem(data["email"]))
            self.ui.list_registered_stdnt.setItem(row, 4, QTableWidgetItem(data["section"]))
            self.ui.list_registered_stdnt.setItem(row, 5, QTableWidgetItem(data["course"]))
            self.ui.list_registered_stdnt.setItem(row, 6, QTableWidgetItem(data["year"]))

        self.ui.list_registered_stdnt.sortItems(0, Qt.AscendingOrder)

    def generate_default_password(self):
        """Generate a default password."""
        default_password = "Student123"
        self.ui.password_stdnt_reg.setText(default_password)

    def register_student(self):
        """Save student details to a JSON file."""
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

        section_text = selected_section.text()  # Example: "A1 - BSIT (1st Year)"
        
        try:
            section, course_year = section_text.split(" - ")  # Split into section and the rest
            course, year = course_year.strip("()").split()  # Extract course and year
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid section format! Contact admin.")
            return

        if not (first_name and last_name and email and student_id and password):
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return

        if student_id in self.students:
            QMessageBox.warning(self, "Error", "Student ID already exists!")
            return

        # Save student details
        self.students[student_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "section": section,
            "course": course,
            "year": year
        }

        self.users["students"] = self.students
        self.save_user_data()

        QMessageBox.information(self, "Success", "Student registered successfully!")
        self.clear_fields()

        # Refresh table with new student
        self.load_students_into_table()


    def remove_student(self):
        """Remove a student using First Name, Last Name, or ID"""
        first_name = self.firstname.text().strip()
        last_name = self.lastname.text().strip()
        id_number = self.idnumber.text().strip()

        if not first_name and not last_name and not id_number:
            QMessageBox.warning(self, "Error", "Please enter First Name, Last Name, or ID Number to remove.")
            return

        student_list = self.users.get("students", {})

        student_to_remove = None
        for key, student in student_list.items():
            if (
                (first_name and student.get("first_name") == first_name) or
                (last_name and student.get("last_name") == last_name) or
                (id_number and key == id_number)  # Match student ID directly
            ):
                student_to_remove = key
                break

        if student_to_remove:
            del self.users["students"][student_to_remove]
            self.save_user_data()
            QMessageBox.information(self, "Success", "Student removed successfully.")
            self.clear_remove_fields()
            self.load_students_into_table()  # Refresh student list in the table
        else:
            QMessageBox.warning(self, "Error", "No matching student found.")

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

class InstructorRegistration(QDialog):
    def __init__(self, instructor_menu=None, parent=None):
        super().__init__(parent)

        self.ui = InstructorRegistrationUi()
        self.ui.setupUi(self)

        self.users = load_user_data()
        self.instructors = self.users.get("instructors", {})

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
        self.load_instructors_into_table()

    def load_user_data(self):
        """Load user data from JSON"""
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"instructors": {}}

    def save_user_data(self):
        """Save user data to JSON"""
        with open("users.json", "w") as file:
            json.dump(self.users, file, indent=4)

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
        self.ui.list_registered_instructor.setColumnCount(5)
        self.ui.list_registered_instructor.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Email", "Password"])

    def load_instructors_into_table(self):
        """Load all instructors into the table widget."""
        self.ui.list_registered_instructor.setRowCount(len(self.instructors))

        for row, (instructor_id, data) in enumerate(self.instructors.items()):
            self.ui.list_registered_instructor.setItem(row, 0, QTableWidgetItem(instructor_id))
            self.ui.list_registered_instructor.setItem(row, 1, QTableWidgetItem(data["first_name"]))
            self.ui.list_registered_instructor.setItem(row, 2, QTableWidgetItem(data["last_name"]))
            self.ui.list_registered_instructor.setItem(row, 3, QTableWidgetItem(data["email"]))

        self.ui.list_registered_instructor.sortItems(0, Qt.AscendingOrder)

    def generate_default_password(self):
        """Generate a default password."""
        default_password = "Instructor123"
        self.ui.password_instructor_reg.setText(default_password)

    def register_instructor(self):
        """Save instructor details to a JSON file."""
        first_name = self.ui.first_name_lineedit_instructor.text().strip()
        last_name = self.ui.lastname_lineedit_instructor.text().strip()
        email = self.ui.email_instructor_lineedit.text().strip()
        instructor_id = self.ui.ID_instructor.text().strip()
        password = self.ui.password_instructor_reg.text().strip()

        if not (first_name and last_name and email and instructor_id and password):
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return

        if instructor_id in self.instructors:
            QMessageBox.warning(self, "Error", "Instructor ID already exists!")
            return

        self.instructors[instructor_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }

        self.users["instructors"] = self.instructors
        save_user_data(self.users)

        QMessageBox.information(self, "Success", "Instructor registered successfully!")
        self.clear_fields()

        # Refresh registration table
        self.load_instructors_into_table()

    def remove_instructor(self):
        """Remove an instructor using First Name, Last Name, or ID"""
        first_name = self.firstname.text().strip()
        last_name = self.lastname.text().strip()
        id_number = self.idnumber.text().strip()

        if not first_name and not last_name and not id_number:
            QMessageBox.warning(self, "Error", "Please enter First Name, Last Name, or ID Number to remove.")
            return

        instructor_list = self.users.get("instructors", {})

        instructor_to_remove = None
        for key, instructor in instructor_list.items():
            if (
                (first_name and instructor.get("first_name") == first_name) or
                (last_name and instructor.get("last_name") == last_name) or
                (id_number and key == id_number)  # Match instructor ID directly
            ):
                instructor_to_remove = key
                break

        if instructor_to_remove:
            del self.users["instructors"][instructor_to_remove]
            self.save_user_data()
            QMessageBox.information(self, "Success", "Instructor removed successfully.")
            self.clear_remove_fields()
            self.load_instructors_into_table()  # Refresh instructor list in the table

        else:
            QMessageBox.warning(self, "Error", "No matching instructor found.")

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
        self.ui.back_btn_composed_msg.clicked.connect(self.close)

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
    window = StaffMenu()
    window.show()
    sys.exit(app.exec())   

    