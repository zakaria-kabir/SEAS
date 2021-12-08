from django.http import request
import numpy as np
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from query import *
from seasapp.models import *


# Create your views here.
semesterlist = ["Spring", "Autumn", "Summer"]
yearlist = [2009, 2010, 2011, 2012, 2013, 2014,
            2015, 2016, 2017, 2018, 2019, 2020, 2021]
schoolList = ['SBE', 'SELS', 'SETS', 'SLASS', 'SPPH']


def loginview(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def logoutview(request):
    logout(request)
    return redirect('loginpage')


def userprofile(request):
    return render(request, 'page-user.html', {})


@login_required(login_url="/login/")
def homeview(request):
    return render(request, 'home.html', {
        'segment': 'homedashboard'
    })


def view_classroom_requirement_course_offer(request):

    if request.method == 'POST':
        #semester = semesterlist[int(request.POST.get('sem'))]
        #year = yearlist[int(request.POST.get('year'))]
        # lbl = ['1-10', '11-20', '21-30', '31-35', '36-40','41-50','51-55','56-65']

        semester = request.POST.get('sem')
        year = request.POST.get('year')
        sections = classroom_requirement_course_offer(semester, year)

        class6 = []
        for i in sections:
            class6.append("{:.2f}".format(i/12))
        print(class6)

        class7 = []
        for i in sections:
            class7.append("{:.2f}".format(i/14))
        print(class7)

        str1 = semester+" "+str(year)
        return render(request, 'classsize.html', {
            'semesters': semesterlist,
            'years': yearlist,
            'class6': class6,
            'class7': class7,
            'sections': sections,
            'seme': str1,
            'search': 0,
            'segment': 'cls_req',
        })

    else:
        return render(request, 'classsize.html', {
            'semesters': semesterlist,
            'years': yearlist,
            'search': 1,
        })


def view_enrolment_course_school(request):
    if request.method == 'POST':
        l = ['1-10', '11-20', '21-30', '31-35', '36-40',
             '41-50', '51-55', '56-60', '60+']
        school = request.POST.getlist('scl')
        semester = request.POST.get('sem')
        year = request.POST.get('year')

        enrollment = []
        labels = []

        for i in school:

            enrollment.append(enrollment_wise_course_school(i, semester, year))

        for j in l:
            for i in school:
                labels.append(i+':'+j)

        #enrollment = [item for t in enrollment for item in t for item in item]
        # print(enrollment)
        list0 = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        for i in enrollment:
            e = [item for t in i for item in t]
            list0.append(e)
            list9.append(e[0])
            list1.append(e[1])
            list2.append(e[2])
            list3.append(e[3])
            list4.append(e[4])
            list5.append(e[5])
            list6.append(e[6])
            list7.append(e[7])
            list8.append(e[8])

        list10.append(sum(list9))
        list10.append(sum(list1))
        list10.append(sum(list2))
        list10.append(sum(list3))
        list10.append(sum(list4))
        list10.append(sum(list5))
        list10.append(sum(list6))
        list10.append(sum(list7))
        list10.append(sum(list8))

        list0.insert(0, list10)
        print(list0)
        print(list10)
        return render(request, 'enrollmentwise.html', {
            'schools': schoolList,
            'selectedschool': school,
            'semesters': semesterlist,
            'years': yearlist,
            # 'enrollment': list9,
            'enrollment': list0,
            'labels': labels,
            'search': 0,
            'segment': 'enroll',
        })

    else:
        return render(request, 'enrollmentwise.html', {
            'schools': schoolList,
            'semesters': semesterlist,
            'years': yearlist,
            'search': 1,
        })


def view_revenue_of_iub(request):
    if request.method == 'POST':
        school = request.POST.getlist('scl')
        yearf = request.POST.get('year1')
        yeart = request.POST.get('year2')
        print(school, yearf, yeart)
        revenue = []
        for i in school:
            revenue.append(iub_revenue(yearf, yeart, i))
        # print(revenue)
        a=abs(int(yearf)-int(yeart))+1
        # print(type(a))

        list1 = []
        list2 = []
        list3=[]
        total=[]

        
        for j in revenue:
            for i in j:
                list1.append(str(i[0])+i[1])
                list2.append(int(i[2]))
        list1 = list(dict.fromkeys(list1))
        list2 = [list2[i:i+a*3] for i in range(0, len(list2), a*3)]

        #print(list1)
        #print(list2)
        return render(request, 'revenueofiub.html', {
            'schools': schoolList,
            'yearfrom': yearlist,
            'yearto': yearlist,
            'selectedschool': school,
            'revenuesemyear': list1,
            'revenue': list2,

            'search': 0,
            'segment': 'rev',
        })

    else:
        return render(request, 'revenueofiub.html', {
            'schools': schoolList,
            'yearfrom': yearlist,
            'yearto': yearlist,
            'search': 1,
        })
