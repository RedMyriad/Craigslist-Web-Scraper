# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Red\Desktop\mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import Scraper
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 677)
        MainWindow.setMinimumSize(QtCore.QSize(855, 677))
        MainWindow.setMaximumSize(QtCore.QSize(855, 677))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 841, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 571))
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setObjectName("tabWidget")
        self.search_tab = QtWidgets.QWidget()
        self.search_tab.setObjectName("search_tab")
        self.searchBar = QtWidgets.QLineEdit(self.search_tab)
        self.searchBar.setGeometry(QtCore.QRect(210, 310, 301, 31))
        self.searchBar.setMaxLength(40)
        self.searchBar.setObjectName("searchBar")
        self.search_banner = QtWidgets.QLabel(self.search_tab)
        self.search_banner.setGeometry(QtCore.QRect(240, 100, 341, 151))
        self.search_banner.setFrameShape(QtWidgets.QFrame.Box)
        self.search_banner.setLineWidth(0)
        self.search_banner.setText("")
        self.search_banner.setObjectName("search_banner")
        self.region_bar = QtWidgets.QLineEdit(self.search_tab)
        self.region_bar.setGeometry(QtCore.QRect(520, 310, 91, 31))
        self.region_bar.setMaxLength(40)
        self.region_bar.setObjectName("region_bar")
        self.region_label = QtWidgets.QLabel(self.search_tab)
        self.region_label.setGeometry(QtCore.QRect(520, 290, 47, 13))
        self.region_label.setObjectName("region_label")
        self.label_2 = QtWidgets.QLabel(self.search_tab)
        self.label_2.setGeometry(QtCore.QRect(600, 280, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setToolTipDuration(10)
        self.label_2.setObjectName("label_2")
        self.search_button = QtWidgets.QPushButton(self.search_tab)
        self.search_button.setGeometry(QtCore.QRect(620, 310, 81, 31))
        self.search_button.setObjectName("search_button")
        self.tabWidget.addTab(self.search_tab, "")
        self.results_tab = QtWidgets.QWidget()
        self.results_tab.setObjectName("results_tab")
        self.label = QtWidgets.QLabel(self.results_tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.results_tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 801, 531))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.results_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 855, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.menuBar.setPalette(palette)
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuhelp = QtWidgets.QMenu(self.menuBar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuexit = QtWidgets.QMenu(self.menuBar)
        self.menuexit.setObjectName("menuexit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menuMenu.addAction(self.actionabout)
        self.menuhelp.addSeparator()
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.menuhelp.menuAction())
        self.menuBar.addAction(self.menuexit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        pixmap = QtGui.QPixmap("Search.png")  # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.search_banner.width(), self.search_banner.height(), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.search_banner.setPixmap(pixmap)  # Set the pixmap onto the label
        self.search_banner.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.search_button.clicked.connect(self.search)

    def search(self):
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(0)
        result_list = Scraper.populate_list(self.searchBar.text(), self.region_bar.text())
        row = 1
        col = 0
        for listing in result_list:
            row_possition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_possition)
            self.tableWidget.setItem(row_possition, col, QtWidgets.QTableWidgetItem(listing['date']))
            col += 1
            self.tableWidget.setItem(row_possition, col, QtWidgets.QTableWidgetItem(listing['title']))
            col += 1
            self.tableWidget.setItem(row_possition, col, QtWidgets.QTableWidgetItem(listing['price']))
            col += 1
            self.tableWidget.setItem(row_possition, col, QtWidgets.QTableWidgetItem(listing['link']))
            col = 0
            row += 1
        self.tableWidget.resizeColumnsToContents()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Craigslist Search"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.region_bar.setPlaceholderText(_translate("MainWindow", "Ex. Pasco, Wa"))
        self.region_label.setText(_translate("MainWindow", "Region"))
        self.label_2.setToolTip(_translate("MainWindow", "For a search of all the USA type in \"All\""))
        self.label_2.setText(_translate("MainWindow", "?"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_tab), _translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Postings"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Link"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), _translate("MainWindow", "Results"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuhelp.setTitle(_translate("MainWindow", "Help"))
        self.menuexit.setTitle(_translate("MainWindow", "Exit"))
        self.actionabout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

