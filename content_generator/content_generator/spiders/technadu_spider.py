import scrapy

class QuotesSpider(scrapy.Spider):
    name = "technadu"

    def start_requests(self):
        urls = [
            'https://www.technadu.com/news/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        nodes = response.css('.item-details > .entry-title > a')
        for node in nodes:
            full_url = node.attrib['href']
            title = node.attrib['title']
            page_id = full_url.split('/')[-2]
            # TODO now I have to save-it
            