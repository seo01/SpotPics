from common_colors import *
import os, sys
import pycoingecko
import requests # to get image from the web
import shutil # to save it locally

# Argument is coingecko image output path

coingecko_client = pycoingecko.CoinGeckoAPI()
top_tokens = coingecko_client.get_coins_markets(vs_currency='USD', per_page=100)
tokens = [(t['id'], t['image'])for t in top_tokens]

path = sys.argv[1]

for (id, image_url) in tokens:
	r = requests.get(image_url, stream = True)
	filename = "%s/%s.png" % (path, id)

	# Check if the image was retrieved successfully
	if r.status_code == 200:
	    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	    r.raw.decode_content = True
	    
	    # Open a local file with wb ( write binary ) permission.
	    with open(filename,'wb') as f:
	        shutil.copyfileobj(r.raw, f)
	        
	    print('Image sucessfully Downloaded: ',filename)
	else:
	    print('Image Couldn\'t be retreived')
