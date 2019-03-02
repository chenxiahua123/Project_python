from django.conf.urls import url

from app01 import views

urlpatterns=[

    url(r'^home/$',views.home,name='home'),

    url(r'^register/$',views.register,name='register'),

    url(r'^checked/$',views.checked,name='checked'),

    url(r'^check_password/$',views.check_password,name='check_password'),

    url(r'^logout/$',views.logout,name='logout'),

    url(r'^login/$',views.login,name='login'),

    url(r'^productDetail/$',views.productDetail,name='productDetail'),

    url(r'^productDetail02/$',views.productDetail02,name='productDetail02'),

    url(r'^productDetail03/$',views.productDetail03,name='productDetail03'),

    url(r'^shopping/$',views.shopping,name='shopping'),

    url(r'^addcart/$',views.addcart,name='addcart'),

    url(r'^minuscart/$',views.minuscart,name='minuscart'),

    url(r'^cart/$',views.cart,name='cart'),

    url(r'^changestatus/$',views.changestatus,name='changestatus'),

    url(r'^deleteall/$',views.deleteall,name='deleteall'),
]