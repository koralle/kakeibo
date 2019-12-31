from django.db import models
import datetime

# Create your models here.
class Balance(models.Model):
  ITEM_CATEGORY_CHOICES = [
    ('給与所得', '給与所得'),
    ('食費', '食費'),
    ('Water Bills', '水道代'),
    ('ガス代', 'ガス代'),
    ('電気代', '電気代'),
    ('携帯代', '携帯代'),
    ('ガチャ課金', 'ガチャ課金'),
    ('通信費', '通信費'),
    ('交際費', '交際費'),
    ('交通費', '交通費'),
    ('家賃', '家賃'),
    ('その他', 'その他')
  ]

  BALANCE_CHOICES = [
    ('収入', '収入'),
    ('支出', '支出')
  ]

  # 項目名
  item_name = models.CharField(verbose_name='名前', max_length=100)

  # 金額
  amount = models.IntegerField(default = 0)

  # 日時
  registered_date = models.DateField(verbose_name='日時', null = True)

  # カテゴリ
  category = models.CharField(max_length=100, verbose_name='カテゴリ', choices=ITEM_CATEGORY_CHOICES)

  # 収入化支出か
  balance_type = models.CharField(max_length=20, verbose_name='収支タイプ' ,choices=BALANCE_CHOICES)

  def __str__(self):
    return self.item_name