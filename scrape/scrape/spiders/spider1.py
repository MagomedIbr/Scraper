import scrapy 
# venv\Scripts\activate     
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
        badletters= {}
        textname = '%s.txt' %page
        with open(filename, 'wb') as file:
            file.write(response.body)
        with open(textname, 'w', encoding='utf-8') as f:
            f.write(page)
            plist = []
            for value in response.css('.mw-headline::text').getall():
                f.write(value+'\n') 
            for tex in response.css('p::text').re('Python'):
                plist.append(tex)
                if(tex.strip() != ',' and tex.strip() != '.' ):
                    f.write(tex+'\n')
            f.write(str(len(plist)))
        print(plist + "!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            