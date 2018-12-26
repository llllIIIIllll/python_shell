#coding:utf-8

import os,shutil

os.chdir('..')
dir = './'
for x in os.listdir('./'):
	
    if os.path.isfile(x):
		filename = os.path.basename(x)
		fileext = os.path.splitext(x)
		name = fileext[0]
		ext = fileext[1]
		ext = ext[1:len(ext)]
	    	
		try:
			src1 = os.path.join(dir,ext)
			src2 = os.path.join(src1,filename)
			if not os.path.exists(src1):
				os.mkdir(src1)
			shutil.move(filename,src2)			

		except:
			pass


#os.remove()
#os.path.isfile('path')
#os.path.isdir('path')
#os.path.isabs('path')
#os.path.exists('path')
#os.path.split('path')
#os.path.splitext('path')
#os.path.dirname('path')
#os.path.basename('path')
#os.path.system()
#os.getenv()
#os.putenv()
#os.linesep()
#os.name
#os.rename('old', new)
#os.makedirs(r'/t/t/t')
#os.mkdir(r'/t')
#os.stat(file)
#os.chmod(file)
#os.exit()
#os.path.getsize(filename)
#os.mknod("test.txt")





