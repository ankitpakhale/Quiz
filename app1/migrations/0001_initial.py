# Generated by Django 3.0 on 2022-04-02 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfCategory', models.CharField(blank=True, max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='registerform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('worng', models.PositiveIntegerField(default=0)),
                ('right', models.PositiveIntegerField(default=0)),
                ('marks', models.FloatField(default=0.0)),
                ('total', models.PositiveIntegerField(default=0)),
                ('score', models.PositiveIntegerField(default=0)),
                ('exam_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='signupform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('confirm_pwd', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Worng Answer 1')),
                ('option2', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Worng Answer 2')),
                ('option3', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Worng Answer 3')),
                ('option4', models.CharField(blank=True, default='', max_length=280, null=True, verbose_name='Worng Answer 4')),
                ('ans', models.CharField(blank=True, default='', max_length=280, verbose_name='Answer')),
                ('categoryName', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
