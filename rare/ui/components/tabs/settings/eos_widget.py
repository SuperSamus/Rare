# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/settings/eos_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EosWidget(object):
    def setupUi(self, EosWidget):
        EosWidget.setObjectName("EosWidget")
        EosWidget.resize(1128, 319)
        EosWidget.setWindowTitle("GroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(EosWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_stack = QtWidgets.QStackedWidget(EosWidget)
        self.info_stack.setObjectName("info_stack")
        self.horizontalLayout.addWidget(self.info_stack)
        self.enable_gb = QtWidgets.QGroupBox(EosWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable_gb.sizePolicy().hasHeightForWidth())
        self.enable_gb.setSizePolicy(sizePolicy)
        self.enable_gb.setObjectName("enable_gb")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.enable_gb)
        self.verticalLayout.setObjectName("verticalLayout")
        self.select_pfx_combo = QtWidgets.QComboBox(self.enable_gb)
        self.select_pfx_combo.setObjectName("select_pfx_combo")
        self.verticalLayout.addWidget(self.select_pfx_combo, 0, QtCore.Qt.AlignTop)
        self.enabled_cb = QtWidgets.QCheckBox(self.enable_gb)
        self.enabled_cb.setObjectName("enabled_cb")
        self.verticalLayout.addWidget(self.enabled_cb)
        self.enabled_info_label = QtWidgets.QLabel(self.enable_gb)
        font = QtGui.QFont()
        font.setItalic(True)
        self.enabled_info_label.setFont(font)
        self.enabled_info_label.setText("")
        self.enabled_info_label.setObjectName("enabled_info_label")
        self.verticalLayout.addWidget(self.enabled_info_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.enable_gb)
        self.installed_info_gb = QtWidgets.QGroupBox(EosWidget)
        self.installed_info_gb.setObjectName("installed_info_gb")
        self.formLayout = QtWidgets.QFormLayout(self.installed_info_gb)
        self.formLayout.setObjectName("formLayout")
        self.installed_version_info_lbl = QtWidgets.QLabel(self.installed_info_gb)
        self.installed_version_info_lbl.setObjectName("installed_version_info_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.installed_version_info_lbl)
        self.installed_version_lbl = QtWidgets.QLabel(self.installed_info_gb)
        self.installed_version_lbl.setText("TextLabel")
        self.installed_version_lbl.setObjectName("installed_version_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.installed_version_lbl)
        self.installed_path_info_lbl = QtWidgets.QLabel(self.installed_info_gb)
        self.installed_path_info_lbl.setObjectName("installed_path_info_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.installed_path_info_lbl)
        self.installed_path_lbl = QtWidgets.QLabel(self.installed_info_gb)
        self.installed_path_lbl.setText("TextLabel")
        self.installed_path_lbl.setObjectName("installed_path_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.installed_path_lbl)
        self.update_available_info_label = QtWidgets.QLabel(self.installed_info_gb)
        self.update_available_info_label.setObjectName("update_available_info_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.update_available_info_label)
        self.update_check_button = QtWidgets.QPushButton(self.installed_info_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_check_button.sizePolicy().hasHeightForWidth())
        self.update_check_button.setSizePolicy(sizePolicy)
        self.update_check_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.update_check_button.setObjectName("update_check_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.update_check_button)
        self.uninstall_info_label = QtWidgets.QLabel(self.installed_info_gb)
        self.uninstall_info_label.setObjectName("uninstall_info_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.uninstall_info_label)
        self.uninstall_button = QtWidgets.QPushButton(self.installed_info_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uninstall_button.sizePolicy().hasHeightForWidth())
        self.uninstall_button.setSizePolicy(sizePolicy)
        self.uninstall_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.uninstall_button.setObjectName("uninstall_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.uninstall_button)
        self.update_button = QtWidgets.QPushButton(self.installed_info_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.update_button.setObjectName("update_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.update_button)
        self.update_info_lbl = QtWidgets.QLabel(self.installed_info_gb)
        self.update_info_lbl.setObjectName("update_info_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.update_info_lbl)
        self.horizontalLayout.addWidget(self.installed_info_gb)
        self.install_overlay_gb = QtWidgets.QGroupBox(EosWidget)
        self.install_overlay_gb.setObjectName("install_overlay_gb")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.install_overlay_gb)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.install_overlay_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.install_button = QtWidgets.QPushButton(self.install_overlay_gb)
        self.install_button.setObjectName("install_button")
        self.verticalLayout_4.addWidget(self.install_button)
        self.horizontalLayout.addWidget(self.install_overlay_gb)

        self.retranslateUi(EosWidget)
        self.info_stack.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(EosWidget)

    def retranslateUi(self, EosWidget):
        _translate = QtCore.QCoreApplication.translate
        EosWidget.setTitle(_translate("EosWidget", "Epic Overlay settings"))
        self.enable_gb.setTitle(_translate("EosWidget", "Enable / Disable"))
        self.enabled_cb.setText(_translate("EosWidget", "Activated"))
        self.installed_info_gb.setTitle(_translate("EosWidget", "Installed Info"))
        self.installed_version_info_lbl.setText(_translate("EosWidget", "Installed version:"))
        self.installed_path_info_lbl.setText(_translate("EosWidget", "Installed path"))
        self.update_available_info_label.setText(_translate("EosWidget", "Updates"))
        self.update_check_button.setText(_translate("EosWidget", "Check for Update"))
        self.uninstall_info_label.setText(_translate("EosWidget", "Uninstall"))
        self.uninstall_button.setText(_translate("EosWidget", "Uninstall"))
        self.update_button.setText(_translate("EosWidget", "Update"))
        self.update_info_lbl.setText(_translate("EosWidget", "Install Update"))
        self.install_overlay_gb.setTitle(_translate("EosWidget", "Install Overlay"))
        self.label.setText(_translate("EosWidget", "No overlays are installed"))
        self.install_button.setText(_translate("EosWidget", "Install"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EosWidget = QtWidgets.QGroupBox()
    ui = Ui_EosWidget()
    ui.setupUi(EosWidget)
    EosWidget.show()
    sys.exit(app.exec_())
