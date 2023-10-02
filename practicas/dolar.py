import argparse
import requests
from functools import lru_cache
from typing import Any
from bs4 import BeautifulSoup


class Dolar:
    def __init__(self) -> None:
        self.divisas_selector:dict[str, str] = {
            "USD": "#dolar > div > div > div.col-sm-6.col-xs-6.centrado > strong",
            "EUR": "#euro > div > div > div.col-sm-6.col-xs-6.centrado > strong"
        }
        self._response = None
        self._response_html = None
        self._data = None
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument("-t", "--tipo", type=str, choices=["bcv", "paralelo"], default="bcv", required=False)
        self._parser.add_argument("-d", "--divisa", type=str, choices=["USD", "EUR"], default="USD", required=False)
    
    @property
    def response(self) -> requests.Response:
        """Hace la petición al BCV

        Returns:
            requests.Response: Response de la petición GET
        """
        if self._response is not None:
            return self._response
        
        self._response = requests.get("https://www.bcv.org.ve/")
        return self._response
    
    @property
    def html(self) -> bytes:
        """retorna el HTML del response y lo almacena en esta propiedad

        Returns:
            bytes: HTML en bytes
        """
        if self._response_html is not None:
            return self._response_html
        
        self._response_html = self.response.content
        return self._response_html
    
    @lru_cache(None)
    def get_soup(self, html) -> BeautifulSoup:
        soup = BeautifulSoup(html, "lxml")
        return soup
    
    def data(self):
        
        ...
    
    
    def get_divisa(self, divisa:str="USD") -> str:
        assert divisa in self.divisas_selector, ("Las opciones disponibles son: %s" % ", ".join(self.divisas_selector.keys()))
        soup = self.get_soup(self.html)
        
        return soup.css.select_one(self.divisas_selector[divisa]).get_text()
    
    def main(self):
        args = self._parser.parse_args()
        for key, value in args._get_kwargs():
            
            if key == "tipo" and value == "paralelo":
                raise NotImplementedError("No implementado todavía :)")
            
            if key == "divisa":
                print(f"""
                    {value} = {self.get_divisa(value)}
                    """)



a = Dolar()
a.main()