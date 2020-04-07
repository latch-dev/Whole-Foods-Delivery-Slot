import bs4

from selenium import webdriver

import sys
import time

import winsound
from datetime import datetime

def getWFSlot(productUrl):
   driver = webdriver.Chrome("C:\\Users\\dines\\programs\\chromedriver_win32\\chromedriver.exe")
   driver.get(productUrl)
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)
   print("Will start sleeping at ",  datetime.now().time()," for 120 seconds to give you enough time to get to the schedule order shipping screen")
   time.sleep(120)
   no_open_slots = True

   duration = 20000
   freq = 800

   while no_open_slots:
      driver.refresh()
      print("Looping.  Refreshing at ",  datetime.now().time())
      html = driver.page_source
      soup = bs4.BeautifulSoup(html)
      time.sleep(4)

      slot_pattern = 'Next available'
      try:
         next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
         if slot_pattern in next_slot_text:
            print("Condition 1: FOUND OPEN SLOTS AT ",  datetime.now().time())
            winsound.Beep(freq, duration)
            no_open_slots = False
            time.sleep(14000)
      except AttributeError:
         continue

      try:
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         if no_slot_pattern == soup.find('h4', class_ ='a-alert-heading').text:
            print("No delivery windows available found at ",  datetime.now().time())
      except AttributeError: 
            print("Condition 2: FOUND OPEN SLOTS AT ",  datetime.now().time())
            winsound.Beep(freq, duration)
            time.sleep(14000)
            no_open_slots = False


getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')

