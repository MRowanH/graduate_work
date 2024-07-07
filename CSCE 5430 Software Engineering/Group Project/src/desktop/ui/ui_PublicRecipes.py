# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PublicRecipesWidget.ui'
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

class Ui_PublicRecipesWidget(object):
    def setupUi(self, PublicRecipesWidget):
        if not PublicRecipesWidget.objectName():
            PublicRecipesWidget.setObjectName(u"PublicRecipesWidget")
        PublicRecipesWidget.resize(977, 587)
        self.formLayout = QFormLayout(PublicRecipesWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(PublicRecipesWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(PublicRecipesWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.add_to_meal_plan = QCheckBox(PublicRecipesWidget)
        self.add_to_meal_plan.setObjectName(u"add_to_meal_plan")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.add_to_meal_plan)

        self.recipes_list = QListWidget(PublicRecipesWidget)
        self.recipes_list.setObjectName(u"recipes_list")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.recipes_list)

        self.recipe_view = QTextBrowser(PublicRecipesWidget)
        self.recipe_view.setObjectName(u"recipe_view")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.recipe_view)

        self.recipe_books_cboxes = QGroupBox(PublicRecipesWidget)
        self.recipe_books_cboxes.setObjectName(u"recipe_books_cboxes")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.recipe_books_cboxes)


        self.retranslateUi(PublicRecipesWidget)

        QMetaObject.connectSlotsByName(PublicRecipesWidget)
    # setupUi

    def retranslateUi(self, PublicRecipesWidget):
        PublicRecipesWidget.setWindowTitle(QCoreApplication.translate("PublicRecipesWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("PublicRecipesWidget", u"Recipes", None))
        self.label_2.setText(QCoreApplication.translate("PublicRecipesWidget", u"Current Recipe", None))
        self.add_to_meal_plan.setText(QCoreApplication.translate("PublicRecipesWidget", u"Add to Meal Plan", None))
        self.recipe_books_cboxes.setTitle(QCoreApplication.translate("PublicRecipesWidget", u"In Recipe Books", None))
    # retranslateUi

