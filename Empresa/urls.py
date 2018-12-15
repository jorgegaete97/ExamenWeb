"""NuevoProyectoPerris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

from django.urls import include, path
from django.conf import settings


from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^pri/', include ('apps.Index.urls')),
	url(r'^tra/', include ('apps.Trabajador.urls')),

	url(r'^$', auth_views.LoginView.as_view(template_name='Empresa/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='Empresa/login.html'), name='logout'),
	path('accounts/', include('allauth.urls')),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
]


if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
