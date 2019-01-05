#!/usr/bin/env python
#coding:utf-8

import codecs

class dataOutput(object):

	def __init__(self):
		self.datas=[]

	def store_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = codecs.open('baike.html','w', encoding='utf-8')
		fout.write('<html>')
		fout.write('<body>')
		fout.write('<table>')
		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>'%data['url'])
			fout.write('<td>%s</td>'%data['title'])
			fout.write('<br/>')
			fout.write('<td>%s</td>'%data['summary'])
			fout.write('</td>')
			self.datas.remove(data)
		fout.write('</table>')
		fout.write('</body>')
		fout.write('</html>')
		fout.close()