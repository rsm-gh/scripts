# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadingDialog(object):
    def setupUi(self, LoadingDialog):
        LoadingDialog.setObjectName("LoadingDialog")
        LoadingDialog.resize(500, 464)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadingDialog.sizePolicy().hasHeightForWidth())
        LoadingDialog.setSizePolicy(sizePolicy)
        LoadingDialog.setMinimumSize(QtCore.QSize(500, 408))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/img/loading_logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoadingDialog.setWindowIcon(icon)
        LoadingDialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(LoadingDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(LoadingDialog)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/logos/img/loading_logo.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(LoadingDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(LoadingDialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(LoadingDialog)
        QtCore.QMetaObject.connectSlotsByName(LoadingDialog)

    def retranslateUi(self, LoadingDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadingDialog.setWindowTitle(_translate("LoadingDialog", "Loading Dialog"))
        self.label.setText(_translate("LoadingDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">LOADING EXEMPLE</span></p></body></html>"))


from loading_window import ressource_rc
