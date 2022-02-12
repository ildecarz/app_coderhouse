from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='app-home'),   
    path('about/', views.about, name='app-about'),
    path('cursos/', views.CursosListView.as_view(), name='curso-listview'),
    path('cursos/<int:pk>', views.CursosDetailView.as_view(), name='curso-detail'),
    path('cursos/new/', views.CursosCreateView.as_view(), name='curso-create'),
    path('cursos/<int:pk>/update', views.CursosUpdateView.as_view(), name='curso-update'),
    path('cursos/<int:pk>/delete', views.CursosDeleteView.as_view(), name='curso-delete'),
]