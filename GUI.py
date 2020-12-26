from PySide2 import QtWidgets, QtCore
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    content = []
    def __init__(self):
        # доступ к переменным в файле design.py
        super().__init__()
        self.setupUi(self) # инициализация интерфейса
        self.addButton.clicked.connect(self.adding) # кнопка добавления
        self.clearButton.clicked.connect(self.clear_space) # кнопка удаления
        self.customContextMenuRequested.connect(self.show_menu) # контекстное меню

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


class ContextMenuWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_menu)
        # self.custom_menu()

        self.menu = QtWidgets.QMenu(self)
        clear = self.menu.addAction('Удалить')
        change = self.menu.addAction('Изменить')
        clear.triggered.connect(self.clear_table)
        change.triggered.connect(self.change_table)

    def show_menu(self, point):
        self.menu.exec(self.mapToGlobal(point))

    def clear_table(self):
        pass

    def change_table(self):
        pass




def main():
    app = QtWidgets.QApplication() # новый экземпляр QApplication
    window = ExampleApp() # новый  объект класса ExampleApp
    # context_menu = ContextMenuWidget()
    # context_menu.resize(400, 400)
    # context_menu.se()
    window.show() # показываем окно
    app.exec_() # запускаем приложение



if __name__ == '__main__':
    main()