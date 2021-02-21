from django.shortcuts import render
from login.models import User
import json
# Create your views here.

#def trans(string):

def home_view(request):
	post_list = []
	for i in range(10):
		ob = User.objects.get(real_id=i)
		post_list.append(ob)  
	return render(request, 'home.html', {'post_list' : post_list})

def recommend_view(request):
	current_user = request.user
	real_id = current_user.id
	ob = User.objects.get(real_id=real_id)
	gpa_class = list(eval(eval(ob.gpa_lessons)).values())
	gpa_reasons = list(eval(eval(ob.gpa_reasons)).values())
	score_class = list(eval(eval(ob.score_lessons)).values())
	score_reasons = list(eval(eval(ob.score_reasons)).values())
	return render(request, 'recommend.html', {'count' : [0,1,2,3,4,5,6,7,8,9],'post' : ob, 'gpa_class' : gpa_class, 'gpa_reasons' : gpa_reasons, 'score_class' : score_class, 'score_reasons' : score_reasons})
