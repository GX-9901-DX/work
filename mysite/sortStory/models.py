from django.db import models
from django.utils import timezone

# Create your models here.
class sortstory(models.Model):
  create_date = models.DateTimeField(default=timezone.now)
  #ショートストーリー　入力
  title = models.CharField(max_length=100)
  sortstory = models.CharField(max_length=300)
  # タグ
  tag = models.CharField(max_length=10)

  def __str__(self):
    return self.title

class storytheme(models.Model):
  # 場所
  place = models.CharField(max_length=30)
  # 人
  human = models.CharField(max_length=30)
  #台詞として入れる単語
  dialogue = models.CharField(max_length=30)

