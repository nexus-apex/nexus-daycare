from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('childs/', views.child_list, name='child_list'),
    path('childs/create/', views.child_create, name='child_create'),
    path('childs/<int:pk>/edit/', views.child_edit, name='child_edit'),
    path('childs/<int:pk>/delete/', views.child_delete, name='child_delete'),
    path('daycareparents/', views.daycareparent_list, name='daycareparent_list'),
    path('daycareparents/create/', views.daycareparent_create, name='daycareparent_create'),
    path('daycareparents/<int:pk>/edit/', views.daycareparent_edit, name='daycareparent_edit'),
    path('daycareparents/<int:pk>/delete/', views.daycareparent_delete, name='daycareparent_delete'),
    path('daycareattendances/', views.daycareattendance_list, name='daycareattendance_list'),
    path('daycareattendances/create/', views.daycareattendance_create, name='daycareattendance_create'),
    path('daycareattendances/<int:pk>/edit/', views.daycareattendance_edit, name='daycareattendance_edit'),
    path('daycareattendances/<int:pk>/delete/', views.daycareattendance_delete, name='daycareattendance_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
