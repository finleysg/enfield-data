"""enfield-data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin

admin.site.site_header = "Enfield Detail Administration"

urlpatterns = [
    url(r"^admin/", admin.site.urls),
]
