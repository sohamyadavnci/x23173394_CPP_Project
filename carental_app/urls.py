from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("customer_signup/", views.customer_signup, name="customer_signup"),
    path("customer_login/", views.customer_login, name="customer_login"),
    path("car_dealer_signup/", views.car_dealer_signup, name="car_dealer_signup"),
    path("car_dealer_login/", views.car_dealer_login, name="car_dealer_login"),
    path("add_car/", views.add_car, name="add_car"),
    path("edit_car/<int:myid>/", views.edit_car, name="edit_car"),
    path("delete_car/<int:myid>/", views.delete_car, name="delete_car"),
    path("customer_homepage/", views.all_cars, name="customer_homepage"),
    path("location_search/", views.location_search, name="location_search"),
    path("search_results/", views.search_results, name="search_results"),
    path("car_rent/", views.car_rent, name="car_rent"),
    path("order_details/", views.order_details, name="order_details"),
    path("past_orders/", views.past_orders, name="past_orders"),
    path("delete_order/<int:myid>/", views.delete_order, name="delete_order"),
    path("all_orders/", views.all_orders, name="all_orders"),
    path("complete_order/", views.complete_order, name="complete_order"),
    path("earnings/", views.earnings, name="earnings"),
    path("signout/", views.signout, name="signout"),
    path("about/", views.about, name="about"),
    path("about2/", views.about2, name="about2"),
]