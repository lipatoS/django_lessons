from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from currency.password_gen import password_generates
from currency.models import Rate
from currency.form import RateForms


# Create your views here.
def hello_world(request):
    return HttpResponse("hello_world")


def gen_pass(request):
    # password_len = int(request.GET.get("password-len"))
    password_len = 10
    password = password_generates(password_len)
    text = {"pass": password}
    return render(request, "gen.html", context=text)
    # return HttpResponse(password)


# def raid_list(request):
#     rates = Rate.objects.all()
#     result = []
#     for i in rates:
#         result.append(
#             f"ID = {i.id} NAME = {i.name} NAME2 = {i.surname} BABOS = {i.salary}</br>"
#         )
#     return HttpResponse(str(result))


def response_codes(request):
    return HttpResponse("Response", status=201)


def raid_list(request):
    rates = Rate.objects.all()
    text = {"message": rates}
    return render(request, "r_list.html", context=text)


def index(request):
    return render(request, "index.html")


def r_create(request):
    # if request.GET:
    #     forms = RateForms(request.GET)
    #     if forms.is_valid():
    #         forms.save()
    #         return HttpResponseRedirect("/rate/")
    # else:
    #     forms = RateForms()
    forms = RateForms()
    if request.method == 'POST':
        form = RateForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/')
    elif request.method == "GET":
        forms = RateForms()
    text = {"form": forms}
    # breakpoint()
    return render(request, "r_create.html", context=text)


def r_details(request, rate_id):
    # try:
    #     rate1 = Rate.objects.get(id=rate_id)
    # except Rate.DoesNotExist:
    #     raise Http404
    rate1 = get_object_or_404(Rate, id=rate_id)
    text = {"object": rate1}
    # print("ошибка тут")
    return render(request, "r_details.html", context=text)


def r_update(request, rate_id):
    rate1 = get_object_or_404(Rate, id=rate_id)
    if request.method == 'POST':
        form = RateForms(request.POST, instance=rate1)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/')
    elif request.method == "GET":
        forms = RateForms(instance=rate1)
    text = {"form": forms}

    return render(request, "r_update.html", context=text)


def r_delete(request, rate_id):
    rate1 = get_object_or_404(Rate, id=rate_id)
    if request.method == 'POST':
        rate1.delete()
        return HttpResponseRedirect('/rate/')
    text = {"object": rate1}

    return render(request, "r_delete.html", context=text)
