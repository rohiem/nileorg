# Generated by Django 3.0.5 on 2020-05-15 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50, verbose_name='category name')),
                ('categoryimg', models.ImageField(upload_to='category/', verbose_name='category img')),
                ('categorydesc', models.TextField(verbose_name='category desc')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='product name')),
                ('desc', models.TextField(verbose_name='product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='cost')),
                ('created', models.DateTimeField(verbose_name='created at')),
                ('prdbrand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.Brand')),
                ('prdcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductImage', models.ImageField(upload_to='product/', verbose_name='image')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodAlternatives', models.ManyToManyField(related_name='alternativeproducts', to='product.Product', verbose_name='product alters')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainproduct', to='product.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product Alternative',
                'verbose_name_plural': 'Product Alternatives',
            },
        ),
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodAccessories', models.ManyToManyField(related_name='alternativeaccproducts', to='product.Product', verbose_name='product accessories')),
                ('productac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainaccproduct', to='product.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product accessory',
                'verbose_name_plural': 'Product accessories',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='product category'),
        ),
        migrations.AddField(
            model_name='category',
            name='categoryparent',
            field=models.ForeignKey(blank=True, limit_choices_to={'categoryparent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='categorty parent'),
        ),
    ]
