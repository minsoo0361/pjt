# Generated by Django 4.2.8 on 2024-05-22 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anonymous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_one', models.BooleanField(default=False)),
                ('gen_two', models.BooleanField(default=False)),
                ('age_one', models.BooleanField(default=False)),
                ('age_two', models.BooleanField(default=False)),
                ('age_thr', models.BooleanField(default=False)),
                ('age_fou', models.BooleanField(default=False)),
                ('age_fiv', models.BooleanField(default=False)),
                ('age_six', models.BooleanField(default=False)),
                ('sal_one', models.BooleanField(default=False)),
                ('sal_two', models.BooleanField(default=False)),
                ('sal_thr', models.BooleanField(default=False)),
                ('sal_fou', models.BooleanField(default=False)),
                ('sal_fiv', models.BooleanField(default=False)),
                ('sal_six', models.BooleanField(default=False)),
                ('whl_one', models.BooleanField(default=False)),
                ('whl_two', models.BooleanField(default=False)),
                ('whl_thr', models.BooleanField(default=False)),
                ('whl_fou', models.BooleanField(default=False)),
                ('whl_five', models.BooleanField(default=False)),
                ('whl_six', models.BooleanField(default=False)),
                ('ten_one', models.BooleanField(default=False)),
                ('ten_two', models.BooleanField(default=False)),
                ('ten_thr', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('isFavorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SaveProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('max_limit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SaveOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100, null=True)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(default=-1, null=True)),
                ('rsv_type', models.CharField(max_length=100, null=True)),
                ('rsrv_type_nm', models.CharField(max_length=100, null=True)),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save_options', to='finlife.saveproducts')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100, null=True)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(default=-1, null=True)),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='finlife.depositproducts')),
            ],
        ),
    ]
