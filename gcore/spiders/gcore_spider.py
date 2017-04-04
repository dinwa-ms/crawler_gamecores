import scrapy
import csv
from scrapy.http.request import Request


class GcoreSpider(scrapy.Spider):
	name = "gcore"
	count = 1

	def start_requests(self):
		urls = []
		with open("urls.csv", "a+") as f:
			writer = csv.writer(f, delimiter=",")
			for i in range (0, 9):
				url = 'http://www.g-cores.com/categories/4/originals?page={}'.format(i)
				writer.writerow([url])

		with open("urls.csv", "rb") as urls:
			for index, url in enumerate(urls):
					yield scrapy.Request(url=url, callback=self.parse, meta={'order': index})


	def parse(self, response):
		articles = response.xpath('//div[@class="showcase showcase-article"]')
		articles.extract()

		with open("gcore_result_{}.csv".format(response.meta["order"]),"a+") as f:
			writer = csv.writer(f, delimiter=",")
			# writer.writerow(["NO.", "TIME", "TITLE", "SUBTITLE"])

			for index, article in enumerate(articles):
				time = article.xpath('div[@class="showcase_time"]/text()').extract()[1]
				title = article.xpath('div[@class="showcase_text"]/h4/a/text()').extract_first()
				subtitle = article.xpath('div[@class="showcase_text"]/div[@class="showcase_info"]/text()').extract_first()
				print "-------- article {} -------".format(self.count)
				print "Title is: {}".format(title.encode('utf-8').strip())
				print "Subtitle is: {}".format(subtitle.encode('utf-8').strip())
				print "Published on {}".format(time.strip())
				print "---------------------------"
				self.count += 1
				writer.writerow([index, time.strip(), title.encode('utf-8').strip(), subtitle.encode('utf-8').strip()])

		print "Total nunmber of artile: {}".format(self.count+1)


