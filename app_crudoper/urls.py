from django.urls import path
from app_crudoper import views

urlpatterns = [
    path('emp/',views.emp,name='emp'),
    path('',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.destro,name='destro'),
]