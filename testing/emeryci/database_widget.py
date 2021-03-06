

from PyQt5 import QtCore, QtGui, QtWidgets



class DatabaseWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(948, 660)
        self.groupBox_15 = QtWidgets.QGroupBox(self)
        self.groupBox_15.setGeometry(QtCore.QRect(0, 5, 941, 651))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setObjectName("groupBox_15")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_15)
        self.groupBox.setGeometry(QtCore.QRect(675, 25, 261, 291))
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 70, 92, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 50, 86, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(120, 95, 116, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_7.setGeometry(QtCore.QRect(120, 115, 86, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_8.setGeometry(QtCore.QRect(120, 135, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 25, 81, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 90, 71, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_12.setGeometry(QtCore.QRect(120, 155, 121, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_13.setGeometry(QtCore.QRect(120, 195, 96, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_14.setGeometry(QtCore.QRect(120, 175, 96, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setObjectName("checkBox_14")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setGeometry(QtCore.QRect(5, 38, 101, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_15.setGeometry(QtCore.QRect(10, 130, 92, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_16.setGeometry(QtCore.QRect(10, 150, 91, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_17.setGeometry(QtCore.QRect(10, 110, 86, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_17.setFont(font)
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_18.setGeometry(QtCore.QRect(10, 190, 92, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_18.setFont(font)
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_20 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_20.setGeometry(QtCore.QRect(10, 170, 96, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_20.setFont(font)
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(120, 10, 96, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_11.setGeometry(QtCore.QRect(120, 70, 71, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(120, 30, 92, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(120, 50, 126, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.line_6 = QtWidgets.QFrame(self.groupBox)
        self.line_6.setGeometry(QtCore.QRect(107, 83, 154, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.groupBox)
        self.line_7.setGeometry(QtCore.QRect(100, 21, 16, 196))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(5, 225, 226, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.line_9 = QtWidgets.QFrame(self.groupBox)
        self.line_9.setGeometry(QtCore.QRect(2, 202, 106, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_11 = QtWidgets.QFrame(self.groupBox)
        self.line_11.setGeometry(QtCore.QRect(106, 208, 156, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(5, 210, 76, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(85, 210, 21, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_27.setGeometry(QtCore.QRect(160, 250, 91, 31))
        self.pushButton_27.setObjectName("pushButton_27")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_15)
        self.tabWidget.setGeometry(QtCore.QRect(5, 290, 386, 286))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView_5 = QtWidgets.QTableView(self.tab)
        self.tableView_5.setGeometry(QtCore.QRect(5, 5, 371, 246))
        self.tableView_5.setObjectName("tableView_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView_7 = QtWidgets.QTableView(self.tab_2)
        self.tableView_7.setGeometry(QtCore.QRect(5, 5, 371, 246))
        self.tableView_7.setObjectName("tableView_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableView_8 = QtWidgets.QTableView(self.tab_3)
        self.tableView_8.setGeometry(QtCore.QRect(5, 5, 371, 246))
        self.tableView_8.setObjectName("tableView_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.tableView_22 = QtWidgets.QTableView(self.tab_18)
        self.tableView_22.setGeometry(QtCore.QRect(5, 5, 371, 246))
        self.tableView_22.setObjectName("tableView_22")
        self.tabWidget.addTab(self.tab_18, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_15)
        self.tabWidget_2.setGeometry(QtCore.QRect(395, 295, 426, 281))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableView_6 = QtWidgets.QTableView(self.tab_4)
        self.tableView_6.setGeometry(QtCore.QRect(5, 5, 411, 241))
        self.tableView_6.setObjectName("tableView_6")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableView_9 = QtWidgets.QTableView(self.tab_5)
        self.tableView_9.setGeometry(QtCore.QRect(5, 5, 411, 241))
        self.tableView_9.setObjectName("tableView_9")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableView_10 = QtWidgets.QTableView(self.tab_6)
        self.tableView_10.setGeometry(QtCore.QRect(5, 5, 411, 241))
        self.tableView_10.setObjectName("tableView_10")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableView_11 = QtWidgets.QTableView(self.tab_7)
        self.tableView_11.setGeometry(QtCore.QRect(5, 5, 411, 241))
        self.tableView_11.setObjectName("tableView_11")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tableView_12 = QtWidgets.QTableView(self.tab_8)
        self.tableView_12.setGeometry(QtCore.QRect(5, 5, 411, 241))
        self.tableView_12.setObjectName("tableView_12")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tableView_13 = QtWidgets.QTableView(self.tab_9)
        self.tableView_13.setGeometry(QtCore.QRect(5, 5, 411, 241))
        self.tableView_13.setObjectName("tableView_13")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_15)
        self.groupBox_3.setGeometry(QtCore.QRect(5, 575, 711, 71))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(550, 25, 166, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(675, 50, 31, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(550, 50, 71, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(430, 25, 116, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(510, 50, 31, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(435, 50, 71, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(285, 25, 146, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(385, 50, 36, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(285, 50, 86, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(110, 50, 31, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(5, 50, 81, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(5, 25, 136, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(245, 50, 31, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(150, 25, 131, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(150, 50, 91, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setGeometry(QtCore.QRect(140, 25, 10, 46))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setGeometry(QtCore.QRect(275, 25, 10, 46))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setGeometry(QtCore.QRect(420, 25, 10, 46))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBox_3)
        self.line_4.setGeometry(QtCore.QRect(540, 25, 10, 46))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.groupBox_15)
        self.tabWidget_3.setGeometry(QtCore.QRect(5, 20, 666, 266))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tableView_14 = QtWidgets.QTableView(self.tab_10)
        self.tableView_14.setGeometry(QtCore.QRect(5, 5, 651, 226))
        self.tableView_14.setObjectName("tableView_14")
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tableView_15 = QtWidgets.QTableView(self.tab_11)
        self.tableView_15.setGeometry(QtCore.QRect(5, 5, 651, 226))
        self.tableView_15.setObjectName("tableView_15")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tableView_16 = QtWidgets.QTableView(self.tab_12)
        self.tableView_16.setGeometry(QtCore.QRect(5, 5, 651, 226))
        self.tableView_16.setObjectName("tableView_16")
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tableView_17 = QtWidgets.QTableView(self.tab_16)
        self.tableView_17.setGeometry(QtCore.QRect(5, 5, 651, 226))
        self.tableView_17.setObjectName("tableView_17")
        self.tabWidget_3.addTab(self.tab_16, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tableView_18 = QtWidgets.QTableView(self.tab_14)
        self.tableView_18.setGeometry(QtCore.QRect(5, 5, 651, 226))
        self.tableView_18.setObjectName("tableView_18")
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tableView_19 = QtWidgets.QTableView(self.tab_15)
        self.tableView_19.setGeometry(QtCore.QRect(5, 5, 651, 226))
        self.tableView_19.setObjectName("tableView_19")
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.tableView_20 = QtWidgets.QTableView(self.tab_17)
        self.tableView_20.setGeometry(QtCore.QRect(5, 5, 651, 226))
        self.tableView_20.setObjectName("tableView_20")
        self.tabWidget_3.addTab(self.tab_17, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tableView_21 = QtWidgets.QTableView(self.tab_13)
        self.tableView_21.setGeometry(QtCore.QRect(5, 5, 651, 226))
        self.tableView_21.setObjectName("tableView_21")
        self.tabWidget_3.addTab(self.tab_13, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_15)
        self.groupBox_2.setGeometry(QtCore.QRect(825, 320, 111, 166))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(5, 25, 66, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(5, 45, 101, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(10, 75, 81, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.line_12 = QtWidgets.QFrame(self.groupBox_2)
        self.line_12.setGeometry(QtCore.QRect(0, 60, 111, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 95, 71, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(85, 95, 21, 17))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_26.setGeometry(QtCore.QRect(10, 125, 91, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.line_13 = QtWidgets.QFrame(self.groupBox_2)
        self.line_13.setGeometry(QtCore.QRect(0, 108, 111, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_15.setTitle(_translate("Form", " DATABASE "))
        self.groupBox.setTitle(_translate("Form", "CLEAR DATABASE "))
        self.checkBox_2.setText(_translate("Form", "METADATA"))
        self.checkBox.setText(_translate("Form", "DATASETS"))
        self.checkBox_6.setText(_translate("Form", "TRADE HISTORY"))
        self.checkBox_7.setText(_translate("Form", "BACKTESTS"))
        self.checkBox_8.setText(_translate("Form", "EG TESTS"))
        self.checkBox_9.setText(_translate("Form", "ALL DATA"))
        self.checkBox_10.setText(_translate("Form", "CONFIG"))
        self.checkBox_12.setText(_translate("Form", "JOHANSEN TESTS"))
        self.checkBox_13.setText(_translate("Form", "KPSS TESTS"))
        self.checkBox_14.setText(_translate("Form", "ADF TESTS"))
        self.checkBox_15.setText(_translate("Form", "WEBSITES"))
        self.checkBox_16.setText(_translate("Form", "WATCHLIST"))
        self.checkBox_17.setText(_translate("Form", "EXCHANGES"))
        self.checkBox_18.setText(_translate("Form", "WALLETS"))
        self.checkBox_20.setText(_translate("Form", "PORTFOLIOS"))
        self.checkBox_3.setText(_translate("Form", "ALGORITHMS"))
        self.checkBox_11.setText(_translate("Form", "SCRIPTS"))
        self.checkBox_4.setText(_translate("Form", "VARIABLES"))
        self.checkBox_5.setText(_translate("Form", "PARAMETER SETS"))
        self.label_16.setText(_translate("Form", "of disk space will be freed up."))
        self.label_22.setText(_translate("Form", "0"))
        self.label_24.setText(_translate("Form", "MB"))
        self.pushButton_27.setToolTip(_translate("Form", "<html><head/><body><p>Clears all data (tables and files) from selected groups. Leaves empty tables.</p><p>Size:</p></body></html>"))
        self.pushButton_27.setText(_translate("Form", "CLEAR DATA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "ALGORITHMS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "VARIABLES"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "PARAMETER SETS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_18), _translate("Form", "SCRIPTS"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "TRADE HISTORY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "BACKTESTS"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form", "EG"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Form", "JOHANSEN"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "ADF"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("Form", "KPSS"))
        self.groupBox_3.setTitle(_translate("Form", " DISK SPACE DATA  "))
        self.label.setText(_translate("Form", "TOTAL DATABASE SIZE"))
        self.label_3.setText(_translate("Form", "MB"))
        self.label_2.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "METADATA SIZE"))
        self.label_5.setText(_translate("Form", "MB"))
        self.label_6.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "MARKET DATA SIZE"))
        self.label_8.setText(_translate("Form", "MB"))
        self.label_9.setText(_translate("Form", "0"))
        self.label_11.setText(_translate("Form", "GB"))
        self.label_12.setText(_translate("Form", "0"))
        self.label_10.setText(_translate("Form", "TOTAL DISK SPACE"))
        self.label_13.setText(_translate("Form", "GB"))
        self.label_14.setText(_translate("Form", "FREE DISK SPACE"))
        self.label_15.setText(_translate("Form", "0"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("Form", "DATASETS"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("Form", "METADATA"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("Form", "CONFIG"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), _translate("Form", "EXCHANGES"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("Form", "WEBSITES"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("Form", "WATCHLIST"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), _translate("Form", "PORTFOLIOS"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("Form", "WALLETS"))
        self.groupBox_2.setTitle(_translate("Form", "DROP TABLE"))
        self.label_25.setText(_translate("Form", "SELECTED:"))
        self.label_26.setText(_translate("Form", "table_name"))
        self.label_20.setText(_translate("Form", "TABLE SIZE:"))
        self.label_21.setText(_translate("Form", "0 "))
        self.label_23.setText(_translate("Form", "MB"))
        self.pushButton_26.setToolTip(_translate("Form", "<html><head/><body><p>Deletes single, currently selected table or file.</p><p>Current selection:</p><p>Size:</p></body></html>"))
        self.pushButton_26.setText(_translate("Form", "DELETE"))


