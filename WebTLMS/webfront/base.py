import io
import time
import requests
import telebot


class Sender:

    def __init__(self, CHANNEL_NAME, API_TOKEN, data_folder, flesson, DELAY_TIMER, STOP_STRING, work_course_folder):
        self.CHANNEL_NAME = CHANNEL_NAME
        self.API_TOKEN = API_TOKEN
        self.data_folder = data_folder
        self.flesson = flesson
        self.DELAY_TIMER = DELAY_TIMER
        self.STOP_STRING = STOP_STRING
        self.work_course_folder = work_course_folder
        Sender.sender(self, API_TOKEN, CHANNEL_NAME, flesson, DELAY_TIMER, STOP_STRING, work_course_folder, data_folder)

    def sendcontentdoc(self, data_folder, cont, CHANNEL_NAME, bot, work_course_folder):
        cont = cont.strip()
        line_doc = work_course_folder.replace("'", '') + data_folder + cont
        doc = open(line_doc.replace("\n", ""), 'rb')
        bot.send_document(CHANNEL_NAME.replace("'", ''), doc)

    def sendcontentvideo(self, data_folder, cont, CHANNEL_NAME, bot, work_course_folder):
        cont = cont.strip().replace("\n", "")
        line_doc = work_course_folder.replace("'", '').replace("\n", "") \
                   + data_folder.replace("\n", "").replace("'", '') + cont
        print(line_doc)
        doc = line_doc.replace("\n", "")
        bot.send_video(CHANNEL_NAME, open(doc, 'rb'), width=720, height=1280, timeout=60)
        # , width=720, height=1280, timeout=60

    def sendcontentphoto(self, data_folder, cont, CHANNEL_NAME, bot, work_course_folder):
        cont = cont.strip()
        line_doc = work_course_folder.replace("'", '') + data_folder + cont
        doc = open(line_doc.replace("\n", ""), 'rb')

        bot.send_photo(CHANNEL_NAME.replace("'", ''), doc, timeout=60)

    def sendcontentmessageHTML(self, cont, CHANNEL_NAME, bot):
        bot.send_message(CHANNEL_NAME.replace("\n", ""), f"{cont}", parse_mode='html')

    def sendcontentmessage(self, cont, API_TOKEN, CHANNEL_NAME):
        TAKE_ID_CHANNEL = 'https://api.telegram.org/bot' + API_TOKEN.replace("\n", "").replace("'", "") \
                          + '/sendMessage?chat_id=' + CHANNEL_NAME.replace("\n", "") + '&text=' + cont

        requests.get(TAKE_ID_CHANNEL)

    def start_bot(self, API_TOKEN):
        bot1 = telebot.TeleBot(API_TOKEN)
        return bot1

    def sender(self, API_TOKEN, CHANNEL_NAME, flesson, DELAY_TIMER, STOP_STRING, work_course_folder, data_folder):

        w_script = work_course_folder.replace("'", '').replace("\n", "") + flesson
        bot = telebot.TeleBot(API_TOKEN.replace("'", ""))

        with io.open(w_script, encoding='utf-8') as file:
            for line in file:

                READ_STRING = str(line)
                if len(line.strip()) == 0:

                    time.sleep(DELAY_TIMER)
                elif 'wait' in READ_STRING:

                    Lfile = READ_STRING.split('#')
                    split = Lfile[1]
                    split.replace("\n", "")
                    WAIT_TIMER = int(split)  # * 60
                    time.sleep(WAIT_TIMER)
                elif READ_STRING == STOP_STRING:
                    print('Закончили')
                    file.close()
                    break
                else:
                    if '#' in READ_STRING:
                        if 'document' in READ_STRING:
                            Lfile = READ_STRING.split('#')
                            cont = Lfile[1]
                            print(f'Нашли документ {cont}')
                            self.sendcontentdoc(data_folder, cont, CHANNEL_NAME, bot, work_course_folder)
                        if 'video' in READ_STRING:
                            Lfile = READ_STRING.split('#')
                            cont = Lfile[1]
                            print(f'Нашли видео {cont}')
                            cont = cont.strip().replace("\n", "")
                            # line_doc = work_course_folder.replace("'", '').replace("\n", "") + data_folder + cont

                            # doc = open(line_doc, 'rb')
                            self.sendcontentvideo(data_folder, cont, CHANNEL_NAME, bot, work_course_folder)
                            # doc = open(line_doc.replace("\n", ""), 'rb')

                            # bot.send_video(CHANNEL_NAME, doc, width=720, height=1280, timeout=60)

                        if 'photo' in READ_STRING:
                            Lfile = READ_STRING.split('#')
                            cont = Lfile[1]
                            print(f'Нашли фото {cont}')
                            self.sendcontentphoto(data_folder, cont, CHANNEL_NAME, bot, work_course_folder)
                        if 'html' in READ_STRING:
                            Lfile = READ_STRING.split('#')
                            cont = Lfile[1]
                            print(f'Нашли HTML {cont}')
                            self.sendcontentmessageHTML(cont, CHANNEL_NAME.replace("'", ''), bot)
                    else:
                        cont = READ_STRING
                        print(f'Нашли текст {cont}')
                        self.sendcontentmessage(cont, API_TOKEN.replace("'", ''), CHANNEL_NAME.replace("'", ''))
        return bot

        bot.infinity_polling()
