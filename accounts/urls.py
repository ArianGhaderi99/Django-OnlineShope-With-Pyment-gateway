from django.urls import path,reverse_lazy
from accounts import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/',views.register_view, name="register"),
    path('logout/',views.logout_view,name='logout'),
    path('<user_id>/profile/', views.edit_account_view, name='profile'),
    
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html',
                                              email_template_name='accounts/password_reset_email.html',
                                              success_url=reverse_lazy('accounts:password_reset_done')),
         name='password_reset'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
        name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html', ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
                                                     success_url=reverse_lazy(
                                                         'accounts:password_reset_complete')
                                                     ),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html', ),
         name='password_reset_complete'),
    
]

