from django.db import models

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    parcen_id = models.IntegerField()
    menu_name = models.CharField(max_length=10)
    menu_url = models.CharField(max_length=20)

    def __unicode__(self):
        return self.menu_name
    
    def set_default_url(self):
        return self.menu_url >= '#'
