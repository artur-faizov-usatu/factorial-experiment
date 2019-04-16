# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\resources\gui\add_factor.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddFactorDialog(object):
    def setupUi(self, AddFactorDialog):
        AddFactorDialog.setObjectName("AddFactorDialog")
        AddFactorDialog.resize(301, 331)
        self.gridLayout = QtWidgets.QGridLayout(AddFactorDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(AddFactorDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(AddFactorDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.factor_name_le = QtWidgets.QLineEdit(self.groupBox)
        self.factor_name_le.setObjectName("factor_name_le")
        self.verticalLayout.addWidget(self.factor_name_le)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.max_factor_value_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.max_factor_value_sb.setObjectName("max_factor_value_sb")
        self.verticalLayout_3.addWidget(self.max_factor_value_sb)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.factor_var_interval_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.factor_var_interval_sb.setObjectName("factor_var_interval_sb")
        self.verticalLayout_3.addWidget(self.factor_var_interval_sb)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.zero_level_value_lbl = QtWidgets.QLabel(self.groupBox)
        self.zero_level_value_lbl.setObjectName("zero_level_value_lbl")
        self.verticalLayout_3.addWidget(self.zero_level_value_lbl, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.min_factor_value_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.min_factor_value_sb.setObjectName("min_factor_value_sb")
        self.verticalLayout_2.addWidget(self.min_factor_value_sb)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(AddFactorDialog)
        self.buttonBox.accepted.connect(AddFactorDialog.accept)
        self.buttonBox.rejected.connect(AddFactorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddFactorDialog)

    def retranslateUi(self, AddFactorDialog):
        _translate = QtCore.QCoreApplication.translate
        AddFactorDialog.setWindowTitle(_translate("AddFactorDialog", "Добавить фактор"))
        self.groupBox.setTitle(_translate("AddFactorDialog", "Параметры"))
        self.label.setText(_translate("AddFactorDialog", "Название"))
        self.label_3.setText(_translate("AddFactorDialog", "Максимальное значение"))
        self.label_5.setText(_translate("AddFactorDialog", "Интервал варьирования"))
        self.label_4.setText(_translate("AddFactorDialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Нулевой уровень</span></p></body></html>"))
        self.zero_level_value_lbl.setText(_translate("AddFactorDialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#48b515;\">0</span></p></body></html>"))
        self.label_2.setText(_translate("AddFactorDialog", "Минимальное значение"))


