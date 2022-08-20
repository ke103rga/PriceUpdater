import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
from interservice_price_parser import parse_price
from new_price_converter import classify_literature
from xls_file_maker import create_table_head, create_new_price, arrange_new_price


def make_new_price(files_data, filename, window, sale=17):
    try:
        new_price = parse_price(filename=files_data.get("interservis_price"), sale=sale)
        converted_price = classify_literature(new_price)

        result_file_path = f'{files_data["result_dir"]}/{filename.get()}.xlsx'

        create_table_head(result_file_path)
        create_new_price(result_file_path, converted_price=converted_price, sale=sale)
        arrange_new_price(result_file_path)

        messagebox.showinfo("Готово!", "Файл успешно сохранен в указаннной вами папке.")
    except Exception:
        messagebox.showinfo("Ошибка!", "Убедитесь в том что верно указали путь ко всем файлам.")
    finally:
        window.destroy()


def choose_file(files_data, key):
    filetypes = (("Excel файл", "*.xlsx *xls"), )
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                  filetypes=filetypes)
    if filename:
        files_data[key] = filename


def choose_directory(files_data, key):
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")
    if directory:
        files_data[key] = directory


def show_result():
    window = tk.Tk()
    window.title("Составитель прайса")
    window.geometry('600x400')
    window.resizable(False, False)

    files_data = {"interservis_price": "",
                  "result_dir": ""}

    search_int_file = "Выберите прайс Интерсервиса"
    lbl_int_file = tk.Label(window, text=search_int_file, font=('Times', 15))
    lbl_int_file.place(x=80, y=50)
    btn_file_int = tk.Button(text="Выбрать файл",
                         command=lambda:choose_file(files_data, "interservis_price"))
    btn_file_int.place(x=450, y=50)

    choose_sale = "Укажите скидку в процентах"
    lbl_sale = tk.Label(window, text=choose_sale, font=('Times', 15))
    lbl_sale.place(x=80, y=120)
    sale = tk.StringVar()
    entry_sale = tk.Entry(width=20, textvariable=sale)
    entry_sale.place(x=450, y=120)

    choose_res_dir = "Выберите папку,\n в которую будет сохранен результат"
    lbl_res_dir = tk.Label(window, text=choose_res_dir, font=('Times', 15))
    lbl_res_dir.place(x=80, y=190)
    btn_res_dir = tk.Button(text="Выбрать папку",
                             command=lambda: choose_directory(files_data, "result_dir"))
    btn_res_dir.place(x=450, y=193)

    choose_file_name = "Введите название итогового файла"
    lbl = tk.Label(window, text=choose_file_name, font=('Times', 15))
    lbl.place(x=80, y=260)
    filename = tk.StringVar()
    entry = tk.Entry(width=20, textvariable=filename)
    entry.place(x=450, y=260)

    btn_mk_price = tk.Button(text="Сформировать прайс",
                                  command=lambda: make_new_price(files_data, filename, window, sale=int(sale.get())))
    btn_mk_price.place(x=240, y=330)

    window.mainloop()

