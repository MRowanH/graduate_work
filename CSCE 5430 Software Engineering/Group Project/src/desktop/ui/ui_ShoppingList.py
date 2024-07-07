# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShoppingListWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_ShoppingListWidget(object):
    def setupUi(self, ShoppingListWidget):
        if not ShoppingListWidget.objectName():
            ShoppingListWidget.setObjectName(u"ShoppingListWidget")
        ShoppingListWidget.resize(912, 718)
        self.gridLayout = QGridLayout(ShoppingListWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.shopping_list = QTreeWidget(ShoppingListWidget)
        self.shopping_list.setObjectName(u"shopping_list")

        self.gridLayout.addWidget(self.shopping_list, 4, 2, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)

        self.remove_button = QPushButton(ShoppingListWidget)
        self.remove_button.setObjectName(u"remove_button")

        self.gridLayout.addWidget(self.remove_button, 5, 3, 1, 1)

        self.add_button = QPushButton(ShoppingListWidget)
        self.add_button.setObjectName(u"add_button")

        self.gridLayout.addWidget(self.add_button, 5, 2, 1, 1)

        self.update_inventory_button = QPushButton(ShoppingListWidget)
        self.update_inventory_button.setObjectName(u"update_inventory_button")

        self.gridLayout.addWidget(self.update_inventory_button, 4, 4, 1, 1)


        self.retranslateUi(ShoppingListWidget)

        QMetaObject.connectSlotsByName(ShoppingListWidget)
    # setupUi

    def retranslateUi(self, ShoppingListWidget):
        ShoppingListWidget.setWindowTitle(QCoreApplication.translate("ShoppingListWidget", u"Form", None))
        ___qtreewidgetitem = self.shopping_list.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("ShoppingListWidget", u"Purchased", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("ShoppingListWidget", u"Units", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ShoppingListWidget", u"Quantity", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ShoppingListWidget", u"Item", None));
        self.remove_button.setText(QCoreApplication.translate("ShoppingListWidget", u"Remove", None))
        self.add_button.setText(QCoreApplication.translate("ShoppingListWidget", u"Add", None))
        self.update_inventory_button.setText(QCoreApplication.translate("ShoppingListWidget", u"Update Inventory", None))
    # retranslateUi

