# Generated by Django 2.2.8 on 2019-12-22 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0004_remove_postmodel_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='user_app.UserModel'),
        ),
    ]
