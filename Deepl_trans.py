from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from time import sleep

class deepl_translator:
    def __init__(self,text,to_lang='zh-ZH'):
        lang_dict = {
            'en-US':"//*[text()='英语（美式）']",
            'en-GB':"//*[text()='英语（英式）']",
            'fr-FR':"//*[text()='法语']",
            'es-ES':"//*[text()='西班牙语']",
            'pt-PT': "//*[text()='葡萄牙语']",
            'pt-BR': "//*[text()='葡萄牙语（巴西）']",
            'it-IT': "//*[text()='意大利语']",
            'nl-NL': "//*[text()='荷兰语']",
            'pl-PL': "//*[text()='波兰语']",
            'ru-RU': "//*[text()='俄语']",
            'ja_JA': "//*[text()='日语']",
            'zh-ZH': "//*[text()='中文（简体）']",
        }
        to_lang = lang_dict[to_lang]
        self.driver_init()
        self.get_translation(text,to_lang)
 #       self.driver.quit()

    def driver_init(self):
        url = 'https://www.deepl.com/translator'
        chrome_opt = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2,
                 'profile.default_content_setting_values':
                     {
                         'notifications': 2
                     }
                 }
        chrome_opt.add_experimental_option('prefs', prefs)
        chrome_opt.add_argument('--headless')
        chrome_opt.add_argument('-lang=zh-cn')

        self.driver = webdriver.Chrome(options=chrome_opt)

        self.driver.get(url)
        sleep(2)
    def get_translation(self,text,to_lang):
        # deal with cookies
        self.driver.find_element_by_xpath('//*[@id="dl_cookieBanner"]/div/div/div/span/div[2]/button[1]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dl_cookieBanner"]/div/div/div/span/div[2]/button[1]').click()
        sleep(1)

        # choose 'to_lang'
        self.driver.find_element_by_xpath('//*[@id="dl_translator"]/div[3]/div[2]/div[3]/div[1]/div[1]/div[1]/button/div').click()
        sleep(0.2)

        self.driver.find_element_by_xpath(to_lang).click()
        sleep(0.2)
        # translation start
        self.driver.find_element_by_xpath('//*[@id="dl_translator"]/div[3]/div[2]/div[1]/div[2]/div/textarea').send_keys(text)
        sleep(2)
        while True:
            self.translation = self.driver.find_element_by_id('target-dummydiv').get_attribute('textContent')
            if self.translation != '':
                break
            sleep(0.5)

        self.translation = self.translation.replace('电晕','新冠')



if __name__ == '__main__':
    text = 'Was wir in der Corona-Krise von anderen Ländern lernen können\nWährend es in Deutschland weiterhin täglich viele neue Corona-Infektionen gibt, können in manchen anderen Ländern schon wieder Großveranstaltungen stattfinden. Was macht man dort anders?\n\nIn Deutschland gelingt es bisher nicht, die Corona-Zahlen im Herbst deutlich zu\xa0senken. Ein Blick in die Welt zeigt aber, dass man einiges von anderen Ländern lernen kann. Anfangsging\xa0man zum Beispiel\xa0davon aus, dass\xa0sich\xa0in Afrika zehn Millionen Menschen in einem halben Jahr\xa0infizieren\xa0würden.\nDie afrikanischen Staaten\xa0kamen\xa0aber bisher ziemlich\xa0glimpflich davon. Sie waren nämlich – anders als Deutschland – gut auf Pandemien vorbereitet. „Das\xa0Problembewusstsein\xa0für Pandemien ist dort viel größer, weil es so etwas dort in der Vergangenheit mehr gegeben hat“, sagt der Wiener Wissenschaftler Peter Klimek.\nAuch Neuseeland\xa0kommt gut durch\xa0die Pandemie: Großveranstaltungen finden wieder statt, nur 25 Menschen starben im Zusammenhang mit Covid-19. Denn hier entschied man sich schon früh für sehr harte Maßnahmen und schloss sofort die Grenzen. Auch die Krisenkommunikation von\xa0Premierministerin\xa0Jacinda Ardern galt als\xa0vorbildlich, weil sie ihre\xa0Maßnahmen\xa0täglich erklärte und bei den Bürgern ein Gemeinschaftsgefühl schuf.\nJapan handelte weniger streng, konnte seine Zahlen aber trotzdem senken. Der\xa0Virologe\xa0Christian Drosten hat zwei Erklärungen dafür: Einerseits\xa0unterband\xa0man dort\xa0gezielt\xa0die Entstehung von Clustern, also Orten, wo sich sehr viele Menschen infizieren. Andererseits ist – wie in vielen anderen asiatischen Ländern – das Tragen von Masken in Japan sehr akzeptiert.\nNicht jeder Erfolg\xa0lässt sich\xa0auf Deutschland\xa0übertragen, weil zum Beispiel Inseln oder Staaten mit einer jungen Bevölkerung\xa0über\xa0bestimmte Vorteile\xa0verfügen. Erklärt man aber\xa0transparent, warum bestimmte Maßnahmen beschlossen werden, und verhindert\xa0konsequent\xa0das Entstehen von Clustern, so ist schon viel gewonnen.\n'
    test = deepl_translator(text,'zh-ZH')

