# -*- coding: utf-8 -*-

# Scrapy settings for maoyan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyan'

SPIDER_MODULES = ['maoyan.spiders']
NEWSPIDER_MODULE = 'maoyan.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'

from fake_useragent import UserAgent
import random
USER_AGENT = UserAgent(verify_ssl=False).random

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Cookie':'uuid_n_v=v1; uuid=63030590B82311EA974289B279A7041DC0A3AE716C6F48FD81BAC6913B0ECA54; mojo-uuid=3c2d7b5f04e7657f93bd709c02e7163d; _lxsdk_cuid=172f3beebe7c8-0d8552c9ed5257-4353760-100200-172f3beebe7c8; _lxsdk=63030590B82311EA974289B279A7041DC0A3AE716C6F48FD81BAC6913B0ECA54; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=73c7282091a649765f6b591c9f87f202ddaf48c18aed8deaf4dcbba8d9f50fb4; mojo-session-id={"id":"923b96aca7bd40de0df893461b378576","time":1593911216720}; lt=cIZXK9lADb0J9uoestvn4INw6sYAAAAAAwsAANiHHXemCo8XRyX9xCUcxgCx5yRWcdJuru2i2vnwmPnCwrXHFhuap9CZTyABCTdE1g; lt.sig=PDNmVyy-SaXk9P9RYxEF180lDDQ; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593310287,1593323746,1593774741,1593912729; __mta=188462999.1593227276279.1593911229910.1593912729809.50; mojo-trace-id=9; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593912741; _lxsdk_s=1731c830ac3-208-1b1-391%7C%7C12',
  'Referer':'https://passport.meituan.com/account/unitivelogin?service=maoyan&continue=https%3A%2F%2Fmaoyan.com%2Fpassport%2Flogin%3Fredirect%3D%252F',
  'Host':'maoyan.com'
  }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyan.middlewares.MaoyanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'maoyan.middlewares.MaoyanDownloaderMiddleware': 543,
   'maoyan.middlewares.RandomHttpProxyMiddleware': 400,
}

HTTP_PROXY_LIST = [
     'http://52.179.231.206:80',
     'http://95.0.194.241:9090',
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'maoyan.pipelines.MaoyanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
