import json
import yaml

import scrapy
from bs4 import BeautifulSoup

def yaml_export(path, data):
    with open(path, 'w') as f:
        f.write('---\n')
        yaml.dump(data, f)
        if 'prg_idx' in data:
            f.write('layout: progression\n')
        else:
            f.write('layout: movement\n')
        f.write('---\n')

class HybridCalisthenicsSpider(scrapy.Spider):
    name = "hybrid_calisthenics"
    allowed_domains = ["www.hybridcalisthenics.com"]
    base_url = "https://www.hybridcalisthenics.com"
    start_urls = ["https://www.hybridcalisthenics.com/index"]

    @classmethod
    def update_settings(cls, settings):
        super().update_settings(settings)
        settings.set("HTTPCACHE_ENABLED", "true", priority="spider")
        """settings.set("FEEDS", json.dumps({
            './data.json': {'format': 'json', 'overwrite': True},
            './data.jsonl': {'format': 'jsonl', 'overwrite': True},
        }), priority="spider")"""

    def parse(self, response):
        for mvt in response.css('p'):
            mvt_n = mvt.css('strong::text').get()
            if mvt_n is None:
                continue
            prg = mvt.css('a::attr(href)').getall()
            yield scrapy.Request(self.base_url + prg[0], callback=self.parse_movement)

    def parse_movement(self, response):
        content = response.css('.content')[0]
        mvt = {}
        mvt['mvt_idx'] = response.url.split('/')[-1]
        mvt['name'] = content.xpath('.//h1/text()').get() or content.xpath('.//h2/text()').get()
        mvt['name'] = mvt['name'].replace(' Progression', '')
        mvt['url'] = response.url
        mvt['desc'] = content.xpath('.//p/text()').get()
        mvt['video'] = content.xpath('.//a/@href').get()
        mvt['background'] = response.css('.section-background img::attr(src)').get()
        
        yaml_export(f'_movement/{mvt["mvt_idx"]}.md', mvt)
        yield mvt

        for i, prog in enumerate(response.css('figure')):
            item = {}
            item['mvt_idx'] = response.url.split('/')[-1]
            item['prg_pos'] = i + 1
            prog_url = prog.css('a::attr(href)').get()
            item['prg_idx'] = prog_url[1:]
            # item['name'] = (prog.css('h3::text').get() or prog.css('h2::text').get()).split('-', 1)[-1].strip()
            item['short_desc'] = prog.css('p::text').getall()[:-1]
            item['url'] = self.base_url + prog_url
            item['thumbnail'] = prog.css('img::attr(src)').get()
            # mvt['progression'][item['url'][1:]] = scrapy.Request(self.base_url + item['url'], self.parse_progression, cb_kwargs={'item': item})
            yield scrapy.Request(item['url'], callback=self.parse_progression, cb_kwargs={'item': item})

    def parse_progression(self, response, item):
        self.logger.info(self.base_url + item['url'])
        item['name'] = (response.css('h2::text').get() or response.css('h3::text').get())
        content = response.css('div .sqs-html-content')
        item['desc'] = [BeautifulSoup(e).get_text() for e in content[2].css('p').getall()]
        item['level'] = [e.strip() for e in content[3].css('h4::text').getall()]
        item['form'] = [BeautifulSoup(e).get_text() for e in content[4].css('p').getall()]
        item['tutorial'] = [BeautifulSoup(e).get_text() for e in content[5].css('p').getall()]
        item['prog_reg'] = [BeautifulSoup(e).get_text() for e in content[6].css('p').getall()[:-1]]
        item['video'] = content[1].css('a::attr(href)').get()

        yaml_export(f'_progression/{item["prg_idx"]}.md', item)
        return item

