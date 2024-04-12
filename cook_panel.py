from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
class Ui_MainWindow_cook(object):
    def setupUi(self, MainWindow_cook):
        MainWindow_cook.setObjectName("MainWindow_cook")
        MainWindow_cook.resize(779, 622)
        MainWindow_cook.setStyleSheet("background-color: rgb(118, 227, 131);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_cook)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 50, 521, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_pan_cook = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pan_cook.setFont(font)
        self.label_pan_cook.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_pan_cook.setScaledContents(False)
        self.label_pan_cook.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pan_cook.setObjectName("label_pan_cook")
        self.verticalLayout.addWidget(self.label_pan_cook)
        self.pushButton_view_orders = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_view_orders.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_view_orders.setStyleSheet("QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid black;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(153, 102, 51);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: black;\n"
"}\n"
"")
        self.pushButton_view_orders.setObjectName("pushButton_view_orders")
        self.verticalLayout.addWidget(self.pushButton_view_orders)
        self.pushButton_change_orders = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_change_orders.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_change_orders.setStyleSheet("QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid black;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(153, 102, 51);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: black;\n"
"}\n"
"")
        self.pushButton_change_orders.setObjectName("pushButton_change_orders")
        self.verticalLayout.addWidget(self.pushButton_change_orders)
        self.pushButton_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid black;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(153, 102, 51);\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: black;\n"
"}\n"
"")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout.addWidget(self.pushButton_exit)
        MainWindow_cook.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_cook)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_cook)

    def retranslateUi(self, MainWindow_cook):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_cook.setWindowTitle(_translate("MainWindow_cook", "Панель повара"))
        self.label_pan_cook.setText(_translate("MainWindow_cook", "Панель повара"))
        self.pushButton_view_orders.setText(_translate("MainWindow_cook", "Просмотр всех заказов"))
        self.pushButton_change_orders.setText(_translate("MainWindow_cook", "Изменение статуса заказа"))
        self.pushButton_exit.setText(_translate("MainWindow_cook", "Выход"))

class CookPanel(QtWidgets.QMainWindow, Ui_MainWindow_cook):
    '''
    Класс представляет панель для повара.
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Панель повара")
        self.pushButton_view_orders.clicked.connect(self.view_orders)
        self.pushButton_change_orders.clicked.connect(self.change_order_status)
        self.pushButton_exit.clicked.connect(self.exit)

        self.conn = sqlite3.connect('cafe.db')
        self.cursor = self.conn.cursor()

        self.tableWidget_orders = QtWidgets.QTableWidget()
        self.verticalLayout.addWidget(self.tableWidget_orders)

        self.setWindowIcon(QtGui.QIcon("icon.png"))


    def view_orders(self):
        '''
        Метод для отображения списка заказов в таблице.
        :return:
        '''
        self.tableWidget_orders.clear()
        self.tableWidget_orders.setColumnCount(6)
        self.tableWidget_orders.setHorizontalHeaderLabels(["ID", "Дата", "Столик", "Кол-во клиентов", "Заказ", "Статус"])

        self.cursor.execute("SELECT * FROM orders")
        orders = self.cursor.fetchall()


        self.tableWidget_orders.setRowCount(len(orders))
        for i, order in enumerate(orders):
            for j, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget_orders.setItem(i, j, item)

    def change_order_status(self):
        '''
        Метод для изменения статуса выбранного заказа.
        :return:
        '''
        selected_row = self.tableWidget_orders.currentRow()
        if selected_row != -1:
            order_id = self.tableWidget_orders.item(selected_row, 0).text()
            new_status, ok = QtWidgets.QInputDialog.getItem(self, "Изменение статуса заказа", "Выберите новый статус:", ["Готовится", "Готов"], 0, False)
            if ok:
                self.cursor.execute("UPDATE orders SET status=? WHERE id=?", (new_status, order_id))
                self.conn.commit()
                self.view_orders()

    def exit(self):
        self.conn.close()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cook_panel = CookPanel()
    cook_panel.show()
    sys.exit(app.exec_())