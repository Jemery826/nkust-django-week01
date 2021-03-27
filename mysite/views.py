from django.shortcuts import render,redirect  #渲染器
from django.http import HttpResponse #不找模板
import random,datetime
from mysite import models #

def play(request, id):
	try:
		post = models.Post.objects.get(id=id) #去找id
		return render(request, "play.html", locals())
	except: #找不到
		return redirect("/") #找不到直接回首頁

def index(request):   #定義index，完整標準，index.html放在templates裡
	posts = models.Post.objects.all() #將Post輸入的資料all全部拿出
	return render(request, "index.html", locals())

def lotto(request):   #定義index，完整標準，index.html放在templates裡
	numbers = [n for n in range(1, 43)] #串列
	random.shuffle(numbers) #將number順序打亂
	lotto = numbers[:6]	 #設定亂數並取6個值
	special = numbers[6]
	return render(request, "lotto.html", locals())

def date(request):  #定義/date的頁面，完全不用	
	now = datetime.datetime.now()
	return HttpResponse("<h1 style= 'font-family:標楷體;'>現在時刻：{}</h1><hr>".format(now))

def dashboard(request):   #定義index，完整標準，index.html放在templates裡
	return render(request, "dashboard.html", locals())