# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class GenshinSpiderPipeline:
    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        # Merge all weapons
        weapons = {}
        for type_key in spider.weapon_dic:
            weapons = {**weapons, **spider.weapon_dic[type_key]}

        with open('result/weapons.db', 'w') as fp:
            json.dump(weapons, fp)
        with open('result/word_keys.db', 'w') as fp:
            json.dump(spider.name_dic, fp)
