from django.shortcuts import render, redirect
from .models import Cliente, Planes, Contrato, Cupon, Usuarios, User
from .forms import ClienteForm, PlanesForm, ContratoForm, CuponesForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login

# Create your views here.




@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def clientes(request):
    cliente = Cliente.objects.all()
    data = {
        'clientes':cliente
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
            formulario.save()
            data['mensaje'] = "Cliente generado con exito" 

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

    return render(request, 'core/modificar_cliente.html', data)

@login_required
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return redirect(to="clientes")

@login_required
def contratos(request):

    contrato = Contrato.objects.all()
    data = {
        'contratos':contrato
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

    return render(request, 'core/modificar_contrato.html', data)

@login_required
def eliminar_contrato(request, id):
    contrato = Contrato.objects.get(id=id)
    contrato.delete()

    return redirect(to="contratos")

@login_required
def cupones(request):
    cupones = cupones.objects.all()
    data = {
        'cupones':cupones
    }

    return render(request, 'core/cupones.html')

@login_required
def historial(request):
    return render(request, 'core/historial.html')

@login_required
def planes(request):
    planes = Planes.objects.all()
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

    return render(request, 'core/modificar_planes.html', data)

@login_required
def eliminar_planes(request, id):
    planes = Planes.objects.get(id=id)
    planes.delete()

    return redirect(to="planes")



@permission_required('core.add_cupon')
def nuevo_cupon(request):
    data = {
        'form':CuponesForm
    }

    if request.method == 'POST':
        formulario = CuponesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        
            data['mensaje'] = "Cupon generado con exito" 

    return render(request, 'core/nuevo_cupon.html', data)

@login_required
def nuevo_usuario(request):
    data = {
        'form':CustomUserForm
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Usuario generado con exito"
            

    return render(request, 'registration/nuevo_usuario.html', data)

@login_required
def modificar_usuario(request, id):
    usuario = User.objects.get(id=id)
    data = {
        'form':CustomUserForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Password actualizado correctamente"

    return render(request, 'registration/modificar_usuario.html', data)

@login_required
def usuarios(request):
    
    usuario = User.objects.all()
    data = {
        'usuarios':usuario
    }


    return render(request, 'registration/usuarios.html', data)


