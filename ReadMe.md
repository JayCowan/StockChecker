#Python PC Part Stock Checking Bot
Currently supports overclockers.co.uk and elara.ie
##What You Must Create
* const.py which you can define your:
    * twilio phone number
    * personal phone number
    * NOT_IN_STOCK value
    * HEADERS value, though ``HEADERS = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}
`` is recommended
* list.py where you create a list of links in the form ``overclockers_links = {}`` and ``elara_links = {}`` both of which take strings of the product's url
* .env file with your twilio account sid and token
##What It Does
Texts you when a product comes into stock from the given links, checking every 15 seconds