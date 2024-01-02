#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:55:57 2021

@author: kianaamaral
"""
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from GroupLists import * 
import xlsxwriter
import unicodedata

def getDiseases(search):
    ''' Input search string; returns a list of all diseases '''
    AllDiseases = []
    url = 'https://rarediseases.org/?s=' + search + '&submit='
    # go to https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent for User-Agent if you use a different browser 
    req = Request(url, headers={'User-Agent': 'Chrome/51.0.2704.103'})
    webpage = urlopen(req).read() 
    
    page_soup = BeautifulSoup(webpage, 'html.parser')
    diseases = page_soup.findAll('h4', 'rdr-one-title') # tag = 'h4' class = 'rdr-one-title' 
    for disease in diseases: 
        AllDiseases.append(disease.text)
        
    print('done Diseases')
    return AllDiseases
    

def getdiseaseURL(AllDiseases, search):
    ''' input list of diseases and search string; returns list of diseases' URL'''
    AllURL = [] 
    url = 'https://rarediseases.org/?s=' + search + '&submit='
    # go to https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent for User-Agent if you use a different browser 
    req = Request(url, headers={'User-Agent': 'Chrome/51.0.2704.103'})
    webpage = urlopen(req).read() 
    
    page_soup = BeautifulSoup(webpage, 'html.parser')
    URLs = page_soup.findAll('a', 'search-result-block-anchor') # tag = 'h4' class = 'rdr-one-title' 
    for u in URLs:
        string = str(u)
        for s in range(len(string)): 
            if string[s:s+4] == 'href':
                start = s+6 
            elif string[s] == '>':
                end = s-1
                break
        finalURL = string[start:end]        
        AllURL.append(finalURL)
        
    return AllURL



def getPopulation(AllDiseases,search):
    ''' Input list of diseases and search string; returns list of affected populations paragraph '''
    AllURL = getdiseaseURL(AllDiseases, search)
    AllPopulations = []
    for i in range(len(AllURL)): 
        url = AllURL[i]
        
        req = Request(url, headers={'User-Agent': 'Chrome/51.0.2704.103'})
        diseasepage = urlopen(req).read() 
        disease_soup = BeautifulSoup(diseasepage, 'html.parser')
    
        population = disease_soup.find('div', 'wpcf-field-wysiwyg wpcf-field-rd_affected_populations')
        try:
            try:
                AllPopulations.append(population.text)
            except AttributeError:
                population = disease_soup.find('div', 'rdr-box', id = 'gard-overview')
                AllPopulations.append(population.text)
                
        except AttributeError:
                AllPopulations.append('delete') 
                           
    print('done Population')
     
    return AllPopulations 

     
    
    
def getCategory(AllPopulations):
    '''input lost of affected populations info; returns categories 
       NOT COMPLETELY ACCURATE''' 
    AllCategories = []
    sort_key = ['Asian', 'African', 'Hispanic', 'Indigenous'] 
    for pop in AllPopulations:
        category = []
        pop = pop.split()
        Asian = True; African = True; Hispanic = True; Indigenous = True  
        
        for word in pop:
            if Asian and word in AsianGroups: 
                category.append(0)
                Asian = False 
                
            elif African and word in AfricanGroups: 
                category.append(1)
                African = False
                
            elif Hispanic and word in HispanicGroups: 
                category.append(2)
                Hispanic = False
                
            elif Indigenous and word in IndigenousGroups: 
                category.append(3)
                Indigenous = False
                
        print('category before if/else', category)        
        if len(category) == 0:
            c = ''
            
        elif len(category) == 1: 
            c = sort_key[category[0]]
            
        else:
            c = ''
            category.sort()
            print('sorted', category)
            for i in range(len(category)):
                category[i] = sort_key[category[i]]
            print(category)
            for k in range(len(category)):
                c += category[k] + '/'
                
        AllCategories.append(c)
            
    return AllCategories
    print(AllCategories)        
def comparelists(lists):
    '''checks for duplicates between NORD and GARD; deletes items in all lists (When necessary)
    also removes articles'''
             
def ExportExcel(AllDiseases, AllPopulations, AllURL, AllCategories, search, name):
    Columns = ['Disease',	'URL', 'Geo. or Racial/Ethnic Disporportionate Pop', 	'Category',	'Accept Haoming', 'Accept Daphne', 'Accept Kiana',	'Additional Data',	'Duplicates',	'List',	'Search']
    
    workbook = xlsxwriter.Workbook(name + '.xlsx')
    worksheet = workbook.add_worksheet()
    
    highlight = workbook.add_format({'bg_color': 'yellow'})
    bold = workbook.add_format({'bold': True, 'bg_color': 'grey'})
    
    worksheet.write(0,0, 'Keyword Search in NORD', bold)
    worksheet.write(0,1, str(len(AllDiseases)) + ' Results', bold)
    worksheet.write(2,0, 'Search String: ' + "'" + search + "'", highlight)
    worksheet.write(3,0, len(AllDiseases)) 
    worksheet.write(2,4, 'Includes Duplicates')
    worksheet.write(2,6, 'NORD List', bold)
    worksheet.write(3,(len(Columns))-1, "From", bold)
    
    for i in range(len(Columns)): 
        worksheet.write(4,i, Columns[i], bold)
    
    
    for d in range(len(AllDiseases)): 
        worksheet.write(5+d, 0, AllDiseases[d])
        worksheet.write(5+d, 1, AllURL[d])
        worksheet.write(5+d, 2, AllPopulations[d])
        worksheet.write(5+d, 3, AllCategories[d])
    
    workbook.close()
    




### Run code here ###    
     
search = 'India'     
name = 'NORD 12 ' + "'" + search + "'" + ' webscrape' 


AllDiseases = getDiseases(search)
AllURL = getdiseaseURL(AllDiseases, search)
AllPopulations = getPopulation(AllDiseases,search)

AllCategories = getCategory(AllPopulations)
print('done Categories')

print('Running Excel')
ExportExcel(AllDiseases, AllPopulations, AllURL, AllCategories, search, name)
print('done')

