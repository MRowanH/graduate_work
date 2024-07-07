from common import CURR_USER, User
from ui.ui_SignUp import Ui_SignUp
from PySide6.QtWidgets import QWidget
#ID = 0
class SignUp(QWidget, Ui_SignUp):
    def __init__(self, parent: QWidget):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.signUp_button.clicked.connect(lambda: self.sign_up())
        self.pushButton.clicked.connect(lambda: self.parent.logout())

    def sign_up(self):
        #self.parent.db.get_all_users()
        #print(f'Processing sign up input')
        username = self.username_input.text()
        password = self.password_input.text()
        self.parent.sign_up(username, password)

