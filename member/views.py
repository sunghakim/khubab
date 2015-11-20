from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import timezone

def join(request):
	return render(request,'join.html')


def join_update(request):

	new_member = User.objects.create_user(request.POST.get('member_id',False),
										request.POST.get('member_email',False),
										request.POST.get('member_passwd',False),)

	new_member.save()
	url  = '/'
	return HttpResponseRedirect(url)
# Create your views here.
