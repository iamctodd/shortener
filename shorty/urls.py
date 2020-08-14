from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from shortener.views import root, link_view, index

urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('link/', link_view, name='link'),
    path('admin/',admin.site.urls),
    path('<str:url_hash>/', root, name='root'),
    url(r'', index, name="index"),
]
 