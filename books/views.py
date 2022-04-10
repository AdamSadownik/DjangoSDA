from uuid import uuid4

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def get_hello(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("hello world")

def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    # uuids = [str(uuid4()) for _ in range(10)] - konwersja na str: str(zmienna) | f"{zmienna}"
    uuids = [f"{uuid4()}" for _ in range(10)]
    return HttpResponse(f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

def get_fun1(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(4+4)

def get_fun2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("raz"+"Dwa")

def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:

    return HttpResponse(f'x={x}, y={y}, z={z}')
    # return HttpResponse('test stringa')
    # path('path-args/<int:first_arg>/<str:second_arg>/<slug:third_arg>/', get_argument_from_path, name="path_args"),
