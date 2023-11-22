from django.urls import path
from main.views import show_main, create_Item, show_xml, show_json, show_json_by_id, show_xml_by_id, register, login_user, logout_user, tambah_amount, kurang_amount, hapus_item, get_product_json,add_product_ajax, hapus_item_ajax, tambah_amount_ajax, kurang_amount_ajax, create_product_flutter

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
    path('hapus_item/<int:id>/', hapus_item, name='hapus_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('hapus_item_ajax/<int:id>/', hapus_item, name='hapus_item'),
    path('kurang_amount_ajax/<int:id>/', get_product_json, name='get_product_json'),
    path('tambah_amount_ajax/<int:id>', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    
]