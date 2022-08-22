import scrapy 

class Postsspider(scrapy.Spider):
    name = "posts"
    page = 0
    start_urls = [
    'https://de.wikipedia.org/wiki/Python_(Programmiersprache)'
    ]
    def parse(self, response):
        page = response.url.partition('wiki/')[-1]
        text = response.css('.mw-headline::text').getall()
        filename = 'posts-%s.html' %page
        textname = '%s.txt' %page
        with open(filename, 'wb') as file:
            file.write(response.body)
        with open(textname,'w') as f:
            f.write(type(text))
        return text
        