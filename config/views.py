from django.shortcuts import render, redirect
from django.views import generic, View

from .models import *
from .uitls import *


class HomeListView(generic.ListView):
    model = Technology
    context_object_name = 'technologies'
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)

        context['portfolios'] = Portfolio.objects.prefetch_related('technologies')
        context['data'] = Data.objects.first()

        return context


class SendView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            send_message(name, email, message)
            return redirect('home')

        return render(request, 'index.html')
