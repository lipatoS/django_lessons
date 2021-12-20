from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from currency.password_gen import password_generates
from currency.models import Rate
from currency.models import Rate2
from currency.models import ContactUs
from currency.form import RateForms
from currency.form import Rate2Forms
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.core.mail import send_mail
# так делать не надо
# from settings import settings
from django.conf import settings


# def gen_pass(request):
#     password_len = 10
#     password = password_generates(password_len)
#     text = {"pass": password}
#     return render(request, "gen.html", context=text)


class GenPassViews(TemplateView):
    template_name = "gen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        password_len = 10
        password = password_generates(password_len)
        context["pass"] = password
        return context


def response_codes(request):
    return HttpResponse("Response", status=201)


#
# def raid_list(request):
#     rates = Rate.objects.all()
#     text = {"message": rates}
#     return render(request, "r_list.html", context=text)


class RateListViews(ListView):
    model = Rate
    template_name = "r_list.html"

    def get(self, request, *args, **kwargs):
        print(request.COOKIES)
        return super().get(request, *args, **kwargs)


class Rate2ListViews(ListView):
    model = Rate2
    template_name = "r_list2.html"


class KursListViews(ListView):
    model = Rate2
    template_name = "kurs_list.html"


# def index(request):
#     return render(request, "index.html")


class IndexViews(TemplateView):
    template_name = "index.html"


# def r_create(request):
#     forms = RateForms()
#     if request.method == 'POST':
#         form = RateForms(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/')
#     elif request.method == "GET":
#         forms = RateForms()
#     text = {"form": forms}
#     # breakpoint()
#     return render(request, "r_create.html", context=text)


class RateCreateViews(CreateView):
    model = Rate
    template_name = "r_create2.html"
    form_class = RateForms
    success_url = reverse_lazy("rate-list")


class Rate2CreateViews(CreateView):
    model = Rate2
    template_name = "r_create2.html"
    form_class = Rate2Forms
    success_url = reverse_lazy("rate-list2")


# def r_details(request, rate_id):
#     rate1 = get_object_or_404(Rate, id=rate_id)
#     text = {"object": rate1}
#     return render(request, "r_details.html", context=text)


class RateDetailViews(DetailView):
    model = Rate
    template_name = "r_details.html"


class Rate2DetailViews(DetailView):
    model = Rate2
    template_name = "r_details2.html"


# def r_update(request, rate_id):
#     rate1 = get_object_or_404(Rate, id=rate_id)
#     if request.method == 'POST':
#         form = RateForms(request.POST, instance=rate1)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/')
#     elif request.method == "GET":
#         forms = RateForms(instance=rate1)
#     text = {"form": forms}
#
#     return render(request, "r_update.html", context=text)


class RateUpdateViews(UpdateView):
    model = Rate
    form_class = RateForms
    success_url = reverse_lazy("rate-list")
    template_name = "r_update.html"


class Rate2UpdateViews(UpdateView):
    model = Rate2
    form_class = Rate2Forms
    success_url = reverse_lazy("rate-list2")
    template_name = "r_update2.html"


# def r_delete(request, rate_id):
#     rate1 = get_object_or_404(Rate, id=rate_id)
#     if request.method == 'POST':
#         rate1.delete()
#         return HttpResponseRedirect('/rate/')
#     text = {"object": rate1}
#
#     return render(request, "r_delete.html", context=text)

class RateDeleteViews(DeleteView):
    model = Rate
    success_url = reverse_lazy("rate-list")
    template_name = "r_delete.html"


class ContactUsViews(CreateView):
    model = ContactUs
    template_name = "contact_us_create.html"
    success_url = reverse_lazy("index")
    fields = ("email_to", "subject", "body")

    def form_invalid(self, form):
        print("ДУРИШЬ ТЫ МЕНЯ")
        return super().form_invalid(form)

    def form_valid(self, form):
        print("Всё огонёк!")
        subject = form.cleaned_data["subject"]
        body = form.cleaned_data["body"]
        email_to = form.cleaned_data["email_to"]
        full_email_body = f"""
        email from: {email_to}
        body: {body}
        """
        from currency.tasks import contact_us
        contact_us.apply_async(args=(subject,), kwargs={"body": full_email_body})
        return super().form_valid(form)

