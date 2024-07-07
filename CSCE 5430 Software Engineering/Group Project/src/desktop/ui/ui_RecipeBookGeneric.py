# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecipeBookGenericWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_RecipeBookGenericWidget(object):
    def setupUi(self, RecipeBookGenericWidget):
        if not RecipeBookGenericWidget.objectName():
            RecipeBookGenericWidget.setObjectName(u"RecipeBookGenericWidget")
        RecipeBookGenericWidget.resize(977, 587)
        self.formLayout = QFormLayout(RecipeBookGenericWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.add_to_meal_plan = QCheckBox(RecipeBookGenericWidget)
        self.add_to_meal_plan.setObjectName(u"add_to_meal_plan")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.add_to_meal_plan)

        self.label = QLabel(RecipeBookGenericWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(RecipeBookGenericWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.recipes_list = QListWidget(RecipeBookGenericWidget)
        self.recipes_list.setObjectName(u"recipes_list")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.recipes_list)

        self.recipe_view = QTextBrowser(RecipeBookGenericWidget)
        self.recipe_view.setObjectName(u"recipe_view")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.recipe_view)

        self.remove_recipe = QPushButton(RecipeBookGenericWidget)
        self.remove_recipe.setObjectName(u"remove_recipe")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.remove_recipe)

        self.delete_book = QPushButton(RecipeBookGenericWidget)
        self.delete_book.setObjectName(u"delete_book")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.delete_book)


        self.retranslateUi(RecipeBookGenericWidget)

        QMetaObject.connectSlotsByName(RecipeBookGenericWidget)
    # setupUi

    def retranslateUi(self, RecipeBookGenericWidget):
        RecipeBookGenericWidget.setWindowTitle(QCoreApplication.translate("RecipeBookGenericWidget", u"Form", None))
        self.add_to_meal_plan.setText(QCoreApplication.translate("RecipeBookGenericWidget", u"Add to Meal Plan", None))
        self.label.setText(QCoreApplication.translate("RecipeBookGenericWidget", u"Recipes", None))
        self.label_2.setText(QCoreApplication.translate("RecipeBookGenericWidget", u"Current Recipe", None))
        self.remove_recipe.setText(QCoreApplication.translate("RecipeBookGenericWidget", u"Remove Recipe From Book", None))
        self.delete_book.setText(QCoreApplication.translate("RecipeBookGenericWidget", u"Delete Book", None))
    # retranslateUi

