import scrapy
import csv
import os

domain = "https://www.hkma.gov.hk/"
class tut1(scrapy.Spider):
    name = "hkma"
    start_urls = ["https://www.hkma.gov.hk/eng/regulatory-resources/regulatory-guides/circulars/"]

    def parse(self, response, **kwargs):
        try:
            # links = response.xpath("//div[@class='index-text']/a[(contains(@href, '.pdf'))]").getall()
            links = response.xpath("//div[@class='index-text']/a/@href").getall()
            texts = response.xpath("//div[@class='index-text']/a[@href]/text()").getall()
            date = response.xpath("//tbody[@id='circular-result']//td[2]/text()").getall()
            print("*********",type(links))
            with open(R'C:\Users\akash\OneDrive\Desktop\scrapy_tut\new_file.csv', 'w',newline='', encoding='utf-8') as myfile:
                spamwriter = csv.writer(myfile, delimiter=',', quotechar=',')
                spamwriter.writerow(['DOC_name', 'DOC_URL', 'Date'])

                for (text,link,date_1) in zip(texts,links,date):
                    print(text,link)
                    spamwriter.writerow([domain + link,text,date_1])
                myfile.close()
        except Exception as e:
            print("****** {a}".format(a=e))




