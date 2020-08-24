from django.shortcuts import render, redirect
from .models import Cliente, Planes, Contrato
from .forms import ClienteForm, PlanesForm, ContratoForm
from django.contrib.auth.decorators import login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
def usuarios(request):
    return render(request, 'core/usuarios.html')