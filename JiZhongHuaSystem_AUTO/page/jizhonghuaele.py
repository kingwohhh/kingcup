from page.basepage import *


class JzhEle(PageObject):
    username = PageElement(xpath="//input[@class='input-inner'and@type='text']")
    password = PageElement(xpath="//input[@type='password'and@placeholder='密码']")
    login_button = PageElement(xpath="//button[@class='x-button x-button-css-var size-large style-primary block login-btn']")
    mytodo = PageElement(xpath="//div[@class='my-todo']")

    def click_login_button(self):
        return self.login_button.click()

    def click_mytodo_button(self):
        return self.mytodo.click()