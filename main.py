import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, path):
        super().__init__(path)
        self.init_menu()
        self.init_instruction()
        self.db = db

    def init_menu(self):
        # Инициализация верхней панели(меню)

        self.book_img = tk.PhotoImage(file="images/book.png")
        self.printer_img = tk.PhotoImage(file="images/printer.png")
        self.laser_img = tk.PhotoImage(file="images/laser.png")
        self.data_img = tk.PhotoImage(file="images/data.png")

        menu = tk.Frame(bg='#d7d8e0', bd=2)
        menu.pack(side=tk.TOP, fill=tk.X)
        btn_info = tk.Button(menu, text='Инструкция', bg='#d7d8e0', bd=0, compound=tk.TOP,
                             command=self.init_instruction, image=self.book_img)
        btn_info.pack(side=tk.LEFT, padx=10)

        btn_printer = tk.Button(menu, text='3D Принтер', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.init_printer,
                                image=self.printer_img)
        btn_printer.pack(side=tk.LEFT, padx=10)

        btn_laser = tk.Button(menu, text='ЛГ-ый Станок', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.init_laser,
                              image=self.laser_img)
        btn_laser.pack(side=tk.LEFT, padx=10)

        btn_data = tk.Button(menu, text='Мои Расчёты', bg='#d7d8e0', bd=0, compound=tk.TOP, command=self.init_data,
                             image=self.data_img)
        btn_data.pack(side=tk.RIGHT)

    def init_instruction(self):
        # Инициализация начального окна(инструкции)

        instruction_frame = tk.Frame(bd=2)
        instruction_frame.place(x=0, y=60, relwidth=1, relheight=1)

        instruction_text_label = tk.Label(instruction_frame, text='Добро пожаловать в программу "3D CalcuPrinter".\n'
                                                                  'Используйте верхнюю панель для навигации по '
                                                                  'приложению\n Нажимайте по кнопкам нужных вам '
                                                                  'инструментов и вводите \nсвои значения. Все '
                                                                  'результаты ваших расчётов сохраняются. \nВ разделе '
                                                                  '"Мои Расчёты" их можно посмотреть.\n Приятного '
                                                                  'пользования!', font='courier 14')

        instruction_text_label.pack()

    def init_printer(self):
        # Инициализация окна расчёта(3Д Принтер)

        self.printer_frame = tk.Frame(bd=2)
        self.printer_frame.place(x=0, y=60, relwidth=1, relheight=1)

        # Наименование детели

        text_add = tk.Label(self.printer_frame, text='Наименование детали:', font='courier 14')
        text_add.place(x=136, y=20)

        self.entry_name = ttk.Entry(self.printer_frame)
        self.entry_name.place(x=360, y=24)

        # Материал

        material_label = tk.Label(self.printer_frame, text='Материал детали:', font='courier 14')
        material_label.place(x=180, y=50)

        self.combobox_material = ttk.Combobox(self.printer_frame,
                                              values=[u"PLA Пластик", u"ABS Пластик", u"PETG Пластик",
                                                      u"Laywood(Дерево)"])
        self.combobox_material.current(0)
        self.combobox_material.place(x=360, y=54)

        # Количество граммов материала

        number_of_grams_label = tk.Label(self.printer_frame, text='Вес материала:', font='courier 14')
        number_of_grams_label.place(x=202, y=80)

        self.entry_number_of_grams = ttk.Entry(self.printer_frame)
        self.entry_number_of_grams.place(x=360, y=84)

        grams_label = tk.Label(self.printer_frame, text='грамм', font='courier 14')
        grams_label.place(x=490, y=80)

        # Потребление

        consumption_label = tk.Label(self.printer_frame, text='Потребление принтера:', font='courier 14')
        consumption_label.place(x=125, y=110)

        self.combobox_consumption = ttk.Combobox(self.printer_frame, values=[u"240", u"360", u"480"])
        self.combobox_consumption.current(0)
        self.combobox_consumption.place(x=360, y=114)

        watt_label = tk.Label(self.printer_frame, text='ватт', font='courier 14')
        watt_label.place(x=505, y=110)

        # Цена принтера

        printer_cost_label = tk.Label(self.printer_frame, text='Цена принтера:', font='courier 14')
        printer_cost_label.place(x=202, y=140)

        self.entry_printer_cost = ttk.Entry(self.printer_frame)
        self.entry_printer_cost.place(x=360, y=144)

        # Количество деталей

        detail_quantity_label = tk.Label(self.printer_frame, text='Количество деталей:', font='courier 14')
        detail_quantity_label.place(x=147, y=170)

        self.entry_detail_quantity = ttk.Entry(self.printer_frame)
        self.entry_detail_quantity.place(x=360, y=174)

        # Дополнительная обработка

        additional_processing_label = tk.Label(self.printer_frame, text='Дополнительная обработка:', font='courier 14')
        additional_processing_label.place(x=81, y=200)

        self.combobox_additional_processing = ttk.Combobox(self.printer_frame, values=[u"Да", u"Нет"])
        self.combobox_additional_processing.current(1)
        self.combobox_additional_processing.place(x=360, y=204)

        # Время изготовления детали

        time_label = tk.Label(self.printer_frame, text='Время печати:', font='courier 14')
        time_label.place(x=213, y=230)

        self.entry_time = ttk.Entry(self.printer_frame)
        self.entry_time.place(x=360, y=234)

        minute_label = tk.Label(self.printer_frame, text='минут', font='courier 14')
        minute_label.place(x=490, y=234)

        # Кнопка Расчёта

        self.calc_img = tk.PhotoImage(file="images/calc.png")

        btn_calculate = tk.Button(self.printer_frame, text='Расчитать', bg='#d7d8e0', bd=0, compound=tk.TOP,
                                  image=self.calc_img, width=300, command=self.init_printer_counter)
        btn_calculate.place(x=210, y=270)

    def init_laser(self):
        # Инициализация окна расчёта(3Д Принтер)

        self.laser_frame = tk.Frame(bd=2)
        self.laser_frame.place(x=0, y=60, relwidth=1, relheight=1)

        # Наименование детели

        text_add = tk.Label(self.laser_frame, text='Наименование детали:', font='courier 14')
        text_add.place(x=136, y=20)

        self.entry_name = ttk.Entry(self.laser_frame)
        self.entry_name.place(x=360, y=24)

        # Материал

        material_label = tk.Label(self.laser_frame, text='Материал детали:', font='courier 14')
        material_label.place(x=180, y=50)

        self.combobox_material = ttk.Combobox(self.laser_frame, values=[u"Фанера", u"Кожа", u"Бумага"])
        self.combobox_material.current(0)
        self.combobox_material.place(x=360, y=54)

        # Длина материала

        number_of_len_label = tk.Label(self.laser_frame, text='Длина материала:', font='courier 14')
        number_of_len_label.place(x=180, y=80)

        self.entry_number_of_len = ttk.Entry(self.laser_frame)
        self.entry_number_of_len.place(x=360, y=84)

        len_label = tk.Label(self.laser_frame, text='см2', font='courier 14')
        len_label.place(x=490, y=80)

        # Потребление

        consumption_laser_label = tk.Label(self.laser_frame, text='Потребление станка:', font='courier 14')
        consumption_laser_label.place(x=147, y=110)

        self.combobox_consumption_laser = ttk.Combobox(self.laser_frame, values=[u"400", u"360", u"480"])
        self.combobox_consumption_laser.current(0)
        self.combobox_consumption_laser.place(x=360, y=114)

        watt_label = tk.Label(self.laser_frame, text='ватт', font='courier 14')
        watt_label.place(x=505, y=110)

        # Цена станка

        printer_cost_laser_label = tk.Label(self.laser_frame, text='Цена станка:', font='courier 14')
        printer_cost_laser_label.place(x=224, y=140)

        self.entry_laser_cost = ttk.Entry(self.laser_frame)
        self.entry_laser_cost.place(x=360, y=144)

        # Количество деталей

        detail_quantity_laser_label = tk.Label(self.laser_frame, text='Количество деталей:', font='courier 14')
        detail_quantity_laser_label.place(x=147, y=170)

        self.entry_detail_quantity_laser = ttk.Entry(self.laser_frame)
        self.entry_detail_quantity_laser.place(x=360, y=174)

        # Дополнительная обработка

        additional_processing_laser_label = tk.Label(self.laser_frame, text='Дополнительная обработка:',
                                                     font='courier 14')
        additional_processing_laser_label.place(x=81, y=200)

        self.combobox_additional_processing = ttk.Combobox(self.laser_frame, values=[u"Да", u"Нет"])
        self.combobox_additional_processing.current(1)
        self.combobox_additional_processing.place(x=360, y=204)

        # Время изготовления детали

        time_label = tk.Label(self.laser_frame, text='Время печати:', font='courier 14')
        time_label.place(x=213, y=230)

        self.entry_time = ttk.Entry(self.laser_frame)
        self.entry_time.place(x=360, y=234)

        minute_label = tk.Label(self.laser_frame, text='минут', font='courier 14')
        minute_label.place(x=490, y=234)

        # Кнопка Расчёта

        self.calc_img = tk.PhotoImage(file="images/calc.png")

        btn_calculate = tk.Button(self.laser_frame, text='Расчитать', bg='#d7d8e0', bd=0, compound=tk.TOP,
                                  image=self.calc_img, width=300, command=self.init_laser_counter)
        btn_calculate.place(x=210, y=270)

    def init_data(self):
        # Инициализация окна всех расчётов(база данных)

        self.data_frame = tk.Frame(bd=2)
        self.data_frame.place(x=0, y=60, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.data_frame,
                                 columns=('ID', 'name', 'name_machine', 'material', 'quantity', 'cost', 'percent'),
                                 height=35, show='headings')
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("name", width=130, anchor=tk.CENTER)
        self.tree.column("name_machine", width=110, anchor=tk.CENTER)
        self.tree.column("material", width=130, anchor=tk.CENTER)
        self.tree.column("quantity", width=90, anchor=tk.CENTER)
        self.tree.column("cost", width=150, anchor=tk.CENTER)
        self.tree.column("percent", width=70, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("name", text='Имя')
        self.tree.heading("name_machine", text='Машина')
        self.tree.heading("material", text='Материал')
        self.tree.heading("quantity", text='Количество')
        self.tree.heading("cost", text='Стоимость')
        self.tree.heading("percent", text='Процент')

        self.tree.pack()
        self.view_values()

    def view_values(self):
        # Отображения элеметов базы данных в виджете TreeView(ttk)

        self.db.cur.execute('''SELECT * FROM calculations''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def add_values(self):
        # Добавление данных в бд

        self.db.insert_data(self.name, self.name_machine, self.material, self.detail_quantity, self.result,
                            self.percent)

    def init_printer_counter(self):
        # Формула расчёта(3Д Принтер)

        # Получение информации из полей
        self.name = self.entry_name.get()
        self.name_machine = 'Принтер'
        self.material = self.combobox_material.get()
        self.amount_of_substance = int(self.entry_number_of_grams.get())
        self.detail_quantity = int(self.entry_detail_quantity.get())
        consumption = int(self.combobox_consumption.get())
        machine_cost = int(self.entry_printer_cost.get())
        additional_processing = self.combobox_additional_processing.get()
        time = int(self.entry_time.get())

        # Расчёт постобработки
        if additional_processing == 'Да':
            cost_processing = 3
        else:
            cost_processing = 0

        # Список стоимостей материалов
        material_cost_dict = {'PLA Пластик': 1300,
                              'ABS Пластик': 1000,
                              'PETG Пластик': 1000,
                              'Laywood(Дерево)': 2000,
                              }

        # Расчёт стоимости материала
        material_cost = material_cost_dict[self.material] / 1000 * self.amount_of_substance

        # Расчёт стоимости электроэнергии
        price_per_kWh = 4
        consumption_cost = consumption / 1000 * price_per_kWh * time

        # Итог(Основная формула)
        self.result = (material_cost + consumption_cost + cost_processing) * self.detail_quantity

        # Вычитание производственного брака(2%)
        self.result -= self.result / 100 * 2

        # Расчёт процента от стоимости принетра
        self.percent = self.result / (machine_cost / 100)

        # Сокращение дробей
        self.result = "%.2f" % self.result
        self.percent = "%.2f" % self.percent

        # Инициализация полей с результатами расчёта
        result_label = tk.Label(self.printer_frame, text='Результат: ' + str(self.result) + ' рублей.',
                                font='courier 14', width=100)
        result_label.place(x=-200, y=350)
        percent_label = tk.Label(self.printer_frame,
                                 text='Что составит ' + str(self.percent) + '% от стоимости принтера',
                                 font='courier 14', width=100)
        percent_label.place(x=-200, y=380)

        # Вызов функции для добавления результатов в базу данных
        self.add_values()

    def init_laser_counter(self):
        # Формула расчёта(Лазурно-Гравивовальный Станок)

        # Получение информации из полей
        self.name = self.entry_name.get()
        self.name_machine = 'ЛГ-ый Станок'
        self.material = self.combobox_material.get()
        self.amount_of_substance = int(self.entry_number_of_len.get())
        self.detail_quantity = int(self.entry_detail_quantity_laser.get())
        consumption = int(self.combobox_consumption_laser.get())
        machine_cost = int(self.entry_laser_cost.get())
        additional_processing = self.combobox_additional_processing.get()
        time = int(self.entry_time.get())

        # Расчёт постобработки
        if additional_processing == 'Да':
            cost_processing = 3
        else:
            cost_processing = 0

        # Список стоимости материалов
        material_cost_dict = {'Фанера': 345,
                              'Кожа': 3000,
                              'Бумага': 100,  # за 1м2
                              }

        # Расчёт стоимости материала
        material_cost = self.amount_of_substance * (material_cost_dict[self.material] / 10000)

        # Расчёт стоимости электроэнергии
        price_per_kWh = 4
        consumption_cost = consumption / 1000 * price_per_kWh * time

        # Итог(Основная формула)
        self.result = (material_cost + consumption_cost + cost_processing) * self.detail_quantity

        # Вычитание производственного брака(2%)
        self.result -= self.result / 100 * 2
        self.percent = self.result / (machine_cost / 100)

        # Сокращение дробей
        self.percent = "%.2f" % self.percent
        self.result = "%.2f" % self.result

        # Инициализация полей с результатами расчёта
        result_label = tk.Label(self.laser_frame, text='Результат: ' + str(self.result) + ' рублей.', font='courier 14',
                                width=100)
        result_label.place(x=-200, y=350)
        percent_label = tk.Label(self.laser_frame, text='Что составит ' + str(self.percent) + '% от стоимости принтера',
                                 font='courier 14', width=100)
        percent_label.place(x=-200, y=380)

        # Вызов функции для добавления результатов в базу данных
        self.add_values()


class DB:
    def __init__(self):
        # Создаём и/или подключаемся к таблице SQLite

        self.conn = sqlite3.connect('calculations.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS calculations (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name text, 
            name_machine text, material text, quantity int, cost int, percent real)''')
        self.conn.commit()

    def insert_data(self, name, name_machine, material, detail_quantity, result, percent):
        # Добавление данных в базу данных

        self.cur.execute(
            '''INSERT INTO calculations(name, name_machine, material, quantity, cost, percent) VALUES (?, ?, ?, ?, ?, 
            ?)''',
            (name, name_machine, material, detail_quantity, result, percent))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("3D CalcuPrinter")
    root.geometry("720x800+0+0")
    root.resizable(False, False)
    root.mainloop()
