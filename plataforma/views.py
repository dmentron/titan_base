from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from plataforma.forms import LoginForm

# Create your views here.


def index_bases(request):
    """
    :param request:
    :return: pagina de logeo
    """

    data = {
        'form': LoginForm,
    }
    return render(request, 'plataforma/bases_login.html', data)


def login_user_bases(request):
    """
    Esta funcion carga el templatedel login, y a su vez carga el login de django
    para poder ingresar al sistema
    :param request:
    :return:
    """
    username = request.POST['username']
    password = request.POST['password']

    request.session['error'] = None

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('panel_bases')
        else:
            mensaje = "El usuario no esta activo, porfavor comunicarse con el administrador"
            pagina = 'plataforma/bases_login.html'
            error = True
    else:
        mensaje = "El usuario no existe"
        pagina = 'plataforma/bases_login.html'
        error = True

    request.session['error'] = error
    request.session['mensaje'] = mensaje

    return redirect('index_bases')


@login_required(login_url='/login/')
def panel_bases(request):
    """
    Funcion para cerrar sesion, mata las sesiones activas
    :param request:
    :return:
    """
    request.session['tipo_sistema'] = 'bases'
    return render(request, 'plataforma/base.html', {})
