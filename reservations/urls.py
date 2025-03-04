from django.urls import path
from .views import ReservationCreateView, ReservationDetailView, UserReservationsView

urlpatterns = [
    path('', ReservationCreateView.as_view(), name='reservation-create'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('user/<int:user_id>/', UserReservationsView.as_view(), name='user-reservations'),
]