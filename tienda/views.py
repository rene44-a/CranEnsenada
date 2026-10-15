from django.shortcuts import render


# Maquetas de la variante B (identidad Rubí).
# Cada vista solo muestra su plantilla; la lógica (modelos, carrito, pagos) se agrega después.

def vista(plantilla):
    def _vista(request):
        return render(request, plantilla)
    return _vista
