from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges  ={
    'january':'Eat no meat for the entire month',
    'february':'Walk for at least 20 minutes every day',
    'march':'Learn Django for at least 20 minutes every day',
    'april':'Learn Django for at least 20 minutes every day',
    'may':'Learn Django for at least 20 minutes every day',
    'june':'Learn Django for at least 20 minutes every day',
    'july':'Learn Django for at least 20 minutes every day',
    'august':'Learn Django for at least 20 minutes every day',
    'september':'Learn Django for at least 20 minutes every day',
    'october':'Learn Django for at least 20 minutes every day',
    'november':'Learn Django for at least 20 minutes every day',
    'december':'Learn Django for at least 20 minutes every day'

}

def index(request):
    return HttpResponse('My Fist website')


def monthly_chalanges(request, month):

    

    try:
        challange=challenges[month]
    
        return HttpResponse(challange)
    
    except:
        HttpResponseNotFound('This month is not supported')

def monthly_chalanges_by_id(request, id):


    months=  list(challenges.keys()) 

    req_month=months[id-1]




    return HttpResponseRedirect(f'/challanges/{req_month}/')






