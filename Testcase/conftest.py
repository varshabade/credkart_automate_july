import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.firefox.options import Options
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("launching chrome")
    elif browser=='edge':
        driver=webdriver.Edge()
        print("launching edge")
    else:
        print("headlessmode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    # options=Options()
    # options.binary_location="c:\\Program Files\\Mozilla Firefox\\Firefox.exe"
    # driver=webdriver.Firefox(options=options)

    driver.get("https://automation.credence.in")
    return driver
# def pytest_metadata(metadata):
#     metadata["batch"]="CT15"
#     metadata["Class"]="Credence"
#     metadata.pop("platform",None)
@pytest.fixture(params=
                [("Credencetest@test.com","Credence@123"),
              ("Credencetest1156@test.com","Credence@123"),
              ("Credencetest@test.com","Credence@1234"),
              ("Credencetest1190@test.com","Credence@1234")
                 ])
def getdataForLogin(request):
    return request.param
