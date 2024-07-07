# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InventoryWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Inventory(object):
    def setupUi(self, Inventory):
        if not Inventory.objectName():
            Inventory.setObjectName(u"Inventory")
        Inventory.resize(1668, 868)
        self.label_2 = QLabel(Inventory)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 40, 241, 20))
        self.label_2.setStyleSheet(u"color:rgb(0, 85, 0)")
        self.label = QLabel(Inventory)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 0, 301, 41))
        self.label.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"color: rgb(85, 0, 127);")
        self.Delete_button = QPushButton(Inventory)
        self.Delete_button.setObjectName(u"Delete_button")
        self.Delete_button.setGeometry(QRect(900, 70, 31, 401))
        self.Delete_button.setLayoutDirection(Qt.LeftToRight)
        self.Delete_button.setStyleSheet(u"\n"
"background-color: rgb(170, 0, 0);")
        self.Add_button = QPushButton(Inventory)
        self.Add_button.setObjectName(u"Add_button")
        self.Add_button.setGeometry(QRect(350, 70, 31, 401))
        self.Add_button.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.remind_label = QLabel(Inventory)
        self.remind_label.setObjectName(u"remind_label")
        self.remind_label.setGeometry(QRect(360, 0, 531, 51))
        self.remind_label.setStyleSheet(u"color: rgb(0, 255, 0)")
        self.label_3 = QLabel(Inventory)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(970, -30, 71, 511))
        self.label_3.setMinimumSize(QSize(0, 14))
        self.label_3.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.listWidget = QListWidget(Inventory)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(40, 70, 271, 398))
        self.tableWidget = QTableWidget(Inventory)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(420, 70, 441, 398))

        self.retranslateUi(Inventory)

        QMetaObject.connectSlotsByName(Inventory)
    # setupUi

    def retranslateUi(self, Inventory):
        Inventory.setWindowTitle(QCoreApplication.translate("Inventory", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Inventory", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Then  click the green button :)</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Inventory", u"<html><head/><body><p><span style=\" font-weight:600;\">Please choose an item which you have at home <br/>each per time in </span><span style=\" font-weight:600; font-style:italic;\">the </span><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">i</span><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">ngredients</span><span style=\" font-size:14pt; font-weight:600;\"> list</span><span style=\" font-weight:600;\"> below </span></p></body></html>", None))
        self.Delete_button.setText(QCoreApplication.translate("Inventory", u"Delete", None))
        self.Add_button.setText(QCoreApplication.translate("Inventory", u"Add", None))
        self.remind_label.setText(QCoreApplication.translate("Inventory", u"<html><head/><body><p><span style=\" font-weight:600;\">You can save a lot of time and money by checking what you have at your home<br/>and add them to the </span><span style=\" font-size:14pt; font-weight:600;\">table</span><span style=\" font-weight:600;\"> below</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Inventory", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Please </span></p><p><span style=\" font-weight:600; font-style:italic;\">click </span></p><p><span style=\" font-weight:600; font-style:italic;\">on </span></p><p><span style=\" font-weight:600; font-style:italic;\">the </span></p><p><span style=\" font-weight:600; font-style:italic;\">item </span></p><p><span style=\" font-weight:600; font-style:italic;\">which </span></p><p><span style=\" font-weight:600; font-style:italic;\">you </span></p><p><span style=\" font-weight:600; font-style:italic;\">want to </span></p><p><span style=\" font-weight:600; font-style:italic;\">delete then </span></p><p><span style=\" font-weight:600; font-style:italic;\">click </span></p><p><span style=\" font-weight:600; font-style:italic;\">the red </span></p><p><span style=\" font-weight:600; font-style:italic;\">button </span></p><p><span style=\" font-weight:600; font-style:italic;\">:)</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Inventory", u"Item", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Inventory", u"Quantity", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Inventory", u"Unit", None));
    # retranslateUi

