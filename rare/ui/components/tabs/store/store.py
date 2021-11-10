# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/store/store.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_ShopWidget(object):
    def setupUi(self, ShopWidget):
        ShopWidget.setObjectName("ShopWidget")
        ShopWidget.resize(850, 572)
        ShopWidget.setWindowTitle("Form")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(ShopWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(ShopWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 828, 550))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.free_game_group_box = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.free_game_group_box.sizePolicy().hasHeightForWidth())
        self.free_game_group_box.setSizePolicy(sizePolicy)
        self.free_game_group_box.setObjectName("free_game_group_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.free_game_group_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.free_stack = QtWidgets.QStackedWidget(self.free_game_group_box)
        self.free_stack.setObjectName("free_stack")
        self.free_widget = QtWidgets.QWidget()
        self.free_widget.setObjectName("free_widget")
        self.free_stack.addWidget(self.free_widget)
        self.verticalLayout_3.addWidget(self.free_stack)
        self.verticalLayout.addWidget(self.free_game_group_box)
        self.discounts_gb = QtWidgets.QGroupBox(self.widget)
        self.discounts_gb.setObjectName("discounts_gb")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.discounts_gb)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.discount_stack = QtWidgets.QStackedWidget(self.discounts_gb)
        self.discount_stack.setObjectName("discount_stack")
        self.discount_widget = QtWidgets.QWidget()
        self.discount_widget.setObjectName("discount_widget")
        self.discount_stack.addWidget(self.discount_widget)
        self.verticalLayout_6.addWidget(self.discount_stack)
        self.verticalLayout.addWidget(self.discounts_gb)
        self.filter_game_gb = QtWidgets.QGroupBox(self.widget)
        self.filter_game_gb.setObjectName("filter_game_gb")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.filter_game_gb)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.game_stack = QtWidgets.QStackedWidget(self.filter_game_gb)
        self.game_stack.setObjectName("game_stack")
        self.game_widget = QtWidgets.QWidget()
        self.game_widget.setObjectName("game_widget")
        self.game_stack.addWidget(self.game_widget)
        self.verticalLayout_4.addWidget(self.game_stack)
        self.verticalLayout.addWidget(self.filter_game_gb)
        self.horizontalLayout.addWidget(self.widget)
        self.filter_gb = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_gb.sizePolicy().hasHeightForWidth())
        self.filter_gb.setSizePolicy(sizePolicy)
        self.filter_gb.setMinimumSize(QtCore.QSize(150, 0))
        self.filter_gb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.filter_gb.setObjectName("filter_gb")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.filter_gb)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reset_button = QtWidgets.QPushButton(self.filter_gb)
        self.reset_button.setObjectName("reset_button")
        self.verticalLayout_2.addWidget(self.reset_button)
        self.price_gb = QtWidgets.QGroupBox(self.filter_gb)
        self.price_gb.setObjectName("price_gb")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.price_gb)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.none_price = QtWidgets.QRadioButton(self.price_gb)
        self.none_price.setChecked(True)
        self.none_price.setObjectName("none_price")
        self.verticalLayout_9.addWidget(self.none_price)
        self.free_button = QtWidgets.QRadioButton(self.price_gb)
        self.free_button.setObjectName("free_button")
        self.verticalLayout_9.addWidget(self.free_button)
        self.under10 = QtWidgets.QRadioButton(self.price_gb)
        self.under10.setObjectName("under10")
        self.verticalLayout_9.addWidget(self.under10)
        self.under20 = QtWidgets.QRadioButton(self.price_gb)
        self.under20.setObjectName("under20")
        self.verticalLayout_9.addWidget(self.under20)
        self.under30 = QtWidgets.QRadioButton(self.price_gb)
        self.under30.setObjectName("under30")
        self.verticalLayout_9.addWidget(self.under30)
        self.above = QtWidgets.QRadioButton(self.price_gb)
        self.above.setObjectName("above")
        self.verticalLayout_9.addWidget(self.above)
        self.on_discount = QtWidgets.QCheckBox(self.price_gb)
        self.on_discount.setObjectName("on_discount")
        self.verticalLayout_9.addWidget(self.on_discount)
        self.verticalLayout_2.addWidget(self.price_gb)
        self.platform_gb = QtWidgets.QGroupBox(self.filter_gb)
        self.platform_gb.setObjectName("platform_gb")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.platform_gb)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_2.addWidget(self.platform_gb)
        self.genre_gb = QtWidgets.QGroupBox(self.filter_gb)
        self.genre_gb.setObjectName("genre_gb")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.genre_gb)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_2.addWidget(self.genre_gb)
        self.type_gb = QtWidgets.QGroupBox(self.filter_gb)
        self.type_gb.setObjectName("type_gb")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.type_gb)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_2.addWidget(self.type_gb)
        self.others_gb = QtWidgets.QGroupBox(self.filter_gb)
        self.others_gb.setObjectName("others_gb")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.others_gb)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_2.addWidget(self.others_gb)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.filter_gb)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ShopWidget)
        QtCore.QMetaObject.connectSlotsByName(ShopWidget)

    def retranslateUi(self, ShopWidget):
        _translate = QtCore.QCoreApplication.translate
        self.free_game_group_box.setTitle(_translate("ShopWidget", "Free Games"))
        self.discounts_gb.setTitle(_translate("ShopWidget", "Discounts from your wishlist"))
        self.filter_game_gb.setTitle(_translate("ShopWidget", "Games"))
        self.filter_gb.setTitle(_translate("ShopWidget", "Filter"))
        self.reset_button.setText(_translate("ShopWidget", "Reset"))
        self.price_gb.setTitle(_translate("ShopWidget", "Price"))
        self.none_price.setText(_translate("ShopWidget", "None"))
        self.free_button.setText(_translate("ShopWidget", "Free"))
        self.under10.setText(_translate("ShopWidget", "Under 10"))
        self.under20.setText(_translate("ShopWidget", "Under 20"))
        self.under30.setText(_translate("ShopWidget", "Under 30"))
        self.above.setText(_translate("ShopWidget", "14.99 and above"))
        self.on_discount.setText(_translate("ShopWidget", "Discount"))
        self.platform_gb.setTitle(_translate("ShopWidget", "Platform"))
        self.genre_gb.setTitle(_translate("ShopWidget", "Genre"))
        self.type_gb.setTitle(_translate("ShopWidget", "Type"))
        self.others_gb.setTitle(_translate("ShopWidget", "Other Tags"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShopWidget = QtWidgets.QWidget()
    ui = Ui_ShopWidget()
    ui.setupUi(ShopWidget)
    ShopWidget.show()
    sys.exit(app.exec_())
