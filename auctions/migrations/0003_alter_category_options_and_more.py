# Generated by Django 4.1.1 on 2022-09-23 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_item',)},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_list',
            new_name='category_item',
        ),
    ]
