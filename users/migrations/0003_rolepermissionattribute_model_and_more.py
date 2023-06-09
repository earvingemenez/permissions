# Generated by Django 4.1 on 2023-04-30 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0002_user_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolepermissionattribute',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='rolepermissionattribute',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_perm_attrs', to='users.rolepermissionattribute'),
        ),
    ]
