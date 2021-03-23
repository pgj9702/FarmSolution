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
