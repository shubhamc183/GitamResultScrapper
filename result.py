import requests
from bs4 import BeautifulSoup
sem=input("Enter sem number: ")
idno=input("Enter your ID: ")
url="https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx"
payload={'__EVENTTARGET': '', '__EVENTARGUMENT': '', 'txtreg':idno , 'Button1': 'Get+Result', '__EVENTVALIDATION': '/wEWFQKj/sbfBgLnsLO+DQLIk+gdAsmT6B0CypPoHQLLk+gdAsyT6B0CzZPoHQLOk+gdAt+T6B0C0JPoHQLIk6geAsiTpB4CyJOgHgLIk5weAsiTmB4CyJOUHgKL+46CBgKM54rGBgK7q7GGCALWlM+bAsr6TbZa4e1ProM8biQQXbC9/wS2', '__VIEWSTATE': '/wEPDwULLTE3MTAzMDk3NzUPZBYCAgMPZBYCAgcPDxYCHgRUZXh0ZWRkZKKjA/8YeuWfLRpWAZ2J1Qp0eXCJ', 'cbosem': sem, '__VIEWSTATEGENERATOR': '65B05190'}
q=requests.post(url,data=payload)
s=BeautifulSoup(q.text,'html.parser')
try:	
		name=s.find("span",{"id":"lblname"}).text
		x=s.find("table",{"class":"table-responsive"})
		a=x.findAll("tr")[1:]
		print(name)
		for i in a:
			for j in i.findAll("td"):
				print(j.text,end=" ")
			print()
		gpa=s.find("span",{"id":"lblgpa"}).text
		print("GPA=",gpa,sep='')
		cgpa=s.find("span",{"id":"lblcgpa"}).text
		print("CGPA=",cgpa,)
except:	
	print("Wrong Inputs....!")
