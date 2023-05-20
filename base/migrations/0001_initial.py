# Generated by Django 4.2.1 on 2023-05-20 13:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commandNumber', models.PositiveIntegerField(default=1)),
                ('clientNumber', models.PositiveIntegerField(default=0)),
                ('status', models.TextField(default='')),
                ('date_cmd', models.DateField(default=django.utils.timezone.now)),
                ('quality', models.PositiveSmallIntegerField(default=1)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'command',
                'db_table': 'command',
                'ordering': ['-date_cmd'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('label', models.CharField(default='', max_length=20)),
                ('price', models.FloatField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/product_image')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='DeliveryInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendingNumber', models.PositiveIntegerField(default=1)),
                ('Type', models.CharField(default='', max_length=20)),
                ('Price', models.FloatField(default=0.0)),
                ('destination', models.TextField(default='Rue, la ville , code de postal')),
                ('commad', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.command')),
            ],
            options={
                'db_table': 'delivery information',
            },
        ),
        migrations.CreateModel(
            name='CommandDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commandNumber', models.PositiveIntegerField(default=0)),
                ('productNumber', models.PositiveIntegerField(default=0)),
                ('productName', models.CharField(default='', max_length=20)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('unitPrice', models.FloatField(default=0.0)),
                ('totalPrice', models.FloatField(default=0.0)),
                ('commad', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.command')),
            ],
            options={
                'db_table': 'command details',
            },
        ),
        migrations.AddField(
            model_name='command',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.product'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(default='', max_length=20)),
                ('categoryDescription', models.CharField(default='', max_length=100)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
