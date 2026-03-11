from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registro(request):
    # Si el usuario le dio clic al botón de "Crear Cuenta" (Método POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # ¡Aquí ocurre la magia! Se guarda en la base de datos
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}. Ya puedes iniciar sesión.')
            return redirect('login') # Lo mandamos a que inicie sesión
    
    # Si el usuario apenas entró a la página a ver el formulario (Método GET)
    else:
        form = UserCreationForm()
        
    # Le mandamos el formulario vacío a tu HTML
    return render(request, 'usuario/registro.html', {'form': form})
# Create your views here.
def registro_profesor(request):
    return render(request, 'usuario/registro_profesor.html')

def registro_alumno(request):
    return render(request, 'usuario/registro_alumno.html')
