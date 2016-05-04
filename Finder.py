#!/usr/bin/env python
#encoding: utf-8
import datetime
import json
import os
import random
import sys
import time
import winsound

import Beep
from bs4 import BeautifulSoup
import pyperclip
import requests

def getvalutess():
    """ A 'valute' fájlból beolvassok az aktuális árfolyamokat. """
    infile = open('valute', 'r').read()
    data = json.loads(infile)
    return data

def importLinks(fileName):
#def importLinks():
    """ Beimportáljuk a linkeket amiket vizsgálni akarunk a 'links' mappából. A fájlnevet argumentumként adjuk meg a hívásnál. """
    try:
        f = open('links\\' + fileName, 'r')
        #f = open('links\\links', 'r')
        data = [i.split(';')[1].strip() for i in f.readlines()]
        return data
    except IOError:
        print 'Does not exist: {0}'.format(fileName)
        sys.exit(1)

def waiting(f, t):
    """ 'f' és 't' közti időt várunk. """
    time.sleep(round(random.uniform(f,t),2))

def readable(url):
    """ Olvasható formájúvá alakítja a linket. """
    tmp_list = url.split('/')
    name = tmp_list[-1]
    return name.replace('%E2%98%85','KNIFE ; ').replace('%E2%84%A2%20', ' ; ').replace(
                        '%20%7C%20',' ; ').replace('%20%28', ' ; ').replace('%20', ' ').replace('%29', '')

def readURL(URL):
    """ A paraméterül kapott URL-t lementjük. (addig próbálkozunk míg el nem érjük a weblapot)
        Ha túl gyorsan próbálkozunk és letilt a STEAM akkor várunk 30 sec-et és 'WAIT' üzenetet adunk vissza.
        Ha nincs árajánlat ehhez a skin-hez akkor 'WRONG' üzenetet adunk vissza.
        Ha elérhető a skin steam market oldala akkor kiszedjük az URL-ből a 'span' tag-eket és a pénznemek ID-ját a 'getCurrencyID' függvénnyel,
        majd visszaadjuk a függvény értékeként párban.
    """
    while(1):
        try:
            r = requests.get(URL)
            l = BeautifulSoup(r.content, 'html.parser')
            break
        except:
            print 'Connection l\'oszt'
            time.sleep(30)

    if l.text.encode('utf-8').find('Please wait and try your request again later.') != -1:
        for i in xrange(11):
            print 'Waiting {0}s'.format(i*5)
            time.sleep(5)
        return ('WAIT','WRONG')
    elif l.text.encode('utf-8').find('There are no listings for this item') != -1:
        return ('WRONG','WRONG')
    data = l.findAll('span')
    try:
        curIDs = getCurrencyID(l)
    except:
        loging('', str(URL) + '\n', str(r)+50*'*')
        print '--- NOT CURRENCY ID\'s ---'
        return ('WRONG', 'WRONG')

    return (data,curIDs)

def valutesToUsd(tmp, curID):
    """ Megkapjuk a skin árát string formátumban (tmp) és a pénznem azonosítóját (curID).
        Az azonosító alapján átalakítjuk a 'tmp' string-et olyanná, hogy float típusúvá tudjuk konvertálni.
        A konvertált alakkal tér vissza a függvény.
    """
    #print str(tmp) + ' ' + str(curID)
    if tmp.find('Sold') != -1:
        return 5014.0
    if curID == '2001':
        return (float(tmp.replace('$','').replace('USD',''))/valutes['USD'])
    if curID == '2002':
        return (float(tmp.replace('£',''))/valutes['GBP'])
    if curID == '2003':
        return (float(tmp.replace('€','').replace(',','.'))/valutes['EUR'])
    if curID == '2004':
        return (float(tmp.replace('CHF ',''))/valutes['CHF'])
    if curID == '2005':
        return (float(tmp.split(' ')[0].replace(',','.'))/valutes['RUB'])
    if curID == '2006':
        print curID
        sys.exit()
    if curID == '2007':
        return (float(tmp.split(' ')[1].replace(',',''))/valutes['BRL']/100)
    if curID == '2008':
        return (float(tmp.split(' ')[1].replace(',','').replace('¥',''))/valutes['JPY'])
    if curID == '2009':
        return (float(tmp.replace(' kr','').replace('.','').replace(',','.'))/valutes['SEK'])
    if curID == '2010':
        return (float(tmp.replace('Rp ','').replace(' ',''))/valutes['IDR'])
    if curID == '2011':
        return (float(tmp.replace('RM','').replace(',',''))/valutes['MYR'])
    if curID == '2012':
        return (float(tmp.replace('P','').replace(',',''))/valutes['PHP'])
    if curID == '2013':
        return (float(tmp.replace('S$',''))/valutes['SGD'])
    if curID == '2014':
        return (float(tmp.replace('฿','').replace(',',''))/valutes['THB'])
    if curID == '2015':
        print curID
        sys.exit()
    if curID == '2016':
        return (float(tmp.replace('₩ ', '').replace(',',''))/valutes['KRW'])
    if curID == '2017':
        return (float(tmp.split(' ')[0].replace(',','.'))/valutes['TRY'])
    if curID == '2018':
        print curID
        sys.exit()
    if curID == '2019':
        return (float(tmp.replace('Mex$ ','').replace(',',''))/valutes['MXN'])
    if curID == '2020':
        return (float(tmp.split(' ')[1].replace(',','.'))/valutes['CAD'])
    if curID == '2021':
        print curID
        sys.exit()
    if curID == '2022':
        return (float(tmp.replace('NZ$ ',''))/valutes['NZD'])
    if curID == '2023':
        return (float(tmp.split(' ')[1].replace(',',''))/valutes['CNY'])
    if curID == '2024':
        return (float(tmp.replace('₹ ','').replace(',',''))/valutes['INR'])
    if curID == '2025':
        return (float(tmp.replace('CLP$', '').replace('.','').replace(',','.'))/valutes['CLP'])
    if curID == '2026':
        return (float(tmp.replace('S/.',''))/valutes['SGD'])
    if curID == '2027':
        return (float(tmp.replace('COL$ ','').replace('.','').replace(',','.'))/valutes['COP'])
    if curID == '2028':
        return (float(tmp.replace('R ','').replace(' ',''))/valutes['ZAR'])
    if curID == '2029':
        return (float(tmp.replace('HK$ ','').replace(',',''))/valutes['HKD'])
    if curID == '2030':
        return (float(tmp.replace('NT$ ','').replace(',',''))/valutes['TWD'])
    if curID == '2031':
        return (float(tmp.replace(' SR', ''))/valutes['SAR'])
    if curID == '2032':
        return (float(tmp.replace(' AED', ''))/valutes['AED'])
    """if curID == '2033':
    if curID == '2034':
    if curID == '2035':
    if curID == '2036':
    if curID == '2037':
    if curID == '2038':
    if curID == '2039':
    if curID == '2040':

    return (float(tmp.split(' ')[0].replace(',','.'))/valutes['RUB'])
    return (float(tmp.replace('฿','').replace(',',''))/valutes['THB'])  
    return (float(tmp.replace('NZ$ ',''))/valutes['NZD'])
    return (float(tmp.replace(' DH', ''))/valutes['AED'])
    """
    print 25*'-'
    print 'SomethingElse:', tmp, curID
    Beep.makeSound('Knife')
    sys.exit()
    
def getPrices(li):
    """ Minden második elemet kiszedünk a listából és rendezve visszaadjuk. """
    #JELENLEG MÁSHOGY ÜZEMEL
    #pli = li[::2]
    pli = li
    pli.sort()
    return pli

def checkValue(li, cat, valutes):
    """ Megkapjuk az árak listáját és a skin kategóriájának nevét, és eldöntjük megéri-e megvenni.
        Ha megéri 'True'-val, ha nem éri meg 'False'-al térünk vissza.
    """
    if len(li) < 2:
        return False

    if (cat == 'normal') and (1.23*li[0]*valutes['EUR'] <= li[1]*valutes['EUR']):
        return True
    if (cat == 'StatTrak') and (1.23*li[0]*valutes['EUR'] <= li[1]*valutes['EUR']):
        return True
    if (cat == 'Souvenir') and (1.75*li[0]*valutes['EUR'] <= li[1]*valutes['EUR']):
        return True
    if (cat == 'Knife') and (1.75*li[0]*valutes['EUR'] <= li[1]*valutes['EUR']):
        return True
    return False

def indicated(url, value1, value2):
    """ Megkapjuk az URL-t és az első 2 árát a skin-nek.
        Beolvassuk a már jelzett skin-eket (indicated fájlból) és megvizsgáljuk, hogy jeleztünk-e már erre az esetre.
        Ha igen akkor 'True'-val térünk vissza, ha nem akkor beleírjuk az 'indicated' fájlba az esetet és 'False'-al térünk vissza.
    """
    f = open('indicated', 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        datas = line.split(';')
        if (datas[0] == url) and (float(datas[1]) == round(value1,2)) and (float(datas[2]) == round(value2,2)):
            return True

    f = open('indicated', 'a')
    f.write('{0};{1};{2}\n'.format(url,round(value1,2), round(value2,2)))
    f.close()
    return False

def copyToClipboard(data):
    """ A kapott string-et a vágólapra másoljuk. """
    tmp = data.replace(' ','').replace(';', ' ')
    pyperclip.copy(tmp)

def buyIt(url, value1, value2, cat):
    """ Jelzünk a felhasználónak, hogy vegye meg a skin-t.
        Beleírjuk a 'buyit' fájlba az esetet, és hanggal jelzünk.
        Várunk egy kis időt, hogy meg lehessen venni a skin-t.
    """
    print '*'*len(readable(url))
    print '{0}%\t{1}\t{2}'.format(round(value2/value1,2)*100,round(value1,2), round(value2,2))
    print '*'*len(readable(url))
    print readable(url)
    print '*'*len(readable(url))

    h = open('buyit', 'a')
    h.write('{0}%;\t{1}€;\t{2}€;\t{3}\n{4}\n'.format(round(value2/value1,2)*100,round(value1,2), round(value2,2), readable(url), url))
    h.close()

    if (cat == 'StatTrak') and (round(value2/value1,2)*100) > 200:
        cat += '+'
    Beep.makeSound(cat)
    time.sleep(20)

def loging(k, url, tmp):
    """ Ha hibát találtunk akkor beleírjuk a 'log' fájlba. """
    print '!!!!!!!! ' + tmp + ' !!!!!!!!'
    log = open('log','a')
    log.write('{0}\t{1}\t{2}\n'.format(k, url, tmp))
    log.close()
    #winsound.Beep(1000, 2500)

def getCurrencyID(html):
    """ Megkapjuk a nyers xml szöveget és kigyűjtjük az árfolyam ID-ket. """
    html_to_string = str(html)
    lines = html_to_string.split('\n')
    for i in lines:
        if i.find('currencyid') != -1:
            line = i
            break

    ids = []
    kk = line.split('currencyid')
    del kk[0]
    for k in kk:
        ids.append(k[3:7])
    return ids

def getCategory(url):
    """ Visszatérünk a skin kategóriájával. """
    if url.find('StatTrak') != -1:
        return 'StatTrak'
    if url.find('Souvenir') != -1:
        return 'Souvenir'
    if url.find('%E2%98%85') != -1:
        return 'Knife'
    return 'normal'


#####################################################################

k = 0
valutes = getvalutess();
while(1):
    links = importLinks(sys.argv[1])
    #links = importLinks()
    print '************************** SHUFFLE **************************'
    random.shuffle(links)
    
    for t_url in links:
        waiting(12,12)
        if not((k+1) % 50):
            #os.system('python Exchanger.py')
            valutes = getvalutess()

        k += 1
        values = []
        print '\n{0}\t{1}.'.format(readable(t_url), k)

        (span_list, currencyIDs) = readURL(t_url)

        if span_list == 'WRONG':
            print 'WRONG'
            continue
        if span_list == 'WAIT':
            print 'Too fast man'    
            continue
        
        count = -1

        for span in span_list:
            if span.get('class') is not None:
                if span.get('class')[0] in ['market_listing_price']:
                    count += 1
                    if(count%3):
                        continue
                    value = span.text.encode('utf-8').strip().replace('-','')
                    values.append(valutesToUsd(value,currencyIDs[count/3]))
                    #print value, valutesToEur(value,currencyIDs[count/3])
                    
        prices = getPrices(values)

        print str(round(((prices[1]*valutes['EUR'])/(prices[0]*valutes['EUR']))*100,2)) + '% | ' + str(round(prices[0]*valutes['EUR'],2)) + ' | ' + str(round(prices[1]*valutes['EUR'],2))

        if checkValue(prices, getCategory(t_url), valutes):
            if indicated(t_url, prices[0]*valutes['EUR'], prices[1]*valutes['EUR']):
                continue
            #copyToClipboard(t_url)
            copyToClipboard(readable(t_url))
            buyIt(t_url, prices[0]*valutes['EUR'], prices[1]*valutes['EUR'], getCategory(t_url))   
    #break