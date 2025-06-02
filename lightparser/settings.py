BOT_NAME = "lightparser"

SPIDER_MODULES = ["lightparser.spiders"]
NEWSPIDER_MODULE = "lightparser.spiders"

ROBOTSTXT_OBEY = True

FEEDS = {
    "lights.json": {
        "format": "json",
        "encoding": "utf8",
        "overwrite": True
    }
}
