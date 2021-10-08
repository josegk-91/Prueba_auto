
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

class TestConsultorMadrid():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_consultorMadrid(self):
    self.driver.get("https://www.alten.es/")
    self.driver.set_window_size(1536, 824)
    self.driver.find_element(By.CSS_SELECTOR, "#menu-item-33 > a").click()
    time.sleep(2)
    WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(
      (By.ID, "tarteaucitronAlertBig")))  # Espera hasta que aparecen las Cookies
    self.driver.find_element(By.XPATH, "/html/body/div[8]/div[3]/button[1]").click()  # Aceptar cookies
    self.driver.find_element(By.CSS_SELECTOR,".filter-profile > div:nth-child(1) > a:nth-child(2)").click()
    time.sleep(1)
    self.driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/form/div[2]/div/div/a[4]").click()
    self.driver.save_screenshot("screenPerfilTecnico")
    self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/form/div[3]/div/a").click()
    self.driver.find_element(By.CSS_SELECTOR, ".opened a:nth-child(3)").click()
    self.driver.save_screenshot("screenMadrid")
    assert self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/form/div[3]/div/a")#Confirma que se utiliza como filtro MADRID
    self.driver.close()
  
