# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MealPlanWidget.ui'
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
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MealPlanWidget(object):
    def setupUi(self, MealPlanWidget):
        if not MealPlanWidget.objectName():
            MealPlanWidget.setObjectName(u"MealPlanWidget")
        MealPlanWidget.resize(1132, 738)
        self.gridLayout = QGridLayout(MealPlanWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(MealPlanWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.recipe_tree = QTreeWidget(MealPlanWidget)
        self.recipe_tree.setObjectName(u"recipe_tree")

        self.gridLayout.addWidget(self.recipe_tree, 1, 0, 1, 1)

        self.label = QLabel(MealPlanWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.meal_plan_tree = QTreeWidget(MealPlanWidget)
        self.meal_plan_tree.setObjectName(u"meal_plan_tree")

        self.gridLayout.addWidget(self.meal_plan_tree, 1, 1, 1, 1)


        self.retranslateUi(MealPlanWidget)

        QMetaObject.connectSlotsByName(MealPlanWidget)
    # setupUi

    def retranslateUi(self, MealPlanWidget):
        MealPlanWidget.setWindowTitle(QCoreApplication.translate("MealPlanWidget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("MealPlanWidget", u"Meal Plan", None))
        ___qtreewidgetitem = self.recipe_tree.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MealPlanWidget", u"hidden_id", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MealPlanWidget", u"Select", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MealPlanWidget", u"Units", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MealPlanWidget", u"Quantity", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MealPlanWidget", u"Serves", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MealPlanWidget", u"Name", None));
        self.label.setText(QCoreApplication.translate("MealPlanWidget", u"Recipes", None))
        ___qtreewidgetitem1 = self.meal_plan_tree.headerItem()
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MealPlanWidget", u"asdfasdf", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MealPlanWidget", u"Select", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MealPlanWidget", u"Units", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MealPlanWidget", u"Quantity", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MealPlanWidget", u"Serves", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MealPlanWidget", u"Name", None));
    # retranslateUi

