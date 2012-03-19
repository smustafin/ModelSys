# -*- coding: UTF-8 -*-
__author__ = 'shom'

from numpy import random,  mean, var, std
import matplotlib.pyplot as plt
class Shows():
	NumFig = 0
	def InitHist(self,n,x,name_rand):
		self.NumFig += 1
		xm = round(mean(x),5)  # mat
		xv = round(var(x),5)  # дисперсия
		#xs = std(x)   # SKO
		plt.figure(self.NumFig)
		T1 = plt.hist(x, 10, facecolor='blue', alpha=0.75)
		plt.xlabel('x')
		plt.ylabel('m')
		plt.title('Histogram of %s:n=%s, mat=%s, dis=%s' % (name_rand,n,xm,xv))
		plt.axis([0, 1, 0, max(T1[0])+5])
		plt.grid(True)
	def ShowHist(self):
		plt.show() #вапвplа
class Random():
	name_rand = ''
	x = []
	class ownrand():
		def generate1(self,n):
			self.x = random.random(size=n)
			return self.x
		def InputName(self):
			self.name_rand = 'Random Python'
			return self.name_rand
	# ...



# ввод n - количество чисел
flag = False
while not flag:
	try:
		n = int(raw_input('Введите количество чисел - '))
		flag = True
		if n<=70:
			flag = False
			print 'Введите заново'
	except:
		print 'Введите заново'
print n
look = Shows()
rand = Random().ownrand()
look.InitHist(n, rand.generate1(n), rand.InputName())
# ....
# ....
look.ShowHist()
#////sdfsdfsdfsdfwqe