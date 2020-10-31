from django.urls import path
from . import views
urlpatterns = [
     path('afterlogin',views.afterlogin,name='afterlogin'),
    path('/',views.index,name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('scan2',views.scan2,name='scan2'),path('cbit',views.cbit,name='cbit'),
    path('cbitcric',views.cbitcric,name='cbitcric'),path('cbitvol',views.cbitvol,name='cbitvol'),
    path('cbitbas',views.cbitbas,name='cbitbas'),path('cbitkab',views.cbitkab,name='cbitkab'),
    path('cricket1/<slug:guess1>/<slug:guess2>',views.cricket1,name='cricket1'),
]
