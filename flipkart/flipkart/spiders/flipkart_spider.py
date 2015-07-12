from scrapy.spiders import Spider
from scrapy.selector import Selector
#import scrapy

from flipkart.items import FlipkartItem

class FlipkartSpider(Spider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    orig="http://www.flipkart.com/mobiles/pr?sid=tyy,4io&start=";
    start_urls=[]
    for j in range(1,1500,20):
        x=orig+str(j)
        start_urls.append(x)
        #print j
    '''start_urls=['http://www.flipkart.com/mobiles/pr?sid=tyy,4io&start=141', 'http://www.flipkart.com/mobiles/pr?sid=tyy,4io&start=1441']'''
            

    
 ############################### parse function   ###############################################################   
    def parse(self, response):
        sel = Selector(response)
        sites=sel.xpath('//div[@class="product-unit unit-4 browse-product new-design "]')
        #sites_price=sel.xpath('//div[@clas="pu-final"]/span[@class="fk-font-17 fk-bold"]')
        #sites_price=sel.xpath('//span[@class="fk-font-17 fk-bold"]')
        #sites_details=sel.xpath('//ul[@class="pu-usp"]')
        #sites_link=sel.xpath('//a[@data-tracking-id="prd_img"]')
        items = []
        for site in sites:
            item=FlipkartItem()
            initial="https://flipkart.com"
            item['link']=initial+''.join(site.xpath('./div[1]/a[1]/@href').extract())
            item['i_link']=site.xpath('./div[1]/a[1]/img[@src]').extract()
            item['details']=site.xpath('div[2]/div[5]/ul/li/span/text()').extract()
            item['price']=site.xpath('div[2]/div[4]/div[1]/div[1]/span/text()').extract()
            item['name']=site.xpath('div[2]/div[1]/a/text()').extract()
           	#initial="https://flipkart.com"
            #item['link']=initial+''.join(sites_link[i].xpath('@href').extract())
            #item['i_link']=sites_link[i].xpath('img/@data-src').extract()
            #items.append(item)
            #item_l['link']=initial+''.join(site_l.xpath('@href').extract()) # ''.join(list) convert list to string
            #item_l['i_link']=site_l.xpath('img/@data-src').extract()
            #item_l['link']=initial+item_l['link']
            items.append(item)
    
        return items
