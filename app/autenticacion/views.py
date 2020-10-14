from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario,password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, f"Bienvenido de nuevo  {nombre_usuario}")
                return redirect("listado_productos")
            else:
                messages.error(request, "los datos son incorrectos")

        else:
            messages.error(request, "los datos son incorrectos")

    form = AuthenticationForm()
    return render(request, "autenticacion/acceder.html", {"form": form})


class VistaRegistro(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        form = UserCreationForm()
        return render(request, "autenticacion/registro.html", {"form": form})

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            messages.success(request, f"Bienvenido {nombre_usuario}")
            login(request, usuario)
            return redirect("listado_productos")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                return render(request, "autenticacion/registro.html", {"form": form})


def salir(request):
    logout(request)
    messages.success(request, f"tu sesion se ha cerrado correctamente ")
    return redirect("acceder")