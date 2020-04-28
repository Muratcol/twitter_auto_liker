from selenium import webdriver
import os
import time 
from selenium.webdriver.common.keys import Keys

container = []
browser = webdriver.Firefox()

browser.get("https://twitter.com/explore")

time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div")

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input") 
password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input")

username.send_keys(os.environ.get('DB_USER_BROWSER'))
password.send_keys(os.environ.get('DB_PASS_BROWSER'))
time.sleep(3)
giris_yap.click()
time.sleep(3)

trend = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
trend.send_keys('csnaber', Keys.ENTER)
time.sleep(4)



##################### Scrolling Script ################################
lenofpage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenofPage=document.body.scrollHeight;return lenofPage;")
match = False
counter = 0
while (match==False):
	lastCount = lenofpage
	time.sleep(5)
	lenofpage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenofPage=document.body.scrollHeight;return lenofPage;")
	counter += 1
	if lastCount == lenofpage or counter == 2:
		match=True


i = 0
while i < 500:
	try:
		liker = browser.find_element_by_css_selector("[data-testid=like]")
		liker.click()
		i += 1
	except:
		pass

browser.close()


"""
for i in range(1, 150):
	for j in range(3, 5):
		try:
			tiktak = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div["+str(i)+"]/div/div/div/article/div/div[2]/div[2]/div[2]/div["+str(j)+"]/div[3]/div")
			tiktak.click()
			time.sleep(0.5)
		except:
			pass













for i in range(1,20):
	try:
		tweets = browser.find_elements_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div["+str(i)+"]/div/div/div/article/div/div[2]/div[2]/div[2]/div[1]/div")	
		for tweet in tweets:
			container.append(tweet.text)
	except:
		pass




with open("C:/Users/Murat/Desktop/Python Çalışmaları/Selenium_Data_Analyses/selenium twitter/tweets.txt", "w+", encoding = "UTF-8") as f:
	for content in container:
		f.write(content + ",")	



SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


    <span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">"Babanın öz kızına şehvet duyması haram değil" açıklaması yapan Diyanet yalnız değilmiş. Ensarcılar, sübyancilar da destekliyormuş.
	<span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">Başka diyecek bir şey yok </span>
</span>
    """
