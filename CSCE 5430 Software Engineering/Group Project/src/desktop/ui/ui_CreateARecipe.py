# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateARecipeWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_CreateARecipeWidget(object):
    def setupUi(self, CreateARecipeWidget):
        if not CreateARecipeWidget.objectName():
            CreateARecipeWidget.setObjectName(u"CreateARecipeWidget")
        CreateARecipeWidget.resize(1174, 589)
        self.formLayout = QFormLayout(CreateARecipeWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(CreateARecipeWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.title_input = QLineEdit(CreateARecipeWidget)
        self.title_input.setObjectName(u"title_input")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.title_input)

        self.label_8 = QLabel(CreateARecipeWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.public_private_combo = QComboBox(CreateARecipeWidget)
        self.public_private_combo.setObjectName(u"public_private_combo")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.public_private_combo)

        self.vegetarian_check = QCheckBox(CreateARecipeWidget)
        self.vegetarian_check.setObjectName(u"vegetarian_check")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.vegetarian_check)

        self.vegan_check = QCheckBox(CreateARecipeWidget)
        self.vegan_check.setObjectName(u"vegan_check")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.vegan_check)

        self.label_3 = QLabel(CreateARecipeWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.label_3)

        self.ingredients_input = QTableWidget(CreateARecipeWidget)
        self.ingredients_input.setObjectName(u"ingredients_input")

        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.ingredients_input)

        self.label = QLabel(CreateARecipeWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.commit_button = QPushButton(CreateARecipeWidget)
        self.commit_button.setObjectName(u"commit_button")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.commit_button)

        self.label_7 = QLabel(CreateARecipeWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_7)

        self.instructions_input = QTextEdit(CreateARecipeWidget)
        self.instructions_input.setObjectName(u"instructions_input")

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.instructions_input)

        self.label_4 = QLabel(CreateARecipeWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_4)

        self.serves_input = QLineEdit(CreateARecipeWidget)
        self.serves_input.setObjectName(u"serves_input")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.serves_input)


        self.retranslateUi(CreateARecipeWidget)

        QMetaObject.connectSlotsByName(CreateARecipeWidget)
    # setupUi

    def retranslateUi(self, CreateARecipeWidget):
        CreateARecipeWidget.setWindowTitle(QCoreApplication.translate("CreateARecipeWidget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("CreateARecipeWidget", u"Title:", None))
        self.label_8.setText(QCoreApplication.translate("CreateARecipeWidget", u"This recipe is:", None))
        self.vegetarian_check.setText(QCoreApplication.translate("CreateARecipeWidget", u"Vegetarian", None))
        self.vegan_check.setText(QCoreApplication.translate("CreateARecipeWidget", u"Vegan", None))
        self.label_3.setText(QCoreApplication.translate("CreateARecipeWidget", u"Ingredients:", None))
        self.label.setText(QCoreApplication.translate("CreateARecipeWidget", u"Create A New Recipe", None))
        self.commit_button.setText(QCoreApplication.translate("CreateARecipeWidget", u"Submit Recipe", None))
        self.label_7.setText(QCoreApplication.translate("CreateARecipeWidget", u"Instructions:", None))
        self.label_4.setText(QCoreApplication.translate("CreateARecipeWidget", u"Serves: ", None))
    # retranslateUi

