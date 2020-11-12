from django.shortcuts import render, redirect
from .models import Cliente, Planes, Contrato, Cupon, Usuarios, User
from .forms import ClienteForm, PlanesForm, ContratoForm, CuponesForm, CustomUserForm, PassUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.utils.timezone import datetime
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.functions import Lower
# Create your views here.




@login_required
def home(request):

    cupones = [2, 4, 5, 7]
    
    data = {
        'cupones':cupones,
        
        
    }
    return render(request, 'core/home.html', data)

@login_required
def clientes(request):
    cliente = Cliente.objects.all()
    

    if request.POST.get('nombre'):
        
        cliente = cliente.all().order_by(Lower('nombre'))
       
    if request.POST.get('email'):

        cliente = cliente.all().order_by("email")
    
    if request.POST.get('telefono'):

        cliente = cliente.all().order_by("telefono")
    
    if request.POST.get('dni'):

        cliente = cliente.all().order_by("dni")
    
    if request.POST.get('direccion'):

        cliente = cliente.all().order_by("direccion")
    
    if request.POST.get('ciudad'):

        cliente = cliente.all().order_by("ciudad")
    
    if request.POST.get('cp'):

        cliente = cliente.all().order_by("codigo_postal")
    
    if request.POST.get('provincia'):

        cliente = cliente.all().order_by("provincia")
    
    if request.POST.get("buscar"):
        busqueda = request.POST.get('busqueda')
        cliente = cliente.filter( Q(nombre__contains=busqueda) | Q(email__contains=busqueda) | Q(telefono__contains=busqueda) | Q(dni__contains=busqueda) | Q(direccion__contains=busqueda) | Q(ciudad__contains=busqueda) | Q(codigo_postal__contains=busqueda) | Q(provincia__contains=busqueda))

    paginator = Paginator(cliente, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'clientes':cliente,
        'page_obj': page_obj,
        
    }

    return render(request, 'core/clientes.html', data)

@permission_required('core.add_cliente')
def nuevo_cliente(request):
    data = {
        'form':ClienteForm
    }
    
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        
        
        if formulario.is_valid():
            first_name = formulario.cleaned_data.get("nombre")
            username = formulario.cleaned_data.get("email")
            email = formulario.cleaned_data.get("email")
            password = formulario.cleaned_data.get("dni")
            usernuevo = User.objects.create_user(first_name = first_name, username = username, email = email, password = password)
            formulario.save()
            usernuevo.save()

            data['mensaje'] = "Cliente generado con exito" 
        else:
            data['mensaje'] = formulario.errors

    return render(request, 'core/nuevo_cliente.html', data)

@login_required
def modificar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    data = {
        'form':ClienteForm(instance=cliente)
    }
    
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Cliente actualizado correctamente"
            return redirect(to="clientes")
        else:
            data['mensaje'] = formulario.errors

    return render(request, 'core/modificar_cliente.html', data)

@login_required
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return redirect(to="clientes")

@login_required
def contratos(request):

    contrato = Contrato.objects.all()
    
    

    if request.POST.get('cliente'):

        contrato = contrato.all().order_by(Lower("cliente"))
    
    if request.POST.get('plan'):

        contrato = contrato.all().order_by("plan")
    
    if request.POST.get('ip'):

        contrato = contrato.all().order_by("ip")
    
    if request.POST.get('detalle'):

        contrato = contrato.all().order_by(Lower('detalle'))
    
    if request.POST.get('fecha_creacion'):

        contrato = contrato.all().order_by("fecha_creacion")

    if request.POST.get("buscar"):
        busqueda = request.POST.get('busqueda')
        contrato = contrato.filter( Q(cliente__nombre__contains=busqueda) | Q(plan__nombre__contains=busqueda) | Q(ip__contains=busqueda) | Q(detalle__contains=busqueda) | Q(fecha_creacion__contains=busqueda))

    paginator = Paginator(contrato, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'contratos':contrato,
        'page_obj':page_obj,
        
    }

    return render(request, 'core/contratos.html', data)

@permission_required('core.add_contrato')
def nuevo_contrato(request):
    data = {
        'form':ContratoForm
    }

    if request.method == 'POST':
        formulario = ContratoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contrato generado con exito" 
        else:
            data['mensaje'] = formulario.errors

    return render(request, 'core/nuevo_contrato.html', data)

@login_required
def modificar_contrato(request, id):
    contrato = Contrato.objects.get(id=id)
    data = {
        'form':ContratoForm(instance=contrato)
    }

    if request.method == 'POST':
        formulario = ContratoForm(data=request.POST, instance=contrato)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contrato actualizado correctamente"
            return redirect(to="contratos")
        else:
            data['mensaje'] = formulario.errors

    return render(request, 'core/modificar_contrato.html', data)

@login_required
def eliminar_contrato(request, id):
    contrato = Contrato.objects.get(id=id)
    contrato.delete()

    return redirect(to="contratos")

@login_required
def cupones(request):
    cupones = Cupon.objects.all()
    
    
    if request.POST.get('cliente'):

        cupones = cupones.all().order_by(Lower("cliente"))
    
    if request.POST.get('contrato'):

        cupones = cupones.all().order_by("contrato")
    
    if request.POST.get('monto'):

        cupones = cupones.all().order_by("monto")
    
    if request.POST.get('detalle'):

        cupones = cupones.all().order_by("detalle")
    
    if request.POST.get('fecha_creacion'):

        cupones = cupones.all().order_by("fecha_creacion")
    
    if request.POST.get('pagado'):

        cupones = cupones.all().order_by("pagado")
    
    if request.POST.get('fecha_pago'):

        cupones = cupones.all().order_by("fecha_pago")
    
    if request.POST.get("buscar"):
        busqueda = request.POST.get('busqueda')
        cupones = cupones.filter( Q(cliente__nombre__contains=busqueda) | Q(contrato__ip__contains=busqueda) | Q(monto__contains=busqueda) | Q(detalle__contains=busqueda) | Q(fecha_creacion__contains=busqueda) | Q(pagado__contains=busqueda) | Q(fecha_pago__contains=busqueda))

    paginator = Paginator(cupones, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'cupones':cupones,
        'page_obj':page_obj,
    }

    return render(request, 'core/cupones.html', data)

@login_required
def historial(request):
    return render(request, 'core/historial.html')

@login_required
def planes(request):
    planes = Planes.objects.all()
    
    if request.POST.get('nombre'):

        planes = planes.all().order_by("nombre")
    
    if request.POST.get('vel_subida'):

        planes = planes.all().order_by("vel_subida")
    
    if request.POST.get('vel_bajada'):

        planes = planes.all().order_by("vel_bajada")
    
    if request.POST.get('precio'):

        planes = planes.all().order_by("precio")
    
    if request.POST.get('detalle'):

        planes = planes.all().order_by("detalle")
    

    data = {
        'planes':planes
    }
    return render(request, 'core/planes.html', data)

@permission_required('core.add_planes')
def nuevo_planes(request):
    data = {
        'form':PlanesForm
    }

    if request.method == 'POST':
        formulario = PlanesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        
            data['mensaje'] = "Plan generado con exito" 
        else:
            data['mensaje'] = formulario.errors

    return render(request, 'core/nuevo_planes.html', data)

@login_required
def modificar_planes(request, id):
    planes = Planes.objects.get(id=id)
    data = {
        'form':PlanesForm(instance=planes)
    }

    if request.method == 'POST':
        formulario = PlanesForm(data=request.POST, instance=planes)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Plan actualizado correctamente"
            return redirect(to="planes")
        else:
            data['mensaje'] = formulario.errors

    return render(request, 'core/modificar_planes.html', data)

@login_required
def eliminar_planes(request, id):
    planes = Planes.objects.get(id=id)
    planes.delete()

    return redirect(to="planes")



@permission_required('core.add_cupon')
def nuevo_cupon(request):
    clientes=Cliente.objects.all()
    data = {
        'cliente_id':"0",
        'contrato_id':"0",
        
        'clientes':clientes,
        
        
    }
    if request.method == 'POST':
        
        cliente_id = request.POST["cliente_select"]
        if cliente_id != "0":
            c = Cliente.objects.get(id=cliente_id)
            contratos_cliente = Contrato.objects.filter(cliente = c)
            data['cliente_id'] =  int(cliente_id)
            data['contratos'] = contratos_cliente
            if request.POST["contrato_select"] != "0" :
                contrato_id = request.POST["contrato_select"]
                co = Contrato.objects.get(id=contrato_id)
                
                if request.POST.get("botonenvio"):
                    nombre = c
                    cont = co
                    precio = request.POST.get('monto')
                    descripcion = request.POST.get('detalle')
                    cupon_nuevo = Cupon.objects.create(cliente = nombre, contrato = cont, monto = precio, detalle = descripcion, pagado = False)
                    cupon_nuevo.save()
                    data['mensaje'] = "CUPON GENERADO CORRECTAMENTE"
                    email_from=settings.EMAIL_HOST_USER
                    send_mail(
                        'Se ha generado una nueva factura',
                        'Estimado cliente, este correo es para informarle que se ha generado una nueva factura a su nombre por el monto de: $' + precio + ' bajo el siguiente concepto: ' + descripcion,
                        email_from,
                        [ c.email ],
                        fail_silently=False,
                    )
                else:
                    data['contrato_monto'] = int(co.plan.precio)
                    data['contrato_id'] = int(contrato_id)
                    data['contrato_detalle'] = (co.plan.detalle)
                    
                    
    else:
        data['contrato_monto']= "0"
        data['contrato_detalle']=""

    return render(request, 'core/nuevo_cupon.html', data)

    

@login_required
def modificar_cupon(request, id):
    cupon = Cupon.objects.get(id=id)
    data = {
        'form':CuponesForm(instance=cupon),
        'cliente': cupon.cliente.nombre,
        'contrato': cupon.contrato.ip,
        'fecha': datetime.today().date
    }

    if request.method == 'POST':
        formulario = CuponesForm(data=request.POST, instance=cupon)
    
        if formulario.is_valid():
            instance = formulario.save(commit=False)
            instance.fecha_pago = datetime.today()
            instance.save()
            email_from=settings.EMAIL_HOST_USER
            send_mail(
                'Se ha registrado un nuevo pago',
                'Estimado cliente, este correo es para informarle que se ha registrado un nuevo pago a su nombre por el monto de: $' +  str(cupon.monto)  + ' bajo el siguiente concepto: ' + cupon.detalle  + ' con fecha: ' + str(datetime.today()),
                email_from,
                [ cupon.cliente.email ],
                fail_silently=False,
            )
            data['mensaje'] = "Cupon actualizado correctamente"
        else:
            
            data['mensaje'] = formulario.errors

    return render(request, 'core/modificar_cupon.html', data)

@login_required
def eliminar_cupon(request, id):
    cupon = Cupon.objects.get(id=id)
    cupon.delete()

    return redirect(to="cupones")

@permission_required('core.add_user')
def nuevo_usuario(request):
    data = {
        'form':CustomUserForm
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Usuario generado con exito"
        else:
            data['mensaje'] = formulario.errors   

    return render(request, 'registration/nuevo_usuario.html', data)

@login_required
def modificar_usuario(request, id):
    usuario = User.objects.get(id=id)
    data = {
        'form':PassUserForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = PassUserForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Password actualizado correctamente"
        else:
            data['mensaje'] = formulario.errors
    
    return render(request, 'registration/modificar_usuario.html', data)

@login_required
def usuarios(request):
    
    usuario = User.objects.all()
    data = {
        'usuarios':usuario
    }


    return render(request, 'registration/usuarios.html', data)


