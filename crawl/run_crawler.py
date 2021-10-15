import sys
sys.path.append('../surf_scrape/surf_scrape/spiders')
import surf_spider
import scrapy
from scrapy.crawler import CrawlerProcess
import os

from scrapy.utils.project import get_project_settings

class CrawlerRunner():

    def __init__(self, name_website="www.amazon.com"):

        settings_file_path = '..surf_scrape.surf_scrape.settings'
        print(os.environ.setdefault('SCRAPY_SETTTINGS_MODULE', settings_file_path))

        print(dir(scrapy.utils.project))

        settings = get_project_settings()

        process = CrawlerProcess(settings)
        process.crawl(surf_spider.SurfSpider, name_website)
        process.start()

                  

if __name__ == "__main__":
    crawlerRunner = CrawlerRunner('www.amazon.com')
