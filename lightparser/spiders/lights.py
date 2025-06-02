import scrapy

class LightsSpider(scrapy.Spider):
    name = "lights"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        products = response.css("div.catalog-product")
        for product in products:
            yield {
                "title": product.css("span[itemprop='name']::text").get(),
                "price": product.css("meta[itemprop='price']::attr(content)").get(),
                "url": response.urljoin(product.css("a.catalog-product__name::attr(href)").get())
            }

        next_page = response.css("a.pagination-widget__page-link_next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
