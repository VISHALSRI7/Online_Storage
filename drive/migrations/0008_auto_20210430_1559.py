# Generated by Django 3.1.7 on 2021-04-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0007_auto_20210430_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_model',
            name='file_name',
            field=models.CharField(max_length=245, null=True),
        ),
    ]
