from django.urls import path
from .views import (
    home,
    success,
    list_contacts,
    update_contact,
    delete_contact,
    recommend_doctors,   # <-- ADD THIS IMPORT
)

urlpatterns = [
    path("", home, name="home"),                            # create form
    path("success/", success, name="success"),
    path("contacts/", list_contacts, name="list"),
    path("contacts/<int:pk>/edit/", update_contact, name="edit"),
    path("contacts/<int:pk>/delete/", delete_contact, name="delete"),

    # ⭐ NEW: Recommendation engine ⭐
    path("recommend/", recommend_doctors, name="recommend"),
]
