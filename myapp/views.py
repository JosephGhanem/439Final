from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm, RecommendationForm
from .models import Contact

# CREATE
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("success"))
    else:
        form = ContactForm()
    return render(request, "myapp/contact_create.html", {"form": form})

# SUCCESS PAGE
def success(request):
    return render(request, "myapp/success.html")

# READ (LIST)
def list_contacts(request):
    contacts = Contact.objects.all().order_by("name")
    return render(request, "myapp/contact_list.html", {"contacts": contacts})

# UPDATE
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("list"))  # matches your URL name
    else:
        form = ContactForm(instance=contact)
    return render(request, "myapp/contact_update.html", {"form": form, "contact": contact})

# DELETE
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return HttpResponseRedirect(reverse("list"))
    return render(request, "myapp/contact_delete.html", {"contact": contact})

# ⭐ RECOMMENDATION ENGINE ⭐
def recommend_doctors(request):
    form = RecommendationForm(request.GET or None)
    doctors = Contact.objects.all()

    if form.is_valid():
        city = form.cleaned_data.get("city")
        speciality = form.cleaned_data.get("speciality")
        max_fee = form.cleaned_data.get("max_fee")

        if city:
            doctors = doctors.filter(city__icontains=city)
        if speciality:
            doctors = doctors.filter(speciality__icontains=speciality)
        if max_fee is not None:
            doctors = doctors.filter(fee__lte=max_fee)

        # Ranking: best rating, then most experience
        doctors = doctors.order_by("-rating", "-years_experience")

    return render(
        request,
        "myapp/recommend.html",
        {"form": form, "doctors": doctors},
    )
