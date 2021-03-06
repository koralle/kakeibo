# Generated by Django 3.0.1 on 2019-12-30 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_balance_registered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='category',
            field=models.CharField(choices=[('給与所得', '給与所得'), ('食費', '食費'), ('Water Bills', '水道代'), ('ガス代', 'ガス代'), ('電気代', '電気代'), ('携帯代', '携帯代'), ('ガチャ課金', 'ガチャ課金'), ('通信費', '通信費'), ('交際費', '交際費'), ('交通費', '交通費'), ('家賃', '家賃'), ('その他', 'その他')], max_length=100, verbose_name='カテゴリ'),
        ),
        migrations.CreateModel(
            name='BalanceDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='詳細')),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='app.Balance', verbose_name='名前')),
            ],
        ),
    ]
