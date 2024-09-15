from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

### Constants
website = "https://www.adamchoi.co.uk/overs/detailed"
path    = r'C:\Users\hp\chromedriver.exe'
xpath_all_matches = "//label[@analytics-event='All matches']"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

### Init
service = Service(executable_path=path)
driver  = webdriver.Chrome(service=service,options=chrome_options)
driver.get(url=website)

### Click on 'all  matches'
all_matches_button = driver.find_element(by=By.XPATH,value=xpath_all_matches)
all_matches_button.click()

### locate the table
date      = []
home_team = []
score     = []
away_team = []

all_matches = driver.find_elements(by=By.TAG_NAME,value="tr")
for match in all_matches :
    ###//tr/td
    date.append(match.find_element(by=By.XPATH,value='./td[1]').text)
    #home_team.append(match.find_element(by=By.XPATH,value='./td[2]').text)
    score.append(match.find_element(by=By.XPATH,value='./td[3]').text)
    #away_team.append(match.find_element(by=By.XPATH,value='./td[4]').text)

print(home_team)
#driver.quit()