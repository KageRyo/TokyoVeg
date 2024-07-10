from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=20, help_text='輸入商店名稱')
    address = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField('上傳日期')
    phone_number = models.CharField(max_length=20, default="無")
    website = models.CharField(max_length=200, default="無")
    introduction = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to='photos')