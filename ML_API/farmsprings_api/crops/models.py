from django.db import models


class Apple(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apple'


class AppleProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'apple_prod_area'


class AppleSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'apple_seg'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cabbage(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cabbage'


class CabbageProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'cabbage_prod_area'


class CabbageSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'cabbage_seg'


class Carrot(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'carrot'


class CarrotProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'carrot_prod_area'


class CarrotSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'carrot_seg'


class Chili(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chili'


class ChiliProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'chili_prod_area'


class ChiliSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'chili_seg'


class Chives(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chives'


class ChivesProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'chives_prod_area'


class ChivesSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'chives_seg'


class DaikonFall(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daikon_fall'


class DaikonFallProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'daikon_fall_prod_area'


class DaikonFallSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'daikon_fall_seg'


class DaikonHighland(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daikon_highland'


class DaikonHighlandProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'daikon_highland_prod_area'


class DaikonHighlandSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'daikon_highland_seg'


class DaikonSpring(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daikon_spring'


class DaikonSpringProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'daikon_spring_prod_area'


class DaikonSpringSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'daikon_spring_seg'


class DaikonWinter(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daikon_winter'


class DaikonWinterProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'daikon_winter_prod_area'


class DaikonWinterSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'daikon_winter_seg'


class Dangam(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dangam'


class DangamProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'dangam_prod_area'


class DangamSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'dangam_seg'


class DataPredict(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    crop = models.CharField(max_length=20)
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_predict'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gamgul(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gamgul'


class GamgulProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'gamgul_prod_area'


class GamgulSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'gamgul_seg'


class Garlic(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garlic'


class GarlicProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'garlic_prod_area'


class GarlicSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'garlic_seg'


class Ginger(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ginger'


class GingerProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'ginger_prod_area'


class GingerSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ginger_seg'


class Grape(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grape'


class GrapeProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'grape_prod_area'


class GrapeSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'grape_seg'


class Largeonion(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'largeonion'


class LargeonionProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'largeonion_prod_area'


class LargeonionSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'largeonion_seg'


class NapacabbageFall(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'napacabbage_fall'


class NapacabbageFallProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'napacabbage_fall_prod_area'


class NapacabbageFallSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'napacabbage_fall_seg'


class NapacabbageHighland(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'napacabbage_highland'


class NapacabbageHighlandProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'napacabbage_highland_prod_area'


class NapacabbageHighlandSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'napacabbage_highland_seg'


class NapacabbageSpring(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'napacabbage_spring'


class NapacabbageSpringProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'napacabbage_spring_prod_area'


class NapacabbageSpringSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'napacabbage_spring_seg'


class NapacabbageWinter(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'napacabbage_winter'


class NapacabbageWinterProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'napacabbage_winter_prod_area'


class NapacabbageWinterSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'napacabbage_winter_seg'


class Onion(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'onion'


class OnionProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'onion_prod_area'


class OnionSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'onion_seg'


class Peach(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peach'


class PeachProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'peach_prod_area'


class PeachSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'peach_seg'


class Peanut(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peanut'


class PeanutProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'peanut_prod_area'


class PeanutSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'peanut_seg'


class Pear(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pear'


class PearProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'pear_prod_area'


class PearSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'pear_seg'


class PotatoFall(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'potato_fall'


class PotatoFallProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'potato_fall_prod_area'


class PotatoFallSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'potato_fall_seg'


class PotatoHighland(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'potato_highland'


class PotatoHighlandProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'potato_highland_prod_area'


class PotatoHighlandSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'potato_highland_seg'


class PotatoSpring(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'potato_spring'


class PotatoSpringProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'potato_spring_prod_area'


class PotatoSpringSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'potato_spring_seg'


class SegDataPredict(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    crop = models.CharField(max_length=20)
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'seg_data_predict'


class Sesame(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sesame'


class SesameProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'sesame_prod_area'


class SesameSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'sesame_seg'


class Spinach(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    avgta = models.DecimalField(db_column='avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minta = models.DecimalField(db_column='minTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxta = models.DecimalField(db_column='maxTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxrn = models.DecimalField(db_column='hr1MaxRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meanrn = models.DecimalField(db_column='meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumrn = models.DecimalField(db_column='sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxinsws = models.DecimalField(db_column='maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    maxws = models.DecimalField(db_column='maxWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgws = models.DecimalField(db_column='avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr24sumrws = models.DecimalField(db_column='hr24SumRws', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgtd = models.DecimalField(db_column='avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    minrhm = models.DecimalField(db_column='minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgrhm = models.DecimalField(db_column='avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpv = models.DecimalField(db_column='avgPv', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgpa = models.DecimalField(db_column='avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ssdur = models.DecimalField(db_column='ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumsshr = models.DecimalField(db_column='sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    hr1maxicsr = models.DecimalField(db_column='hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    sumgsr = models.DecimalField(db_column='sumGsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmefs = models.DecimalField(db_column='ddMefs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    ddmes = models.DecimalField(db_column='ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgts = models.DecimalField(db_column='avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    mintg = models.DecimalField(db_column='minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm5te = models.DecimalField(db_column='avgCm5Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm10te = models.DecimalField(db_column='avgCm10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm20te = models.DecimalField(db_column='avgCm20Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgcm30te = models.DecimalField(db_column='avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm05te = models.DecimalField(db_column='avgM05Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm10te = models.DecimalField(db_column='avgM10Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm15te = models.DecimalField(db_column='avgM15Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm30te = models.DecimalField(db_column='avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    avgm50te = models.DecimalField(db_column='avgM50Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    meandtr = models.DecimalField(db_column='meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase.
    numwdtr = models.IntegerField(db_column='numWdtr', blank=True, null=True)  # Field name made lowercase.
    numtyp = models.IntegerField(db_column='numTyp', blank=True, null=True)  # Field name made lowercase.
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    sumcw = models.IntegerField(db_column='sumCw', blank=True, null=True)  # Field name made lowercase.
    sumhw = models.IntegerField(db_column='sumHw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spinach'


class SpinachProdArea(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    prod_per_area = models.DecimalField(max_digits=20, decimal_places=15)

    class Meta:
        managed = False
        db_table = 'spinach_prod_area'


class SpinachSeg(models.Model):
    idx = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    year = models.IntegerField()
    prod = models.IntegerField()
    area = models.DecimalField(max_digits=20, decimal_places=15)
    numimpt = models.IntegerField(db_column='numImpT', blank=True, null=True)  # Field name made lowercase.
    number_1_sumrn = models.DecimalField(db_column='1_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumrn = models.DecimalField(db_column='2_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumrn = models.DecimalField(db_column='3_sumRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgta = models.DecimalField(db_column='1_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meanrn = models.DecimalField(db_column='1_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_maxinsws = models.DecimalField(db_column='1_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgws = models.DecimalField(db_column='1_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgtd = models.DecimalField(db_column='1_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_minrhm = models.DecimalField(db_column='1_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgrhm = models.DecimalField(db_column='1_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgpa = models.DecimalField(db_column='1_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ssdur = models.DecimalField(db_column='1_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumsshr = models.DecimalField(db_column='1_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_hr1maxicsr = models.DecimalField(db_column='1_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_ddmes = models.DecimalField(db_column='1_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgts = models.DecimalField(db_column='1_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_mintg = models.DecimalField(db_column='1_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgcm30te = models.DecimalField(db_column='1_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_avgm30te = models.DecimalField(db_column='1_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgta = models.DecimalField(db_column='2_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meanrn = models.DecimalField(db_column='2_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_maxinsws = models.DecimalField(db_column='2_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgws = models.DecimalField(db_column='2_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgtd = models.DecimalField(db_column='2_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_minrhm = models.DecimalField(db_column='2_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgrhm = models.DecimalField(db_column='2_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgpa = models.DecimalField(db_column='2_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ssdur = models.DecimalField(db_column='2_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumsshr = models.DecimalField(db_column='2_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_hr1maxicsr = models.DecimalField(db_column='2_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_ddmes = models.DecimalField(db_column='2_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgts = models.DecimalField(db_column='2_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_mintg = models.DecimalField(db_column='2_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgcm30te = models.DecimalField(db_column='2_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_avgm30te = models.DecimalField(db_column='2_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgta = models.DecimalField(db_column='3_avgTa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meanrn = models.DecimalField(db_column='3_meanRn', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_maxinsws = models.DecimalField(db_column='3_maxInsWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgws = models.DecimalField(db_column='3_avgWs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgtd = models.DecimalField(db_column='3_avgTd', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_minrhm = models.DecimalField(db_column='3_minRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgrhm = models.DecimalField(db_column='3_avgRhm', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgpa = models.DecimalField(db_column='3_avgPa', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ssdur = models.DecimalField(db_column='3_ssDur', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumsshr = models.DecimalField(db_column='3_sumSsHr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_hr1maxicsr = models.DecimalField(db_column='3_hr1MaxIcsr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_ddmes = models.DecimalField(db_column='3_ddMes', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgts = models.DecimalField(db_column='3_avgTs', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_mintg = models.DecimalField(db_column='3_minTg', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgcm30te = models.DecimalField(db_column='3_avgCm30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_avgm30te = models.DecimalField(db_column='3_avgM30Te', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_meandtr = models.DecimalField(db_column='1_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_meandtr = models.DecimalField(db_column='2_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_meandtr = models.DecimalField(db_column='3_meanDtr', max_digits=20, decimal_places=15, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_numwdtr = models.IntegerField(db_column='1_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_numwdtr = models.IntegerField(db_column='2_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_numwdtr = models.IntegerField(db_column='3_numWdtr', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumcw = models.IntegerField(db_column='1_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumcw = models.IntegerField(db_column='2_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumcw = models.IntegerField(db_column='3_sumCw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1_sumhw = models.IntegerField(db_column='1_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2_sumhw = models.IntegerField(db_column='2_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3_sumhw = models.IntegerField(db_column='3_sumHw', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'spinach_seg'