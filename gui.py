import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
LARGE_FONT=("Veranda",9)

name=''
result=[]
gpa=''
cgpa=''
error=0
def getResult(sem1,idno1):
	sem1=sem1.get()
	idno1=idno1.get()
	url="https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx"
	payload={'__EVENTTARGET': '', '__EVENTARGUMENT': '', 'txtreg':idno1 , 'Button1': 'Get+Result', '__EVENTVALIDATION': '/wEWFQKj/sbfBgLnsLO+DQLIk+gdAsmT6B0CypPoHQLLk+gdAsyT6B0CzZPoHQLOk+gdAt+T6B0C0JPoHQLIk6geAsiTpB4CyJOgHgLIk5weAsiTmB4CyJOUHgKL+46CBgKM54rGBgK7q7GGCALWlM+bAsr6TbZa4e1ProM8biQQXbC9/wS2', '__VIEWSTATE': '/wEPDwULLTE3MTAzMDk3NzUPZBYCAgMPZBYCAgcPDxYCHgRUZXh0ZWRkZKKjA/8YeuWfLRpWAZ2J1Qp0eXCJ', 'cbosem': sem1, '__VIEWSTATEGENERATOR': '65B05190'}
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	q=requests.post(url,data=payload,headers=headers)
	s=BeautifulSoup(q.text,'html.parser')
	global name,result,gpa,cgpa,error
	name,cgpa,gpa='','',''
	result=[]
	error=0
	try:
		name=s.find("span",{"id":"lblname"}).text
		x=s.find("table",{"class":"table-responsive"})
		a=x.findAll("tr")[1:]
		for i in a:
			t=[]
			for j in i.findAll("td"):
				t.append(j.text)
			result.append(t)
		gpa=s.find("span",{"id":"lblgpa"}).text
		cgpa=s.find("span",{"id":"lblcgpa"}).text
		error=0
	except:
		error=1		

class gui(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		container=ttk.Frame(self)
		container.pack() #side="top" ,fill="both",expand=True)
		self.frames={}
		for F in (Intro,Result):
			frame=F(container,self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky='nsew')
		self.show_frame(Intro)
	
	def show_frame(self,selected):
		f=self.frames[selected]
		f.tkraise()

def popup(msg):
	popup=tk.Tk()
	popup.title('    !    ')
	def leave():
		popup.destroy()
	l=ttk.Label(popup,text=msg,font=('Verenda',15))
	l.pack(padx=10,pady=10)
	b=ttk.Button(popup,text='OK',command=leave)
	b.pack(padx=40,pady=40)
	popup.mainloop()

class Intro(ttk.Frame):
	def __init__(self,parent,controller):
		ttk.Frame.__init__(self,parent)
	
		self['padding']='100'
	
		labelId=ttk.Label(self,text='Id',font=LARGE_FONT)
		labelId.grid(row=2,column=1,sticky='W')

		self.idno=tk.StringVar()

		entryId=ttk.Entry(self,width=10,textvariable=self.idno,font=LARGE_FONT)
		entryId.grid(row=2,column=2)

		buttonResult=ttk.Button(self,text='Get Result',command=lambda : self.work(controller))	#lambda: controller.show_frame(Result))
		buttonResult.grid(row=4,column=2)
		
		labelSem=ttk.Label(self,text='Semester',font=LARGE_FONT)
		labelSem.grid(row=1,column=1)
	
		self.sem=tk.StringVar()
		
		sembox=ttk.Combobox(self,textvariable=self.sem,width=9)
		sembox['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15')
		sembox.grid(row=1,column=2)
	
	def work(self,controller):
		if self.idno.get()=='' and  self.sem.get()=='':
			popup('Sem and Id can\'t be NULL')
		elif self.idno.get()=='':
			popup('Id can\'t be NULL')
		elif self.sem.get()=='':
			popup('Sem can\'t be NULL')
		elif len(self.idno.get())!=10 :
			popup('Id is 10 digit long')
		
		else:
			getResult(self.sem,self.idno)
			controller.frames[Result].generate()
			controller.show_frame(Result)

class Result(ttk.Frame):
	def __init__(self,parent,controller):
		ttk.Frame.__init__(self,parent)
		buttonResult=tk.Button(self,text='Check another Result',command=lambda:self.work(controller))	
		buttonResult.grid(row=20,column=4)
	
	def work(self,controller):
		for child in self.winfo_children():
			child.destroy()
		buttonResult=tk.Button(self,text='Check another Result',command=lambda:self.work(controller))	
		buttonResult.grid(row=20,column=4)
		controller.show_frame(Intro)
	
	def generate(self):
		global name,result,cgpa,gpa,error
		if error==1:
			l=ttk.Label(self,text='Error..!',font=LARGE_FONT)
			l.grid(row=2,column=2)
		else:
			n=tk.Label(self,text=name,font=('Verenda',15)).grid(row=1,column=2)
			cc=tk.Label(self,text='Course Code',font=LARGE_FONT).grid(row=4,column=1)
			cn=tk.Label(self,text='Course Name',font=LARGE_FONT).grid(row=4,column=2) 	
			credits=tk.Label(self,text='Credits',font=LARGE_FONT).grid(row=4,column=3)
			grade=tk.Label(self,text='GRADE',font=LARGE_FONT).grid(row=4,column=4)
			x=5
			for i in result:
				c=1
				for j in i:
					if c==2:
						tk.Label(self,text=j,font=LARGE_FONT,width=50).grid(row=x,column=c)
					else:
						tk.Label(self,text=j,font=LARGE_FONT).grid(row=x,column=c)
					c+=1
				x+=1
			x+=2
			tk.Label(self,text='GPA :'+gpa,font=('Verenda',13)).grid(row=x,column=4)
			x+=1
			tk.Label(self,text='GGPA:'+cgpa,font=('Verenda',13)).grid(row=x,column=4)
	

app=gui()
app.geometry('700x400')
app.resizable(width=False,height=False)
app.title('Gitam Result')
app.mainloop()
