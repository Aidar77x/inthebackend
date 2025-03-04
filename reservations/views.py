from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class UserReservationsView(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Reservation.objects.filter(user_id=user_id)