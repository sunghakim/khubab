from django.db import models

class Bab(models.Model):
   bab_img = models.FileField(upload_to='',blank = True , null = True, max_length = 100)
   bab_name = models.CharField(max_length = 100)
   bab_date = models.DateField()
   bab_contents = models.TextField()

   def __unicode__(self):
      return self.bab_name

class Spoint(models.Model):
   bab_number = models.IntegerField()
   point_id = models.CharField(max_length = 100)
   point = models.IntegerField()


   def __unicode__(self):
      return self.point_id