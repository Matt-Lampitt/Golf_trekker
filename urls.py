from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('register', views.register, name="register"),
    path('member_login', views.member_login, name="member_login"),
    path('login_success', views.login_success, name="login_success"),
    path('member_logout', views.member_logout, name="member_logout"),
    path('rounds', views.rounds, name="rounds"),
    path('one_round', views.one_round, name="one_round"),
    path('post_round', views.post_round, name="post_round"),
    path('rounds/<int:round_id>', views.rounds, name="one_round"),
    path('round_success', views.round_success, name="round_success"),
    path('instruction_success', views.instruction_success, name="instruction_success"),
    path('instruction', views.instruction, name="instruction"),
    path('add_instruction', views.add_instruction, name="add_instruction"),
]