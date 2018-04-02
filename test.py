#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


#THING TO CHANGE IN THIS BOT
# MAKE IT FASTER
# CHANGE THE WHILE LOOPS TO CHECK FOR RESPONSE = 200
# GUI BUILDING

import urllib3
import re
import webbrowser
import requests
import sys
# import cookielib
import timeit
import time
import Tkinter as tk
import os
import json
import codecs
import datetime
import multiprocessing
import tkMessageBox as messagebox
from time import sleep
from random import randint
import Cookie
from bs4 import BeautifulSoup
from collections import OrderedDict



utf1 = '%E2%9C%93' #how to send request to atc
commit1 = 'add to cart'
_UTMC = '74692624'
_GAT = '1'
__UTMT = '1'
__UTMA= '74692624.1540672019.1492808721.1493098767.1493149663.16'
__UTMZ='74692624.1492808721.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
SUPREMECART = 'http:www.supremenewyork.com/shop/cart'
SITEKEY = "6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz"
CAPTANSWER ='03AIezHSZ6y7GJ2AYcb1z031JlZOwNb7JEzqMdP5m6rF7Ty3ZjB96g8T0eqtOqeUxCkmVjbGE2xkKJ5IFqrEh28RXT7KWpeoK4ywKcAtosSqL2fcCBOBbcMiG-TGERpoNxZ-2nTFzJrvRclQWyRkocQqJv5V-SDEj00kk4--yJmk2UMw4K2TchZqF01mly0-FV91dFKGlis4QUwWZEM3xZZ42hPM3WIbbEyrVHj7GLgMRhWhsVdaOq4Ro_mEZ-hdkdh7MSLlWQlBqlqmoZ2o_qSWRWDneqSnaPbfD8DUPIWcygWmqg13d3nszG7TQvlplzLsJWFt_sQis1WHo8OEsVgw6DmvXI99uADKnLbRYQ61e5S1JPxxOIV0eLfPHPLFSmL510O-qRTRjwvlEeWw2qsV_QodxLxIIRI7dRNgFkdmFJ_2_NBywKu3A'
SUPREME = 'http://www.supremenewyork.com'
SUPREMEJACKETS = 'http://www.supremenewyork.com/shop/all/jackets'
SUPREMESHIRTS = 'http://www.supremenewyork.com/shop/all/shirts'
SUPREMESWEATERS = 'http://www.supremenewyork.com/shop/all/tops_sweaters'
SUPREMESWEATSHIRT = 'http://www.supremenewyork.com/shop/all/sweatshirts'
SUPREMEPANTS = 'http://www.supremenewyork.com/shop/all/pants'
SUPREMESHORTS= 'http://www.supremenewyork.com/shop/all/shorts'
SUPREMEHATS = 'http://www.supremenewyork.com/shop/all/hats'
SUPREMEACCESSORIES = 'http://www.supremenewyork.com/shop/all/accessories'
SUPREMETSHIRTS = 'http://www.supremenewyork.com/shop/all/t-shirts'
SUPREMECHECKOUT = 'https://www.supremenewyork.com/checkout.json'
SUPREMESHOES = 'http://www.supremenewyork.com/shop/all/shoes'
SUPREMEBAGS = 'http://www.supremenewyork.com/shop/bags'
SUPREMEEMAIL = 'https://www.supremenewyork.com/store_credits/verify?email='




def Categories(wyw): #category
    if wyw == "jackets":
        supreme = SUPREMEJACKETS
        return supreme
    if wyw == "shirts":
        supreme = SUPREMESHIRTS
        return supreme
    if wyw == "tshirts":
        supreme = SUPREMETSHIRTS
        return supreme
    if wyw == "sweaters":
        supreme = SUPREMESWEATERS
        return supreme
    if wyw == "sweatshirts":
        supreme = SUPREMESWEATSHIRT
        return supreme
    if wyw == "pants":
        supreme = SUPREMEPANTS
        return supreme
    if wyw == "shorts":
        supreme = SUPREMESHORTS
        return supreme
    if wyw == "hats":
        supreme = SUPREMEHATS
        return supreme
    if wyw == "accessories":
        supreme = SUPREMEACCESSORIES
        return supreme
    if wyw == "shoes":
        supreme = SUPREMESHOES
        return supreme
    if wyw == 'bags':
        supreme = SUPREMEBAGS
        return supreme

########       Old Item Finder          #########################################################################################################################################################################


def keywordhunter(cop, keyword, colorway): #finds keyword and color returns the final link
    final1 = str("")
    final2 = str("") #you need this for keyword searcher

    name_box = cop.find_all('p', attrs={'p': 'href'})  #this is used for all hrefs
    for lins in cop.find_all('a', {'class':'name-link'}):   #this forloop searches for classlink to sift all hrefs
        if keyword in lins.text:                            #uses keyword to find item
            matcher = lins["href"]
            for lines in cop.find_all("a", {'class':'name-link'}):
                if colorway in lines.text:                  #uses color to find the color
                    if matcher in lines["href"]:            # matches text
                        print (matcher)


########       Item Finder         #########################################################################################################################################################################


def wordscrambler(cop, keyword, colorway):
    for lins in cop.find_all('a', {'class':'name-link'}):
        # if "http://www.supremenewyork.com" in lins["href"]:
        #     results = requests.get(lins["href"])
        #     print (results.content)
        #     if keyword in results.title:
        #         if colorway in results.title:
        #             return (lins["href"])
        # else:
            link = "http://www.supremenewyork.com" + str(lins["href"])
            #print (link)
            results = requests.get(link)
            #print (results.content)
            while 'shop' not in str(results.content):
                print ("waiting still")
                sleep(0.1)
                results = requests.get(link)
            results = BeautifulSoup(results.text, "html.parser")
            result = results.encode('ascii', "ignore")
            #print (result)
            if keyword in str(results.find("title")):       #& colorway in str(results.find("title"))
                if colorway in str(results.find("title")):
                    print (lins["href"])
                    return (lins["href"])


########       Session Id        #########################################################################################################################################################################


def get_session_id(csrftoken): #look for session id
        csrf = "csrf-token"
        csrftok = csrftoken.find("meta",{'name':csrf})["content"]
        return csrftok


########       Size Code         #########################################################################################################################################################################


def Sizefinder(target, size): #simplified s = size

    final1 = ""
    captcha_page = requests.get(target)

    while 'Supreme' not in str(captcha_page.content):
        print ("waiting still")
        sleep(0.1)
        print (str(captcha_page.content))
        captcha_page = requests.get(target)
    print ("Entered Size")
    print (size)

    soup = BeautifulSoup(captcha_page.content, "html.parser")
    for action in soup.find_all('select'):
        for actions in action.find_all('option'):
            print(actions)
            if size in actions:
                size1 = actions['value']
                return size1
    if size == "Small":
        size = "Medium"
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                print(actions)
                if size in actions:
                    size1 = actions['value']
                    return size1
    elif size == "Medium":
        size = "Large"
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                print(actions)
                if size in actions:
                    size1 = actions['value']
                    return size1
    elif size == "Large":
        size = "XLarge"
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                print(actions)
                if size in actions:
                    size1 = actions['value']
                    return size1
    if size == "XLarge":
        size = "Small"
        for action in soup.find_all('select'):
            for actions in action.find_all('option'):
                print(actions)
                if size in actions:
                    size1 = actions['value']
                    return size1

########       Style Code         #########################################################################################################################################################################

def Stylecode(link): #style code s = style
    final1 = ""
    swag = ""
    captcha_page = requests.get(link)
    while 'Supreme' not in str(captcha_page.content):
        print ("waiting still")
        sleep(0.1)
        print (str(captcha_page.content))
        captcha_page = requests.get(link)

    soup = BeautifulSoup(captcha_page.content, "html.parser")

    return soup.find(id="st")["value"]


########      Last Cart Link         #########################################################################################################################################################################


def atclink1(link,size5, style1, size): #final link to add to cart and simplified
    atclink = requests.get(link)
    #print (atclink.content)

    while 'Supreme' not in str(atclink.content):
        print ("waiting still")
        sleep(0.1)
        #print (str(atclink.content))
        atclink = requests.get(link)

    swag = ""
    soup = BeautifulSoup(atclink.content, "html.parser")
    for action in soup.find_all('form'):
        swag = action['action']
    return SUPREME + swag


def quit():
        category = var.get()
        size = var1.get()
        keyword = keyword1.get()
        colorwave = colorwave1.get()
        fullname = fullname1.get()
        email = email1.get()
        tele = tele1.get()
        address = address2.get()

        adres1 = (SecAddress.get())
        address1 = str(adres1)

        zipcode = zipcode1.get()
        city = city1.get()
        state = state1.get()
        creditcardtype = var2.get()
        creditcard = creditcard1.get()
        creditmonth = creditmonth1.get()
        credityear = credityear1.get()
        creditsec = creditsec1.get()
        captcharesp = captcharesp1.get()
        open('supremesave', 'w').close()

        f = open('supremesave', 'r+')
        array = [category, keyword, colorwave, size, fullname, email, tele, address,address1, zipcode, city, state, creditcardtype,creditcard, creditmonth, creditmonth, credityear, creditsec]

        f.write(category + '\n')
        f.write(keyword + '\n')
        f.write(colorwave + '\n')
        f.write(size + '\n')
        f.write(fullname + '\n')
        f.write(email + '\n')
        f.write(tele + '\n')
        f.write(address + '\n')
        f.write(address1 + '\n')
        f.write(zipcode + '\n')
        f.write(city + '\n')
        f.write(state + '\n')
        f.write(creditcardtype + '\n')
        f.write(creditcard + '\n')
        f.write(creditmonth + '\n')
        f.write(credityear + '\n')
        f.write(creditsec + '\n')
        f.write(captcharesp + '\n')


        master.destroy()

def change_dropdown(*args):
        print( tkvar.get() )

def clear_text():
    captcharesp1.delete(0, 'end')

def cop():

    timer1 = timer.get()
    start = time.time()
    lastidcookie = str(int(time.time()))
    category = var.get()
    size = var1.get()
    keyword = keyword1.get()
    colorwave = colorwave1.get()
    fullname = fullname1.get()
    email = email1.get()
    tele = tele1.get()
    address = address2.get()
    adres1 = (SecAddress.get())
    address1 = str(adres1)
    zipcode = zipcode1.get()
    city = city1.get()
    state = state1.get()
    creditcardtype = var2.get()
    creditcard = creditcard1.get()
    creditmonth = creditmonth1.get()
    credityear = credityear1.get()
    creditsec = creditsec1.get()
    captcharesp = captcharesp1.get()

    if "" not in timer1:
        sleep(int(timer1))

    supreme = Categories(category)
    supreme = requests.get(supreme)

    while 'Supreme' not in str(supreme.content):
        print ("waiting still")
        sleep(0.1)
        supreme = requests.get(link)

    cop = BeautifulSoup(supreme.content, "html.parser")

    # link = cop.find_all("article")

    print ("Benchmark1: Item Finder")
    target =  wordscrambler(cop,keyword, colorwave) #look for things link
    try:
        if "http://www.supremenewyork.com/" not in target:
            target = "http://www.supremenewyork.com" + target
        print (target)
    except:
        print ("out of stock")

    print ("Benchmark2: Size Finder")
    sizearray = ['Small', 'Medium', 'Large', 'XLarge']#this is for size swap if ur size is out of stock only things with these sizes


########       Multiprocess Size and Style         #########################################################################################################################################################################


    try:
        style1 = Stylecode(target)
        size1 = Sizefinder(target,size)
    except:
        print("Style and Size are gone")




    print(" ")
    print("---------------       SIZE AND STYLE CODE       ---------------------------------------------------------------------------------------------------------")
    print(" ")
    print ("Style Code: ", str(style1))
    print ("Size Code: ", str(size1))
    print(" ")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" ")






#################### THIS IS HOW TO CREATE CART COOKIE HOWEVER YOU NEED PURE CART TO REGISTER IT PROPERLY  #############################################################

    print("Benchmark3: Cookie jar")
    cookiecart = "1+item--"
    cookiecart = cookiecart + str(size1) + "%2C" + str(style1)
    "https://www.supremenewyork.com/checkout.js?utf8=%E2%9C%93&authenticity_token=q5%2F5KXf%2Fo4ZQiX43m5pkCZV%2FzzCpQToFFDd6ZEKihacdhWzzkNMiSnZu%2Fbr8Mvd8IW0f5SJctD9rMEbP9dV1nQ%3D%3D&order%5Bbilling_name%5D=Joshua+Jio+Jung&order%5Bemail%5D=jungjio%40yahoo.com&order%5Btel%5D=310-616-6650&order%5Bbilling_address%5D=2+Buswell+St&order%5Bbilling_address_2%5D=Apt+4&order%5Bbilling_zip%5D=&order%5Bbilling_city%5D=Boston&order%5Bbilling_state%5D=MA&order%5Bbilling_country%5D=USA&asec=Rmasn&same_as_billing_address=1&store_credit_id=&credit_card%5Bnlb%5D=&credit_card%5Bmonth%5D=11&credit_card%5Byear%5D=2017&credit_card%5Brvv%5D=&order%5Bterms%5D=0&g-recaptcha-response=&credit_card%5Bvval%5D=&cnt=1"
    fullname123 = fullname.replace(" ", "+")
    address123 = address.replace(" ", "+")
    addy = fullname123 + '%7C' + address + '%7C' + address1 + '%7C' + city + '%7C' + state + '%7C' + zipcode + '%7C' + 'USA' + '%7C' + email + '%7C' + tele

#################### BOT ACTIONS ARE FILLED HERE BROWSERLESS ##########################################################################################################################


    atclink = atclink1(target, size1,style1, size)


    with requests.Session() as response:


############################       form data           ################################################################################################################################

        print ("Benchmark4: Form data")
        headers1 = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
        cartdata = {
                    "utf8": "%E2%9C%93&",
                    "st" : str(style1),
                    "s" : str(size1),
                    "commit" : "add to cart"
                    }
        headding = {
            "Host": "www.google-analytics.com",
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
            "Accept" : "*/*",
            "Accept-Language" : "en-US,en;q=0.5",
            "Accept-Encoding" : "gzip, deflate, br",
            "Referer" : "https://www.supremenewyork.com/shop",
            "Connection": "keep-alive"
        }

        cart_page = requests.get(target)
        while 'Supreme' not in str(cart_page.content):
            print ("waiting still")
            sleep(0.1)
            #print (str(supreme.content))
            cart_page = requests.get(target)
        cart_page = cart_page.text
        soup = BeautifulSoup(cart_page, "html.parser")


        for strings in soup.strings:
            if "$" in str(strings.encode('ascii', 'ignore')):
                value = (str(strings))

        purecart = {
                    size1: "1",
                    "cookie" : cookiecart,
                    "total": value
                    }
        mp = {"distinct_id": "1601fd8eb1842-0e7d3679fd025b-173c6d54-13c680-1601fd8eb191ca","Store Location": "US Web","$initial_referrer": "$direct","$initial_referring_domain": "$direct"}

        print(" ")
        print("----------------     PureCart     ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        print (("PureCart String: ") + (str(purecart)))


##########################################################################################################################################################################





############################       Add to the cart         ##########################################################################################################################
        r = response.post(atclink, data=cartdata, headers = headers1)  #send response to add to cart
        #while ('200' not in str(r.status_code)) & ('Supreme' not in str(r.content)):
        while ('200' not in str(r.status_code)):
            print ("waiting still")
            sleep(0.1)
            print (str(r))
            r = response.post(atclink, data=cartdata, headers = headers1)
        print(" ")
        print("--------------      Initial Cookies        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        print("Cookies in Responses:")
        for name, value in response.cookies.items():
            print(name, value)



        # print ("Fat")
        csrf = get_session_id(BeautifulSoup(r.content, "html.parser"))
        # print(r.headers)
        # print (response.cookies.get_dict())
        cookied = response.cookies.get_dict()
        print(cookied)
        gaid = '74692624'
        vistorid = str(randint(1000000000, 9999999999))
        currenttime = str(int(time.time()))

        cookied['__utma'] = gaid + '.' + vistorid + '.'+ lastidcookie + '.'+ lastidcookie + '.'+ currenttime + '.1' #.1 gets incremented to 2
        cookied['__utmb'] = '74692624' + '5.10.' + lastidcookie
        cookied['__utmc'] = '74692624'
        cookied['__utmt'] = '1'
        cookied['__utmz'] = '74692624.' + lastidcookie + '.1.1' + '.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
        #cookied['lastid'] = lastidcookie

        cookied['mp_c5c3c493b693d7f413d219e72ab974b2_mixpanel'] = str(mp)
        cookied["mp_mixpanel__c"] = '8'


        print(" ")
        print("--------------     'Google Validation Cookies:'     ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        print(("cookied:"), cookied)


        # for j in response.cookies.get_dict():
        #     if j in "_supreme_sess":
        #         print j
        #         supreme_session = j
        #     if j in "request_method":
        #         request_method = j
        #     if j in "cart":
        #         cart = j
        # print "Supreme_session: " + supreme_session
        # print "request method:" + request_method
        # print "cart:" + cart
###########################            Checkout INFO        ############################################################################################################################################
        #this addtocart = checkout formdata

        addtocart = {
                    "utf8": "✓",
                    "authenticity_token": csrf,
                    "order[billing_name]": fullname,
                    "order[email]": email,
                    "order[tel]": tele,
                    "order[billing_address]": address,
                    "order[billing_address_2]": adres1,
                    "order[billing_zip]": zipcode,
                    "order[billing_city]": city,
                    "order[billing_state]": state,
                    "order[billing_country]": "USA",
                    "asec": "Rmasn",
                    "same_as_billing_address":"1",
                    "store_credit_id" : "",
                    "credit_card[nlb]": creditcard,
                    "credit_card[month]": creditmonth,
                    "credit_card[year]": credityear,
                    "credit_card[rvv]": creditsec,
                    "order[terms]": "0",
                    "order[terms]": "1",
                    "g-recaptcha-response": captcharesp,
                    "credit_card[vval]": ""
                    }
        preaddtocart = {
                    "utf8": "✓",
                    "authenticity_token": csrf,
                    "order[billing_name]": fullname,
                    "order[email]": email,
                    "order[tel]": tele,
                    "order[billing_address]": address,
                    "order[billing_address_2]": adres1,
                    "order[billing_zip]": zipcode,
                    "order[billing_city]": city,
                    "order[billing_state]": state,
                    "order[billing_country]": "USA",
                    "asec": "Rmasn",
                    "same_as_billing_address":"1",
                    "store_credit_id" : "",
                    "credit_card[nlb]": "",
                    "credit_card[month]": creditmonth,
                    "credit_card[year]": credityear,
                    "credit_card[rvv]": "",
                    "order[terms]": "",
                    "order[terms]": "",
                    "g-recaptcha-response": "",
                    "credit_card[vval]": "",
                    "cnt": "2"
                    }
        realheaders = {
                    "Host": "www.supremenewyork.com",
                    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
                    "Accept" : "*/*",
                    "Accept-Language" : "en-US,en;q=0.5",
                    "Accept-Encoding" : "gzip, deflate, br",
                    "Referer" : "https://www.supremenewyork.com/checkout",
                    "X-CSRF-Token" : csrf,
                    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With" : "XMLHttpRequest",
                    "Content-Length" : "1044",
                    "Connection": "keep-alive"
                    }

        emailheaders = {
                        "Host": "www.supremenewyork.com",
                        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
                        "Accept" : "text/html, */*; q=0.01",
                        "Accept-Language" : "en-US,en;q=0.5",
                        "Accept-Encoding" : "gzip, deflate, br",
                        "Referer" : "https://www.supremenewyork.com/checkout",
                        "X-CSRF-Token" : csrf,
                        "X-Requested-With" : "XMLHttpRequest",
                        "Connection": "keep-alive",
                        }


        # checkoutjs = str("utf8" + (quote("✓")) + '&' +
        #              "authenticity_token=" + (quote(csrf)) + "&" +
        #              (quote("order[billing_name]=")) + fullname.replace(" ", "+") + "&" +
        #              (quote("order[email]=")) + (quote(email)) + "&" +
        #              (quote("order[tel]=")) + tele.replace(" ", "-") + "&" +
        #              (quote("order[billing_address]=")) + address.replace(" ", "+") + "&" +
        #              (quote("order[billing_address_2]=")) + adres1.replace(" ", "+") + "&" +
        #              (quote("order[billing_zip]=")) + zipcode + "&" +
        #              (quote("order[billing_city]=")) + city + "&" +
        #              (quote("order[billing_state]=")) + state + "&" +
        #              (quote("order[billing_counter]=USA")) + "&" +
        #              "asec=Rmasn&" +
        #              "same_as_billing_address=1" +
        #              "&store_credit_id=&" +
        #              (quote("credit_card[nlb]=")) + creditcard.replace(" ", "+") + "&" +
        #              (quote("credit_card[month]=")) + creditmonth + "&" +
        #              (quote("credit_card[year]=")) + credityear + "&" +
        #              (quote("credit_card[rvv]=")) + creditsec + "&" +
        #              "order%5Bterms%5D=1&g-recaptcha-response=&credit_card%5Bvval%5D=&cnt=1")
        # # # print("https://www.supremenewyork.com/checkout.js?utf8=%E2%9C%93&authenticity_token=PvLRi8NfQidg81b5SO6jKfVaeQrfn45aBlAg3CsGam%2BI6ERRJHPD60YU1XQvRjBcQUip31SCAGB5Vxx3nHGaVQ%3D%3D&order%5Bbilling_name%5D=Joshua+Jung&order%5Bemail%5D=jungjio2%40yahoo.com&order%5Btel%5D=310-616-6650&order%5Bbilling_address%5D=860+Beacon+Street&order%5Bbilling_address_2%5D=Box+604&order%5Bbilling_zip%5D=02215&order%5Bbilling_city%5D=Boston&order%5Bbilling_state%5D=MA&order%5Bbilling_country%5D=USA&asec=Rmasn&same_as_billing_address=1&store_credit_id=&credit_card%5Bnlb%5D=&credit_card%5Bmonth%5D=11&credit_card%5Byear%5D=2017&credit_card%5Brvv%5D=&order%5Bterms%5D=0&g-recaptcha-response=&credit_card%5Bvval%5D=&cnt=3")
        # print ('https://www.supremenewyork.com/checkout.js?'+checkoutjs)
        # utfcheckout = 'https://www.supremenewyork.com/checkout.js?'+checkoutjs

################## PreCheckout Get ##########################################################################################
        cookied['__utmb'] = '74692624' + '6.10' + str(lastidcookie)
        cookied['pure_cart'] = str(purecart)
        r = response.get("https://www.supremenewyork.com/checkout.js", data = preaddtocart, headers= emailheaders, cookies = cookied )
        while ('200' not in str(r.status_code)):      #check if the data is for the cart
            print ("waiting still")
            print("Precheckout GET")
            sleep(0.1)
            print (str(r))
            r = response.get("https://www.supremenewyork.com/checkout.js", data = preaddtocart, headers= emailheaders, cookies = cookied )

        print("--------------   Post Headers    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        print (r.headers)
        print(" ")



        zz = r.cookies.get_dict()
        newsupsesh = r.cookies.get_dict()


        print("-------------------    Updated Cookies    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        print(newsupsesh)

        cookied['_supreme_sess'] = newsupsesh['_supreme_sess']
        print (cookied)


        r = response.get("https://www.supremenewyork.com/checkout.js", data = preaddtocart, headers= emailheaders, cookies = cookied )
        print (str(r))
        while ('200' not in str(r.status_code)):      #check if the data is for the cart
            print ("waiting still")
            print("Precheckout GET")
            sleep(0.1)
            print (str(r))
            r = response.get("https://www.supremenewyork.com/checkout.js", data = preaddtocart, headers= emailheaders, cookies = cookied )

        zz = r.cookies.get_dict()


        newsupsesh = r.cookies.get_dict()
        cookied["mp_mixpanel__c"] = '9'
        print("-------------------    Updated Cookies    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        print(newsupsesh)

        cookied['_supreme_sess'] = newsupsesh['_supreme_sess']
        print (cookied)
        print(" ")


        email123 = {
                'email': email
        }

        headers = {
                    'Content-type': 'application/json',
                    }
        headers123 = {
                    'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                    'Content-type': 'application/x-www-form-urlencoded',
                    'Accept': 'text/plain'
                    }


#####################################################################################################################################

        # r = requests.get(SUPREMECHECKOUT, data=(addtocart), headers=headers)
        # print r.text
        #
        # print ("lol")
        # supemail = str(supemail) + str(email)
        # supemail = supemail.replace('@', '%40')
        # print (supemail)

##################  Email HTTP POST ##########################################################################################
        supemail = 'https://www.supremenewyork.com/store_credits/verify?email='
        r = requests.get(supemail, data = email123, headers = emailheaders, cookies = cookied)

        print(" ")
        print("--------------   Email Post request    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")

        print (r.cookies.get_dict())
        while ('supreme_sess' not in str((r.cookies.get_dict()))) & ('404' in str(r.status_code)):       #check if the data is for the cart
            print ("waiting still")
            sleep(0.1)
            print (str(r))

        cookied['__utmb'] = '74692624' + '6.10' + str(lastidcookie)
        # print ('email support')
        # print (r.headers)
        # print (r.cookies.get_dict())
        # print (creditsec)
        # print ('email')

        newsupsesh = r.cookies.get_dict()           #this is the newer sesh that supreme wants
        # print (newsupsesh['_supreme_sess'])
        cookied['_supreme_sess'] = newsupsesh['_supreme_sess']

        print (cookied)
        print(" ")
#####################################################################################################################################


################## Checkout ##########################################################################################
        print("--------------   Checkout    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        currenttiem = str(int(time.time()))
        # files = {
        #         'json': (None, json.dumps(addtocart), 'application/json')}
        # atc = json.dumps(addtocart)
        payload = {'checkout_form': json.dumps(addtocart)}
        cookied['__utmb'] = '74692624' + '6.10' + str(lastidcookie)
        # print (atc)

        # r = requests.post(SUPREMECHECKOUT, json = payload, cookies = cookied, headers = headers)

        r = requests.post(SUPREMECHECKOUT, data = (addtocart), headers=realheaders, cookies = cookied)
        print (r.content)
        while ('200' not in str(r.status_code)) & ('slug' not in str(r.content)):
            print ("waiting still")
            sleep(0.1)
            print (str(r))
            r = response.post(atclink, data=cartdata, headers = headers1)

        print (r.headers)
        print (r.status_code)
        print (r.cookies.get_dict())
        #   print ((r.json()))
        print ("pat")
        print (str(r.content))
        if "failed" in str(r.content):
            print ("you failed")
            messagebox.showinfo("Supperbot", "Order Failed")
        if "slug" in str(r.content):
            print ("your order is in que")
            messagebox.showinfo("Supperbot", "Order Queued")


        print(" ")
#####################################################################################################################################
        # headers = {'Content-type': 'multipart/form-data', 'Accept': 'text/plain'}
        #
        # print("test 2")
        # r = requests.post(SUPREMECHECKOUT, data = addtocart, headers=headers, cookies = cookied)
        #
        # print (r.headers)
        # print (r.json)
        # print ("patter")
        # print (str(r.text).encode('utf-8'))
        # print (r.content)
    # except:
    #     print "could not check out item sorry"


    end = time.time()

    elapsed = end - start
    print (elapsed)

if __name__ == '__main__':

    try:


        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = os.environ.get(name)
            if user:
                username = (user)

        f = open('supremesave', 'r+')

        category = f.readline()
        category = category.replace('\n', "")

        keyword = f.readline()
        keyword = keyword.replace('\n', "")

        colorwave = f.readline()
        colorwave = colorwave.replace('\n', "")

        size = f.readline()
        size = size.replace('\n', "")

        fullname= f.readline()
        fullname = fullname.replace('\n', "")

        email = f.readline()
        email = email.replace('\n', "")

        tele = f.readline()
        tele = tele.replace('\n', "")

        address = f.readline()
        address = address.replace('\n', "")

        address1 = f.readline()
        address1 = address1.replace('\n', "")

        zipcode = f.readline()
        zipcode = zipcode.replace('\n', "")

        city = f.readline()
        city = city.replace('\n', "")

        state = f.readline()
        state = state.replace('\n', "")

        creditcardtype = f.readline()
        creditcardtype = creditcardtype.replace('\n', "")

        creditcard = f.readline()
        creditcard = creditcard.replace('\n', "")

        creditmonth = f.readline()
        creditmonth = creditmonth.replace('\n', "")

        credityear = f.readline()
        credityear = credityear.replace('\n', "")

        creditsec = f.readline()
        creditsec = creditsec.replace('\n', "")

        captcharesp = f.readline()
        captcharesp = captcharesp.replace('\n', "")





####### FIRST COLUMN GUI ###########################################################################################
        master = tk.Tk()
        COLOR = "snow2"
        pad = 10
        master.configure(background=COLOR)
        master.geometry("325x600+30+30")
        master.title("The Supper Bot")
        tk.Label(master, text="Category", bg=COLOR).grid(row=0, sticky = "W", ipadx=pad)
        tk.Label(master, text="Keyword", bg=COLOR).grid(row=1, sticky = "W", ipadx=pad)
        tk.Label(master, text="Colorwave", bg=COLOR).grid(row=2, sticky = "W", ipadx=pad)
        tk.Label(master, text="Size", bg=COLOR).grid(row=3, sticky = "W", ipadx=pad)
        tk.Label(master, text="Full Name", bg=COLOR).grid(row=4,  sticky = "W", ipadx=pad)
        tk.Label(master, text="Email", bg=COLOR).grid(row=5, sticky = "W", ipadx=pad)
        tk.Label(master, text="Tele", bg=COLOR).grid(row=6, sticky = "W", ipadx=pad)
        tk.Label(master, text="Address", bg=COLOR).grid(row=7, sticky = "W", ipadx=pad)
        tk.Label(master, text="Address 1", bg=COLOR).grid(row=8, sticky = "W", ipadx=pad)
        tk.Label(master, text="Zipcode", bg=COLOR).grid(row=9, sticky = "W", ipadx=pad)
        tk.Label(master, text="City", bg=COLOR).grid(row=10, sticky = "W", ipadx=pad)
        tk.Label(master, text="State", bg=COLOR).grid(row=11, sticky = "W", ipadx=pad)
        tk.Label(master, text="Card Type ", bg=COLOR).grid(row=12, sticky = "W", ipadx=pad)
        tk.Label(master, text="Credit Card #", bg=COLOR).grid(row=14, sticky = "W", ipadx=pad)
        tk.Label(master, text="Credit Month", bg=COLOR).grid(row=15, sticky = "W", ipadx=pad)
        tk.Label(master, text="Credit Year", bg=COLOR).grid(row=16, sticky = "W", ipadx=pad)
        tk.Label(master, text="Credit SEC", bg=COLOR).grid(row=17, sticky = "W", ipadx=pad)
        tk.Label(master, text="Timer", bg=COLOR).grid(row=18, sticky = "W", ipadx=pad)
        tk.Label(master, text="Captcha Code", bg=COLOR).grid(row=20, sticky = "W", ipadx=pad)


######## FIRST COLUMN GUI ###########################################################################################


######## SECOND COLUMN GUI  ###########################################################################################

        var = tk.StringVar()

        category1 =tk.OptionMenu(master, var,"jackets", "shirts", "tshirts", "sweaters", "sweatshirts", "pants", "shorts", "hats", "accessories", "shoes", "bags")
        var.set(category)
        category1.config(width=20, bg=COLOR)
        category1.grid(row=0, column=1)

        keyword1 = tk.Entry(master)
        keyword1.insert(0,keyword)
        keyword1.config(highlightbackground= COLOR)

        colorwave1 = tk.Entry(master, textvariable=colorwave)
        colorwave1.insert(0,colorwave)
        colorwave1.config(highlightbackground= COLOR)

        var1 = tk.StringVar()
        size1 =tk.OptionMenu(master, var1,'' ,'S/M','L/XL','Small', 'Medium', 'Large', 'XLarge')
        var1.set(size)
        size1.config(width=20,bg=COLOR)
        size1.grid(row=3, column=1)

        fullname1 = tk.Entry(master, textvariable=fullname)
        fullname1.config(highlightbackground= COLOR)
        fullname1.insert(0,fullname)

        email1 = tk.Entry(master, textvariable=email)
        email1.config(highlightbackground= COLOR)
        email1.insert(0,email)

        tele1 = tk.Entry(master, textvariable=tele)
        tele1.config(highlightbackground= COLOR)
        tele1.insert(0,tele)

        address2 = tk.Entry(master, textvariable=address)
        address2.config(highlightbackground= COLOR)
        address2.insert(0,address)

        SecAddress = tk.Entry(master, textvariable=address1)
        SecAddress.config(highlightbackground= COLOR)
        SecAddress.insert(0,address1)

        zipcode1 = tk.Entry(master, textvariable=zipcode)
        zipcode1.config(highlightbackground= COLOR)
        zipcode1.insert(0,zipcode)

        city1 = tk.Entry(master, textvariable = city)
        city1.config(highlightbackground= COLOR)
        city1.insert(0,city)

        state1 = tk.Entry(master, textvariable = state)
        state1.config(highlightbackground= COLOR)
        state1.insert(0,state)

        var2 = tk.StringVar()
        creditcardtype3 =tk.OptionMenu(master, var2,'visa', 'american_express', 'mastercard')
        creditcardtype3.config(width=20,bg=COLOR)
        var2.set(creditcardtype)

        creditcard1 = tk.Entry(master, textvariable = creditcard)
        creditcard1.config(highlightbackground= COLOR)
        creditcard1.insert(0,creditcard)

        creditmonth1 = tk.Entry(master, textvariable = creditmonth)
        creditmonth1.config(highlightbackground= COLOR)
        creditmonth1.insert(0,creditmonth)

        credityear1 = tk.Entry(master, textvariable = credityear)
        credityear1.config(highlightbackground= COLOR)
        credityear1.insert(0,credityear)

        creditsec1 = tk.Entry(master, textvariable = creditsec)
        creditsec1.config(highlightbackground= COLOR)
        creditsec1.insert(0,creditsec)

        captcharesp1 = tk.Entry(master, textvariable = captcharesp)
        captcharesp1.config(highlightbackground= COLOR)
        captcharesp1.insert(0,captcharesp)

        end = tk.Button(master, text="Exit", highlightbackground = COLOR, command = quit)
        end.config(width = 10)

        buy = tk.Button(master, text="Buy", highlightbackground = COLOR, command = cop) # this is to cop, create the function
        buy.config(width = 10)

        timer = tk.Entry(master)
        timer.config(highlightbackground= COLOR)

        captchaclearnbutton = tk.Button(master, text="Clear Captcha",highlightbackground = COLOR, command=clear_text)
        captchaclearnbutton.config(width = 10)



        category1.grid(row=0, column=1)
        keyword1.grid(row=1, column=1)
        colorwave1.grid(row=2, column=1)
        size1.grid(row=3, column=1)
        fullname1.grid(row=4, column=1)
        email1.grid(row=5, column=1)
        tele1.grid(row=6, column=1)
        address2.grid(row=7, column=1)
        SecAddress.grid(row=8, column=1)
        zipcode1.grid(row=9, column=1)
        city1.grid(row=10, column=1)
        state1.grid(row=11, column=1)
        creditcardtype3.grid(row=12, column=1)
        creditcard1.grid(row=14, column=1)
        creditmonth1.grid(row=15, column=1)
        credityear1.grid(row=16, column=1)
        creditsec1.grid(row=17, column=1)
        timer.grid(row=18, column=1)
        captcharesp1.grid(row=20, column = 1)
        captchaclearnbutton.grid(row=21, column = 1)
        end.grid(row=22, column = 1)
        buy.grid(row=21, column = 0)


######## SECOND COLUMN GUI  ###########################################################################################


######## Main loop logic  ###########################################################################################
        # master.attributes("-topmost", True)
        master.lift()
        master.attributes('-topmost',True)
        master.after_idle(master.attributes,'-topmost',False)

        master.mainloop()

        category = var.get()
        size = var1.get()
        keyword = keyword1.get()
        colorwave = colorwave1.get()
        fullname = fullname1.get()
        email = email1.get()
        tele = tele1.get()
        address = address2.get()

        adres1 = (SecAddress.get())
        address1 = str(adres1)

        zipcode = zipcode1.get()
        city = city1.get()
        state = state1.get()
        creditcardtype = var2.get()
        creditcard = creditcard1.get()
        creditmonth = creditmonth1.get()
        credityear = credityear1.get()
        creditsec = creditsec1.get()
        open('supremesave', 'w').close()


        f = open('supremesave', 'r+')
        array = [category, keyword, colorwave, size, fullname, email, tele, address,address1, zipcode, city, state, creditcardtype,creditcard, creditmonth, creditmonth, credityear, creditsec]

        f.write(category + '\n')
        f.write(keyword + '\n')
        f.write(colorwave + '\n')
        f.write(size + '\n')
        f.write(fullname + '\n')
        f.write(email + '\n')
        f.write(tele + '\n')
        f.write(address + '\n')
        f.write(address1 + '\n')
        f.write(zipcode + '\n')
        f.write(city + '\n')
        f.write(state + '\n')
        f.write(creditcardtype + '\n')
        f.write(creditcard + '\n')
        f.write(creditmonth + '\n')
        f.write(credityear + '\n')
        f.write(creditsec + '\n')



######## Data Organization  #################################################################################################################################################################################################################################################################################


        #     # driver.find_element_by_css_('order_terms').click()
        #     #
        #     #
        #     #
        #     #
        #     #
        #     #
        #     # driver.find_element_by_name('order[terms]').click()
        #     # #driver.find_element_by_id("order_terms").click()
        #     # driver.find_element_by_id("order_terms").click()
        #     # swag =
        #     # swag.click()
        #     # driver.find_element_by_id("store_address").click()
        #     # driver.find_element_by_xpath("//*[@id='cart-cc']/fieldset/p[2]/label/div").click
        #     #
        #     #
        #t
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #     # post_data1get = response.post(SUPREMECHECKOUT, headers = headers1, params =d)
        #     # print "cunt"
        #     # #data= request.POST.get('data','')
        #     # print post_data1get.headers
        #     # #post_data1 = response.post(SUPREMECHECKOUT, data = payload1, headers = headers1, cookies = response.cookies)#checks out the item
        #     # print post_data1get.request.headers
        #     # print post_data1get.headers
        #     # print post_data1get.POST.get('data', '')
        #     #
        #     # print post_data1get.content
        #

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
          #you need this to throw the exception
