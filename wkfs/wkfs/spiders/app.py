import scrapy
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

domain = "https://www.hkma.gov.hk/"
class tut1(scrapy.Spider):
    name = "hkma"
    start_urls = ["https://www.hkma.gov.hk/eng/regulatory-resources/regulatory-guides/circulars/"]

    def parse(self,response):
        driver = webdriver.Chrome('E:\Desktop\hkma\hkma\wkfs\chromedriver.exe')
        driver.get('https://www.hkma.gov.hk/eng/regulatory-resources/regulatory-guides/circulars/')
        driver.find_element_by_xpath('//div[@tabindex="1"]').click()
        for i in range(0,3):
            driver.find_element_by_xpath('//a[@id="btn-circular-more"]').click()
            sleep(2)
        sleep(5)
        page = Selector(text=driver.page_source)
        heading = page.xpath('//div[@class="index-text"]/a/text()').extract()
        date = page.xpath('//tr/td[2]/text()').extract()
        doc_url = page.xpath('//div[@class="index-text"]/a/@href').extract()
        for a,b,c in zip(heading,date,doc_url):
            yield{
                'doc_name': a,
                'date':b,
                'url':c,
            }






