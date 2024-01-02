#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:36:08 2021

@author: kianaamaral
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import xlsxwriter
import unicodedata


search = 'Japan'


GARDdisease = []
for i in range(6): 
    url = 'https://rarediseases.info.nih.gov/search?keyword=' + search + '&page=' + str(i) + '&filters=contentType%3Ddisease%3Blanguage%3Denglish'
    
    # go to https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent for User-Agent if you use a different browser 
    req = Request(url, headers={'User-Agent': 'Chrome/51.0.2704.103'})
    webpage = urlopen(req).read() 
    
    page_soup = BeautifulSoup(webpage, 'html.parser')
    diseases = page_soup.findAll('div', 'col-lg-9 col-md-9 col-sm-12 col-xs-12 body-search-result') # tag = 'h4' class = 'rdr-one-title' 
    
    for disease in diseases: 
        diseasestring = str(disease.text)
        
    
    for i in range(len(diseasestring)):
        if diseasestring[i] == '\n':
            start = i + 1
        elif diseasestring[i:i+9] == '(Disease)':
            d = i-1
            
            clean = diseasestring[start:d]
            GARDdisease.append(clean)
    
    print(GARDdisease)
    print(len(GARDdisease))