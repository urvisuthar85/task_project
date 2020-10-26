# Generated by Django 3.1.2 on 2020-10-26 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsrRegModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_name', models.CharField(max_length=500)),
                ('usr_email', models.CharField(blank=True, max_length=500, null=True)),
                ('usr_email_password', models.CharField(blank=True, max_length=500, null=True)),
                ('usr_ph_otp', models.PositiveIntegerField(blank=True, max_length=6, null=True)),
                ('usr_email_otp', models.PositiveIntegerField(blank=True, max_length=6, null=True)),
                ('root_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
