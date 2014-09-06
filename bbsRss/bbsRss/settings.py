# -*- coding: utf-8 -*-

# Scrapy settings for bbsRss project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbsRss'

SPIDER_MODULES = ['bbsRss.spiders']
NEWSPIDER_MODULE = 'bbsRss.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'QSCTech (+http://tech.myqsc.com/)'
