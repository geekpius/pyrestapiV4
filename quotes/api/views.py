from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from quotes.api.paginations import SmallSetPagination
from quotes.api.permissions import IsAdminUserOrReadOnly

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer


class QuoteListCreateAPIView(ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    pagination_class = SmallSetPagination
    permission_classes = [IsAdminUserOrReadOnly]


class QuoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
