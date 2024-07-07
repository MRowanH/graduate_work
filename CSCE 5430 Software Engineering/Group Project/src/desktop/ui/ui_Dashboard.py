# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(1154, 766)
        self.gridLayout = QGridLayout(Dashboard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Dashboard)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.recipe_tree = QTreeWidget(Dashboard)
        self.recipe_tree.setObjectName(u"recipe_tree")

        self.gridLayout.addWidget(self.recipe_tree, 1, 0, 3, 1)

        self.meal_plan_tree = QTreeWidget(Dashboard)
        self.meal_plan_tree.setObjectName(u"meal_plan_tree")

        self.gridLayout.addWidget(self.meal_plan_tree, 1, 2, 1, 1)

        self.label_2 = QLabel(Dashboard)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(Dashboard)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(Dashboard)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.inventory_table = QTableWidget(Dashboard)
        if (self.inventory_table.columnCount() < 3):
            self.inventory_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.inventory_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.inventory_table.setObjectName(u"inventory_table")

        self.gridLayout.addWidget(self.inventory_table, 3, 2, 1, 1)

        self.shopping_list_tree = QTreeWidget(Dashboard)
        self.shopping_list_tree.setObjectName(u"shopping_list_tree")

        self.gridLayout.addWidget(self.shopping_list_tree, 1, 3, 3, 1)


        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Dashboard", u"Shopping List", None))
        ___qtreewidgetitem = self.recipe_tree.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("Dashboard", u"hidden_id", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Dashboard", u"Select", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Dashboard", u"Units", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Dashboard", u"Quantity", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Dashboard", u"Serves", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dashboard", u"Name", None));
        ___qtreewidgetitem1 = self.meal_plan_tree.headerItem()
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("Dashboard", u"hidden_id", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("Dashboard", u"Select", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("Dashboard", u"Unit", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Dashboard", u"Quantity", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Dashboard", u"Serves", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Dashboard", u"Name", None));
        self.label_2.setText(QCoreApplication.translate("Dashboard", u"Meal Plan", None))
        self.label.setText(QCoreApplication.translate("Dashboard", u"Recipes", None))
        self.label_4.setText(QCoreApplication.translate("Dashboard", u"Inventory", None))
        ___qtablewidgetitem = self.inventory_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dashboard", u"Item", None));
        ___qtablewidgetitem1 = self.inventory_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dashboard", u"Quantity", None));
        ___qtablewidgetitem2 = self.inventory_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dashboard", u"Unit", None));
        ___qtreewidgetitem2 = self.shopping_list_tree.headerItem()
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("Dashboard", u"Purchased", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("Dashboard", u"Units", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("Dashboard", u"Quantity", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Dashboard", u"Item", None));
    # retranslateUi

