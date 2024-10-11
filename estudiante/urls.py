from django.urls import path
from estudiante import views

app_name = 'estudiante'

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta_estudiante, name='alta_estudiante'),
    path('listar_cursos', views.listar_cursos, name='listar_cursos'),
    path('listar_estudiantes', views.listar_estudiantes, name='listar_estudiantes'),
    path('mayores/<int:edad>/', views.estudiante_mayores, name='estudiante_mayores'),
    path('curso/<int:id>/', views.mostrar_curso, name='mostrar_curso'),
]