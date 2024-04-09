from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_paginated_context_data(queryset, paginate_by, page_number):
    paginator = Paginator(queryset, paginate_by)

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return {'page_obj': page_obj}
