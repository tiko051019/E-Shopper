from django.shortcuts import render
from django.views.generic import ListView,DetailView

class HomeListView(ListView):
    template_name = 'index.html'
    def get(self,request):

        context = {

        }

        return render(request,self.template_name,context)