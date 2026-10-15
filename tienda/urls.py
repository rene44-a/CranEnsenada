from django.urls import path

from .views import vista

urlpatterns = [
    path('', vista('tienda/inicio.html'), name='inicio'),
    path('catalogo/', vista('tienda/catalogo.html'), name='catalogo'),
    path('producto/', vista('tienda/producto.html'), name='producto'),
    path('carrito/', vista('tienda/carrito.html'), name='carrito'),
    path('checkout/', vista('tienda/checkout.html'), name='checkout'),
    path('pago/', vista('tienda/pago.html'), name='pago'),
    path('pago/transferencia/', vista('tienda/transferencia.html'), name='transferencia'),
    path('confirmacion/', vista('tienda/confirmacion.html'), name='confirmacion'),
    path('recetas/', vista('tienda/recetas.html'), name='recetas'),
    path('recetas/detalle/', vista('tienda/receta_detalle.html'), name='receta_detalle'),
    path('catalogo/movil/', vista('tienda/catalogo_movil.html'), name='catalogo_movil'),
    path('panel/', vista('administracion/login.html'), name='panel_login'),
    path('panel/dashboard/', vista('administracion/dashboard.html'), name='panel_dashboard'),
    path('panel/pedidos/', vista('administracion/pedidos.html'), name='panel_pedidos'),
    path('panel/pagos/', vista('administracion/pagos_facturas.html'), name='panel_pagos'),
    path('panel/productos/', vista('administracion/productos.html'), name='panel_productos'),
    path('panel/productos/nuevo/', vista('administracion/producto_form.html'), name='panel_producto_form'),
    path('panel/inventario/', vista('administracion/inventario.html'), name='panel_inventario'),
    path('panel/mermas/', vista('administracion/mermas.html'), name='panel_mermas'),
    path('panel/promociones/', vista('administracion/promociones.html'), name='panel_promociones'),
    path('panel/recetas/', vista('administracion/recetas.html'), name='panel_recetas'),
]
