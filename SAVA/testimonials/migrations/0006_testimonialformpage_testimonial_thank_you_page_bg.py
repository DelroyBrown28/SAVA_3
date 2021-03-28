# Generated by Django 3.1.7 on 2021-03-27 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('testimonials', '0005_testimonialformpage_testimonial_form_page_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialformpage',
            name='testimonial_thank_you_page_bg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
