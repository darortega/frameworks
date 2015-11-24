from django.conf.urls import patterns, include, url
from django.contrib import admin

from gestoregresados.views import IndexView

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^entrada/(?P<pk>\d+)/$','gestoregresados.views.entrada'),
    url(r'^add/$','gestoregresados.views.add'),
    url(r'^$', IndexView.as_view()),
    
    url(r'^ponpostgrado/(?P<pk>\d+)/$','gestoregresados.views.ponpostgrado'),
    url(r'^ponexperiencia/(?P<pk>\d+)/$','gestoregresados.views.ponexperiencia'),
    url(r'^ponred/(?P<pk>\d+)/$','gestoregresados.views.ponred'),
    url(r'^addredes/(?P<pk>\d+)/$','gestoregresados.views.addredes'),
    url(r'^addpostgrados/(?P<pk>\d+)/$','gestoregresados.views.addpostgrados'),
    url(r'^addexperiencias/(?P<pk>\d+)/$','gestoregresados.views.addexperiencias'),

    url(r'^delete/(?P<pk>\d+)/$','gestoregresados.views.delete'),
    url(r'^update/(?P<pk>\d+)/$','gestoregresados.views.update'),
    url(r'^modegresado/(?P<pk>\d+)/$','gestoregresados.views.modegresado'),
    url(r'^nuevoegresado/$','gestoregresados.views.nuevoegresado'),
    
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^salir/$','gestoregresados.views.salir'),
    url(r'principal','gestoregresados.views.main'),  
]