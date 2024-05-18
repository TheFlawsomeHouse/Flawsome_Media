"""
URL configuration for flawsomemedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from flawsome_web.views.views import index
from flawsome_web.views.services import services
from flawsome_web.views.portfolio import portfolio, Project
from flawsome_web.views.contact import contact, contact_form
from flawsome_web.views.team import team
from flawsome_web.views.terms import terms
from flawsome_web.views.privacy import privacy
from flawsome_web.views.refund import refund
from flawsome_web.views.SMM import SMM
from flawsome_web.views.TFH import tfh
from flawsome_web.views.Brand import Brand
from flawsome_web.views.website import website
from flawsome_web.views.branding import branding
from flawsome_web.views.advertising import advertising
from flawsome_web.views.creative import creative
from flawsome_blog.views import blog_Preview, Blog_details

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('Brand-Shoot/', Brand, name='Brand-Shoot'),
    path('Social-Media-Marketing/', SMM, name='Social-Media-Marketing'),
    path('team/', team, name='team'),
    path('terms-and-conditions/', terms, name='terms-and-condition'),
    path('privacy-policy/', privacy, name='privacy-policy'),
    path('refunds-and-cancellation/', refund, name='refunds and cancellation'),
    path('The-Flawsome-House/', tfh, name='TFH'),
    path('team/', team, name='team'),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact'),
    path('contact_form/', contact_form, name='contact_form'),
    path('blogs/', blog_Preview, name='blogs'),
    path('Blog/', Blog_details, name='blogs'),
    path('Website-Design-And-Development/', website, name='Website-Design-And-Development'),
    path('Branding-And-Design-Identity/', branding, name='Branding-And-Design-Identity'),
    path('Adertising-And-Marketing/', advertising, name='Adertising-And-Marketing'),
    path('Creative-consulting/', creative, name='Creative-consulting'),
    path('Project/', Project, name='Project'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
                                            