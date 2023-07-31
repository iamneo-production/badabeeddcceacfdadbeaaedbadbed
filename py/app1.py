from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


remote_url = "http://127.0.0.1:4444"  # Specify the URL of the remote WebDriver

options = Options()

driver = webdriver.Remote(command_executor=remote_url, options=options)


driver.get('https://www.example.com')

current_url = driver.current_url
print("Current URL:", current_url)

# Close the WebDriver
driver.quit()



