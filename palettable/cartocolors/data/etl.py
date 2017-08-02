import sys
import os
import json
import webcolors

os.system('wget https://raw.githubusercontent.com/CartoDB/CartoColor/master/cartocolor.js')
os.system("sed -n -e '3,1834p' cartocolor.js | sed -e 's/var cartocolor = //; s/};/}/'  > cartocolors_raw.json")
os.remove('cartocolor.js')

def hexlist2rgblist(hexlist):
    return [list(webcolors.hex_to_rgb(h)) for h in hexlist]

cc_raw = json.loads(open('cartocolors_raw.json').read())

new_cc = {'Diverging': {},
          'Sequential': {},
          'Qualitative': {}}

for color in cc_raw:
    curr_cat = cc_raw[color]['tags'][0]
    if curr_cat == 'diverging':
        long_cat = 'Diverging'
        short_cat = 'div'
    elif curr_cat in ('quantitative', 'aggregation'):
        long_cat = 'Sequential'
        short_cat = 'seq'
    elif curr_cat == 'qualitative':
        long_cat = 'Qualitative'
        short_cat = 'qual'
    else:
        raise Exception(curr_cat)
        
    new_cc[long_cat][color] = {k: dict(NumOfColors=k,
                                       Type=short_cat,
                                       Colors=hexlist2rgblist(cc_raw[color][k]))
                                  for k in cc_raw[color] if k != 'tags'}

with open('cartocolors.json', 'w') as f:
    json.dump(new_cc, f)
os.remove('cartocolors_raw.json')
