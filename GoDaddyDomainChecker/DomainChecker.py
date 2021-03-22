from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

def checkDomainAvailability(url=None):
    # Path to the chrome driver
    chrome_driver_path="../../Selenium/chromedriver"

    # Initialize the web driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    isAvailable = "NO"
    price = "0"

    # Scraping code
    with chrome_driver as driver:

        driver.get(url)  # loads the url in headless browser
        driver.implicitly_wait(8) # waits for 8 seconds to load any dynamic html elements
        html = str(driver.page_source)
        # print(driver.page_source)

        pattern = r'.*class="ms7 text-primary-o">MXN([0-9,\.]*)<\/span>.*'
        # result = re.search(pattern, html) # This line is slow because the HTML file has to many chars

        if "exact-match-price-main" in html:
            indexStart = html.index("exact-match-price-main")
            sentence = html[indexStart:indexStart + 100]
            print(f"The sentence is: {sentence}")

            result = re.search(pattern, sentence) # By shortening the html to only a line of text the match is found faster
            if result is not None:
                price = result.groups()[0]

            print("The domain is available, price: ", price)
            isAvailable = "YES"
        else:
            print("Is not available")

        driver.close()
        print("\n\n")

    return isAvailable, price

def main():
    with open("domains.txt") as domains_source:
        with open("report.txt", "w") as report:
            for domain in domains_source:
                domain = domain.rstrip()
                print(domain)
                isAvailable, price = checkDomainAvailability(domain)

                report.write(domain)
                report.write(" ")
                report.write(isAvailable)
                report.write(" ")
                report.write(price)
                report.write("\n")

if __name__ == "__main__":
    main()