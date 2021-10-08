
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBusquedaPalabraClav():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_busquedaPalabraClav(self):
    self.driver.get("https://www.alten.es/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-33 > a").click()
    self.driver.execute_script("window.scrollTo(0,2467.199951171875)")
    WebDriverWait(self.driver,6).until(expected_conditions.presence_of_element_located((By.ID, "tarteaucitronAlertBig")))# Espera hasta que aparecen las Cookies
    self.driver.find_element(By.XPATH, "/html/body/div[8]/div[3]/button[1]").click() #Aceptar cookies
    time.sleep(3)
    self.driver.find_element(By.NAME, "text").click()
    self.driver.find_element(By.NAME, "text").send_keys("tester")
    self.driver.find_element(By.NAME, "text").send_keys(Keys.ENTER)
    self.driver.save_screenshot("screenPalabraclave")
    time.sleep(2)
    assert self.driver.find_element(By.CSS_SELECTOR, ".fadein:nth-child(1) > .job-title").text == "QA Tester"#Confirma que en los resultado se encuentra  QAtester
    self.driver.close()
  
