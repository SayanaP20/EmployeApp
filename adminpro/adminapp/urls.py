from django.urls import path
from . import views




urlpatterns = [
    path('', views.index,name="index"),
    path('admin_login/',views.admin_login),
    path('admin_view',views.admin_view,name="admin_view"),
    # path('',views.'admin_home',name='admin_home'),

    path('insert_data/', views.insert_data),

    path("add_employee/",views.add_employee),

    # path('login/', views.login_view, name='login'),




    path('python_dashboard/<str:designation>/', views.python_dashboard, name='python_dashboard'),
    path('php_dashboard/<str:designation>/', views.php_dashboard, name='php_dashboard'),
    path('hr_dashboard/<str:designation>/', views.hr_dashboard, name='hr_dashboard'),
    path('user_login/', views.user_login),


#    path('view_employees/', view_employees, name='view_employees'),
     path('employee_list/', views.employee_list, name='employee_list'),

     path('daily_updates/', views.daily_updates, name='daily_updates'),

     path('view_updates/', views.view_updates, name='view_updates'),





    path("php_view_juniors/",views.php_view_juniors),
    path("php_view_seniors/",views.php_view_seniors),


    path("python_view_juniors/",views.python_view_juniors),
    path("python_view_seniors/",views.python_view_seniors),





]
