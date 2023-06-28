import datetime as dat
class Time:
	def start_time(self,y,m,d,H,M,S):
		self.time1=dat.datetime(int(y),int(m),int(d),int(H),int(M),int(S))
	def end_time(self,y,m,d,H,M,S):
		self.time2=dat.datetime(int(y),int(m),int(d),int(H),int(M),int(S))
	def total_time(self):
		try:
			total=self.time2-self.time1
			if total>0:
				print("Total time:",total)
				return
			else:
				raise Exception
		except:
			print("Invalid Input!")


if __name__=='__main__':
	exam=Time()
	print("For Starting time of exam")
	d1=input("Enter date: ")
	m1=input("Enter month: ")
	y1=input("Enter year: ")
	H1=input("Enter hour: ")
	M1=input("Enter minutes: ")
	S1=input("Enter seconds: ")
	exam.start_time(y1,m1,d1,H1,M1,S1)
	print("For Completing time of exam")
	d2=input("Enter date: ")
	m2=input("Enter month: ")
	y2=input("Enter year: ")
	H2=input("Enter hour: ")
	M2=input("Enter minutes: ")
	S2=input("Enter seconds: ")
	exam.end_time(y2,m2,d2,H2,M2,S2)
	exam.total_time()
