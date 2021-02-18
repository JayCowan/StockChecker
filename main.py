import overclockers as oc
import elara
import const
import notify
from time import sleep
import random
from links import *
try:
    while True:
        for link in overclockers_links:
            stock = oc.overclockers_check(link)
            if stock != const.NOT_IN_STOCK:
                notify.notify(stock)

                break
        for link in elara_links:
            stock = elara.check(link)
            if stock != const.NOT_IN_STOCK:
                notify.notify(stock)
                break
        sleep(25 + random.randint(0, 10)/random.randint(1,7))
except ConnectionError as e:
    print(e)
    notify.notify_error(e)
