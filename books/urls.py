from django.urls import path

from books.views import get_uuids_a, get_uuids_b, get_fun1, get_fun2, get_argument_from_path, \
    get_arguents_from_query, check_http_query_type, get_headers, raise_error_for_fun, AuthorListBaseView, \
    CategoryListTemplateView, BooksListView, BookDetailsView, CategoryCreateFormView, AuthorCreateView, \
    AuthorUpdateView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b),
    path('get-fun1', get_fun1),
    path('get-fun2', get_fun2),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('query-args', get_arguents_from_query, name="get_from_query"),
    path('query-type', check_http_query_type, name="get_query_type"),
    path('get-headers', get_headers, name="get_headers"),
    path('raise-error', raise_error_for_fun, name='raise-error'),
    path('author-list/', AuthorListBaseView.as_view(), name='author_list'),
    path('category-list/', CategoryListTemplateView.as_view(), name='category_list'),
    path('books_list/', BooksListView.as_view(), name='books_list'),
    path('book_details/<int:pk>', BookDetailsView.as_view(), name='book_details'),
    path('category-create/', CategoryCreateFormView.as_view(), name='category_create'),
    path('author-create/', AuthorCreateView.as_view(), name='author_create'),
    path('author-update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    # path('author-update/', AuthorUpdateView.as_view(), name='author_update_name'),
]