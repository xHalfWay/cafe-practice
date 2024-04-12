import sys
from admin_panel import AdminPanel
from cook_panel import CookPanel
from waiter_panel import WaiterPanel
from database import authenticate_user
from ui_main_window import Ui_MainWindow_register
from PyQt5 import QtWidgets

class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow_register):
    '''
    Окно авторизации
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Авторизация")
        self.pushButton_login.clicked.connect(self.authenticate)
        self.pushButton_exit.clicked.connect(self.close)

        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)

    def authenticate(self):
        '''
        Проверка веденных учетных данных
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()