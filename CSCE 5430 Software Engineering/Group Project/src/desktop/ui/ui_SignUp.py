# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignUpWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"Login")
        SignUp.resize(1440, 986)
        self.gridLayout = QGridLayout(SignUp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.username_input = QLineEdit(SignUp)
        self.username_input.setObjectName(u"username_input")

        self.gridLayout.addWidget(self.username_input, 4, 1, 1, 1)

        self.signUp_button = QPushButton(SignUp)
        self.signUp_button.setObjectName(u"signUp_button")

        self.gridLayout.addWidget(self.signUp_button, 8, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.label_3 = QLabel(SignUp)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.password_input = QLineEdit(SignUp)
        self.password_input.setObjectName(u"password_input")

        self.gridLayout.addWidget(self.password_input, 7, 1, 1, 1)

        self.label_2 = QLabel(SignUp)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 10, 1, 1, 1)

        self.label = QLabel(SignUp)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.pushButton = QPushButton(SignUp)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 9, 1, 1, 1)


        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("SignUp", u"Form", None))
        self.signUp_button.setText(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.label_3.setText(QCoreApplication.translate("SignUp", u"<html><head/><body><p align=\"center\">Password</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SignUp", u"<html><head/><body><p align=\"center\">Username</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.pushButton.setText(QCoreApplication.translate("SignUp", u"Logout", None))
    # retranslateUi

