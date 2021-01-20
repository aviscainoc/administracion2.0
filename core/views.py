from django.shortcuts import render
from django.contrib import messages
import mysql.connector as mcdb
import datetime
import locale

from core.models import Empresa
from core.models import Usuario
from core.models import Usuariorol
from core.models import Promocionproducto
from core.models import Multimedia


conn =mcdb.connect(host="localhost", user="root", passwd="minoche53", database="promoscuencav2", auth_plugin='mysql_native_password')
cur=conn.cursor()


locale.setlocale(locale.LC_ALL, 'nl_NL')

# Create your views here.

def home(request):

    return render(request,"core/index.html")



def aprobadas(request):

    conn.commit()

    cur.execute("select co.id, co.nombre, DATE_FORMAT(co.fechaCreacion, '%d-%m-%Y') , co.estado from empresa as co where co.estado = 'AP' ")
    datos= cur.fetchall()     
    return render(request,'core/aprobadas.html',{'empresa':datos})


    


def pendientes(request):

    conn.commit()


    cur.execute("select co.id, co.nombre, DATE_FORMAT(co.fechaCreacion, '%d-%m-%Y') , co.estado from empresa as co where co.estado = 'PEN' ")
    datos= cur.fetchall()   
    return render(request, 'core/pendientes.html',{'empresa':datos})

def productos(request):

    conn.commit()

    cur.execute("SELECT pro.id, pro.nombre, pro.descripcion, pro.slug, pro.precioActual, pro.estado, emp.nombre FROM promocionproducto as pro, empresa as emp WHERE pro.Empresa_idEmpresa = emp.id and pro.servicio = 0")
    productosLista = cur.fetchall()
    
    return render(request, 'core/productos.html', {'productosLista':productosLista})

def servicios(request):

    conn.commit()

    cur.execute("SELECT pro.id, pro.nombre, pro.descripcion, pro.slug, pro.precioActual, pro.estado, emp.nombre FROM promocionproducto as pro, empresa as emp WHERE pro.Empresa_idEmpresa = emp.id and pro.servicio = 1")
    productosLista = cur.fetchall()
    
    return render(request, 'core/servicios.html', {'productosLista':productosLista})


def reportesEfectivo(request):

    conn.commit()

    cur.execute("select com.id, com.idusuariocliente, us.apellidos, com.idempresa, emp.nombre , com.codigomotorizado, com.subtotal, com.total, com.costoentrega, com.direccionentrega  from compra as com, empresa as emp, usuario as us where com.idusuariocliente = us.id and com.idempresa = emp.id and com.metodopago like '%cash%' " )
    reportes = cur.fetchall()
    
    return render(request, "core/reportesEfectivo.html", {'reportes':reportes})



def reportesTCredito(request):

    conn.commit()

    cur.execute("select com.id, com.idusuariocliente, us.apellidos, com.idempresa, emp.nombre , com.codigomotorizado, com.subtotal, com.total, com.costoentrega, com.direccionentrega  from compra as com, empresa as emp, usuario as us where com.idusuariocliente = us.id and com.idempresa = emp.id and com.metodopago like '%tarjeta%' " )
    reportes = cur.fetchall()
    
    return render(request, "core/reportesTCredito.html", {'reportes':reportes})

def usuarios(request):

    return render(request, "core/usuarios.html")



def editarEmpresa(request, id):

    

    cur.execute("select * from empresa as emp where id = {}".format(id))
    editarEmpresa = cur.fetchone()

    cur.execute("select co.id, co.nombre from categoriaempresa as co ")
    categoria = cur.fetchall()

    if request.method == 'POST':
        
        empres = request.POST['empresa']
        slogan = request.POST['slogan']
        descripcion = request.POST['desc']
        facebook = request.POST['face']
        twritter = request.POST['twritter']
        pagWeb = request.POST['web']
        #catServicio=request.POST['opcion1']
        porcetComision = request.POST['porcentaje']
        HoraAbre=request.POST['abre']
        HoraCierra=request.POST['cierra']
        estado=request.POST['estado']
        fechaActual = datetime.datetime.now()

        

        Empresa.objects.filter(pk=id).update(descripcion=descripcion,eslogan=slogan,facebook=facebook,nombre=empres,twitter=twritter,web=pagWeb, top=0, estado=estado, horaapertura=HoraAbre,horacierre=HoraCierra,comision=porcetComision)

    print ("Datos de edicion:")
    print(list(editarEmpresa))
    
    conn.commit()
    return render(request,"core/editarEmpresa.html",{'editarEmpresa':editarEmpresa, 'categoria':categoria})


def editarProductoServicio(request, id):

    
    cur.execute("select * from promocionproducto where id = {}".format(id))
    producto = cur.fetchone()

    cur.execute("SELECT emp.nombre FROM promocionproducto as pro, empresa as emp WHERE pro.Empresa_idEmpresa = emp.id  and emp.id = {}".format(id))
    categoria = cur.fetchall()

    print('holi',producto[5])


    if request.method == 'POST':
    
        nombre = request.POST['nombre']
        comentario = request.POST['comentario']
        descripcion = request.POST['descripcion']
        baner = request.POST['baner']
        estado = request.POST['estado']
        fechacreacion = request.POST.get('fechacreacion')
        fechafinplataforma = request.POST['fechafinplataforma']
        fechafinpromocion=request.POST['fechafinpromocion']
        fechainiciopromocion=request.POST['fechainiciopromocion']
        fechamodificacion=datetime.datetime.now()
        gananciacupon=request.POST['gananciacupon']
        mostrarprecio=request.POST['mostrarprecio']
        mostrardescuento=request.POST['mostrardescuento']
        numerocuponespromocion=request.POST['numerocuponespromocion']
        numerocuponesusados=request.POST['numerocuponesusados']
        porcentajedescuento=request.POST['porcentajedescuento']
        precioactual=request.POST['precioactual']
        precioinicial=request.POST['precioinicial']
        prioridad=request.POST['prioridad']
        restricciones=request.POST['restricciones']
        eslogan=request.POST['eslogan']
        cupones=request.POST['cupones']
        ahorro=request.POST['ahorro']
    
        Promocionproducto.objects.filter(pk=id).update(comentarios=comentario, descripcion=descripcion, esbaner=baner, estado=estado,   fechafinenlaplataforma=fechafinplataforma, fechafinpromocion=fechafinpromocion, fechainiciopromocion=fechainiciopromocion, fechamodificacion=fechamodificacion, gananciacupon=locale.atof(gananciacupon), mostrarprecio=mostrarprecio, mostrarprocentajedescuento=mostrardescuento, nombre=nombre, numerocuponespromo=numerocuponespromocion, porcentajedescuentoparaclientes=locale.atof(porcentajedescuento), precioactual=precioactual, precioinicial=precioinicial, prioridad=prioridad, restricciones=restricciones, slug=eslogan, tienecupones=cupones, valorahorro=ahorro)

    conn.commit()



    return render(request,"core/editarProductoServicio.html",{'producto':producto, 'categoria':categoria})



def crearEmpresa(request):
    conn =mcdb.connect(host="localhost", user="root", passwd="minoche53", database="promoscuencav2", auth_plugin='mysql_native_password')
    cur=conn.cursor()

    cur.execute("select co.id, co.nombre from categoriaempresa as co ")
    datos= cur.fetchall()    
    # print(list(datos) ,'\n')   
    if request.method == 'POST':

        if bool(request.FILES.get('image',False))==True:
            logo=request.FILES['image']
        empres = request.POST['empresa']
        slogan = request.POST['slogan']
        descripcion = request.POST['desc']
        facebook = request.POST['face']
        twritter = request.POST['twritter']
        pagWeb = request.POST['web']
        catServicio=request.POST['opcion1']
        porcetComision = request.POST['porcentaje']
        HoraAbre=request.POST['abre']
        HoraCierra=request.POST['cierra']

        estado="PEN"

        
        fechaActual = datetime.datetime.now()

        #insertar datos
        empresa = Empresa(descripcion=descripcion,eslogan=slogan,facebook=facebook,nombre=empres,twitter=twritter,web=pagWeb,
        fechacreacion=fechaActual ,fechafin=fechaActual, top=0, vecesvisitada=0,servicios= 0, slug=catServicio,comision=porcetComision,
        estado=estado, horaapertura=HoraAbre,horacierre=HoraCierra, urlfotoperfil=logo)
        
        empresa.save()
        print("empresa creada")


    return render(request,'core/crearEmpresa.html',{'categoriaempresa':datos})
     

def CrearProductos(request):


    if request.method == 'POST':
    
        urlImg = request.POST['url']
        nombre = request.POST['nombre']
        comentario = request.POST['comentario']
        descripcion = request.POST['descripcion']
        baner = request.POST['baner']
        estado = request.POST['estado']
        fechacreacion = request.POST.get('fechacreacion')
        fechafinplataforma = request.POST['fechafinplataforma']
        fechafinpromocion=request.POST['fechafinpromocion']
        fechainiciopromocion=request.POST['fechainiciopromocion']
        fechamodificacion=datetime.datetime.now()
        gananciacupon=request.POST['gananciacupon']
        mostrarprecio=request.POST['mostrarprecio']
        mostrardescuento=request.POST['mostrardescuento']
        numerocuponespromocion=request.POST['numerocuponespromocion']
        numerocuponesusados=request.POST['numerocuponesusados']
        porcentajedescuento=request.POST['porcentajedescuento']
        precioactual=request.POST['precioactual']
        precioinicial=request.POST['precioinicial']
        prioridad=request.POST['prioridad']
        restricciones=request.POST['restricciones']
        eslogan=request.POST['eslogan']
        cupones=request.POST['cupones']
        ahorro=request.POST['ahorro']
    
        producto = Promocionproducto(comentarios=comentario, descripcion=descripcion, esbaner=baner, estado=estado,   fechafinenlaplataforma=fechafinplataforma, fechafinpromocion=fechafinpromocion, fechainiciopromocion=fechainiciopromocion, fechamodificacion=fechamodificacion, gananciacupon=locale.atof(gananciacupon), mostrarprecio=mostrarprecio, mostrarprocentajedescuento=mostrardescuento, nombre=nombre, numerocuponespromo=numerocuponespromocion, porcentajedescuentoparaclientes=locale.atof(porcentajedescuento), precioactual=precioactual, precioinicial=precioinicial, prioridad=prioridad, restricciones=restricciones, slug=eslogan, tienecupones=cupones, valorahorro=ahorro)
        multimedia = Multimedia(url=urlImg)   
        producto.save()
        multimedia.save()
    return render(request,"core/crearProductoServicio.html")

