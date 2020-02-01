import requests
from re import *

if __name__ == '__main__':
    r = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia?scene=2&clicktime=1579582238&enterid=1579582238&from=singlemessage&isappinstalled=0")
    # with open('page.html', 'w') as f: f.write(r.text)
    regex = '"countRemark":"*","confirmedCount":(?P<confirmed>\d*),"suspectedCount":(?P<suspected>\d*),"curedCount":(?P<cured>\d*),"deadCount":(?P<dead>\d*),'
    s = search(regex, r.text)
    print('''Confirmed: {}\nSuspected: {}\nCured: {}\nDead: {}'''.format(s['confirmed'], s['suspected'], s['cured'], s['dead']))

