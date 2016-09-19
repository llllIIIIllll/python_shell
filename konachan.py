#-*-coding:utf-8-*-
import urllib2
import urllib
import json
import time
import os
def main(tag, page, limit):
	# 获得数据
	url = 'https://konachan.net/post.json?tag=%r?page=%r?limit=%r' % (tag, page, limit)
	req = urllib2.Request(url)
	r = urllib2.urlopen(req)
	
	#处理数据
	imagelist = []	
	result = json.loads(r.read())
	for i in range(len(result)):
		imagelist.append(result[i]['jpeg_url'])
	print imagelist
	#创建目录
	if not os.path.exists(tag):
		os.makedirs(tag)

	#下载图片并保存
	n = len(imagelist)
	for j in range(1,n+1):
		print imagelist[j]
		filename = "%s/%s_%s.jpeg" % (tag, page, j)
		urllib.urlretrieve(url=imagelist[j],filename=filename)

	exit()

if __name__ == '__main__':
	#输入参数
	tag = 'breasts'
	page = 1 
	limit = 10 
	#主函数运行
	for i in range(1,5):
		main(tag, i, limit)
