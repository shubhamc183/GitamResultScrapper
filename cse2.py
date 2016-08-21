from dbResult import result
import MySQLdb
db=MySQLdb.connect(host='localhost',user='user_name',passwd='ur_password',db='result')
c=db.cursor()
db.set_character_set('utf8')
res=0
s=[  '12103147', '12103148', '12103149','12103140']
for i in s:
	sec=0
	for j in range(1,10):
		t=i+'0'+str(j)
		for sem in range(1,5):
			l=result(str(sem),t)
			if l!=[]:
				for d in l:
					c.execute(d)
				db.commit()
				sec+=1
	for j in range(10,68):
		t=i+str(j)
		for sem in range(1,5):
			l=result(str(sem),t)
			if l!=[]:
				for d in l:
					c.execute(d)
				db.commit()
				sec+=1
	res+=sec
	print(i+'*',sec,"results scraped")
print("total",res,"scraped :p")
