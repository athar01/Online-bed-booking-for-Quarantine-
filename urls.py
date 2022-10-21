from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('abc/',views.abc,name='abc'),
    path('addd/',views.addd,name='addd'),
    path('display/',views.display,name='display'),
    path('users/',views.users,name='users'),
    path('search/',views.search,name='search'),
    path('disp/',views.disp,name='disp'),
    path('mmi/',views.mmi,name='mmi'),
    path('Symptoms/',views.Symptoms,name='Symptoms'),
    path('medic_info/',views.medic_info,name='medic_info'),
    path('ssss/<int:id>/<str:Email>/<str:Age>/<str:Name>/<str:Gender>/<str:Contact>/<str:Hometown>/<str:symptom1>/<str:symptom2>/<str:symptom3>/<str:symptom4>',views.ssss, name="ssss"),
    path('allrequest/',views.allrequest,name='allrequest'),
    # path('Beds_info/',views.Beds_info,name='Beds_info'),
    path('uvw/<str:place>/<str:number_of_beds>',views.uvw,name='uvw'),
    path('ms/<str:Hometown>/<str:Email>/<str:Name>',views.ms,name='ms')
]
