#导入CrawlProcess类，此类可以让计算机在程序中启动爬虫
from scrapy.crawler import CrawlerProcess
#导入获取项目设置信息
from scrapy.utils.project import get_project_settings

#程序入口
if __name__ == '__main__':
    #创建CrawlerProcess类对象并传入项目设置信息参数
    process = CrawlerProcess(get_project_settings())
    #设置需要启动的爬虫名称
    process.crawl('quotes')
    #启动爬虫
    process.start()