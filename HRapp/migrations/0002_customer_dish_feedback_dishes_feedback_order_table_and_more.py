# Generated by Django 4.2.3 on 2023-07-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='dish_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_ratings', models.CharField(max_length=5)),
                ('review_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=50)),
                ('dish_status', models.BooleanField()),
                ('dish_image', models.ImageField(upload_to='images/dishes')),
                ('dish_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('total_cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu_status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='', upload_to='images/menus'),
        ),
    ]