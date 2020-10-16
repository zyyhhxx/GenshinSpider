import scrapy


class WeaponSpider(scrapy.Spider):
    name = "weapon"

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.weapon_dic = {}
        self.name_dic = {}

    def start_requests(self):
        urls = [
            'https://genshin-impact.fandom.com/wiki/Bows',
            'https://genshin-impact.fandom.com/wiki/Catalysts',
            'https://genshin-impact.fandom.com/wiki/Claymores',
            'https://genshin-impact.fandom.com/wiki/Polearms',
            'https://genshin-impact.fandom.com/wiki/Swords',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.xpath(
            '//*[@class="wikitable sortable" and @style="width: 99%;"]//tr')

        type_name = response.css('title::text').get().split(" | ")[
            0][:-1].lower()
        weapon_dic = {}
        for row in rows[1:]:
            name = row.xpath('td[1]//text()').extract_first()
            name_key = name.lower().replace(" ", "_")
            rarity = int(row.xpath('td[3]//text()').extract_first())
            weapon_dic[name_key] = {
                'ascension_material': '',
                'rarity': rarity,
                'type': type_name,
            }
            self.name_dic[name_key] = {"zh_s": "", "en": name}

        self.weapon_dic[type_name] = weapon_dic
