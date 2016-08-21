import requests
from bs4 import BeautifulSoup

def result(sem,idno):
	url="https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx"
	payload={'__EVENTTARGET': '', '__EVENTARGUMENT': '', 'txtreg':idno , 'Button1': 'Get+Result', '__EVENTVALIDATION': '/wEWFQKj/sbfBgLnsLO+DQLIk+gdAsmT6B0CypPoHQLLk+gdAsyT6B0CzZPoHQLOk+gdAt+T6B0C0JPoHQLIk6geAsiTpB4CyJOgHgLIk5weAsiTmB4CyJOUHgKL+46CBgKM54rGBgK7q7GGCALWlM+bAsr6TbZa4e1ProM8biQQXbC9/wS2', '__VIEWSTATE': '/wEPDwULLTE3MTAzMDk3NzUPZBYCAgMPZBYCAgcPDxYCHgRUZXh0ZWRkZKKjA/8YeuWfLRpWAZ2J1Qp0eXCJ', 'cbosem': sem, '__VIEWSTATEGENERATOR': '65B05190'}
	q=requests.post(url,data=payload)
	s=BeautifulSoup(q.text,'html.parser')
	try:	
		name=s.find("span",{"id":"lblname"}).text
		name=name[:130]	
		x=s.find("table",{"class":"table-responsive"})
		a=x.findAll("tr")[1:]
		gpa=float(s.find("span",{"id":"lblgpa"}).text)
		cgpa=float(s.find("span",{"id":"lblcgpa"}).text)
		l=[]
		for i in a:
			sql="insert into r_2014 values ( '%s' ,'%s' ,'%s' " %( sem, idno , name )
			for j in i.findAll("td"):
				sql+=", '%s' " % j.text
			sql+=" , %3.2f ,%3.2f )" %(gpa,cgpa)
			l.append(sql)
		return l
	except:	
		return []
