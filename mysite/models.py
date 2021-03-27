#資料庫

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    vid = models.CharField(max_length=20,default="vi1CYWbyE-Q")
    pub_date = models.DateTimeField(default=timezone.now) #傳回defalt，系統時間timezone.now

    class Meta:
        ordering = ('-pub_date',) #-為遞減排序

    def __str__(self):
        return self.title #以title秀出，若pub_data則為發布時間