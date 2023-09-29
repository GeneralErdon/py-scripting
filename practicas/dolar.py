import argparse
from typing import Any
import requests
import scrapy as sc
from scrapy.http import Response, Request

class Spider(sc.Spider):
    name = "dolar_spider"
    start_urls = ["https://www.bcv.org.ve/"]
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        div_numero = response.css("#dolar > div > div > div.col-sm-6.col-xs-6.centrado > strong").get()
        
        print(div_numero)
        
        return super().parse(response, **kwargs)


class Dolar:
    def __init__(self) -> None:
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument("-t", "--tipo", type=str, choices=["bcv", "paralelo"], default="bcv", required=False)
    
    def main(self):
        
        print(self._parser.parse_args())
        
        spider = Spider()
        
        response = Request("https://www.bcv.org.ve/",).callback()
        
        spider.parse(response=response)


a = Dolar()
a.main()