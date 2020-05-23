# Generated by Django 3.0.5 on 2020-05-23 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('product', '0006_auto_20200519_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=15)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_orderd', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='shoppingcart.OrderItem', verbose_name='item')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile', verbose_name='owner')),
            ],
        ),
    ]