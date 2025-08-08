from selenium import webdriver
import pytest
import json

USERNAME = "aryasharma_CA1R9w"
ACCESS_KEY = "cFunTaqWYcPmmj7uKF9P"

capabilities = [
    {
        'browserName': 'Chrome',
        'browserVersion': 'latest',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'buildName': 'Parallel Build',
            'sessionName': 'Chrome Test'
        }
    },
    {
        'browserName': 'Firefox',
        'browserVersion': 'latest',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'buildName': 'Parallel Build',
            'sessionName': 'Firefox Test'
        }
    },
    {
        'browserName': 'Safari',
        'browserVersion': 'latest',
        'bstack:options': {
            'os': 'OS X',
            'osVersion': 'Ventura',
            'buildName': 'Parallel Build',
            'sessionName': 'Safari Test'
        }
    },
    {
        'browserName': 'iPhone',
        'bstack:options': {
            'deviceName': 'iPhone 14',
            'osVersion': '16',
            'realMobile': 'true',
            'buildName': 'Parallel Build',
            'sessionName': 'iPhone Safari Test'
        }
    },
    {
        'browserName': 'Android',
        'bstack:options': {
            'deviceName': 'Samsung Galaxy S23',
            'osVersion': '13.0',
            'realMobile': 'true',
            'buildName': 'Parallel Build',
            'sessionName': 'Android Chrome Test'
        }
    }
]

@pytest.mark.parametrize("caps", capabilities)
def test_browserstack(caps):
    
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", caps.get("browserName"))
    if "browserVersion" in caps:
        options.set_capability("browserVersion", caps.get("browserVersion"))
    for key, value in caps.items():
        if key != "browserName" and key != "browserVersion":
            options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    driver.get("https://elpais.com/opinion/")
    assert "Opinión" in driver.title

    
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Title verified"}}'
    )

    driver.quit()
