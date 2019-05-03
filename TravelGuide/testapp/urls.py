from django.conf.urls import url
from testapp import views
from django.views.generic import RedirectView
from django.urls import path

app_name='testapp'
urlpatterns=[

     url(r'^tourist/',views.Tourist_registration,name='Tourist_registration'),
     url(r'^guide/',views.Guide_registration,name='Guide_registration'),
     url(r'^tourist_login/',views.tourist_login,name='tourist_login'),
     url(r'^tourist_logout/',views.tourist_logout,name='tourist_logout'),
     url(r'^guide_Login/', views.guide_login, name='guide_login'),
     url(r'^guide_logout/', views.guide_logout, name='guide_logout'),
     url(r'^tourist_language_view/',views.tourist_language_view,name='tourist_language_view'),
     url(r'^guide_booking_view/',views.guide_booking_view,name='guide_booking_view'),
     url(r'^favicon\.ico$', RedirectView.as_view(url='/static/Images/favicon.ico')),
     url(r'^hyderabad1/',views.Hyderabad_view1,name='Hyderabad_view1'),
     url(r'^hyderabad2/',views.Hyderabad_view2,name='Hyderabad_view2'),
     url(r'^hyderabad3/',views.Hyderabad_view3,name='Hyderabad_view3'),
     url(r'^warangal1/',views.Warangal_view1,name='Warangal_view1'),
     url(r'^vizag1/',views.Vizag_view1,name='Vizag_view1'),
     url(r'^vijayawada1/',views.Vijayawada_view1,name='Vijayawada_view1'),
     url(r'^adilabad1/',views.Adilabad_view1,name='Adilabad_view1'),
     url(r'^warangal2/', views.Warangal_view2, name='Warangal_view2'),
     url(r'^vizag2/', views.Vizag_view2, name='Vizag_view2'),
     url(r'^vijayawada2/', views.Vijayawada_view2, name='Vijayawada_view2'),
     url(r'^adilabad2/', views.Adilabad_view2, name='Adilabad_view2'),
     url(r'^warangal3/', views.Warangal_view3, name='Warangal_view3'),
     url(r'^vizag3/', views.Vizag_view3, name='Vizag_view3'),
     url(r'^vijayawada3/', views.Vijayawada_view3, name='Vijayawada_view3'),
     url(r'^guide_book/',views.guide_booking_view,name='guide_booking_view'),
     path('display_view/', views.display_book_view, name='display_book_view'),

]