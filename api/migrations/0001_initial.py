# Generated by Django 2.0.6 on 2020-07-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emploee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(default='pic/right.jpg', upload_to='pic')),
                ('salary', models.IntegerField()),
                ('age', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'db_table': 'emp_emplist',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('real_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('sex', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'emp_user',
            },
        ),
    ]
