from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow_admin(object):
    def setupUi(self, MainWindow_admin):
        MainWindow_admin.setObjectName("MainWindow_admin")
        MainWindow_admin.resize(800, 600)
        MainWindow_admin.setStyleSheet("\n""background-color: rgb(118, 227, 131);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_admin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 60, 521, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_pan_adm = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pan_adm.setFont(font)
        self.label_pan_adm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_pan_adm.setScaledContents(False)
        self.label_pan_adm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pan_adm.setObjectName("label_pan_adm")
        self.verticalLayout.addWidget(self.label_pan_adm)
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
        self.pushButton_shift_contr = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_shift_contr.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_shift_contr.setStyleSheet("QPushButton{\n"
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
        self.pushButton_shift_contr.setObjectName("pushButton_shift_contr")
        self.verticalLayout.addWidget(self.pushButton_shift_contr)
        self.pushButton_reg_new_user = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_reg_new_user.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_reg_new_user.setStyleSheet("QPushButton{\n"
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
        self.pushButton_reg_new_user.setObjectName("pushButton_reg_new_user")
        self.verticalLayout.addWidget(self.pushButton_reg_new_user)
        self.pushButton_empl_contr = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_empl_contr.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_empl_contr.setStyleSheet("QPushButton{\n"
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
        self.pushButton_empl_contr.setObjectName("pushButton_empl_contr")
        self.verticalLayout.addWidget(self.pushButton_empl_contr)
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
        MainWindow_admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_admin)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_admin)

    def retranslateUi(self, MainWindow_admin):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_admin.setWindowTitle(_translate("MainWindow_admin", "Панель администратора"))
        self.label_pan_adm.setText(_translate("MainWindow_admin", "Панель администратора"))
        self.pushButton_view_orders.setText(_translate("MainWindow_admin", "Просмотр всех заказов"))
        self.pushButton_shift_contr.setText(_translate("MainWindow_admin", "Управление сменами"))
        self.pushButton_reg_new_user.setText(_translate("MainWindow_admin", "Регистрация нового пользователя"))
        self.pushButton_empl_contr.setText(_translate("MainWindow_admin", "Управление сотрудниками"))
        self.pushButton_exit.setText(_translate("MainWindow_admin", "Выход"))
class RegisterUserWindow(QtWidgets.QWidget):
    '''
    Интерфейс для регистрации нового пользователя
    Содержит поля для ввода логина, пароля и выбора роли пользователя,
    '''
    def __init__(self, conn):
        super().__init__()
        self.setWindowTitle("Регистрация нового пользователя")
        self.conn = conn
        self.cursor = self.conn.cursor()
        layout = QtWidgets.QVBoxLayout(self)

        self.label_login = QtWidgets.QLabel("Логин:")
        self.edit_login = QtWidgets.QLineEdit()
        layout.addWidget(self.label_login)
        layout.addWidget(self.edit_login)

        self.label_password = QtWidgets.QLabel("Пароль:")
        self.edit_password = QtWidgets.QLineEdit()
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)

        self.label_role = QtWidgets.QLabel("Роль:")
        self.combo_role = QtWidgets.QComboBox()
        self.combo_role.addItems(["Администратор", "Повар", "Официант"])
        layout.addWidget(self.label_role)
        layout.addWidget(self.combo_role)

        self.button_register = QtWidgets.QPushButton("Зарегистрировать")
        layout.addWidget(self.button_register)

        self.button_register.clicked.connect(self.register_user)

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.setMinimumSize(600, 400)

    def register_user(self):
        '''
        Метод выполняет регистрацию нового пользователя, извлекая данные из полей ввода и выполняя SQL-запрос для добавления новой записи в базу данных.
        :return:
        '''
        login = self.edit_login.text()
        password = self.edit_password.text()
        role = self.combo_role.currentText()

        if login and password:
            self.cursor.execute("INSERT INTO users (login, password, role) VALUES (?, ?, ?)", (login, password, role))
            self.conn.commit()
            QtWidgets.QMessageBox.information(self, "Успех", "Пользователь успешно зарегистрирован.")
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
class EmployeesWindow(QtWidgets.QWidget):
    '''
    Класс представляет интерфейс для управления списком сотрудников.
    Содержит таблицу с данными о сотрудниках и кнопки для добавления, увольнения, а также изменения статуса сотрудников.
    '''
    def __init__(self, conn):
        super().__init__()
        self.setWindowTitle("Список сотрудников")
        self.conn = conn
        self.cursor = self.conn.cursor()
        layout = QtWidgets.QVBoxLayout(self)

        self.tableWidget_employees = QtWidgets.QTableWidget()
        layout.addWidget(self.tableWidget_employees)

        self.pushButton_add_employee = QtWidgets.QPushButton("Добавить сотрудника")
        self.pushButton_fire = QtWidgets.QPushButton("Уволить сотрудника")
        self.pushButton_accept_employee = QtWidgets.QPushButton("Изменить статус на - принят")
        self.pushButton_dismiss_employee = QtWidgets.QPushButton("Изменить статус на - уволен")
        layout.addWidget(self.pushButton_add_employee)
        layout.addWidget(self.pushButton_fire)
        layout.addWidget(self.pushButton_accept_employee)
        layout.addWidget(self.pushButton_dismiss_employee)

        self.load_employees()

        self.pushButton_add_employee.clicked.connect(self.add_employee)
        self.pushButton_fire.clicked.connect(self.fire_employee)
        self.pushButton_accept_employee.clicked.connect(self.accept_employee)
        self.pushButton_dismiss_employee.clicked.connect(self.dismiss_employee)

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.setMinimumSize(600, 400)

    def load_employees(self):
        '''
        Метод загружает данные о сотрудниках из базы данных и отображает их в таблице.
        :return:
        '''
        self.tableWidget_employees.clear()
        self.tableWidget_employees.setColumnCount(4)
        self.tableWidget_employees.setHorizontalHeaderLabels(["ID", "Имя", "Роль", "Статус"])

        self.cursor.execute("SELECT * FROM employees")
        data = self.cursor.fetchall()
        self.tableWidget_employees.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                self.tableWidget_employees.setItem(row_num, col_num, item)

    def add_employee(self):
        '''
        Метод позволяет добавлять новых сотрудников
        :return:
        '''
        name, ok_name = QtWidgets.QInputDialog.getText(self, "Добавление нового сотрудника", "Введите имя сотрудника:")

        role_dialog = QtWidgets.QInputDialog()
        role_dialog.setOptions(QtWidgets.QInputDialog.UseListViewForComboBoxItems)
        role_dialog.setComboBoxItems(["Администратор", "Повар", "Официант"])
        role_dialog.setWindowTitle("Добавление нового сотрудника")
        role_dialog.setLabelText("Выберите роль сотрудника:")
        role_dialog.resize(200, 100)
        role_dialog.exec_()
        role = role_dialog.textValue()

        status_dialog = QtWidgets.QInputDialog()
        status_dialog.setOptions(QtWidgets.QInputDialog.UseListViewForComboBoxItems)
        status_dialog.setComboBoxItems(["Принят", "Уволен"])
        status_dialog.setWindowTitle("Добавление нового сотрудника")
        status_dialog.setLabelText("Выберите статус сотрудника:")
        status_dialog.resize(200, 100)
        status_dialog.exec_()
        status = status_dialog.textValue()

        if ok_name and role and status:
            self.cursor.execute("INSERT INTO employees (name, role, status) VALUES (?, ?, ?)", (name, role, status))
            self.conn.commit()
            self.load_employees()

    def fire_employee(self):
        '''
        Метод для увольнения
        :return:
        '''
        selected_row = self.tableWidget_employees.currentRow()
        if selected_row != -1:
            employee_id = self.tableWidget_employees.item(selected_row, 0).text()
            self.cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
            self.conn.commit()
            self.load_employees()

    def accept_employee(self):
        '''
        Метод для изменения статуса сотрудника
        :return:
        '''
        selected_row = self.tableWidget_employees.currentRow()
        if selected_row != -1:
            employee_id = self.tableWidget_employees.item(selected_row, 0).text()
            self.cursor.execute("UPDATE employees SET status='Принят' WHERE id=?", (employee_id,))
            self.conn.commit()
            self.load_employees()

    def dismiss_employee(self):
        '''
        Метод для изменения статуса сотрудника
        :return:
        '''
        selected_row = self.tableWidget_employees.currentRow()
        if selected_row != -1:
            employee_id = self.tableWidget_employees.item(selected_row, 0).text()
            self.cursor.execute("UPDATE employees SET status='Уволен' WHERE id=?", (employee_id,))
            self.conn.commit()
            self.load_employees()
class ShiftsWindow(QtWidgets.QWidget):
    '''
    Класс предоставляет интерфейс для управления списком смен.
    Содержит таблицу с данными о сменах и кнопки для создания новой смены и удаления существующей.
    '''
    def __init__(self, conn):
        super().__init__()
        self.setWindowTitle("Список смен")
        self.conn = conn
        self.cursor = self.conn.cursor()
        layout = QtWidgets.QVBoxLayout(self)

        self.tableWidget_shifts = QtWidgets.QTableWidget()
        layout.addWidget(self.tableWidget_shifts)

        self.pushButton_create_shift = QtWidgets.QPushButton("Создать новую смену")
        self.pushButton_delete_shift = QtWidgets.QPushButton("Удалить смену")
        layout.addWidget(self.pushButton_create_shift)
        layout.addWidget(self.pushButton_delete_shift)

        self.pushButton_create_shift.clicked.connect(self.create_shift)
        self.pushButton_delete_shift.clicked.connect(self.delete_shift)

        self.load_shifts()

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.setMinimumSize(600, 400)

    def load_shifts(self):
        '''
        Метод загружает данные о сменах из базы данных и отображает их в таблице.
        :return:
        '''

        self.tableWidget_shifts.clear()
        self.tableWidget_shifts.setColumnCount(3)
        self.tableWidget_shifts.setHorizontalHeaderLabels(["ID смены", "Дата", "Имя сотрудника"])

        self.cursor.execute("SELECT shifts.id, shifts.date, employees.name "
                            "FROM shifts "
                            "INNER JOIN employees ON shifts.employee_id = employees.id")
        data = self.cursor.fetchall()
        self.tableWidget_shifts.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                self.tableWidget_shifts.setItem(row_num, col_num, item)

    def create_shift(self):
        '''
        Метод открывает диалоговое окно для создания новой смены.
        :return:
        '''
        dialog = QtWidgets.QDialog()
        layout = QtWidgets.QVBoxLayout(dialog)
        date_label = QtWidgets.QLabel("Дата:")
        date_edit = QtWidgets.QDateEdit()
        date_edit.setDate(QtCore.QDate.currentDate())
        employee_label = QtWidgets.QLabel("Сотрудник:")
        employee_combo = QtWidgets.QComboBox()

        self.cursor.execute("SELECT name FROM employees")
        employees = self.cursor.fetchall()
        for employee in employees:
            employee_combo.addItem(employee[0])

        buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        layout.addWidget(date_label)
        layout.addWidget(date_edit)
        layout.addWidget(employee_label)
        layout.addWidget(employee_combo)
        layout.addWidget(buttons)

        if dialog.exec_():
            date = date_edit.date().toString(QtCore.Qt.ISODate)
            employee_name = employee_combo.currentText()

            self.cursor.execute("SELECT id FROM employees WHERE name=?", (employee_name,))
            employee_id = self.cursor.fetchone()[0]

            self.cursor.execute("INSERT INTO shifts (date, employee_id) VALUES (?, ?)", (date, employee_id))
            self.conn.commit()
            self.load_shifts()

    def delete_shift(self):
        '''
        Метод удаляет выбранную смену из базы данных после подтверждения пользователя.
        :return:
        '''
        selected_row = self.tableWidget_shifts.currentRow()
        if selected_row != -1:
            shift_id = self.tableWidget_shifts.item(selected_row, 0).text()
            self.cursor.execute("DELETE FROM shifts WHERE id=?", (shift_id,))
            self.conn.commit()
            self.load_shifts()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите смену для удаления")
class OrdersWindow(QtWidgets.QWidget):
    '''
    Класс предоставляет интерфейс для управления списком заказов.
    Содержит таблицу с данными о заказах и кнопку для удаления выбранного заказа.
    '''
    def __init__(self, conn):
        super().__init__()
        self.setWindowTitle("Список заказов")
        self.conn = conn
        self.cursor = self.conn.cursor()
        layout = QtWidgets.QVBoxLayout(self)

        self.tableWidget_orders = QtWidgets.QTableWidget()
        layout.addWidget(self.tableWidget_orders)

        self.delete_order_button = QtWidgets.QPushButton("Удалить заказ")
        layout.addWidget(self.delete_order_button)

        self.load_orders()

        self.setMinimumSize(800, 400)

        self.delete_order_button.clicked.connect(self.delete_order)

        self.setWindowIcon(QtGui.QIcon("icon.png"))

    def load_orders(self):
        '''
        Метод загружает данные о заказах из базы данных и отображает их в таблице.
        :return:
        '''
        self.tableWidget_orders.clear()
        self.tableWidget_orders.setColumnCount(6)
        self.tableWidget_orders.setHorizontalHeaderLabels(["ID", "Дата", "Столик", "Кол-во клиентов", "Заказ", "Статус"])

        self.cursor.execute("SELECT * FROM orders")
        data = self.cursor.fetchall()
        self.tableWidget_orders.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                self.tableWidget_orders.setItem(row_num, col_num, item)

    def delete_order(self):
        '''
        Метод удаляет выбранный заказ из базы данных после подтверждения пользователя.
        :return:
        '''
        selected_row = self.tableWidget_orders.currentRow()
        if selected_row != -1:
            order_id = self.tableWidget_orders.item(selected_row, 0).text()
            reply = QtWidgets.QMessageBox.question(self, 'Удаление заказа',
                                                   f"Вы уверены, что хотите удалить заказ {order_id}?",
                                                   QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.cursor.execute("DELETE FROM orders WHERE id=?", (order_id,))
                self.conn.commit()
                self.load_orders()
class AdminPanel(QtWidgets.QMainWindow, Ui_MainWindow_admin):
    '''
    Класс представляет панель администратора приложения.
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Панель администратора")
        self.pushButton_view_orders.clicked.connect(self.view_orders)
        self.pushButton_shift_contr.clicked.connect(self.manage_shifts)
        self.pushButton_reg_new_user.clicked.connect(self.register_new_user)
        self.pushButton_empl_contr.clicked.connect(self.manage_employees)
        self.pushButton_exit.clicked.connect(self.exit)

        self.conn = sqlite3.connect('cafe.db')
        self.cursor = self.conn.cursor()

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.shifts_window = None
        self.register_user_window = None
        self.employees_window = None
        self.orders_window = None

    def __del__(self):
        self.conn.close()

    def view_orders(self):
        '''
        Метод создает и отображает окно для просмотра заказов.
        :return:
        '''
        self.orders_window = OrdersWindow(self.conn)
        self.orders_window.show()

    def manage_shifts(self):
        '''
        Метод создает и отображает окно для управления сменами.
        :return:
        '''
        self.shifts_window = ShiftsWindow(self.conn)
        self.shifts_window.show()

    def register_new_user(self):
        '''
        Метод создает и отображает окно для регистрации нового пользователя.
        :return:
        '''
        self.register_user_window = RegisterUserWindow(self.conn)
        self.register_user_window.show()

    def manage_employees(self):
        '''
        Метод создает и отображает окно для управления списком сотрудников.
        :return:
        '''
        self.employees_window = EmployeesWindow(self.conn)
        self.employees_window.show()

    def exit(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_panel = AdminPanel()
    admin_panel.show()
    sys.exit(app.exec_())