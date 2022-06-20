# import sys
# from base import Sender
# import os
import io
import time
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
# from tkinter.ttk import Progressbar
from tkinter import scrolledtext
import threading
from datetime import datetime
import requests
import telebot


class IORedirector(object):

    def __init__(self, text_area):
        self.text_area = text_area


class StdoutRedirector(IORedirector):

    def write(self, str):
        self.text_area.insert(INSERT, dtime() + str + "\n")
        self.text_area.see(tk.END)


# TOKEN_CONTROL_BOT = "5101294140:AAGy3NfCRep4SQaMZCU9QeeeddDZz_yGCAs"
API_TOKEN = '5171970699:AAGe79XHfZpVESLIPUNNvughwyvu5TLlPPU'
conf_dir = 'conf/'
flesson = 'datas_text.txt'
CHANNEL_NAME = '@thcfbdev'
data_folder = 'course/'
work_course_folder = 'test_cource/'
DELAY_TIMER = 5
WAIT_TIMER = 5
STOP_STRING = '###'
file_log_path = 'conf/console.txt'
file_err_path = 'conf/console_err.txt'
course_config = 'conf/course.txt'
bot_config = 'conf/bot.txt'
channel_config = 'conf/chanel.txt'
current_datetime = datetime.now()
len_str_f = 0


class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def run(self):
        print('Script is Running')

        def sendcontentdoc(data_folder, cont, CHANNEL_NAME, bot, work_course_folder):
            cont = cont.strip()
            line_doc = work_course_folder.replace("'", '') + data_folder + cont
            doc = open(line_doc.replace("\n", ""), 'rb')
            bot.send_document(CHANNEL_NAME.replace("'", ''), doc)

        def sendcontentvideo(data_folder, cont, CHANNEL_NAME, bot, work_course_folder):
            cont = cont.strip().replace("\n", "")
            line_doc = work_course_folder.replace("'", '').replace("\n", "") \
                       + data_folder.replace("\n", "").replace("'", '') + cont
            print(line_doc)
            doc = line_doc.replace("\n", "")
            bot.send_video(CHANNEL_NAME, open(doc, 'rb'), width=720, height=1280, timeout=60)

        def sendcontentphoto(data_folder, cont, CHANNEL_NAME, bot, work_course_folder):
            cont = cont.strip()
            line_doc = work_course_folder.replace("'", '') + data_folder + cont
            doc = open(line_doc.replace("\n", ""), 'rb')
            bot.send_photo(CHANNEL_NAME.replace("'", ''), doc, timeout=60)

        def sendcontentmessageHTML(cont, CHANNEL_NAME, bot):
            bot.send_message(CHANNEL_NAME.replace("\n", ""), f"{cont}", parse_mode='html')

        def sendcontentmessage(cont, API_TOKEN, CHANNEL_NAME):
            TAKE_ID_CHANNEL = 'https://api.telegram.org/bot' + API_TOKEN.replace("\n", "").replace("'", "") \
                              + '/sendMessage?chat_id=' + CHANNEL_NAME.replace("\n", "") + '&text=' + cont

            requests.get(TAKE_ID_CHANNEL)

        def sender(API_TOKEN, CHANNEL_NAME, flesson, DELAY_TIMER, STOP_STRING, work_course_folder,
                   data_folder):

            w_script = work_course_folder.replace("'", '').replace("\n", "") + flesson
            bot = telebot.TeleBot(API_TOKEN.replace("'", ""))
            dfile = open(w_script, "r", encoding='utf-8')
            data_lines = dfile.readlines()
            t = 0
            print(self.__flag)

            while data_lines: #or self.__running.is_set():
                #
                # self.__flag.wait()

                # line = dfile.readline()
                # print(data_lines)
                READ_STRING = str(data_lines[t])
                if len(READ_STRING.strip()) == 0:

                    time.sleep(DELAY_TIMER)
                elif 'wait' in READ_STRING:
                    Lfile = READ_STRING.split('#')
                    split = Lfile[1]
                    split.replace("\n", "")
                    WAIT_TIMER = int(split)  # * 60
                    time.sleep(WAIT_TIMER)
                elif READ_STRING == STOP_STRING:
                    print('Закончили')
                    dfile.close()
                    break
                else:
                    if '#' in READ_STRING:
                        if 'document' in READ_STRING:
                            Lfile = READ_STRING.split('#')
                            cont = Lfile[1]
                            print(f'Нашли документ {cont}')
                            sendcontentdoc(data_folder, cont, CHANNEL_NAME, bot, work_course_folder)
                        if 'video' in READ_STRING:
                            Lfile = READ_STRING.split('#')
                            cont = Lfile[1]
                            print(f'Нашли видео {cont}')
                            cont = cont.strip().replace("\n", "")
                            sendcontentvideo(data_folder, cont, CHANNEL_NAME, bot, work_course_folder)
                        if 'photo' in READ_STRING:
                            Lfile = READ_STRING.split('#')
                            cont = Lfile[1]
                            print(f'Нашли фото {cont}')
                            sendcontentphoto(data_folder, cont, CHANNEL_NAME, bot, work_course_folder)
                        if 'html' in READ_STRING:
                            Lfile = READ_STRING.split('#')
                            cont = Lfile[1]
                            print(f'Нашли HTML {cont}')
                            sendcontentmessageHTML(cont, CHANNEL_NAME.replace("'", ''), bot)
                    else:
                        cont = READ_STRING
                        print(f'Нашли текст {cont}')
                        sendcontentmessage(cont, API_TOKEN.replace("'", ''), CHANNEL_NAME.replace("'", ''))
                    t = t + 1
                bot.infinity_polling()

            time.sleep(1)
            dfile.close()

        sender(API_TOKEN, CHANNEL_NAME, flesson, DELAY_TIMER, STOP_STRING, work_course_folder,
               data_folder)

    def pause(self):
        print('Script on a Break')
        self.__flag.clear()

    def resume(self):
        print('Script Resume')
        self.__flag.set()

    def stop(self):
        print('Script is Stopped')
        self.__flag.set()
        self.__running.clear()


CStart = Job()


def count_lines(filename):
    i = 0
    with io.open(filename, encoding='utf-8') as file:
        for line in file:
            i += 1
    return i


def set_course(event):
    global work_course_folder
    widget.insert(INSERT, dtime() + "course selected " + selected_course.get() + "\n")
    widget.see(tk.END)
    read_select_course = read_course_config(course_config)
    work_course_folder = read_select_course.get(str(selected_course.get())).replace("'", '').replace("\n", '')
    print('set global course ' + work_course_folder)


def set_bot(event):
    global API_TOKEN
    widget.insert(INSERT, dtime() + "bot selected " + selected_bot.get() + "\n")
    widget.see(tk.END)
    read_select_bot = read_bot_config(bot_config)
    API_TOKEN = read_select_bot.get(str(selected_bot.get())).replace("\n", "")
    print('set global bot ' + API_TOKEN)


def set_chanel(event):
    global CHANNEL_NAME
    widget.insert(INSERT, dtime() + "chanel selected " + selected_chanel.get() + "\n")
    widget.see(tk.END)
    read_select_channel = read_channel_config(channel_config)
    CHANNEL_NAME = read_select_channel.get(str(selected_chanel.get())).replace("'", '').replace("\n", '')
    print('set global chanel ' + CHANNEL_NAME)


def dtime():
    tdatetime = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
    cdatetime = str(tdatetime) + '  '
    return cdatetime


def read_course_config(*args):
    course_list = {}
    with open(*args, 'r') as fcourse:
        for line in fcourse:
            key, value = line.split(': ')
            course_list.update({key: value})
    return course_list


def read_bot_config(*args):
    bot_list = {}
    with open(*args, 'r') as fbot:
        for line in fbot:
            key, value = line.split(': ')
            bot_list.update({key: value})
    return bot_list


def read_channel_config(*args):
    channel_list = {}
    with open(*args, 'r') as fchannel:
        for line in fchannel:
            key, value = line.split(': ')
            channel_list.update({key: value})
    return channel_list


def out(*args):
    with open('file_log_path', 'a') as flog:
        z = 1
        flog.write(*args)
        flog.close()


def err(*args):
    with open('file_err_path', 'a') as ferrlog:
        ferrlog.write(*args)
        ferrlog.close()


def send_log(*args):
    stext = str(args) + '/n'
    widget.insert(INSERT, stext)


def start_clicked():
    global len_str_f
    signal = False
    if selected_course.get() == 'Set Course' or selected_bot.get() == 'Set Bot' \
            or selected_chanel.get() == 'Set channel':
        widget.insert(INSERT, dtime() + "Not selected parameter" + "\n")
        widget.see(tk.END)
    else:
        # global x

        len_str_f = count_lines(work_course_folder.replace("'", '').replace("\n", "") + flesson)
        print(len_str_f)
        widget.insert(INSERT, dtime() + "Строк в файле" + str(len_str_f) + "\n")
        CStart.start()
        '''
         x = threading.Thread(target=Sender, name='course_process', args=(CHANNEL_NAME, API_TOKEN, data_folder
                                                                              , flesson, DELAY_TIMER, STOP_STRING,
                                                                              work_course_folder),
                             daemon=True)
        '''
        # x.start()
        # progress_bar.start()
        # progress_bar.step(1)


def break_clicked():
    global a
    CStart.pause()
    a = Toplevel()
    label = tk.Label(a, text='Скрипт обучения на паузе, для старта нажми EXIT')
    button = Button(a, text="Exit", command=resume_clicked())
    button.pack()
    label.pack()


def resume_clicked():
    print(threading.get_native_id())
    CStart.resume()
    a.destroy


def stop_clicked():
    print(threading.get_native_id())
    CStart.stop()
    # print(x.is_alive())


window = Tk()

window.title("Добро пожаловать в LMS HCFB@DocentoFF")
window.geometry('800x700')

menu = Menu(window)
menu_file = Menu(menu)
menu_file.add_command(label='Новый')
menu_file.add_separator()
menu_file.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=menu_file)

menu_settings = Menu(menu, )
menu_settings.add_command(label='Редактировать список ботов')
menu_settings.add_separator()
menu_settings.add_command(label='Редактировать список курсов')
menu_settings.add_separator()
menu_settings.add_command(label='Редактировать config.ini')
menu.add_cascade(label='Настройки', menu=menu_settings)

menu_faq = Menu(menu)
menu_faq.add_command(label='Документация')
menu_faq.add_separator()
menu_faq.add_command(label='Версия')
menu.add_cascade(label='FAQ', menu=menu_faq)

window.config(menu=menu)

selected_course = tk.StringVar()
combo_course = Combobox(window, textvariable=selected_course)
combo_course['values'] = list(read_course_config('conf/course.txt').keys())
combo_course.current(0)  # установите вариант по умолчанию

combo_course.grid(column=0, row=1, padx=20, pady=20)

lbl_course = Label(window, text="Выбираем курс")
lbl_course.grid(column=1, row=1)

selected_bot = tk.StringVar()
combo_bot = Combobox(window, textvariable=selected_bot)
combo_bot['values'] = list(read_bot_config('conf/bot.txt').keys())
combo_bot.current(0)  # установите вариант по умолчанию
combo_bot.grid(column=0, row=2, padx=20, pady=20)

lbl_bot = Label(window, text="Выбираем бот")
lbl_bot.grid(column=1, row=2)

selected_chanel = tk.StringVar()
combo_chanel = Combobox(window, textvariable=selected_chanel)
combo_chanel['values'] = list(read_channel_config('conf/chanel.txt').keys())
combo_chanel.current(0)  # установите вариант по умолчанию
combo_chanel.grid(column=0, row=3, padx=20, pady=20)

lbl_bot = Label(window, text="Выбираем канал")
lbl_bot.grid(column=1, row=3)

btn1 = Button(window, text="Пауза", command=break_clicked)
btn1.grid(column=1, row=4)

btn2 = Button(window, text="Пуск", command=start_clicked)
btn2.grid(column=0, row=4)

btn2 = Button(window, text="Стоп", command=stop_clicked)
btn2.grid(column=0, row=5)

widget = scrolledtext.ScrolledText(window, width=65, height=20, padx=20, pady=20)
widget.grid(column=0, row=0)
'''
progress_bar = Progressbar(window, orient="horizontal", mode="determinate", maximum=len_str_f, value=0)
progress_bar.grid(row=5, column=0, padx=20, pady=20)
progress_bar.start()
progress_bar.step(1)
'''

widget.insert(INSERT, dtime() + "Выбираем курс, какнал и бот" + "\n")
widget.insert(INSERT, dtime() + "Бот должен быть добавлен в администраторы канала!!" + "\n")
widget.see(tk.END)

combo_course.bind("<<ComboboxSelected>>", set_course)
combo_bot.bind("<<ComboboxSelected>>", set_bot)
combo_chanel.bind("<<ComboboxSelected>>", set_chanel)

# sys.stdout = StdoutRedirector(widget)
# sys.stderr = StdoutRedirector(widget)
widget.see(tk.END)

window.mainloop()
