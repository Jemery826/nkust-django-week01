from django.shortcuts import render  #渲染器
from django.http import HttpResponse #不找模板
import random,datetime

def index(request):   #定義index，完整標準，index.html放在templates裡
	
	return render(request, "index.html", locals())

def lotto(request):   #定義index，完整標準，index.html放在templates裡
	numbers = [n for n in range(1, 43)] #串列
	random.shuffle(numbers) #將number順序打亂
	lotto = numbers[:6]	 #設定亂數並取6個值
	special = numbers[6]
	return render(request, "lotto.html", locals())

def date(request):  #定義/date的頁面，完全不用	
	now = datetime.datetime.now()
	return HttpResponse("現在時刻：{}".format(now))

def dashboard(request):   #定義index，完整標準，index.html放在templates裡
	
	return render(request, "dashboard.html", locals())