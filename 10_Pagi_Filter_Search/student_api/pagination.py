from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


class MyNumberPagination(PageNumberPagination):
    page_size=5  # her sayfa icin max obje sayisi
    page_query_param="sayfa "  # query deki key page yerine
    page_size_query_param="adet"  # donen veriyi sinirla
    max_page_size=3


class MyLimitPagination(LimitOffsetPagination):
    default_limit=8
    limit_query_param="kac_tane"
    offset_query_param="kacinci"

class MyCursorPagination(CursorPagination):
    page_size=10
    ordering="-first_name"    


  