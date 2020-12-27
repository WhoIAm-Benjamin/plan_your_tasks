from PySide2 import QtWidgets, QtCore, QtGui
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    content = []
    def __init__(self):
        # доступ к переменным в файле design.py
        super().__init__()
        self.setupUi(self) # инициализация интерфейса
        self.addButton.clicked.connect(self.adding) # кнопка добавления
        self.clearButton.clicked.connect(self.clear_space) # кнопка удаления

        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.menu = QtWidgets.QMenu(self)
        self.tableWidget.menu.setGeometry(QtCore.QRect(16, 229, 525, 227))
        change = self.tableWidget.menu.addAction('Изменить')
        clear = self.tableWidget.menu.addAction('Удалить')
        self.tableWidget.customContextMenuRequested.connect(self.show_menu)
        # clear.triggered.connect(self.clear_table)
        # change.triggered.connect(self.change_table)
        clear.triggered.connect(lambda: QtWidgets.QMessageBox.information(self, 'Info', 'Очистка'))
        change.triggered.connect(lambda: QtWidgets.QMessageBox.information(self, 'Info', 'Добавление'))

    # noinspection PyArgumentList
    def adding(self):
        name = str(self.nameEvent.displayText())
        time_and_date = str(self.timeAndDate.dateTime().toString('HH:mm dd-MM-yyyy'))
        string = '{} в {}'.format(name, time_and_date)
        if len(string) > 0:
            if string not in self.content:
                string = str(len(self.content) + 1) + '. ' + string
                print(string)
                self.myList.addItem(string)
                self.content.append(string)
                self.clear_space()
        else:
            pass

    # noinspection PyArgumentList
    def clear_space(self):
        self.nameEvent.setText('')
        time = QtCore.QDateTime.currentDateTime()
        self.timeAndDate.setDateTime(time)

    # noinspection PyBroadException
    def show_menu(self, point):
        self.tableWidget.menu.exec_(QtGui.QCursor.pos())

    def clear_table(self):
        pass

    def change_table(self):
        pass

def main():
    app = QtWidgets.QApplication() # новый экземпляр QApplication
    window = ExampleApp() # новый  объект класса ExampleApp
    window.show() # показываем окно
    app.exec_() # запускаем приложение



if __name__ == '__main__':
    main()