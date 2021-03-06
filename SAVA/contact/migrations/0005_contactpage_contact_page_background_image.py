# Generated by Django 3.1.7 on 2021-03-29 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('contact', '0004_remove_contactpage_form_blurb'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='contact_page_background_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
