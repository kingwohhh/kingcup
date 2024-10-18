import time
import pytest
from config.conf import ConfigManager
from page.jizhonghuaele import JzhEle


@pytest.fixture(scope='class', autouse=True)
def login_in(drivers):
    drivers.get(ConfigManager.PROJECT_URL)
    login_ele = JzhEle(drivers)
    assert login_ele.username.get_attribute("placeholder") == '手机号/邮箱'
    assert login_ele.password.get_attribute("placeholder") == "密码"
    login_ele.username = ConfigManager.USERNAME
    login_ele.password = ConfigManager.PASSWORD
    login_ele.click_login_button()
    yield

class TestUpload:
    @pytest.mark.smoke
    def test_001(self, drivers):
        login_ele = JzhEle(drivers)
        login_ele.click_mytodo_button()
        time.sleep(6)