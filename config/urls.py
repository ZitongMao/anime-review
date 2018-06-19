from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from kanban import views as kanban_views
from kanban import operations as kanban_operations





urlpatterns = [
    url(r'^$', kanban_views.home, name='home'),
    # url(r'^contact/$', kanban_views.contact, name='contact'),
    url(r'^accounts/profile/$', kanban_views.profile, name='profile'),
    url(r'^about/$', kanban_views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^kanban/$', kanban_views.dashboard, name='kanban'),
    url(r'^kanban/details/(?P<id>\w{0,50})/$', kanban_views.details),
    url(r'^kanban/add/$', kanban_views.add, name='add'),
    url(r'^dashboard/$', kanban_views.dashboard, name='dashboard'),
    url(r'^kanban/deletion/(?P<id>\w{0,50})/$', kanban_operations.delete),
    # url(r'^kanban/done/(?P<id>\w{0,50})/$', 'kanban.operations.done'),
    url(r'^kanban/edit/(?P<id>\w{0,50})/$', kanban_operations.edit, name='edit'),
    # url(r'^kanban/$', views.TitleList.as_view()),
    url(r'^kanban/api/$', kanban_views.TitleList.as_view()),
    url(r'^kanban/api/(?P<pk>[0-9]+)/$', kanban_views.TitleDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
