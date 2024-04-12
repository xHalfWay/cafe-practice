from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow_waiter(object):
    def setupUi(self, MainWindow_waiter):
        MainWindow_waiter.setObjectName("MainWindow_waiter")
        MainWindow_waiter.resize(800, 600)
        MainWindow_waiter.setStyleSheet("background-color: rgb(118, 227, 131);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_waiter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 50, 521, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_pan_waiter = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pan_waiter.setFont(font)
        self.label_pan_waiter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_pan_waiter.setScaledContents(False)
        self.label_pan_waiter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pan_waiter.setObjectName("label_pan_waiter")
        self.verticalLayout.addWidget(self.label_pan_waiter)
        self.pushButton_create_new_orders = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_create_new_orders.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_create_new_orders.setStyleSheet("QPushButton{\n"
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
        self.pushButton_create_new_orders.setObjectName("pushButton_create_new_orders")
        self.verticalLayout.addWidget(self.pushButton_create_new_orders)
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
        MainWindow_waiter.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_waiter)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_waiter)

    def retranslateUi(self, MainWindow_waiter):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_waiter.setWindowTitle(_translate("MainWindow_waiter", "Панель официанта"))
        self.label_pan_waiter.setText(_translate("MainWindow_waiter", "Панель официанта"))
        self.pushButton_create_new_orders.setText(_translate("MainWindow_waiter", "Создание нового заказа"))
        self.pushButton_view_orders.setText(_translate("MainWindow_waiter", "Просмотр всех заказов"))
        self.pushButton_change_orders.setText(_translate("MainWindow_waiter", "Изменение статуса заказа"))
        self.pushButton_exit.setText(_translate("MainWindow_waiter", "Выход"))
class WaiterPanel(QtWidgets.QMainWindow, Ui_MainWindow_waiter):
    '''
    Класс представляет панель для официанта.
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Панель официанта")
        self.pushButton_create_new_orders.clicked.connect(self.create_new_order)
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

        self.cursor.execute("SELECT id, date, table_number, num_customers, items, status FROM orders")
        orders = self.cursor.fetchall()

        self.tableWidget_orders.setRowCount(len(orders))
        for i, order in enumerate(orders):
            for j, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget_orders.setItem(i, j, item)

    def create_new_order(self):
        '''
        Метод для создания нового заказа.
        :return:
        '''
        table_number, ok = QtWidgets.QInputDialog.getInt(self, "Введите номер столика", "Номер столика:", 1, 1, 100)
        if ok:
            num_customers, ok = QtWidgets.QInputDialog.getInt(self, "Введите количество клиентов", "Количество клиентов:", 1, 1, 100)
            if ok:
                items, ok = QtWidgets.QInputDialog.getText(self, "Введите заказ", "Заказ:")
                if ok and items:
                    self.cursor.execute("INSERT INTO orders (date, table_number, num_customers, items, status) VALUES (CURRENT_TIMESTAMP, ?, ?, ?, 'Принят')",
                                        (table_number, num_customers, items))
                    self.conn.commit()
                    self.view_orders()

    def change_order_status(self):
        '''
        Метод для изменения статуса выбранного заказа.
        :return:
        '''
        selected_row = self.tableWidget_orders.currentRow()
        if selected_row != -1:
            order_id = self.tableWidget_orders.item(selected_row, 0).text()
            new_status, ok = QtWidgets.QInputDialog.getItem(self, "Изменение статуса заказа", "Выберите новый статус:", ["Принят", "Оплачен"], 0, False)
            if ok:
                self.cursor.execute("UPDATE orders SET status=? WHERE id=?", (new_status, order_id))
                self.conn.commit()
                self.view_orders()

    def exit(self):
        self.conn.close()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    waiter_panel = WaiterPanel()
    waiter_panel.show()
    sys.exit(app.exec_())
