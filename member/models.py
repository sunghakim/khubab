from django.db import models
class member(models.Model):
	m_id = models.CharField(max_length = 100)
	m_nick2 = models.CharField(max_length = 100)
	m_email = models.EmailField(max_length = 100)
	m_passwd = models.CharField(max_length = 100)
	m_date = models.DateField('join date')

	def __unicode__(self):
		return self.m_nick2
# Create your models here.
