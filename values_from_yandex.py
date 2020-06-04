from selenium import webdriver

class yand_sel(object):
    def get_dollar(self):
        dollar = self.browser.find_element_by_css_selector(".inline-stocks__item_id_2002 .inline-stocks__value_inner")  # class value in the tag
        return dollar.text

    def get_euro(self):
        euro = self.browser.find_element_by_css_selector(".inline-stocks__item_id_2000 .inline-stocks__value_inner")  # class value in the tag
        return euro.text

    def get_oil(self):
        oil = self.browser.find_element_by_css_selector(".inline-stocks__item_id_1006 .inline-stocks__value_inner")  # class value in the tag
        return oil.text

    def main(self):
        self.browser = webdriver.Chrome()
        link = "https://yandex.ru"
        self.browser.get(link)
        print(f"Dollar: {self.get_dollar()}")
        print(f"Euro: {self.get_euro()}")
        print(f"Oil:{self.get_oil()}")
        self.browser.quit()

if __name__ == '__main__':
    yand_sel().main()

