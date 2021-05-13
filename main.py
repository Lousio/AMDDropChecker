import time
from multiprocessing.connection import Client
import requests
from bs4 import BeautifulSoup as bs4

conn = None  # Declared here as it tends to complain about conn not being declared before initialisation
dropping1 = 0  # Multiple dropping counter variables as multiple cards can drop at once
dropping2 = 0
dropping3 = 0
dropping4 = 0
dropping5 = 0
dropping6 = 0


# This method sets up the connection through a socket with the discord bot, can be commented out if not wanted
def setupConnection():
    global conn
    conn = Client(('localhost', 6000), authkey='CHANGEKEY'.encode('utf-8'))


# This method checks on the DigitalRiver link for CAT_000016 error through HTML parsing, then sends message to bot
def checkRX6700XT():
    dropSoon = False    # Flag to see if there will be a drop soon
    global dropping1    # dropping counter
    idChanged = False   # Flag to check if Product-ID changed
    # Link of DigitalRiver's API
    url = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5496921400&SiteID=defaults'
    r = requests.get(url)
    soup = bs4(r.text, 'html.parser')   # Parse it to HTML
    text = soup.get_text()  # Get the text from the parsed HTML
    str1 = "RX 6700 XT "    # First part of the string for the output string
    if "CAT_000016" in text:    # Check if CAT_000016 is in the text from the HTML. CAT_000016 = Drop now or soon
        dropSoon = True
    if "CAT_000001" in text:    # CAT_000001 means Product-ID is wrong
        idChanged = True
    if dropSoon:    # If it will be dropping soon or now, then set up the proper string with the product link
        str2 = "will be dropping soon! Get ready! https://www.amd.com/de/direct-buy/5496921400/de "
        dropping1 = dropping1 + 1
    else:
        str2 = "won't drop at the moment!"

    result = str1 + str2    # Combine both strings for the result string
    print(result)
    if idChanged:   # Send to author of code that the product ID changed (DM on discord)
        conn.send("Product-ID changed 6700XT")
    if dropSoon and dropping1 < 4:      # The bot will ping a maximum of 3 times before stopping to do so
        conn.send(result)


# Check if RX 6800 is dropping soon. Function is identical as the RX6700 XT one.
def checkRX6800():
    dropSoon = False
    global dropping2
    idChanged = False
    url = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5458374000&SiteID=defaults'
    r = requests.get(url)
    soup = bs4(r.text, 'html.parser')
    text = soup.get_text()
    str1 = "RX 6800 "
    if "CAT_000016" in text:
        dropSoon = True
    if "CAT_000001" in text:
        idChanged = True
    if dropSoon:
        str2 = "will be dropping soon! Get ready! https://www.amd.com/de/direct-buy/5458374000/de "
        dropping2 = dropping2 + 1
    else:
        str2 = "won't drop at the moment!"

    result = str1 + str2
    print(result)
    if idChanged:
        conn.send("Product-ID changed 6800")
    if dropSoon and dropping2 < 4:
        conn.send(result)


# Check if RX 6800XT is dropping soon. Function is identical as the RX6700 XT one.
def checkRX6800XT():
    dropSoon = False
    idChanged = False
    global dropping3
    url = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5458374100&SiteID=defaults'
    r = requests.get(url)
    soup = bs4(r.text, 'html.parser')
    text = soup.get_text()
    str1 = "RX 6800 XT "
    if "CAT_000016" in text:
        dropSoon = True
    if "CAT_000001" in text:
        idChanged = True
    if dropSoon:
        str2 = "will be dropping soon! Get ready! https://www.amd.com/de/direct-buy/5458374100/de "
        dropping3 = dropping3 + 1
    else:
        str2 = "won't drop at the moment!"

    result = str1 + str2
    print(result)
    if idChanged:
        conn.send("Product-ID changed 6800XT")
    if dropSoon and dropping3 < 4:
        conn.send(result)


# Check if RX 6800XT Midnight Black edition is dropping soon. Function is identical as the RX6700 XT one.
def checkRX6800XTMB():
    dropSoon = False
    global dropping4
    idChanged = False
    url = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5496921500&SiteID=defaults'
    r = requests.get(url)
    soup = bs4(r.text, 'html.parser')
    text = soup.get_text()
    str1 = "RX 6800 XT MB "
    if "CAT_000016" in text:
        dropSoon = True
    if "CAT_000001" in text:
        idChanged = True
    if dropSoon:
        str2 = "will be dropping soon! Get ready! https://www.amd.com/de/direct-buy/5496921500/de "
        dropping4 = dropping4 + 1
    else:
        str2 = "won't drop at the moment!"

    result = str1 + str2
    print(result)
    if idChanged:
        conn.send("Product-ID changed 6800XT MB")
    if dropSoon and dropping4 < 4:
        conn.send(result)


# Check if RX 6900XT is dropping soon. Function is identical as the RX6700 XT one.
def checkRX6900XT():
    dropSoon = False
    global dropping5
    idChanged = False
    url = 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=de_DE&ProductID=5458374200&SiteID=defaults'
    r = requests.get(url)
    soup = bs4(r.text, 'html.parser')
    text = soup.get_text()
    str1 = "RX 6900 XT "
    if "CAT_000016" in text:
        dropSoon = True
    if "CAT_000001" in text:
        idChanged = True
    if dropSoon:
        str2 = "will be dropping soon! Get ready! https://www.amd.com/de/direct-buy/5458374200/de "
        dropping5 = dropping5 + 1
    else:
        str2 = "won't drop at the moment!"

    result = str1 + str2
    print(result)
    if idChanged:
        conn.send("Product-ID changed 6900XT")
    if dropSoon and dropping5 < 4:
        conn.send(result)


# This function checks if it's the specified hot time where a drop could happen. (Wed-Fri 5-9 PM CEST)
# It's based on current local time
def checkTime():
    while True:
        now = time.localtime()      # Get current local time
        # Check if it's Wed-Fri but not hot phase -> Sleep till it is time (5-9PM)
        if (0 <= now.tm_hour < 16 or now.tm_hour > 21) and now.tm_wday in [2, 3, 4]:
            print('It\'s {:d}:{:d}, so won\'t check now'.format(now.tm_hour, now.tm_min))
            time.sleep(60)
        # If it's not Wed-Fri, then don't bother checking, no point
        elif now.tm_wday not in [2, 3, 4]:
            print("It's not Wednesday, Thursday, Friday")
            time.sleep(3600)
        # We will exit the while true loop once it is hot phase and it's Wed-Fri
        else:
            break


if __name__ == '__main__':
    setupConnection()
    counter = 1
    while True:
        checkTime()     # Check if it's time for drop, otherwise we never leave checkTime()
        checkRX6700XT()     # Then proceed to check all the cards
        checkRX6800()
        checkRX6800XT()
        checkRX6800XTMB()
        checkRX6900XT()
        print('Finished round {:d}'.format(counter))    # Just informative string saying how many checks completed
        print("")
        counter = counter + 1   
        time.sleep(60)              # Check every minute for availability
