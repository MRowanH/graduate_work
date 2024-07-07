# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateABookWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_CreateABookWidget(object):
    def setupUi(self, CreateABookWidget):
        if not CreateABookWidget.objectName():
            CreateABookWidget.setObjectName(u"CreateABookWidget")
        CreateABookWidget.resize(1174, 589)
        self.formLayout = QFormLayout(CreateABookWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(CreateABookWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.label_2 = QLabel(CreateABookWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.title_input = QLineEdit(CreateABookWidget)
        self.title_input.setObjectName(u"title_input")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.title_input)

        self.commit_button = QPushButton(CreateABookWidget)
        self.commit_button.setObjectName(u"commit_button")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.commit_button)


        self.retranslateUi(CreateABookWidget)

        QMetaObject.connectSlotsByName(CreateABookWidget)
    # setupUi

    def retranslateUi(self, CreateABookWidget):
        CreateABookWidget.setWindowTitle(QCoreApplication.translate("CreateABookWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("CreateABookWidget", u"Create A New Recipe Book", None))
        self.label_2.setText(QCoreApplication.translate("CreateABookWidget", u"Title:", None))
        self.commit_button.setText(QCoreApplication.translate("CreateABookWidget", u"Create Book", None))
    # retranslateUi

