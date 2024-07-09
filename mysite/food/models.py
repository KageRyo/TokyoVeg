from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=20, help_text='輸入商店名稱')
    address = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField('上傳日期')

    def __str__(self):
        return self.name