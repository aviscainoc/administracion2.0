# Generated by Django 3.1.4 on 2021-01-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliacion',
            fields=[
                ('codigo', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=10)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechafin', models.DateTimeField(blank=True, db_column='fechaFin', null=True)),
                ('fechavalidacion', models.DateTimeField(blank=True, db_column='fechaValidacion', null=True)),
                ('comentariosaprobacion', models.CharField(blank=True, max_length=500, null=True)),
                ('urlcombprobante1', models.CharField(blank=True, max_length=200, null=True)),
                ('urlcombprobante2', models.CharField(blank=True, max_length=200, null=True)),
                ('costoafiliacion', models.FloatField()),
                ('pagonivel1', models.IntegerField(blank=True, null=True)),
                ('pagonivel2', models.IntegerField(blank=True, null=True)),
                ('cuentapagocomision', models.CharField(blank=True, max_length=100, null=True)),
                ('bancopagocomision', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'afiliacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
                ('icono', models.CharField(blank=True, max_length=200, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('esprincipal', models.IntegerField()),
                ('logo', models.CharField(blank=True, max_length=200, null=True)),
                ('tienehijos', models.IntegerField()),
                ('mall', models.IntegerField()),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoriaempresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('icono', models.CharField(blank=True, max_length=200, null=True)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('esprincipal', models.IntegerField()),
                ('logo', models.CharField(blank=True, max_length=200, null=True)),
                ('tienehijos', models.IntegerField()),
                ('esservicio', models.IntegerField()),
            ],
            options={
                'db_table': 'categoriaempresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('particionmes', models.CharField(max_length=10)),
                ('fechacompra', models.DateTimeField()),
                ('codigomotorizado', models.CharField(max_length=20)),
                ('fechadespachado', models.DateTimeField(blank=True, null=True)),
                ('codigoentregacliente', models.CharField(max_length=20)),
                ('iva', models.CharField(max_length=45)),
                ('subtotal', models.FloatField()),
                ('total', models.FloatField()),
                ('comisionventa', models.FloatField()),
                ('descuento', models.FloatField()),
                ('latitudentrega', models.FloatField()),
                ('longitudentrega', models.FloatField()),
                ('costoentrega', models.FloatField()),
                ('fechaentrega', models.DateTimeField(blank=True, null=True)),
                ('distanciaentrega', models.FloatField()),
                ('direccionentrega', models.CharField(max_length=200)),
                ('telefonocontactoentrega', models.CharField(max_length=12)),
                ('cedulafactura', models.CharField(max_length=20)),
                ('nombrefactura', models.CharField(max_length=100)),
                ('direccionfactura', models.CharField(max_length=200)),
                ('telefonofactura', models.CharField(blank=True, max_length=12, null=True)),
                ('despachado', models.IntegerField()),
                ('entregado', models.IntegerField()),
                ('reversado', models.IntegerField()),
                ('pagovendedor', models.IntegerField()),
                ('observacionescliente', models.CharField(blank=True, max_length=200, null=True)),
                ('referenciapago', models.CharField(blank=True, max_length=100, null=True)),
                ('direccionposible', models.CharField(blank=True, max_length=300, null=True)),
                ('metodopago', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=45)),
                ('idempresa', models.IntegerField()),
                ('fechareverso', models.DateTimeField(blank=True, null=True)),
                ('motivoreverso', models.CharField(blank=True, max_length=500, null=True)),
                ('diacompra', models.DateField()),
                ('idsucursal', models.IntegerField()),
                ('aceptacionvendedor', models.IntegerField(blank=True, null=True)),
                ('fechaaceptacionvendedor', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compradetalle',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('idcompra', models.BigIntegerField()),
                ('preciounitario', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('particionmes', models.CharField(max_length=10)),
                ('observacionescliente', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'compradetalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Creditcard',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=200)),
                ('transaction_reference', models.CharField(max_length=200)),
                ('bin', models.CharField(max_length=45)),
                ('binenmascarado', models.CharField(max_length=100)),
                ('expiry_month', models.IntegerField()),
                ('expiry_year', models.IntegerField()),
                ('message', models.CharField(max_length=45)),
                ('number', models.CharField(max_length=45)),
                ('origin', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('fechainicio', models.DateTimeField()),
                ('fechafin', models.DateTimeField()),
                ('imeiregistro', models.CharField(blank=True, max_length=50, null=True)),
                ('ipregistro', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'creditcard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activa', models.IntegerField()),
                ('codigo', models.CharField(max_length=200)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechaeliminacion', models.DateTimeField(blank=True, db_column='fechaEliminacion', null=True)),
                ('fechareclamacion', models.DateTimeField(blank=True, db_column='fechaReclamacion', null=True)),
                ('fechavalidez', models.DateTimeField(db_column='fechaValidez')),
                ('reclamado', models.IntegerField()),
                ('usuariovalidador', models.BigIntegerField(blank=True, db_column='usuarioValidador', null=True)),
                ('vecesreclamado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cupon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'dia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diaatencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaapertura', models.CharField(blank=True, db_column='horaApertura', max_length=10, null=True)),
                ('horacierre', models.CharField(blank=True, db_column='horaCierre', max_length=10, null=True)),
            ],
            options={
                'db_table': 'diaatencion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('eslogan', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechafin', models.DateTimeField(db_column='fechaFin')),
                ('nombre', models.CharField(max_length=100)),
                ('top', models.IntegerField()),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('urlbaner', models.CharField(blank=True, db_column='urlBaner', max_length=200, null=True)),
                ('urlfotoperfil', models.ImageField(blank=True, db_column='urlFotoPerfil', null=True, upload_to='ftperfil')),
                ('vecesvisitada', models.IntegerField(db_column='vecesVisitada')),
                ('web', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.CharField(blank=True, max_length=150, null=True)),
                ('estado', models.CharField(max_length=10)),
                ('comision', models.FloatField(blank=True, null=True)),
                ('servicios', models.IntegerField()),
                ('horaapertura', models.CharField(max_length=5)),
                ('horacierre', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresacategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
            ],
            options={
                'db_table': 'empresacategoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmpresaEmpresacategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'empresa_empresacategoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IdGen',
            fields=[
                ('gen_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('gen_val', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'id_gen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('esimagen', models.IntegerField(db_column='esImagen')),
                ('esprincipal', models.IntegerField(db_column='esPrincipal')),
                ('fechacreado', models.DateTimeField(db_column='fechaCreado')),
                ('fechamodificado', models.DateTimeField(blank=True, db_column='fechaModificado', null=True)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('thumb', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(max_length=100)),
                ('urlinterna', models.IntegerField(db_column='urlInterna')),
                ('web', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'multimedia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('notificacioncol', models.CharField(blank=True, max_length=45, null=True)),
                ('vista', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'notificacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('iva', models.FloatField()),
                ('numerofactura', models.CharField(blank=True, db_column='numeroFactura', max_length=45, null=True)),
                ('tienefactura', models.SmallIntegerField(db_column='tieneFactura')),
                ('urlfactura', models.CharField(blank=True, db_column='urlFactura', max_length=100, null=True)),
                ('valor', models.FloatField()),
            ],
            options={
                'db_table': 'pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pagocomisionafiliacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=200)),
                ('total', models.FloatField()),
                ('nivel', models.IntegerField()),
                ('fechapago', models.DateTimeField()),
                ('estado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'pagocomisionafiliacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('clave', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('fechavigente', models.DateTimeField(db_column='fechaVigente')),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechamodificacion', models.DateTimeField(db_column='fechaModificacion')),
                ('valor', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'parametros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Passwordrecover',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.IntegerField()),
                ('fechacaducidad', models.DateTimeField(db_column='fechaCaducidad')),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechaultimocorreoenviado', models.DateTimeField(blank=True, db_column='fechaUltimoCorreoEnviado', null=True)),
                ('fechauso', models.DateTimeField(blank=True, db_column='fechaUso', null=True)),
                ('token', models.CharField(max_length=200)),
                ('usado', models.IntegerField()),
                ('vecescorreoenviado', models.IntegerField(db_column='vecesCorreoEnviado')),
                ('verificationcode', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'passwordrecover',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Planpromo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=1000)),
                ('dias', models.IntegerField()),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('ganaciaporcomision', models.IntegerField(db_column='ganaciaPorComision')),
                ('nombre', models.CharField(max_length=200)),
                ('porcentajeganancia', models.FloatField(db_column='porcentajeGanancia')),
                ('precio', models.FloatField()),
                ('prioridad', models.IntegerField()),
            ],
            options={
                'db_table': 'planpromo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Precioafiliacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=10)),
                ('fechainicio', models.DateTimeField(db_column='fechaInicio')),
                ('fechafin', models.DateTimeField(db_column='fechaFin')),
                ('precio', models.FloatField()),
                ('precioreferido', models.IntegerField()),
            ],
            options={
                'db_table': 'precioafiliacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productocategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
            ],
            options={
                'db_table': 'productocategoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promocionproducto',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('comentarios', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(max_length=600)),
                ('esbaner', models.IntegerField(db_column='esBaner')),
                ('estado', models.CharField(max_length=10)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechafinenlaplataforma', models.DateTimeField(db_column='fechaFinEnLaPlataforma')),
                ('fechafinpromocion', models.DateTimeField(db_column='fechaFinPromocion')),
                ('fechainiciopromocion', models.DateTimeField(db_column='fechaInicioPromocion')),
                ('fechamodificacion', models.DateTimeField()),
                ('gananciacupon', models.FloatField(db_column='gananciaCupon')),
                ('mostrarprecio', models.IntegerField()),
                ('mostrarprocentajedescuento', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('numerocuponespromo', models.IntegerField(db_column='numeroCuponesPromo')),
                ('numerocuponesusados', models.IntegerField(blank=True, db_column='numeroCuponesUsados', null=True)),
                ('porcentajedescuentoparaclientes', models.FloatField(blank=True, db_column='porcentajeDescuentoParaClientes', null=True)),
                ('precioactual', models.FloatField(blank=True, db_column='precioActual', null=True)),
                ('precioinicial', models.FloatField(blank=True, db_column='precioInicial', null=True)),
                ('prioridad', models.IntegerField(blank=True, null=True)),
                ('restricciones', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('tienecupones', models.IntegerField(db_column='tieneCupones')),
                ('valorahorro', models.FloatField(db_column='valorAhorro')),
                ('vecesvista', models.IntegerField(db_column='vecesVista')),
                ('cabecera', models.CharField(blank=True, max_length=200, null=True)),
                ('fondo', models.CharField(blank=True, max_length=200, null=True)),
                ('pie', models.CharField(blank=True, max_length=200, null=True)),
                ('tienefondo', models.IntegerField()),
                ('tipo', models.CharField(blank=True, max_length=200, null=True)),
                ('servicio', models.IntegerField()),
            ],
            options={
                'db_table': 'promocionproducto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promocionproductohistorial',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comentarios', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('esbaner', models.IntegerField(db_column='esBaner')),
                ('estado', models.CharField(max_length=255)),
                ('fdesde', models.DateTimeField()),
                ('fechacreacion', models.DateTimeField(blank=True, db_column='fechaCreacion', null=True)),
                ('fechafinenlaplataforma', models.DateTimeField(db_column='fechaFinEnLaPlataforma')),
                ('fechafinpromocion', models.DateTimeField(db_column='fechaFinPromocion')),
                ('fechainiciopromocion', models.DateTimeField(db_column='fechaInicioPromocion')),
                ('fechamodificacion', models.DateTimeField()),
                ('gananciacupon', models.FloatField(db_column='gananciaCupon')),
                ('idpromocion', models.BigIntegerField()),
                ('mostrarprecio', models.IntegerField()),
                ('mostrarprocentajedescuento', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('numerocuponespromo', models.IntegerField(db_column='numeroCuponesPromo')),
                ('numerocuponesusados', models.IntegerField(blank=True, db_column='numeroCuponesUsados', null=True)),
                ('porcentajedescuentoparaclientes', models.FloatField(blank=True, db_column='porcentajeDescuentoParaClientes', null=True)),
                ('precioactual', models.FloatField(blank=True, db_column='precioActual', null=True)),
                ('precioinicial', models.FloatField(blank=True, db_column='precioInicial', null=True)),
                ('prioridad', models.IntegerField(blank=True, null=True)),
                ('restricciones', models.CharField(blank=True, max_length=200, null=True)),
                ('tienecupones', models.IntegerField(db_column='tieneCupones')),
                ('valorahorro', models.FloatField(db_column='valorAhorro')),
                ('vecesvista', models.IntegerField(db_column='vecesVista')),
                ('slug', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'promocionproductohistorial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.IntegerField()),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
                ('descripcion', models.CharField(max_length=1000)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'seccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('agente', models.CharField(blank=True, max_length=500, null=True)),
                ('dispositivo', models.CharField(blank=True, max_length=45, null=True)),
                ('estado', models.CharField(max_length=45)),
                ('fechamodificacion', models.DateTimeField(blank=True, db_column='fechaModificacion', null=True)),
                ('fechacreacion', models.DateTimeField()),
                ('fechaexpiracion', models.DateTimeField()),
                ('fechainicio', models.DateTimeField()),
                ('firebase', models.CharField(blank=True, max_length=500, null=True)),
                ('ip', models.CharField(max_length=45)),
                ('token', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'sesion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('horaapertura', models.CharField(blank=True, db_column='horaApertura', max_length=5, null=True)),
                ('horacierre', models.CharField(blank=True, db_column='horaCierre', max_length=5, null=True)),
                ('latitud', models.CharField(blank=True, max_length=45, null=True)),
                ('longitud', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono1', models.CharField(blank=True, max_length=10, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=10, null=True)),
                ('urlfotoperfil', models.CharField(blank=True, db_column='urlFotoPerfil', max_length=200, null=True)),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activa', models.IntegerField()),
                ('codigo', models.CharField(max_length=200, unique=True)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechaeliminacion', models.DateTimeField(blank=True, db_column='fechaEliminacion', null=True)),
                ('fechavalidez', models.DateTimeField(db_column='fechaValidez')),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiponotificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tiponotificacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usariopublicacionguardada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activa', models.IntegerField()),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
            ],
            options={
                'db_table': 'usariopublicacionguardada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activo', models.IntegerField()),
                ('apellidos', models.CharField(max_length=60)),
                ('cedula', models.CharField(blank=True, max_length=10, null=True)),
                ('celular', models.CharField(blank=True, max_length=10, null=True)),
                ('codigoactivacion', models.CharField(blank=True, db_column='codigoActivacion', max_length=100, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=200, null=True)),
                ('correo', models.CharField(max_length=45, unique=True)),
                ('cuentaconfb', models.IntegerField(db_column='cuentaConFb')),
                ('cuentaconfirmada', models.IntegerField(db_column='cuentaConfirmada')),
                ('facebookid', models.CharField(blank=True, db_column='facebookId', max_length=100, null=True)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechanacimiento', models.DateTimeField(blank=True, db_column='fechaNacimiento', null=True)),
                ('fechaultimologin', models.DateTimeField(blank=True, db_column='fechaUltimoLogin', null=True)),
                ('genero', models.CharField(blank=True, max_length=255, null=True)),
                ('intentosfallidos', models.IntegerField(blank=True, db_column='intentosFallidos', null=True)),
                ('nombres', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=100)),
                ('passwordtemporal', models.CharField(blank=True, db_column='passwordTemporal', max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('tokenfb', models.CharField(blank=True, db_column='tokenFB', max_length=255, null=True)),
                ('urlfoto', models.CharField(blank=True, db_column='urlFoto', max_length=200, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarioempresa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activa', models.IntegerField()),
                ('puedeeditarpromociones', models.IntegerField()),
                ('puedevalidarcupon', models.IntegerField()),
            ],
            options={
                'db_table': 'usuarioempresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuariorol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
            ],
            options={
                'db_table': 'usuariorol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Validacuenta',
            fields=[
                ('idvalidacuenta', models.BigIntegerField(primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=45)),
                ('uuid', models.CharField(max_length=100)),
                ('fechacreacion', models.DateTimeField(db_column='fechaCreacion')),
                ('fechafin', models.DateTimeField(db_column='fechaFin')),
                ('validado', models.IntegerField()),
                ('fechavalidacion', models.DateTimeField(db_column='fechaValidacion')),
                ('ip', models.CharField(blank=True, max_length=45, null=True)),
                ('token', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'validacuenta',
                'managed': False,
            },
        ),
    ]
