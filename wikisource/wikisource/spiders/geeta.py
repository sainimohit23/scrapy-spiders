# -*- coding: utf-8 -*-
import scrapy


class GeetaSpider(scrapy.Spider):
    name = 'geeta'
    allowed_domains = ['wikisource.org']
    
    def start_requests(self):
    	url = "https://wikisource.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%B9%E0%A4%B0%E0%A4%BF%E0%A4%97%E0%A5%80%E0%A4%A4%E0%A4%BE"
    	yield scrapy.Request(url=url, callback=self.parseChapters)


    def parseChapters(self, response):
    	for chapter in response.xpath("//div[@class='mw-parser-output']/ul/li"):
    		link = chapter.xpath(".//a/@href").extract_first()
    		next_page = response.urljoin(link)
    		yield scrapy.Request(url=next_page, callback=self.parse)
    		# yield {'link': next_page}


    def parse(self, response):
        data = response.xpath("//div[@class='verse']/pre/text()").extract_first()
        title = response.xpath("//h1[@id='firstHeading']/text()").extract_first()

        if data != None:
	        yield{'title': title,
	        		'data': data}



