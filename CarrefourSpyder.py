
import requests as r
from lxml import html
import time

def carrefourspider(url):
  base_url = "https://www.carrefoursa.com"
  res = r.get(url)
  dom = html.fromstring(res.content)

  c_price = dom.xpath("// span[@itemprop='price']/text()")

  c_price2 = dom.xpath("// span[@class='priceLineThrough js-variant-price']/text()")

  c_title = dom.xpath("// span[@itemprop='sku']/text()")

  c_image_url = dom.xpath(".//span[contains(@class, 'thumb')]//img[@src and contains(@itemprop, 'image')]/@src")

  c_url = dom.xpath(".//div[contains(@class, 'product_click')]/a/@href")

  c_brand = dom.xpath(".//div[contains(@class, 'product_click')]//input[@value and contains(@id, 'productBrandNamePost')]/@value")

  c_barcode = dom.xpath(".//span[@content and contains(@class, 'item-name')]/@content")

  print(c_price)
  print(c_price2)
  print(c_title)
  print(c_image_url)
  print(c_url)
  print(c_brand)
  print(c_barcode)

  if dom.xpath(".//a[@href and contains(@rel, 'next')]/@href") != []:
   time.sleep(3)
   next_page = dom.xpath(".//a[@href and contains(@rel, 'next')]/@href")[0]
   url = f"{base_url}{next_page}"
   carrefourspider(url)
  else:
    return
#zaaaaaaaaaaaaaaaaaaasdsafsdfasf<saadsadfasfasdfasdasdfasfdsadfsfa
#zaaaaaaaaaaaaaaaaaaasdsafsdfasf<saadsadfasfasdfasdasdfasfdsadfsfa
#zaaaaaaaaaaaaaaaaaaasdsafsdfasf<saadsadfasfasdfasdasdfasfdsadfsfa
#zaaaaaaaaaaaaaaaaaaasdsafsdfasf<saadsadfasfasdfasdasdfasfdsadfsfasadfsfdasfdasf
#zaaaaaaaaaaaaaaaaaaasdsafsdfasf<saadsadfasfasdfasdasdfasfdsadfsfa
#zaaaaaaaaaaaaaaaaaaasdsafsdfasf<saadsadfasfasdfasdasdfasfdsadfsfa
carrefourspider('https://www.carrefoursa.com/bulasik-makinesi-deterjanlari/c/1614')