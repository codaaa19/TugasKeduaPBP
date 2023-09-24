from django.urls import path
from main.views import show_main, create_Item, show_xml, show_json, show_json_by_id, show_xml_by_id, register, login_user, logout_user, tambah_amount, kurang_amount, hapus_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_Item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('tambah_amount/<int:id>/', tambah_amount, name='tambah_amount'),
    path('kurang_amount/<int:id>/', kurang_amount, name='kurang_amount'),
    path('hapus_item/<int:id>/', hapus_item, name='hapus_item')
]