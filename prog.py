# -*- coding: UTF-8 -*-
__author__ = 'shom'

from numpy import random,  mean, var, std
import matplotlib.pyplot as plt
import time, math
class Shows:
	def __init__(self):
		self.NumFig = 0
	def InitHist(self,n,x,name_rand):
		self.NumFig += 1
		xm = round(mean(x),5)  # mat
		xv = round(var(x),5)  # дисперсия
		#xs = std(x)   # SKO
		numint = 10
		plt.figure(self.NumFig)
		T1 = plt.hist(x, numint, facecolor='green', alpha=0.75)
		hi = 0
		#print T1[0]
		#print T1[0][1]
		for T in T1[0]:
			ehi = float(((T - n/numint)**2)/(n/numint))
			hi = hi + ehi
		#print hi
		plt.xlabel('x')
		plt.ylabel('m')
		plt.title('%s:n=%s, mat=%s, dis=%s, hi^2=%s' % (name_rand,n,xm,xv,hi))
		plt.axis([0, 1, 0, max(T1[0])+5])
		plt.grid(True)
	def ShowHist(self):
		plt.show() #вапвplа
	def Input(self,a,b):
		flag = False
		while not flag:
			try:
				n = float(raw_input())
				flag = True
				if not a<=n<=b:
					flag = False
					print 'Введите заново'
			except:
				print 'Введите заново'
		return n
class Random():
	def randtime(self, zz = False,ee=2):
		t0 = time.time()
		t0 = int(t0*100000000)
		c = str(t0)
		if not zz:
			c = '0.'+ c[11:]
			t0 = float(c)
		else:
			c = c[11:]
			t0 = int(c)
		return round(t0,ee)
	class OwnRand:
		def __init__(self,ee):
			self.ee = ee
		def generate(self):
			self.x = random.random()
			self.name_rand = 'Random Python'
			return round(self.x,self.ee)
	class Neiman:
		def __init__(self,t1,ee):
			self.nm = []
			self.t = t1
			self.name_rand = "Neiman"
			self.ee = ee
		#for i in xrange(n):
		def generate(self):
			c = str(self.t**2)
			#Если число после возведения в кв уменьшило длину, дописываем 11 в конец
			if len(c)<14:
				for i in xrange(14-len(c)):
					c = c + '1'
			#обрезаем три первых и один последний
			c = '0.' + c[5:len(c)-1]
			self.t = float(c)
			return round(self.t,self.ee)
	class Multiplication:
		def __init__(self,a,t0,ee):
			self.k = a*8-3
			self.t = t0
			self.name_rand = 'Multiplication'
			self.ee = ee
		def generate(self):
			self.t = self.k*self.t - int(self.k*self.t)
			return round(self.t,self.ee)
	class RandomMultiplication:
		def __init__(self, x0, x1, ee):
			assert "size digits after point <> n",\
			len(str(math.modf(x0)[0])[2:]) == len(str(math.modf(x1)[0])[2:])
			self.x0 = x0
			self.x1 = x1
			self.n = len(str(math.modf(x0)[0])[2:])
			self.name_rand = 'Method of Multi-tion'
			self.ee = ee

		def generate(self):
			try:
				test = str(math.modf(self.x0 * self.x1)[0])[2:]
				q2 = str(math.modf(self.x0 * self.x1)[0])[2:]
				if 'e' in q2:
					q2 = str(math.modf(self.x0 * self.x1)[0])
					order_num = int(q2.split('e')[1])
					q2 = q2.split("e")[0]
					q2 = q2.replace('.', '')
					order_num += 1
					order_num *= -1
					for i in range(order_num):
						q2 = '0' + q2
				if len(q2) > self.n:
					index = (len(q2) - self.n) / 2
					q2 = '0.' + q2[index:index + self.n]
				else:
					q2 = '0.' + q2
				self.x0 = self.x1
				self.x1 = float(q2)
				return round(self.x1, self.ee)
			except ValueError, e:
				print 'exp_str= ',e
				print 'q2= ',q2
				print 'test= ',test

	class MultiCongruential:
		def __init__(self, k, alpha, d,ee):
			self.alpha = alpha
			self.k = k
			self.q = 10**d
			self.name_rand = 'MultiCongruential'
			self.ee = ee

		def generate(self):
			self.alpha = (self.k*self.alpha) % self.q
			return round(float(self.alpha) / self.q,self.ee)

	class Lemer(MultiCongruential):
		def __init__(self, k, alpha, d,ee):
			self.alpha = alpha
			self.k = k
			self.q = 2**d
			self.name_rand = 'Lemer'
			self.ee = ee
			# ...



# ввод n - количество чисел
print 'Введите количество генерированных чисел'
look = Shows()
n = int(look.Input(10,10000))
print 'Введите точность количество знаков после запятой (2 - 8)'
ee = int(look.Input(2,8))
print 'Введите начальное число для Неймана'
x0 = look.Input(0.001,0.999)
rand1 = Random().OwnRand(ee)
rand2 = Random().Neiman(x0,ee)
print 'Введите коэф-нт k мультипликативного метода'
p = look.Input(2,1000)
rand3 = Random().Multiplication(p, Random().randtime(False, ee),ee)
rand4 = Random().RandomMultiplication(Random().randtime(False, ee),Random().randtime(False, ee),ee)
print 'Введите коэф-нт K для конгруэнтного метода'
p = look.Input(2,1000)
print 'Введите степень d для конгруэнтного метода'
pp = look.Input(2,1000)
rand5 = Random().MultiCongruential(p,Random().randtime(True,ee),pp,ee)
print 'Введите коэф-нт K для метода Лемера'
p = look.Input(2,1000)
print 'Введите степень d для метода Лемера'
pp = look.Input(2,1000)
rand6 = Random().Lemer(p,Random().randtime(True,ee),pp,ee)
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
for i in xrange(n):
	x1.append(rand1.generate())
	x2.append(rand2.generate())
	x3.append(rand3.generate())
	x4.append(rand4.generate())
	x5.append(rand5.generate())
	x6.append(rand6.generate())
print 'Родной рэндом'
print x1
print 'Метод Неймана'
print x2
print 'Мультипликативный'
print x3
print 'Метод произведений'
print x4
print 'Конгруэнтный метод'
print x5
print 'Метод Лемера'
print x6
look.InitHist(n, x1, rand1.name_rand)
look.InitHist(n, x2, rand2.name_rand)
look.InitHist(n, x3, rand3.name_rand)
look.InitHist(n, x4, rand4.name_rand)
look.InitHist(n, x5, rand5.name_rand)
look.InitHist(n, x6, rand6.name_rand)
#print round(Random().randtime(),4)
look.ShowHist()
#////sdfsdfsdfsdfwqe