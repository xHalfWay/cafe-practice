from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from database import authenticate_user
from admin_panel import AdminPanel
from cook_panel import CookPanel
from waiter_panel import WaiterPanel
class Ui_MainWindow_register(object):
    def setupUi(self, MainWindow_register):
        MainWindow_register.setObjectName("MainWindow_register")
        MainWindow_register.resize(581, 430)
        MainWindow_register.setStyleSheet("background-color: rgb(118, 227, 131)")
        self.centralwidget = QtWidgets.QWidget(MainWindow_register)
        self.centralwidget.setObjectName("centralwidget")

        layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.label_image = QtWidgets.QLabel(self.centralwidget)
        pixmap = QtGui.QPixmap("icon.png")  # Замените "your_image_path.png" на путь к вашему изображению
        self.label_image.setPixmap(pixmap)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label_image)

        self.label_regist = QtWidgets.QLabel(self.centralwidget)
        self.label_regist.setGeometry(QtCore.QRect(140, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_regist.setFont(font)
        self.label_regist.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_regist.setStyleSheet("color: white;")
        self.label_regist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_regist.setObjectName("label_regist")
        self.lineEdit_log = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_log.setGeometry(QtCore.QRect(80, 130, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_log.setFont(font)
        self.lineEdit_log.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_log.setStyleSheet("border-radius: 10px;\n"
"background-color: white;\n"
"color: black;")
        self.lineEdit_log.setText("")
        self.lineEdit_log.setObjectName("lineEdit_log")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(80, 200, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setStyleSheet("border-radius: 10px;\n"
"background-color: white;\n"
"color: black;")
        self.lineEdit_pass.setText("")
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(180, 280, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton{\n"
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
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(180, 350, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_exit.setFont(font)
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
        MainWindow_register.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_register)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_register)

        self.setWindowIcon(QtGui.QIcon("icon.png"))

    def retranslateUi(self, MainWindow_register):
        '''
        Установка текстовых значений элементов интерфейса и соединение кнопки "Вход" с методом для обработки входа.
        :param MainWindow_register:
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow_register.setWindowTitle(_translate("MainWindow_register", "Авторизация"))
        self.label_regist.setText(_translate("MainWindow_register", "Авторизация"))
        self.lineEdit_log.setPlaceholderText(_translate("MainWindow_register", "Логин"))
        self.lineEdit_pass.setPlaceholderText(_translate("MainWindow_register", "Пароль"))
        self.pushButton_login.setText(_translate("MainWindow_register", "Вход"))
        self.pushButton_exit.setText(_translate("MainWindow_register", "Выход"))

        self.pushButton_login.clicked.connect(self.handle_login)

    def handle_login(self):
        '''
        Обработка входа: получение логина и пароля, проверка, открытие окна или вывод ошибки.
        :return:
        '''
        login = self.lineEdit_log.text()
        password = self.lineEdit_pass.text()

        user = authenticate_user(login, password)
        if user:
            role = user[3]
            self.open_main_window(role)
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль.")

    def open_main_window(self, role):
        '''
        Открывает главное окно в зависимости от роли пользователя
        :param role:
        :return:
        '''
        if role == "Администратор":
            self.main_window = AdminPanel()
        elif role == "Повар":
            self.main_window = CookPanel()
        elif role == "Официант":
            self.main_window = WaiterPanel()
        self.main_window.show()
        self.close()