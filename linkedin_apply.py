from dotenv import load_dotenv
import os
from playwright.sync_api import sync_playwright
from datetime import datetime

def apply_linkedin_jobs():
    load_dotenv()
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.linkedin.com/login")

        page.fill('input[name="session_key"]', email)
        page.fill('input[name="session_password"]', password)
        page.click('button[type="submit"]')

        page.goto("https://www.linkedin.com/jobs/search/?keywords=DevOps%20Engineer&location=India&f_AL=true")
        page.wait_for_timeout(5000)

        jobs = page.locator(".jobs-apply-button").all()
        for job in jobs[:20]:
            try:
                job.click()
                page.wait_for_timeout(2000)
                if page.locator('button:has-text("Submit application")').is_visible():
                    page.click('button:has-text("Submit application")')
                    log_job("LinkedIn", "DevOps Engineer", "Company", page.url)
            except:
                continue

        browser.close()

def log_job(platform, title, company, link):
    with open("apply_log.csv", "a") as f:
        f.write(f"{platform},{title},{company},{link},{datetime.now().date()}
")
