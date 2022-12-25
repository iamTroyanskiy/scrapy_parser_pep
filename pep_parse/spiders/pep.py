import scrapy
from scrapy.linkextractors import LinkExtractor

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_ALLOWED_DOMAINS, PEP_START_URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = PEP_ALLOWED_DOMAINS
    start_urls = PEP_START_URLS

    link_extractor = LinkExtractor(
        allow=r'pep-\d+$',
        restrict_css='#numerical-index'
    )

    def parse(self, response):
        return response.follow_all(
            urls=self.link_extractor.extract_links(response),
            callback=self.parse_pep
        )

    def parse_pep(self, response):
        h1 = response.css('h1.page-title::text').get().split(' – ')
        number = int(h1[0].split()[1])
        name = h1[1]
        status = response.css('abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
