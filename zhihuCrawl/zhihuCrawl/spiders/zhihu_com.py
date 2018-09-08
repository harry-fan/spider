# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from zhihuCrawl.items import ZhihucrawlItem


class ZhihuComSpider(CrawlSpider):
    name = 'zhihu.com'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = ZhihucrawlItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def start_requests(self):
        return [Request('https://www.zhihu.com/# signin',
                callback=self.start_login,
                meta = {'cookiejar':1}
            )]

    def start_login(self, response):
        # 开始登陆
        self.xsrf = Selector(response).xpath(
                '// input[@name="_xsrf"]/@value'
                ).extract_first()
        return [FormRequest(
                'https://www.zhihu.com/login/phone_num',
                method = 'POST',
                meta = {'cookiejar':response.mmeta['cookiejar']},
                formdata = {
                        '_xsrf':self.xsrf,
                        'phone_num':'xxxxxx',
                        'password':'xxxxxx',
                        'captcha_type':'cn'
                    },
                callback = self.after_login
            )]

    def after_login(self, response):
        if json.loads(response.body)['msg'].encode('utf-8') == '登陆成功':
            self.logger.info(str(response.meta['cookiejar']))
            return [Request(
                    self.start_urls[0],
                    meta = {'cookiejar':response.meta['cookiejar']},
                    callback = self.parse_user_info,
                    errback = self.parse_err,
                )]
        else:
            self.logger.error('登陆失败')
            return

class parse_user_info(self, response):
    user_id = os.path.split(response.url)[-1]
    user_image_url = response.xpath("//img[@class='AvatarAvatar--l']/@src").extract_first()
    name = response.xpath("//*[@class='title-section']/span/text()").extract_first()
    location = response.xpath("//*[@class='location item']/@title").extract_first()
    business = response.xpath("//*[@class='business item']/@title").extract_first()
    gender = response.xpath("//*[@class='item gender']/i/@class").extract_first()
    if gender and u"female" in gender:
        gender = u"female"
    else:
        gender = u"male"
    employment = response.xpath("//*[@class='employment item']/@title").extract_first()
    position = response.xpath("//*[@class='position item']/@title").extract_first()
    education = response.xpath("//*[@class='education item']/@title").extract_first()
