# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApibdtutoriasAlmuno(models.Model):
    id = models.BigAutoField(primary_key=True)
    matricula = models.IntegerField(db_column='Matricula')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=70)  # Field name made lowercase.
    totorf = models.ForeignKey('ApibdtutoriasTutorrep', models.DO_NOTHING, db_column='TotorF_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apibdtutorias_almuno'


class ApibdtutoriasHorasalumno(models.Model):
    id = models.BigAutoField(primary_key=True)
    matricula = models.IntegerField(db_column='Matricula')  # Field name made lowercase.
    tutoragrupal = models.CharField(db_column='Tutor�aGrupal', max_length=45)  # Field name made lowercase.
    tutoraindividua = models.CharField(db_column='Tutor�aIndividua', max_length=45)  # Field name made lowercase.
    estudiantescanalizadosenelsemestre = models.CharField(db_column='EstudiantesCanalizadosEnElSemestre', max_length=45)  # Field name made lowercase.
    totalhorasacumuladas = models.CharField(db_column='TotalHorasAcumuladas', max_length=45)  # Field name made lowercase.
    reacanalizada = models.CharField(db_column='�reaCanalizada', max_length=45)  # Field name made lowercase.
    alumnof = models.ForeignKey(ApibdtutoriasAlmuno, models.DO_NOTHING, db_column='AlumnoF_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apibdtutorias_horasalumno'


class ApibdtutoriasTutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    rfc = models.CharField(max_length=13)
    periodo = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'apibdtutorias_tutor'


class ApibdtutoriasTutorrep(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=70)  # Field name made lowercase.
    fecha = models.CharField(max_length=50)
    programaeducativo = models.CharField(db_column='ProgramaEducativo', max_length=45)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=45)  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apibdtutorias_tutorrep'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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
