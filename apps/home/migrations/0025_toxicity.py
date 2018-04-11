# Generated by Django 2.0.4 on 2018-04-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_delete_toxicity'),
    ]

    operations = [
        migrations.CreateModel(
            name='toxicity',
            fields=[
                ('m4id', models.AutoField(primary_key=True, serialize=False)),
                ('m5id', models.IntegerField()),
                ('spid', models.CharField(max_length=50)),
                ('stkc', models.IntegerField()),
                ('stkc_unit', models.CharField(max_length=50)),
                ('tested_conc_unit', models.CharField(max_length=50)),
                ('spid_legacy', models.CharField(max_length=50)),
                ('chid', models.IntegerField()),
                ('casn', models.CharField(max_length=50)),
                ('chnm', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('aeid', models.IntegerField()),
                ('aenm', models.CharField(max_length=50)),
                ('resp_unit', models.CharField(max_length=50)),
                ('nconc', models.IntegerField()),
                ('npts', models.IntegerField()),
                ('nrep', models.IntegerField()),
                ('nmed_gtbl', models.IntegerField()),
                ('hitc', models.IntegerField()),
                ('modl', models.CharField(max_length=50)),
                ('fitc', models.IntegerField()),
                ('coff', models.FloatField()),
                ('bmad', models.FloatField()),
                ('gsid_rep', models.IntegerField()),
                ('chit', models.CharField(max_length=50)),
                ('flag_ids', models.IntegerField()),
                ('flags', models.CharField(max_length=50)),
                ('resp_max', models.FloatField()),
                ('resp_min', models.FloatField()),
                ('max_mean', models.FloatField()),
                ('max_mean_conc', models.FloatField()),
                ('max_med', models.FloatField()),
                ('max_med_conc', models.FloatField()),
                ('logc_max', models.FloatField()),
                ('logc_min', models.FloatField()),
                ('actp', models.FloatField()),
                ('modl_er', models.FloatField()),
                ('modl_tp', models.FloatField()),
                ('modl_ga', models.FloatField()),
                ('modl_gw', models.FloatField()),
                ('modl_la', models.FloatField()),
                ('modl_lw', models.FloatField()),
                ('modl_rmse', models.FloatField()),
                ('modl_prob', models.FloatField()),
                ('modl_acc', models.FloatField()),
                ('modl_acb', models.FloatField()),
                ('cnst', models.IntegerField()),
                ('hill', models.IntegerField()),
                ('hcov', models.IntegerField()),
                ('gnls', models.IntegerField()),
                ('gcov', models.IntegerField()),
                ('cnst_er', models.FloatField()),
                ('cnst_aic', models.FloatField()),
                ('cnst_rmse', models.FloatField()),
                ('cnst_prob', models.CharField(max_length=50)),
                ('hill_tp', models.FloatField()),
                ('hill_tp_sd', models.FloatField()),
                ('hill_ga', models.FloatField()),
                ('hill_ga_sd', models.FloatField()),
                ('hill_gw', models.FloatField()),
                ('hill_gw_sd', models.FloatField()),
                ('hill_er', models.FloatField()),
                ('hill_er_sd', models.FloatField()),
                ('hill_aic', models.FloatField()),
                ('hill_rmse', models.FloatField()),
                ('hill_prob', models.FloatField()),
                ('gnls_tp', models.FloatField()),
                ('gnls_tp_sd', models.FloatField()),
                ('gnls_ga', models.FloatField()),
                ('gnls_ga_sd', models.FloatField()),
                ('gnls_gw', models.FloatField()),
                ('gnls_gw_sd', models.FloatField()),
                ('gnls_la', models.FloatField()),
                ('gnls_la_sd', models.FloatField()),
                ('gnls_lw', models.FloatField()),
                ('gnls_lw_sd', models.FloatField()),
                ('gnls_er', models.FloatField()),
                ('gnls_er_sd', models.FloatField()),
                ('gnls_aic', models.FloatField()),
                ('gnls_rmse', models.FloatField()),
                ('gnls_prob', models.FloatField()),
            ],
        ),
    ]
