# Generated by Django 3.0.1 on 2019-12-29 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='category',
            field=models.CharField(choices=[('Wage Income', '給与所得'), ('Food Expenses', '食費'), ('Water Bills', '水道代'), ('Gas Charges', 'ガス代'), ('Electricity Charges', '電気代'), ('Cellphone Charges', '携帯代'), ('Gacha Charges', 'ガチャ課金'), ('Communication Costs', '通信費'), ('Rent', '家賃')], max_length=100, verbose_name='カテゴリ'),
        ),
    ]
