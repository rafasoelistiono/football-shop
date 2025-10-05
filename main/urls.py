from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, edit_product, delete_product, add_product_entry_ajax, edit_product_ajax, login_ajax, register_ajax, logout_ajax, login_page, register_page

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('login_ajax/', login_ajax, name='login_ajax'),
    path('register_ajax/', register_ajax, name='register_ajax'),
    path('logout_ajax/', logout_ajax, name='logout_ajax'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('add-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('product/<uuid:id>/edit-ajax/', edit_product_ajax, name='edit_product_ajax'),
]
