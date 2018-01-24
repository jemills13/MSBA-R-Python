#I wrote this program to allow the computer to automatically play 2048. It tries 4 times play
#If your computer doesn't selenium or webdriver to run the code, see video tutorial here: https://www.screencast.com/t/oleCu3Oy

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 


browser = webdriver.Firefox() 
browser.get('https://gabrielecirulli.github.io/2048/') #url
htmlElem = browser.find_element_by_tag_name('html') 

for i in range(1,5):
    for i in range(1,256): 
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
    linkElem = browser.find_element_by_link_text('Try again') 
    linkElem.click()






