import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
apikey = 'IITYZ49L2LBBLXKG'
stock_name = 'IBM'
interval = '5min'
func = 'TIME_SERIES_INTRADAY'
url = f'https://www.alphavantage.co/query?function={func}&symbol={stock_name}&interval={interval}&apikey={apikey}'
print('url=>',url)
r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    from pprint import pp
    pp(data)
else:
    print(r.status_code)
    print('there was a problem')