import requests
from lib.parser import *

class Exalead():
	def __init__(self,target):
		self.target = target

	def search(self):
		print('Searching "%s" in Exalead...'%(self.target))
		url = "http://www.exalead.com/search/web/results/?q=%40{target}&elements_per_page=50&start_index=0".format(
			target=self.target)
		try:
			headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
			'cache-control': 'max-age=0',
			'cookie': '',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
			'Referer': 'http://exalead.com/search/web/results/?q=%40{target}'.format(target=self.target)
			}
			resp = requests.get(url,headers=headers)
			return self.getemail(resp.content,self.target)
		except Exception as e:
			pass

	def getemail(self,content,target):
		return parser(content,target).email()