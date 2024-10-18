import time

import pytest

from config.conf import ConfigManager
from page.jizhonghuaele import JzhEle


class TestLogin:
    @pytest.mark.test1
    def test_login_success(self, drivers):
        drivers.get(ConfigManager.PROJECT_URL)
        login_ele = JzhEle(drivers)
        assert login_ele.username.get_attribute("placeholder") == '手机号/邮箱'
        assert login_ele.password.get_attribute("placeholder") == "密码"
        login_ele.username = ConfigManager.USERNAME
        login_ele.password = ConfigManager.PASSWORD
        login_ele.click_login_button()
        time.sleep(6)


