#-*- coding: utf-8 -*-
import urllib2
import urllib
import json
import time
import os
import re
import xlwt
def main():
	user_id = []
	for i in range(1,2):
		# 获得数据
		url = 'http://tieba.baidu.com/p/4477549692?pn=%r' % i
		r = urllib.urlopen(url)
		result = r.read()
		# 正则
		datalist = [[]]	
		# 获得楼主数据
		pattern = re.compile(r'<div\sclass="l_post.+>')
		datalist =  pattern.findall( result ) 	

		n1 = len(datalist)
		# 匹配id
		user_id_pattern = re.compile(r'user_id&quot;:(\d+),')
		# 匹配pid
		user_pid_pattern = re.compile(r'post_id&quot;:(\d+),')

		

		for j in range(n1):
			# 增加用户记录
			user_id.append([])
			# 获得用户id
			temp_user_id = user_id_pattern.findall( datalist[j] )
			user_id[j].append( temp_user_id )
			# 获得用户发帖标识
			temp_post_id = user_pid_pattern.findall( datalist[j] )
			user_id[j].append (temp_post_id )
			pid = int(  temp_post_id[0] )
			print pid
			#pid 的总回复
			pid_total_num_pattern = re.compile(r'pid&quot;:(%s),&quot;total_num&quot;:(\d+)' % (pid) ) 
			pid_total_num_temp = pid_total_num_pattern.findall( result  )			
			user_id[j].append ( pid_total_num_temp )	

	f = xlwt.Workbook()
	sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) 
	for k in range(len(user_id[0])):
		try:
			sheet1.write(k,1,str(user_id[k][2]) )
		except:
			print "error"
	f.save('text.xls')
	print user_id










if __name__ == '__main__':
	main()	

