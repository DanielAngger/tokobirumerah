"""
URL configuration for tokobirumerah project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from main.views import logout_user
from main.views import login_user
from main.views import register
from django.urls import path
from main.views import show_main, create_pesanan_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, create_pesanan_flutter
from main.views import edit_pesanan
from main.views import delete_pesanan
from main.views import products_view
from main.views import add_pesanan_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-pesanan-entry', create_pesanan_entry, name='create_pesanan_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-pesanan/<uuid:id>', edit_pesanan, name='edit_pesanan'),
    path('delete/<uuid:id>', delete_pesanan, name='delete_pesanan'),
    path('products/', products_view, name='products'),
    path('create-pesanan-entry-ajax', add_pesanan_entry_ajax, name='add_pesanan_entry_ajax'),
    path('create-flutter/', create_pesanan_flutter, name='create_pesanan_flutter'),
]