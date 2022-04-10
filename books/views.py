from uuid import uuid4

from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def get_hello(request: WSGIRequest) -> HttpResponse:
    hello = "Hello world"
    return render(request, template_name='hello_world.html', context={"hello_var": hello})


def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    # uuids = [str(uuid4()) for _ in range(10)] - konwersja na str: str(zmienna) | f"{zmienna}"
    uuids = [f"{uuid4()}" for _ in range(10)]
    return HttpResponse(f"uuids={uuids}")


def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids": uuids})


def get_fun1(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(4 + 4)


def get_fun2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("raz" + "Dwa")


def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:
    return HttpResponse(f'x={x}, y={y}, z={z}')
    # return HttpResponse('test stringa')
    # path('path-args/<int:first_arg>/<str:second_arg>/<slug:third_arg>/', get_argument_from_path, name="path_args"),


def get_arguents_from_query(request: WSGIRequest) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(a))

    return HttpResponse(f'a={a}, b={b}, c={c}')

@csrf_exempt
def check_http_query_type(request: WSGIRequest) -> HttpResponse:
    query_type = 'Unknown'
    if request.method == "GET":
        query_type = "This is GET"
    elif request.method == "POST":
        query_type = "This is POST"
    elif request.method == "PUT":
        query_type = "This is PUT"
    elif request.method == "DELETE":
        query_type = "This is DELETE"

    return HttpResponse(query_type)

def get_headers(request:WSGIRequest) -> JsonResponse:
    our_headers = request.headers

    return JsonResponse({"headers": dict(our_headers)})

@csrf_exempt
def raise_error_for_fun(request: WSGIRequest) -> HttpResponse:
    if request.method != "GET":
        raise BadRequest("Method not allowed")

    return HttpResponse('Wszystko ok')


