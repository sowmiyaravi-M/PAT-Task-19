from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramProfileScraper:
    def __init__(self, profile_url):
        self.profile_url = profile_url
        self.driver = webdriver.Chrome()  

    def scrape_followers_following(self):
        self.driver.get(self.profile_url)
        try:
            # Wait until the followers count is visible
            followers_count = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "/followers/")]/span'))
            ).get_attribute('title')

            # Wait until the following count is visible
            following_count = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "/following/")]/span'))
            ).get_attribute('title')

            print(f"Followers: {followers_count}")
            print(f"Following: {following_count}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    profile_url = "https://www.instagram.com/guviofficial/"
    scraper = InstagramProfileScraper(profile_url)
    scraper.scrape_followers_following()


