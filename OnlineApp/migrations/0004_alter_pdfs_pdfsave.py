# Generated by Django 3.2.13 on 2022-06-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineApp', '0003_pdfs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfs',
            name='PDFSave',
            field=models.FileField(null=True, upload_to='SECUPDF/', verbose_name=''),
        ),
    ]
