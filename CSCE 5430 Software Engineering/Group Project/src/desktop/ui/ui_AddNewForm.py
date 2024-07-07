# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewForm.ui'
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

class Ui_AddNewForm(object):
    def setupUi(self, AddNewForm):
        if not AddNewForm.objectName():
            AddNewForm.setObjectName(u"AddNewForm")
        AddNewForm.resize(400, 167)
        self.gridLayout = QGridLayout(AddNewForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.finish_button = QPushButton(AddNewForm)
        self.finish_button.setObjectName(u"finish_button")

        self.gridLayout.addWidget(self.finish_button, 4, 2, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 2, 1, 1)

        self.name = QLineEdit(AddNewForm)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 3, 1, 1)

        self.label_2 = QLabel(AddNewForm)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.add_another_button = QPushButton(AddNewForm)
        self.add_another_button.setObjectName(u"add_another_button")

        self.gridLayout.addWidget(self.add_another_button, 4, 0, 1, 2)

        self.label = QLabel(AddNewForm)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(AddNewForm)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.unit = QLineEdit(AddNewForm)
        self.unit.setObjectName(u"unit")

        self.gridLayout.addWidget(self.unit, 2, 1, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 1, 1, 1)

        self.quantity = QLineEdit(AddNewForm)
        self.quantity.setObjectName(u"quantity")

        self.gridLayout.addWidget(self.quantity, 1, 1, 1, 3)

        self.status_label = QLabel(AddNewForm)
        self.status_label.setObjectName(u"status_label")

        self.gridLayout.addWidget(self.status_label, 3, 0, 1, 4)

        QWidget.setTabOrder(self.name, self.quantity)
        QWidget.setTabOrder(self.quantity, self.unit)
        QWidget.setTabOrder(self.unit, self.add_another_button)
        QWidget.setTabOrder(self.add_another_button, self.finish_button)

        self.retranslateUi(AddNewForm)

        self.add_another_button.setDefault(True)


        QMetaObject.connectSlotsByName(AddNewForm)
    # setupUi

    def retranslateUi(self, AddNewForm):
        AddNewForm.setWindowTitle(QCoreApplication.translate("AddNewForm", u"Form", None))
        self.finish_button.setText(QCoreApplication.translate("AddNewForm", u"Finish", None))
        self.label_2.setText(QCoreApplication.translate("AddNewForm", u"quantity", None))
        self.add_another_button.setText(QCoreApplication.translate("AddNewForm", u"Add Another", None))
        self.label.setText(QCoreApplication.translate("AddNewForm", u"name", None))
        self.label_3.setText(QCoreApplication.translate("AddNewForm", u"unit", None))
        self.status_label.setText("")
    # retranslateUi

