from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # cuando se escriben expresiones regulares en phyton es importante colocar la letra r al principio, funciona como pista
    # para python y que este entienda que la cadena contendra caracteres especiales.
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
