# Generated by Django 3.1.7 on 2021-03-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0003_appleprodarea_appleseg_cabbageprodarea_cabbageseg_carrotprodarea_carrotseg_chiliprodarea_chiliseg_ch'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPredict',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=20)),
                ('crop', models.CharField(max_length=20)),
                ('area', models.DecimalField(decimal_places=15, max_digits=20)),
                ('avgta', models.DecimalField(blank=True, db_column='avgTa', decimal_places=15, max_digits=20, null=True)),
                ('minta', models.DecimalField(blank=True, db_column='minTa', decimal_places=15, max_digits=20, null=True)),
                ('maxta', models.DecimalField(blank=True, db_column='maxTa', decimal_places=15, max_digits=20, null=True)),
                ('hr1maxrn', models.DecimalField(blank=True, db_column='hr1MaxRn', decimal_places=15, max_digits=20, null=True)),
                ('meanrn', models.DecimalField(blank=True, db_column='meanRn', decimal_places=15, max_digits=20, null=True)),
                ('sumrn', models.DecimalField(blank=True, db_column='sumRn', decimal_places=15, max_digits=20, null=True)),
                ('maxinsws', models.DecimalField(blank=True, db_column='maxInsWs', decimal_places=15, max_digits=20, null=True)),
                ('maxws', models.DecimalField(blank=True, db_column='maxWs', decimal_places=15, max_digits=20, null=True)),
                ('avgws', models.DecimalField(blank=True, db_column='avgWs', decimal_places=15, max_digits=20, null=True)),
                ('hr24sumrws', models.DecimalField(blank=True, db_column='hr24SumRws', decimal_places=15, max_digits=20, null=True)),
                ('avgtd', models.DecimalField(blank=True, db_column='avgTd', decimal_places=15, max_digits=20, null=True)),
                ('minrhm', models.DecimalField(blank=True, db_column='minRhm', decimal_places=15, max_digits=20, null=True)),
                ('avgrhm', models.DecimalField(blank=True, db_column='avgRhm', decimal_places=15, max_digits=20, null=True)),
                ('avgpv', models.DecimalField(blank=True, db_column='avgPv', decimal_places=15, max_digits=20, null=True)),
                ('avgpa', models.DecimalField(blank=True, db_column='avgPa', decimal_places=15, max_digits=20, null=True)),
                ('ssdur', models.DecimalField(blank=True, db_column='ssDur', decimal_places=15, max_digits=20, null=True)),
                ('sumsshr', models.DecimalField(blank=True, db_column='sumSsHr', decimal_places=15, max_digits=20, null=True)),
                ('hr1maxicsr', models.DecimalField(blank=True, db_column='hr1MaxIcsr', decimal_places=15, max_digits=20, null=True)),
                ('sumgsr', models.DecimalField(blank=True, db_column='sumGsr', decimal_places=15, max_digits=20, null=True)),
                ('ddmefs', models.DecimalField(blank=True, db_column='ddMefs', decimal_places=15, max_digits=20, null=True)),
                ('ddmes', models.DecimalField(blank=True, db_column='ddMes', decimal_places=15, max_digits=20, null=True)),
                ('avgts', models.DecimalField(blank=True, db_column='avgTs', decimal_places=15, max_digits=20, null=True)),
                ('mintg', models.DecimalField(blank=True, db_column='minTg', decimal_places=15, max_digits=20, null=True)),
                ('avgcm5te', models.DecimalField(blank=True, db_column='avgCm5Te', decimal_places=15, max_digits=20, null=True)),
                ('avgcm10te', models.DecimalField(blank=True, db_column='avgCm10Te', decimal_places=15, max_digits=20, null=True)),
                ('avgcm20te', models.DecimalField(blank=True, db_column='avgCm20Te', decimal_places=15, max_digits=20, null=True)),
                ('avgcm30te', models.DecimalField(blank=True, db_column='avgCm30Te', decimal_places=15, max_digits=20, null=True)),
                ('avgm05te', models.DecimalField(blank=True, db_column='avgM05Te', decimal_places=15, max_digits=20, null=True)),
                ('avgm10te', models.DecimalField(blank=True, db_column='avgM10Te', decimal_places=15, max_digits=20, null=True)),
                ('avgm15te', models.DecimalField(blank=True, db_column='avgM15Te', decimal_places=15, max_digits=20, null=True)),
                ('avgm30te', models.DecimalField(blank=True, db_column='avgM30Te', decimal_places=15, max_digits=20, null=True)),
                ('avgm50te', models.DecimalField(blank=True, db_column='avgM50Te', decimal_places=15, max_digits=20, null=True)),
                ('meandtr', models.DecimalField(blank=True, db_column='meanDtr', decimal_places=15, max_digits=20, null=True)),
                ('numwdtr', models.IntegerField(blank=True, db_column='numWdtr', null=True)),
                ('numtyp', models.IntegerField(blank=True, db_column='numTyp', null=True)),
                ('numimpt', models.IntegerField(blank=True, db_column='numImpT', null=True)),
                ('sumcw', models.IntegerField(blank=True, db_column='sumCw', null=True)),
                ('sumhw', models.IntegerField(blank=True, db_column='sumHw', null=True)),
            ],
            options={
                'db_table': 'data_predict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SegDataPredict',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=20)),
                ('crop', models.CharField(max_length=20)),
                ('area', models.DecimalField(decimal_places=15, max_digits=20)),
                ('numimpt', models.IntegerField(blank=True, db_column='numImpT', null=True)),
                ('number_1_sumrn', models.DecimalField(blank=True, db_column='1_sumRn', decimal_places=15, max_digits=20, null=True)),
                ('number_2_sumrn', models.DecimalField(blank=True, db_column='2_sumRn', decimal_places=15, max_digits=20, null=True)),
                ('number_3_sumrn', models.DecimalField(blank=True, db_column='3_sumRn', decimal_places=15, max_digits=20, null=True)),
                ('number_1_avgta', models.DecimalField(blank=True, db_column='1_avgTa', decimal_places=15, max_digits=20, null=True)),
                ('number_1_meanrn', models.DecimalField(blank=True, db_column='1_meanRn', decimal_places=15, max_digits=20, null=True)),
                ('number_1_maxinsws', models.DecimalField(blank=True, db_column='1_maxInsWs', decimal_places=15, max_digits=20, null=True)),
                ('number_1_avgws', models.DecimalField(blank=True, db_column='1_avgWs', decimal_places=15, max_digits=20, null=True)),
                ('number_1_avgtd', models.DecimalField(blank=True, db_column='1_avgTd', decimal_places=15, max_digits=20, null=True)),
                ('number_1_minrhm', models.DecimalField(blank=True, db_column='1_minRhm', decimal_places=15, max_digits=20, null=True)),
                ('number_1_avgrhm', models.DecimalField(blank=True, db_column='1_avgRhm', decimal_places=15, max_digits=20, null=True)),
                ('number_1_avgpa', models.DecimalField(blank=True, db_column='1_avgPa', decimal_places=15, max_digits=20, null=True)),
                ('number_1_ssdur', models.DecimalField(blank=True, db_column='1_ssDur', decimal_places=15, max_digits=20, null=True)),
                ('number_1_sumsshr', models.DecimalField(blank=True, db_column='1_sumSsHr', decimal_places=15, max_digits=20, null=True)),
                ('number_1_hr1maxicsr', models.DecimalField(blank=True, db_column='1_hr1MaxIcsr', decimal_places=15, max_digits=20, null=True)),
                ('number_1_ddmes', models.DecimalField(blank=True, db_column='1_ddMes', decimal_places=15, max_digits=20, null=True)),
                ('number_1_avgts', models.DecimalField(blank=True, db_column='1_avgTs', decimal_places=15, max_digits=20, null=True)),
                ('number_1_mintg', models.DecimalField(blank=True, db_column='1_minTg', decimal_places=15, max_digits=20, null=True)),
                ('number_1_avgcm30te', models.DecimalField(blank=True, db_column='1_avgCm30Te', decimal_places=15, max_digits=20, null=True)),
                ('number_1_avgm30te', models.DecimalField(blank=True, db_column='1_avgM30Te', decimal_places=15, max_digits=20, null=True)),
                ('number_2_avgta', models.DecimalField(blank=True, db_column='2_avgTa', decimal_places=15, max_digits=20, null=True)),
                ('number_2_meanrn', models.DecimalField(blank=True, db_column='2_meanRn', decimal_places=15, max_digits=20, null=True)),
                ('number_2_maxinsws', models.DecimalField(blank=True, db_column='2_maxInsWs', decimal_places=15, max_digits=20, null=True)),
                ('number_2_avgws', models.DecimalField(blank=True, db_column='2_avgWs', decimal_places=15, max_digits=20, null=True)),
                ('number_2_avgtd', models.DecimalField(blank=True, db_column='2_avgTd', decimal_places=15, max_digits=20, null=True)),
                ('number_2_minrhm', models.DecimalField(blank=True, db_column='2_minRhm', decimal_places=15, max_digits=20, null=True)),
                ('number_2_avgrhm', models.DecimalField(blank=True, db_column='2_avgRhm', decimal_places=15, max_digits=20, null=True)),
                ('number_2_avgpa', models.DecimalField(blank=True, db_column='2_avgPa', decimal_places=15, max_digits=20, null=True)),
                ('number_2_ssdur', models.DecimalField(blank=True, db_column='2_ssDur', decimal_places=15, max_digits=20, null=True)),
                ('number_2_sumsshr', models.DecimalField(blank=True, db_column='2_sumSsHr', decimal_places=15, max_digits=20, null=True)),
                ('number_2_hr1maxicsr', models.DecimalField(blank=True, db_column='2_hr1MaxIcsr', decimal_places=15, max_digits=20, null=True)),
                ('number_2_ddmes', models.DecimalField(blank=True, db_column='2_ddMes', decimal_places=15, max_digits=20, null=True)),
                ('number_2_avgts', models.DecimalField(blank=True, db_column='2_avgTs', decimal_places=15, max_digits=20, null=True)),
                ('number_2_mintg', models.DecimalField(blank=True, db_column='2_minTg', decimal_places=15, max_digits=20, null=True)),
                ('number_2_avgcm30te', models.DecimalField(blank=True, db_column='2_avgCm30Te', decimal_places=15, max_digits=20, null=True)),
                ('number_2_avgm30te', models.DecimalField(blank=True, db_column='2_avgM30Te', decimal_places=15, max_digits=20, null=True)),
                ('number_3_avgta', models.DecimalField(blank=True, db_column='3_avgTa', decimal_places=15, max_digits=20, null=True)),
                ('number_3_meanrn', models.DecimalField(blank=True, db_column='3_meanRn', decimal_places=15, max_digits=20, null=True)),
                ('number_3_maxinsws', models.DecimalField(blank=True, db_column='3_maxInsWs', decimal_places=15, max_digits=20, null=True)),
                ('number_3_avgws', models.DecimalField(blank=True, db_column='3_avgWs', decimal_places=15, max_digits=20, null=True)),
                ('number_3_avgtd', models.DecimalField(blank=True, db_column='3_avgTd', decimal_places=15, max_digits=20, null=True)),
                ('number_3_minrhm', models.DecimalField(blank=True, db_column='3_minRhm', decimal_places=15, max_digits=20, null=True)),
                ('number_3_avgrhm', models.DecimalField(blank=True, db_column='3_avgRhm', decimal_places=15, max_digits=20, null=True)),
                ('number_3_avgpa', models.DecimalField(blank=True, db_column='3_avgPa', decimal_places=15, max_digits=20, null=True)),
                ('number_3_ssdur', models.DecimalField(blank=True, db_column='3_ssDur', decimal_places=15, max_digits=20, null=True)),
                ('number_3_sumsshr', models.DecimalField(blank=True, db_column='3_sumSsHr', decimal_places=15, max_digits=20, null=True)),
                ('number_3_hr1maxicsr', models.DecimalField(blank=True, db_column='3_hr1MaxIcsr', decimal_places=15, max_digits=20, null=True)),
                ('number_3_ddmes', models.DecimalField(blank=True, db_column='3_ddMes', decimal_places=15, max_digits=20, null=True)),
                ('number_3_avgts', models.DecimalField(blank=True, db_column='3_avgTs', decimal_places=15, max_digits=20, null=True)),
                ('number_3_mintg', models.DecimalField(blank=True, db_column='3_minTg', decimal_places=15, max_digits=20, null=True)),
                ('number_3_avgcm30te', models.DecimalField(blank=True, db_column='3_avgCm30Te', decimal_places=15, max_digits=20, null=True)),
                ('number_3_avgm30te', models.DecimalField(blank=True, db_column='3_avgM30Te', decimal_places=15, max_digits=20, null=True)),
                ('number_1_meandtr', models.DecimalField(blank=True, db_column='1_meanDtr', decimal_places=15, max_digits=20, null=True)),
                ('number_2_meandtr', models.DecimalField(blank=True, db_column='2_meanDtr', decimal_places=15, max_digits=20, null=True)),
                ('number_3_meandtr', models.DecimalField(blank=True, db_column='3_meanDtr', decimal_places=15, max_digits=20, null=True)),
                ('number_1_numwdtr', models.IntegerField(blank=True, db_column='1_numWdtr', null=True)),
                ('number_2_numwdtr', models.IntegerField(blank=True, db_column='2_numWdtr', null=True)),
                ('number_3_numwdtr', models.IntegerField(blank=True, db_column='3_numWdtr', null=True)),
                ('number_1_sumcw', models.IntegerField(blank=True, db_column='1_sumCw', null=True)),
                ('number_2_sumcw', models.IntegerField(blank=True, db_column='2_sumCw', null=True)),
                ('number_3_sumcw', models.IntegerField(blank=True, db_column='3_sumCw', null=True)),
                ('number_1_sumhw', models.IntegerField(blank=True, db_column='1_sumHw', null=True)),
                ('number_2_sumhw', models.IntegerField(blank=True, db_column='2_sumHw', null=True)),
                ('number_3_sumhw', models.IntegerField(blank=True, db_column='3_sumHw', null=True)),
            ],
            options={
                'db_table': 'seg_data_predict',
                'managed': False,
            },
        ),
    ]
