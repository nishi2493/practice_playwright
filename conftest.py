import pytest
from playwright.sync_api import Page
import config
from pages.login_page import LoginPage

SESSION_FILE="session.json"

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="uat"
    )

@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def base_url(environment):
    return config.get_base_url(environment)


@pytest.fixture(scope="session")
def logged_in_session(browser,base_url):
    context=browser.new_context()
    page=context.new_page()

    login_page=LoginPage(page,base_url)
    login_page.open()
    login_page.login(config.USERNAME, config.PASSWORD)
    expect(login_page.heading).to_be_visible()

    context.storage_state(path=SESSION_FILE)

    context.close()

    return SESSION_FILE

@pytest.fixture
def browser_context_args(browser_context_args, logged_in_session):
    return {
        **browser_context_args,
        "storage_state": logged_in_session,
    }      

@pytest.fixture
def logged_out_page(browser):
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if not page:
            page = item.funcargs.get("logged_out_page")

        if page:

            page.screenshot(
                path=f"screenshots/{item.name}.png",
                full_page=True
            )

