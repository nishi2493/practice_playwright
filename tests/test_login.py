from playwright.sync_api import Page,expect
import pytest

import config
from pages.login_page import LoginPage
from utils.json_utils import read_json_file

@pytest.mark.smoke
def test_login(logged_out_page,base_url):

    login_page = LoginPage(logged_out_page,base_url)
    login_page.open()
    login_page.login(config.USERNAME, config.PASSWORD)
    expect(login_page.heading).to_be_visible()
    print(login_page.heading)
    
    
    

def test_json_read():
    data=read_json_file("data/test_data.json")
    print(data["user"]["username"])
