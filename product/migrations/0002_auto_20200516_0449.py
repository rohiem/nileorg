# Generated by Django 3.0.5 on 2020-05-16 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProductImage',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='price'),
        ),
    ]