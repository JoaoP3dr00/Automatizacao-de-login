from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.service = Service(executable_path='C:\\Users\\---')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=C:\\Users\\---')
        self.chrome = webdriver.Chrome(service=self.service, options=self.options)

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element('link text', 'Sign in')
            btn_sign_in.click()
        except Exception as e:
            print("Erro ao clicar:", e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login = self.chrome.find_element('id', 'login_field')
            input_password = self.chrome.find_element('id', 'password')
            btn_login = self.chrome.find_element('name', 'commit')

            input_login.send_keys('---')
            input_password.send_keys('---')
            btn_login.click()
        except Exception as e:
            print('Erro ao fazer login:', e)

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element("css selector",
                                              'body > div.logged-in.env-production.page-responsive.full-width > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > site-header-logged-in-user-menu > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def clica_log_out(self):
        try:
            logout = self.chrome.find_element('css selector',
                                              'body > div.logged-in.env-production.page-responsive.full-width > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > site-header-logged-in-user-menu > details > details-menu > form > button')
            logout.click()
        except Exception as e:
            print('Erro ao clicar no logout:', e)

    def verifica_user(self, usuario):
        profile_link = self.chrome.find_element('class name', 'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')

        assert usuario in profile_link_html


if __name__ == '__main__':
    chrome = ChromeAuto()
    sleep(1)
    chrome.acessa('https://github.com/')
    sleep(1)

    chrome.clica_perfil()
    sleep(1)
    chrome.clica_log_out()

    chrome.clica_sign_in()
    sleep(1)
    chrome.faz_login()
    sleep(1)
    chrome.clica_perfil()
    sleep(1)
    chrome.verifica_user('---')

    sleep(1)
    chrome.clica_log_out()

    sleep(2)
    chrome.sair()
