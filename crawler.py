#!/usr/bin/env python
#coding:utf-8
import dataOutput
import htmlDownloader
import htmlParser
import traceback
import urlManager

class crawler(object):
	
	def __init__(self):
		self.manager = urlManager.urlManager()
		self.downloader = htmlDownloader.htmlDownloader()
		self.parser = htmlParser.htmlParser()
		self.output = dataOutput.dataOutput()

	def crawl(self, root_url):
		self.manager.add_new_url(root_url)
		while(self.manager.has_new_url() and self.manager.old_url_size()<100):
			try:
				new_url = self.manager.get_new_url()
				html = self.downloader.download(new_url)
				new_urls,data = self.parser.parser(new_url,html)
				self.manager.add_new_urls(new_urls)
				self.output.store_data(data)
			except Exception as e:
				traceback.print_exc()

		self.output.output_html()

if __name__ == "__main__":
	root_url = "http://baike.baidu.com/view/284853.htm"
	cl = crawler()
	cl.crawl(root_url)
