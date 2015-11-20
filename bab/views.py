
#-*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from bab.models import Bab, Spoint
from django.http import HttpResponseRedirect

def restaurant(request):
   context = Bab.objects.all()
   return render(request, 'index.html', {'context' : context})

def detail(request, bab_id):
   average = 0
   cnt = 0
   my_point = 0
   select = get_object_or_404(Bab, pk = bab_id)

   try:
      s_point = Spoint.objects.all().filter(bab_number = bab_id)
   except Spoint.DoesNotExist:
      s_point = None

   for point in s_point:
      average += point.point
      cnt = cnt + 1
      if point.point_id == 'admin':
         my_point = point.point
   try :
      average = average / float(cnt)
   except ZeroDivisionError:
      average = 0;   
   
   
   return render(request, 'detail.html', {'select': select, 'my_point': my_point, 'average': average})
      
def point(request, bab_id):

   check = Spoint.objects.all().filter(bab_number = bab_id)
   if check != None:
      point_data = Spoint (bab_number = bab_id,
                  point_id = 'admin',
                  point = request.POST.get('_Spoint', False)
                  )
      point_data.save()
      url = '/bab/'+bab_id
      return HttpResponseRedirect(url)
   