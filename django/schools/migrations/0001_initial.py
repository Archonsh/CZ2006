# Generated by Django 2.0.2 on 2018-03-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kindergarten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Centre Name')),
                ('isoperation', models.BooleanField(default=True, verbose_name='Operation Status')),
                ('type', models.CharField(max_length=50, verbose_name='Kindergarten Type')),
                ('address', models.CharField(max_length=100, verbose_name='Centre Address')),
                ('postalcode', models.IntegerField(verbose_name='Postal Code')),
                ('email', models.EmailField(max_length=254, verbose_name='Centre Email Address')),
                ('website', models.CharField(max_length=100, verbose_name='Website')),
                ('number', models.IntegerField(verbose_name='Centre Contact Number')),
                ('facebook', models.CharField(max_length=100, verbose_name='Facebook')),
                ('capacity', models.IntegerField(verbose_name='Accomodation Capacity')),
                ('outdoor', models.BooleanField(verbose_name='Provision of outdoor playground/garden')),
                ('bus', models.BooleanField(verbose_name='Bus Service')),
                ('sparkCer', models.BooleanField(verbose_name='SPARK Certified')),
                ('sparkvalidity', models.CharField(max_length=100, verbose_name='SPARK Validity (end)')),
                ('registrationfee', models.CharField(max_length=10, verbose_name='Registration Fees')),
                ('k2fee', models.CharField(max_length=10, verbose_name='Kindergarten Two Fees')),
                ('k1fee', models.CharField(max_length=10, verbose_name='Kindergarten One Fees')),
                ('nurseryfee', models.CharField(max_length=10, verbose_name='Nursery Fees')),
                ('prenurseryfee', models.CharField(max_length=10, verbose_name='Pre-Nursery Fees')),
                ('playgroupfee', models.CharField(max_length=10, verbose_name='Playgroup Fees')),
            ],
            options={
                'verbose_name': 'Kindergarten',
                'verbose_name_plural': 'Kindergarten',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Chinese', 'Chinese'), ('Tamil', 'Tamil'), ('Hindi', 'Hindi'), ('Malay', 'Malay'), ('Arabic', 'Arabic')], max_length=20, verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre_name', models.CharField(max_length=100, verbose_name='Centre Name')),
                ('centre_code', models.CharField(max_length=20, verbose_name='Centre Code')),
                ('program_hours', models.CharField(max_length=100, verbose_name='Program Hour')),
                ('vacancy', models.BooleanField(default=False, verbose_name='Vacancy Available')),
                ('registration_fee', models.FloatField(verbose_name='Registration Fee')),
                ('fee', models.FloatField(verbose_name='Fees')),
                ('level', models.CharField(choices=[('Playgroup', 'Playgroup'), ('Pre-Nursery', 'Pre-Nursery'), ('Kindergarten 1', 'Kindergarten 1'), ('Kindergarten 2', 'Kindergarten 2'), ('Nursery', 'Nursery')], default='', max_length=20, verbose_name='Level')),
                ('language', models.CharField(choices=[('Chinese', 'Chinese'), ('Tamil', 'Tamil'), ('Hindi', 'Hindi'), ('Malay', 'Malay'), ('Arabic', 'Arabic')], default='', max_length=20, verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Kindergarten',
                'verbose_name_plural': 'Kindergartens',
            },
        ),
        migrations.AddField(
            model_name='kindergarten',
            name='language',
            field=models.ManyToManyField(to='schools.Language', verbose_name='Language Offered'),
        ),
    ]
