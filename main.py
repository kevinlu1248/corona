import requests
from re import *
from time import time

if __name__ == '__main__':
    start = time()
    print("Getting files...")
    r = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia?scene=2&clicktime=1579582238&enterid=1579582238&from=singlemessage&isappinstalled=0")
    print("Parsing...\n")
    regex = '"countRemark":"*","confirmedCount":(?P<confirmed>\d*),"suspectedCount":(?P<suspected>\d*),"curedCount":(?P<cured>\d*),"deadCount":(?P<dead>\d*),'
    s = search(regex, r.text)
    print('''Confirmed: {}\nSuspected: {}\nCured: {}\nDead: {}'''.format(s['confirmed'], s['suspected'], s['cured'], s['dead']))
    print("\nWriting it to the file...")
    with open('page.html', 'w') as f: f.write(r.text)
    print("Done in {} seconds\n".format(time() - start))
