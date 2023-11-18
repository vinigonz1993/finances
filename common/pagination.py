from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'total-records': self.page.paginator.count,
            'total-pages': self.page.paginator.num_pages,
            'page': self.page.number,
            'results': data
        })
