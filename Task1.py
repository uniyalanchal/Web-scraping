import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("Flipkart")
inputElement.submit()
elem = driver.find_element_by_partial_link_text("Flipkart")
elem.click()
print("element found")

elem1 = driver.find_element_by_name("q")
elem1.send_keys("Realme Phones")
elem1.submit()

# finding  phonenames and prices of phones by class names
phonenames=driver.find_element_by_class("_4rR01T").click()
prices=driver.find_element_by_class("_30jeq3 ").click()

# creating two list for storing phonenames and phone prices 
myphone=[]
myprice=[]

for phone in phonenames:
	print(phone.text)
	myphone.append(phone.text)


for price in prices:
    print(price.text)	
    myprice.append(price.text)
    
    #zipping both lists 
finallist=zip(myphone,myprice)

for data in list(finallist):
	print(data)



