from django.db import models

# Create your models here.


class Board(models.Model):
	writer = models.CharField(max_length = 20)
	title = models.CharField(max_length = 70)
	board_contents = models.TextField()
	board_date = models.DateTimeField()
	
	def __unicode__(self):
		return self.title