from rest_framework import generics
from backend.models import Staff
from backend.api.permissions import IsAdminUserOrReadOnly
from backend.api.serializers import StaffSerializer


class ListView(generics.ListCreateAPIView):
    queryset = Staff.objects.all().order_by("-id")
    serializer_class = StaffSerializer
    # permission_classes = [IsAdminUserOrReadOnly]


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    # permission_classes = [IsAdminUserOrReadOnly]