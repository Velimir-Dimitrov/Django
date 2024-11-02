from django.urls import path, re_path, include

from urlAndViews.departments import views
urlpatterns = [
    path('', views.index, name='home'),
    path('softuni/', views.redirect_to_softuni),
    path('redirect-to-view', views.redirect_to_view, name='redirect-view'),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk, name='numbers'),
        path('<int:pk>/<slug:slug>/', views.view_with_slug)
    ])),
    path('<str:variable>/', views.view_with_variable), #matches till /
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),

    path('<path:variable>', views.view_with_variable) # matches after / as well


    # path('<uuid:id>, views.view_with_uuid)

]