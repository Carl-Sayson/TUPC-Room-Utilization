from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QListWidgetItem, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from Log_in_ui import Ui_Log_In as login
from Admin_menu_ui import Ui_MainWindow as AdminUI
from Student_menu_ui import Ui_MainWindow as StudentUI
from Staff_menu_ui import Ui_MainWindow as StaffUI
from Instructor_menu_ui import Ui_MainWindow as InstructorUI

from Change_pass_ui import Ui_Dialog as ChangePassUi
from Room_Request_Instructor_ui import Ui_Dialog as RoomRequestInstructorUi
from Room_Request_Staff_ui import Ui_Dialog as RoomRequestStaffUi
from Compose_Message_staff_ui import Ui_Dialog as ComposeReportStaffUi
from Edit_students_ui import Ui_Dialog as EditStudentUi
from Force_change_Password_ui import Ui_Form as ForceChangePasswordUi
import sys

class MainWindow(QMainWindow):
    user_data = {
            "student": {"role": "student", "password": "student123", "default_password": True},
            "staff": {"role": "staff", "password": "staff123", "default_password": True},
            "instructor": {"role": "instructor", "password": "instructor123", "default_password": True},
            "admin": {"role": "admin", "password": "admin123", "default_password": False},
        }
    
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
        user_info = MainWindow.user_data.get(username)
        if not user_info or user_info['password'] != password:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            return
        
        role = user_info['role']
        default_password = user_info['default_password']
        
        if role != "admin" and default_password:
            self.force_change_password(username, role)
        else:
            self.open_role_module(role)

    def toggle_password_visibility(self):
        if self.ui.password.echoMode() == QLineEdit.Password:
            self.ui.password.setEchoMode(QLineEdit.Normal)  # Show password
            self.ui.show_password.setText("Hide Password")
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)  # Hide password
            self.ui.show_password.setText("Show Password")  

    def force_change_password(self, username, role):
        dialog = ForceChangePassword(self, username)
        if dialog.exec():
            new_password = dialog.new_password
            if new_password:
                MainWindow.user_data[username]['password'] = new_password  # Save new password
                MainWindow.user_data[username]['default_password'] = False  # Mark password as changed
            self.open_role_module(role)

    def open_role_module(self, role):
        if role == "student":
            self.switch_window(StudentMenu)
        elif role == "staff":
            self.switch_window(StaffMenu)
        elif role == "instructor":
            self.switch_window(InstructorMenu)
        elif role == "admin":
            self.switch_window(AdminMenu)

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

        self.ui.add_rm.clicked.connect(self.add_room) 
        self.ui.del_rm.clicked.connect(self.delete_room)
        self.ui.room_list.itemDoubleClicked.connect(self.edit_room)
        self.ui.logout_btn.clicked.connect(self.open_logout)  

        self.ui.room_btn.clicked.connect(lambda: self.open_page(0))  # Student view
        self.ui.instructor_btn.clicked.connect(lambda: self.open_page(4))  # Instructor view
        self.ui.student_btn.clicked.connect(lambda: self.open_page(1))  # Instructor view
        self.ui.staff_btn.clicked.connect(lambda: self.open_page(2))  # Instructor view
        self.ui.inbox_btn.clicked.connect(lambda: self.open_page(3))

        self.ui.log_rm.clicked.connect(lambda: self.open_roompage(3))
        self.ui.edit_rm.clicked.connect(lambda: self.open_roompage(2))  # Instructor view
        self.ui.view_sched.clicked.connect(lambda: self.open_roompage(1))

        self.bck_btn_editsched = self.ui.schedule_stackedwidget.widget(2).findChild(QPushButton, "back_2")
        self.bck_btn_display = self.ui.schedule_stackedwidget.widget(1).findChild(QPushButton, "back")
        self.bck_btn_logs = self.ui.schedule_stackedwidget.widget(3).findChild(QPushButton, "back_3")
        self.bck_btn_editsched.clicked.connect(self.return_roomview)
        self.bck_btn_display.clicked.connect(self.return_roomview)
        self.bck_btn_logs.clicked.connect(self.return_roomview)

        self.add_student = self.ui.schedule_stackedwidget.widget(2).findChild(QPushButton, "add_student")
        self.add_student.clicked.connect(self.open_add_student) 

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
        self.ui.tabWidget.setCurrentIndex(index)
        self.new_window = None
        
    def open_logout(self):
        self.switch_window(MainWindow)

    def switch_window(self, new_window_class):
        self.new_window = new_window_class()
        self.new_window.show()
        self.close()

class EditStudent(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # Ensures it stays on top of the main window

        self.ui = EditStudentUi()
        self.ui.setupUi(self)
        self.ui.cancel.clicked.connect(self.close)

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
        self.ui.back_btn_request_instructor.clicked.connect(self.close)
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
        self.ui.back_btn_request_staff.clicked.connect(self.close)
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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())   