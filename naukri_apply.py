from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
from datetime import datetime

def apply_naukri_jobs():
    load_dotenv()
    email = os.getenv("NAUKRI_EMAIL")
    password = os.getenv("NAUKRI_PASSWORD")

    driver = webdriver.Chrome()
    driver.get("https://www.naukri.com/")
    driver.find_element(By.ID, "login_Layer").click()
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(5)

    driver.get("https://www.naukri.com/devops-engineer-jobs?k=devops%20engineer")
    time.sleep(5)

    apply_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Apply')]")
    for btn in apply_buttons[:20]:
        try:
            btn.click()
            time.sleep(2)
            log_job("Naukri", "DevOps Engineer", "Company", driver.current_url)
        except:
            continue

    driver.quit()

def log_job(platform, title, company, link):
    with open("apply_log.csv", "a") as f:
        f.write(f"{platform},{title},{company},{link},{datetime.now().date()}
")
