from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Example additional option

remote_url = "http://34.85.201.58:443"  # Replace with the actual URL of your Selenium Grid hub

driver = webdriver.Remote(
    command_executor=remote_url,
    options=options
)

driver.get('https://google.com')

current_url = driver.current_url
print("Current URL:", current_url)
driver.quit()