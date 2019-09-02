# Generated by Django 2.2.4 on 2019-09-02 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shieldServer', '0005_merge_20190829_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower',
            name='borrower_sum',
        ),
        migrations.AddField(
            model_name='borrower',
            name='annual_income',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='borrower',
            name='application_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='borrower',
            name='collect_attention',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='borrower',
            name='delinq_2yrs',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='borrower',
            name='dti',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='borrower',
            name='emp_length',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='borrower',
            name='emp_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='borrower',
            name='funded_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='borrower',
            name='grade',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='borrower',
            name='home_ownership',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='borrower',
            name='installment',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='borrower',
            name='last_pymnt_amnt',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='borrower',
            name='last_pymnt_d',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrower',
            name='loan_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='borrower',
            name='loan_status',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='borrower',
            name='out_prncp',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrower',
            name='purpose',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='borrower',
            name='rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='borrower',
            name='total_pymnt',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrower',
            name='total_rec_late_fee',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrower',
            name='vertification_status',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
