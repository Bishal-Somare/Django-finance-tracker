from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login
from django.views import View
from .forms import RegisterForm,TranscationForm # make sure this is your form
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transcation # make sure this is your model
from .admin import TranscationResource

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'finance/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # replace 'home' with your actual URL name
        return render(request, 'finance/register.html', {'form': form})  # also return this if form is invalid
    
class Dashboardview(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        return render(request, 'finance/dashboard.html')
    
class TranscationView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        form=TranscationForm()
        return render(request,'finance/transcation.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=TranscationForm(request.POST)
        if form.is_valid():
            transcation=form.save(commit=False)
            transcation.user=request.user
            transcation.save()
            return redirect('dashboard')
        return render(request,'finance/transcation.html',{'form':form})
def export_transcation(request):
     user_transcations = Transcation.objects.filter(user=request.user)
     transcations_resource = TranscationResource()
     dataset = transcations_resource.export(queryset=user_transcations)
     excel_data =dataset.export('xlsx')
     response = HttpResponse(excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
     response['Content-Disposition'] = 'attachment; filename="transcations.xlsx"'
     return response

     

