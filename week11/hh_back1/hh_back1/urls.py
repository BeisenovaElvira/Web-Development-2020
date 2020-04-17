"""hh_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views.views import companies_list, company_detail, company_vacancies, vacancy_list, vacancy_detail
#from api.views.viewsCBV import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', obtain_jwt_token),
    # path('api/companies/', CompanyList.as_view()),
    # path('api/companies/<int:pk>/', CompanyDetails.as_view()),
    # path('api/companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
    # path('api/vacancies/', VacancyList.as_view()),
    # path('api/vacancies/<int:pk>/', VacancyDetails.as_view()),

#]
# urlpatterns = [
    path('api/companies/', companies_list),
    path('api/companies/<int:company_id>/', company_detail),
    path('api/companies/<int:company_id>/vacancies/', company_vacancies),
    path('api/vacancies/', vacancy_list),
    path('api/vacancies/<int:vacancy_id>/', vacancy_detail),
]
