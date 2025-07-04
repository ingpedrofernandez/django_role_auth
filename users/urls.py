from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="users-register"),
    path('profile', views.profile, name='users-profile'),
    path('login', auth_views.LoginView.as_view(
        template_name='users/login.html'),
         name='users-login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='users/logout.html'),
         name='users-logout'),
    path('logout_user', views.logout_user, name="logout_user"),
    path('change_password/', views.UserPasswordChangeView.as_view(),
         name='users-change-password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('clients', views.clients, name='clients'),
    path('update_client/<id>', views.update_client, name='update_client'),
    path('delete_client/<id>', views.delete_client, name='delete_client'),
    path('show_client/<id>', views.show_client, name='show_client'),

]