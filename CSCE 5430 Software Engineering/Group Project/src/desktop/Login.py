from common import CURR_USER, User
from ui.ui_Login import Ui_Login
from PySide6.QtWidgets import QMessageBox, QWidget
import sys


# TODO (nikhil): add a profile page that shows profile info / options to change that info
# TODO (nikhil): make the login window a floating dialogue box
#       if it is easier / makes more sense to just have the widget change the way it looks (swapping widget
#       out and then updating the view) then we can do that rather than a floating windw
# TODO (nikhil): add a create account floating window
# TODO (nikhil): make a floating dialogue for changing password / username

# NOTE: if we decide to go the route of connecting with user's google keep / todoist / other apps accounts
#       then we can include all that information in the profile page as well. they can add / manage those
#       app connections there

class Login(QWidget, Ui_Login):
    def __init__(self, parent: QWidget):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.signIn_button.clicked.connect(lambda: self.get_login_info())
        self.pushButton.clicked.connect(lambda: self.parent.logout())

    def get_login_info(self):
        #self.parent.db.get_all_users()
        username = self.username_input.text()
        password = self.password_input.text()
        self.parent.login(username, password)
