import sys
import graph as g
import utilities as utils
import cage_controller as cc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

class ControllerWindow(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(640, 320)
        window.setMinimumSize(QtCore.QSize(660, 450))
        window.setMaximumSize(QtCore.QSize(1920, 1080))
        window.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(11)
        window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        window.setToolTipDuration(2)
        window.setAutoFillBackground(True)
        window.setWindowFilePath("")
        window.setAnimated(False)
        self.widget = QtWidgets.QWidget(window)
        self.widget.setObjectName("widget")
        self.psu_1_voltage_input = QtWidgets.QLineEdit(self.widget)
        self.psu_1_voltage_input.setGeometry(QtCore.QRect(70, 30, 100, 30))
        self.psu_1_voltage_input.setObjectName("psu_1_voltage_input")
        self.psu_1_label = QtWidgets.QLabel(self.widget)
        self.psu_1_label.setGeometry(QtCore.QRect(10, 35, 45, 20))
        self.psu_1_label.setObjectName("psu_1_label")
        self.apply_button = QtWidgets.QPushButton(self.widget)
        self.apply_button.setGeometry(QtCore.QRect(190, 135, 100, 30))
        self.apply_button.setObjectName("apply_button")
        self.apply_button.clicked.connect(self.update_power_supplies)
        self.psu_1_current_input = QtWidgets.QLineEdit(self.widget)
        self.psu_1_current_input.setGeometry(QtCore.QRect(190, 30, 100, 30))
        self.psu_1_current_input.setObjectName("psu_1_current_input")
        self.voltage_label = QtWidgets.QLabel(self.widget)
        self.voltage_label.setGeometry(QtCore.QRect(70, 10, 100, 20))
        self.voltage_label.setObjectName("voltage_label")
        self.current_label = QtWidgets.QLabel(self.widget)
        self.current_label.setGeometry(QtCore.QRect(190, 10, 100, 20))
        self.current_label.setObjectName("current_label")
        self.psu_2_current_input = QtWidgets.QLineEdit(self.widget)
        self.psu_2_current_input.setGeometry(QtCore.QRect(190, 65, 100, 30))
        self.psu_2_current_input.setObjectName("psu_2_current_input")
        self.psu_2_voltage_input = QtWidgets.QLineEdit(self.widget)
        self.psu_2_voltage_input.setGeometry(QtCore.QRect(70, 65, 100, 30))
        self.psu_2_voltage_input.setObjectName("psu_2_voltage_input")
        self.psu_2_label = QtWidgets.QLabel(self.widget)
        self.psu_2_label.setGeometry(QtCore.QRect(10, 70, 45, 20))
        self.psu_2_label.setObjectName("psu_2_label")
        self.psu_3_current_input = QtWidgets.QLineEdit(self.widget)
        self.psu_3_current_input.setGeometry(QtCore.QRect(190, 100, 100, 30))
        self.psu_3_current_input.setObjectName("psu_3_current_input")
        self.psu_3_voltage_input = QtWidgets.QLineEdit(self.widget)
        self.psu_3_voltage_input.setGeometry(QtCore.QRect(70, 100, 100, 30))
        self.psu_3_voltage_input.setObjectName("psu_3_voltage_input")
        self.psu_3_label = QtWidgets.QLabel(self.widget)
        self.psu_3_label.setGeometry(QtCore.QRect(10, 105, 45, 20))
        self.psu_3_label.setObjectName("psu_3_label")
        self.graph = g.Graph(self.widget)
        self.graph.add_line(g.Line(color='r'))
        self.graph.add_line(g.Line(color='g'))
        self.graph.add_line(g.Line(color='b'))
        self.graph.setGeometry(QtCore.QRect(300, 30, 320, 320))
        self.graph.setAutoFillBackground(True)
        self.graph.setObjectName("graph")
        window.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 26))
        self.menubar.setObjectName("menubar")
        self.menu_main = QtWidgets.QMenu(self.menubar)
        self.menu_main.setObjectName("menuMain")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)
        self.save_graph_menu = QtWidgets.QAction(window)
        self.save_graph_menu.setObjectName("save_graph_menu")
        self.shut_down_menu = QtWidgets.QAction(window)
        self.shut_down_menu.setObjectName("shut_down_menu")
        self.menu_main.addAction(self.save_graph_menu)
        self.menu_main.addAction(self.shut_down_menu)
        self.menubar.addAction(self.menu_main.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(utils.TICK_TIME)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Helmholtz Cage Controller"))
        window.setToolTip(_translate("window", "Helmholtz Cage Controller"))
        self.psu_1_voltage_input.setText(_translate("window", "12"))
        self.psu_1_label.setText(_translate("window", "PSU 1"))
        self.apply_button.setText(_translate("window", "Apply"))
        self.psu_1_current_input.setText(_translate("window", "1.5"))
        self.voltage_label.setText(_translate("window", "Voltage (V)"))
        self.current_label.setText(_translate("window", "Current (A)"))
        self.psu_2_current_input.setText(_translate("window", "1.5"))
        self.psu_2_voltage_input.setText(_translate("window", "12"))
        self.psu_2_label.setText(_translate("window", "PSU 2"))
        self.psu_3_current_input.setText(_translate("window", "1.5"))
        self.psu_3_voltage_input.setText(_translate("window", "12"))
        self.psu_3_label.setText(_translate("window", "PSU 3"))
        self.menu_main.setTitle(_translate("window", "Main"))
        self.save_graph_menu.setText(_translate("window", "Save Graph"))
        self.shut_down_menu.setText(_translate("window", "Shut Down Cage"))

    def tick(self):
        self.graph.update_graph()

    def save_data(self):
        for i in range(0, 3):
            utils.log(0, str(self.graph.lines[i]))

    def update_power_supplies(self):
        voltages = [ float(self.psu_1_voltage_input.text()), float(self.psu_2_voltage_input.text()), float(self.psu_3_voltage_input.text()) ]
        currents = [ float(self.psu_1_current_input.text()), float(self.psu_2_current_input.text()), float(self.psu_3_current_input.text()) ]
        utils.log(0, 'Applying volts:\t\t' + str(voltages) + '\n\tApplying currents:\t' + str(currents))

        if(utils.supply_available()):
            for i in range(0, 3):
                print(str(i + 1))
                utils.POWER_SUPPLIES[i + 1].set_voltage(voltages[i])
                utils.POWER_SUPPLIES[i + 1].set_current(currents[i])
        else:
            utils.log(3, 'No supplies are available for updating!\n\tThrowing away button press event.')

def interface():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ControllerWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
