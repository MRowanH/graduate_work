# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrivateRecipesWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_PrivateRecipesWidget(object):
    def setupUi(self, PrivateRecipesWidget):
        if not PrivateRecipesWidget.objectName():
            PrivateRecipesWidget.setObjectName(u"PrivateRecipesWidget")
        PrivateRecipesWidget.resize(977, 587)
        self.formLayout = QFormLayout(PrivateRecipesWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.add_to_meal_plan = QCheckBox(PrivateRecipesWidget)
        self.add_to_meal_plan.setObjectName(u"add_to_meal_plan")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.add_to_meal_plan)

        self.label = QLabel(PrivateRecipesWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(PrivateRecipesWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.recipes_list = QListWidget(PrivateRecipesWidget)
        self.recipes_list.setObjectName(u"recipes_list")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.recipes_list)

        self.recipe_view = QTextBrowser(PrivateRecipesWidget)
        self.recipe_view.setObjectName(u"recipe_view")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.recipe_view)

        self.recipe_books_cboxes = QGroupBox(PrivateRecipesWidget)
        self.recipe_books_cboxes.setObjectName(u"recipe_books_cboxes")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.recipe_books_cboxes)


        self.retranslateUi(PrivateRecipesWidget)

        QMetaObject.connectSlotsByName(PrivateRecipesWidget)
    # setupUi

    def retranslateUi(self, PrivateRecipesWidget):
        PrivateRecipesWidget.setWindowTitle(QCoreApplication.translate("PrivateRecipesWidget", u"Form", None))
        self.add_to_meal_plan.setText(QCoreApplication.translate("PrivateRecipesWidget", u"Add to Meal Plan", None))
        self.label.setText(QCoreApplication.translate("PrivateRecipesWidget", u"Recipes", None))
        self.label_2.setText(QCoreApplication.translate("PrivateRecipesWidget", u"Current Recipe", None))
        self.recipe_books_cboxes.setTitle(QCoreApplication.translate("PrivateRecipesWidget", u"In Recipe Books", None))
    # retranslateUi

