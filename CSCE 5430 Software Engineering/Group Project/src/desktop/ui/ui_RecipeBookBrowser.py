# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecipeBookBrowserWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTabWidget,
    QWidget)

class Ui_RecipeBookBrowserWidget(object):
    def setupUi(self, RecipeBookBrowserWidget):
        if not RecipeBookBrowserWidget.objectName():
            RecipeBookBrowserWidget.setObjectName(u"RecipeBookBrowserWidget")
        RecipeBookBrowserWidget.resize(977, 587)
        self.gridLayout = QGridLayout(RecipeBookBrowserWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.browser = QTabWidget(RecipeBookBrowserWidget)
        self.browser.setObjectName(u"browser")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.browser.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.browser.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.browser, 0, 0, 1, 1)


        self.retranslateUi(RecipeBookBrowserWidget)

        QMetaObject.connectSlotsByName(RecipeBookBrowserWidget)
    # setupUi

    def retranslateUi(self, RecipeBookBrowserWidget):
        RecipeBookBrowserWidget.setWindowTitle(QCoreApplication.translate("RecipeBookBrowserWidget", u"Form", None))
        self.browser.setTabText(self.browser.indexOf(self.tab_3), QCoreApplication.translate("RecipeBookBrowserWidget", u"Tab 1", None))
        self.browser.setTabText(self.browser.indexOf(self.tab_4), QCoreApplication.translate("RecipeBookBrowserWidget", u"Tab 2", None))
    # retranslateUi

