
from django.utils import timezone
from .models import Pinball, Repair, Company, Location, PinballInstance
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddPinballForm, AddPinballInstanceForm, AddLocationForm, RepairForm, AddCompanyForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.forms import inlineformset_factory, modelformset_factory

def repair_list(request, pk):
    pinball = get_object_or_404(Pinball, pk=pk)
    repairs = Repair.objects.filter(pinball__pinball=pinball)
    sites = Location.objects.all()
    return render(request, 'pinball/repair_list.html', {'pinball': pinball, 'repairs':repairs, 'sites':sites,})

def repair_list_instance(request, pk):
    pinball=get_object_or_404(PinballInstance, pk=pk)
    #pinball=PinballInstance.objects.get(pk=pk)
    repairs = Repair.objects.filter(pinball=pinball)
    sites = Location.objects.all()
    return render(request, 'pinball/repair_list_instance.html', {'pinball': pinball, 'repairs':repairs, 'sites':sites,})

def pinball_list(request):
    pinballs = Pinball.objects.all()
    sites = Location.objects.all()
    return render(request, 'pinball/pinball_list.html', {'pinballs':pinballs, 'sites':sites,})

def pinball_detail(request, pk):
    pinball = get_object_or_404(Pinball, pk=pk)
    sites = Location.objects.all()
    return render(request, 'pinball/pinball_detail.html', {'pinball':pinball, 'sites':sites,})

def company_detail(request, pk):
    sites = Location.objects.all()
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'pinball/company_detail.html', {'company':company, 'sites':sites,})

def year_detail(request, pk):
    year = get_object_or_404(Release_Year, pk=pk)
    sites = Location.objects.all()
    return render(request, 'pinball/year_detail.html', {'year':year, 'sites':sites,})


def pinball_new(request):
    sites= Location.objects.all()
    if request.method == "POST":
        form = AddPinballForm(request.POST)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return redirect(pinball_detail, pk=add.pk)
    else:
        form = AddPinballForm()
    return render(request, 'pinball/pinball_add.html', {'form': form, 'sites':sites})

def company_new(request):
    sites = Location.objects.all()

    if request.method == "POST":
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return redirect(company_detail, pk=add.pk)
    else:
        form = AddPinballForm()
    return render(request, 'pinball/company_add.html', {'form': form, 'sites':sites,})

def location_edit(request, location_id):
    sites=Location.objects.all()
    location=Location.objects.get(pk=location_id)
    site= get_object_or_404(Location, pk=location_id)
    PinballModelFormset=modelformset_factory(PinballInstance, can_delete=False, extra=0, fields=('location','status'), exclude=('id',))
    if request.method == 'POST':
        formset=PinballModelFormset(request.POST, queryset=PinballInstance.objects.filter(location_id=location_id))
        if formset.is_valid():
            formset.save()
            return redirect('location_edit', location_id=location.id)
    else:
        formset=PinballModelFormset(queryset=PinballInstance.objects.filter(location_id=location.id))
    return render(request, 'location_edit.html', {'formset':formset, 'site':site, 'location':location, 'sites':sites })       

def location_new(request):
    sites=Location.objects.all()
    if request.method == "POST":
        form = AddLocationForm(request.POST)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return redirect(location_detail, pk=add.pk)
    else:
        form = AddLocationForm()
    return render(request, 'pinball/location_add.html', {'form': form, 'sites':sites})

def location_detail(request, pk):
    location=Location.objects.get(pk=pk)
    return render(request, 'pinball/location_detail.html', {'form': form, 'sites':sites})


def repair_new(request, pinball_id):
    sites=Location.objects.all()
    pinball=PinballInstance.objects.get(id=pinball_id)
    #RepairFormset=inlineformset_factory(PinballInstance, Repair, can_delete=False, form=RepairForm, extra=1)
    if request.method == 'POST':
        #formset = RepairFormset(request.POST, instance=pinball)
        form = RepairForm(request.POST, instance=pinball)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return redirect('repair_list_instance', pk=pinball_id)
    else:
        form = RepairForm(instance=pinball)
    return render(request, 'pinball/repair_new.html', {'form':form, 'sites':sites, 'pinball':pinball})


