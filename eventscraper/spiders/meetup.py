import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from eventscraper.items import Event

class MeetupSpider(CrawlSpider):
    name = 'meetup'
    allowed_domains = ['meetup.com']
    start_urls = ['https://www.meetup.com/find/events/tech/']

    def parse(self, response):
        event = Event()
        tech_meetups = response.xpath('//div[@class="chunk"]')
        for tech_meetup in tech_meetups:
            event['name'] = tech_meetup.xpath('a/span/text()').extract_first()
            event['group'] = tech_meetup.xpath('div/a/span/text()').extract_first()
            yield event
