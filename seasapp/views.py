from django.http import request
import numpy as np
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from query import *
from seasapp.models import *
from operator import itemgetter
import bisect



# Create your views here.
semesterlist = ["Spring", "Autumn", "Summer"]
yearlist = [2009, 2010, 2011, 2012, 2013, 2014,
            2015, 2016, 2017, 2018, 2019, 2020, 2021]
schoolList = ['SBE', 'SELS', 'SETS', 'SLASS', 'SPPH']
SETSdeptList=['CSE','EEE','PhySci']
##############################################################################################################################
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

##############################################################################################################################
def logoutview(request):
    logout(request)
    return redirect('loginpage')

##############################################################################################################################
def userprofile(request):
    return render(request, 'page-user.html', {})

##############################################################################################################################
@login_required(login_url="/login/")
def homeview(request):
    return render(request, 'home.html', {
        'segment': 'homedashboard'
    })

##############################################################################################################################
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
##############################################################################################################################

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

##############################################################################################################################
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
            'segment': 'rev',
        })

##############################################################################################################################
def view_rev_change(request):
    if request.method == 'POST':
        yearf = request.POST.get('year1')
        yeart = request.POST.get('year2')
        revenue = []

        revenue.append(iub_revenue_total(yearf, yeart))
        #print(revenue)
        y = abs(int(yearf)-int(yeart))+1
        # print(type(a))

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
        total = []

        for j in revenue:
            for i in j:
                list1.append(str(i[0])+i[1])
                list2.append(int(i[2]))
        list1 = list(dict.fromkeys(list1))
        total=list2
        list2 = [list2[i:i+3] for i in range(0, len(list2), 3)]
        print(total)
        for i in list2:
            list3.append(i[0])
            list4.append(i[1])
            list5.append(i[2])
        #print(list3)
        for i in list3:
            #if(list3.index(i)<len(list3)):
                if list3.index(i)!=0:
                    a=list3[abs(list3.index(i)-1)]
                    b=i
                    c = int(((b-a)/b)*100)
                else:
                    a = list3[abs(list3.index(i))]
                    b = i
                    c = int(((b-a)/b)*100)
                list6.append(c)
        for i in list4:
            #if(list3.index(i)<len(list3)):
                if list4.index(i)!=0:
                    a=list4[abs(list4.index(i)-1)]
                    b=i
                    c = int(((b-a)/b)*100)
                else:
                    a = list4[abs(list4.index(i))]
                    b = i
                    c = int(((b-a)/b)*100)
                list7.append(c)
        for i in list5:
            #if(list3.index(i)<len(list3)):
                if list5.index(i) != 0:
                    a = list5[abs(list5.index(i)-1)]
                    b = i
                    c = int(((b-a)/b)*100)
                else:
                    a = list5[abs(list5.index(i))]
                    b = i
                    c = int(((b-a)/b)*100)
                list8.append(c)
        #for i in list8:
        for j in range(y):
            list9.append(list6[j])
            list9.append(list7[j])
            list9.append(list8[j])

        #list9=[list6]+[list7]+[list8]

        #print(list1)
        print(list2)
        #print(list9)
        
        return render(request, 'revenuechange.html', {
            'yearfrom': yearlist,
            'yearto': yearlist,
            'revenuesemyear': list1,
            'revenueper': list9,
            'totalrev': total,
            'search': 0,
            'segment': 'rev',
        })

    else:
        return render(request, 'revenuechange.html', {
            'yearfrom': yearlist,
            'yearto': yearlist,
            'search': 1,
            'segment': 'rev',
        })

##############################################################################################################################


##############################################################################################################################
def view_sets_rev(request):
    if request.method == 'POST':
        dept = request.POST.getlist('dept')
        yearf = request.POST.get('year1')
        yeart = request.POST.get('year2')
        print(dept, yearf, yeart)
        revenue = []
        for i in dept:
            revenue.append(SETS_revenue(yearf, yeart, i))
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

        print(list1)
        print(list2)
        return render(request, 'setsrev.html', {
            'dept': SETSdeptList,
            'yearfrom': yearlist,
            'yearto': yearlist,
            'selecteddept': dept,
            'revenuesemyear': list1,
            'revenue': list2,

            'search': 0,
            'segment': 'sets',
        })

    else:
        return render(request, 'setsrev.html', {
            'dept': SETSdeptList,
            'yearfrom': yearlist,
            'yearto': yearlist,
            'search': 1,
            'segment': 'sets',
        })

##########################################################################################################################


def view_deptwise_rev_per(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        yearf = request.POST.get('year1')
        yeart = request.POST.get('year2')
        # print(dept, yearf, yeart)
        revenue = []
        revenue.append(SETS_revenue(yearf, yeart, dept))
        # print(revenue)
        y = abs(int(yearf)-int(yeart))+1
        # print(type(a))

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
        total = []

        for j in revenue:
            for i in j:
                list1.append(str(i[0])+i[1])
                list2.append(int(i[2]))
        list1 = list(dict.fromkeys(list1))
        total=list2
        list2 = [list2[i:i+3] for i in range(0, len(list2), 3)]

      
        print(list1)
        for i in list2:
            list3.append(i[0])
            list4.append(i[1])
            list5.append(i[2])
        
        for i in list3:
            #if(list3.index(i)<len(list3)):
                if list3.index(i) != 0:
                    a = list3[abs(list3.index(i)-1)]
                    b = i
                    c = int(((b-a)/b)*100)
                else:
                    a = list3[abs(list3.index(i))]
                    b = i
                    c = int(((b-a)/b)*100)
                list6.append(c)
        for i in list4:
            #if(list3.index(i)<len(list3)):
                if list4.index(i) != 0:
                    a = list4[abs(list4.index(i)-1)]
                    b = i
                    c = int(((b-a)/b)*100)
                else:
                    a = list4[abs(list4.index(i))]
                    b = i
                    c = int(((b-a)/b)*100)
                list7.append(c)
        for i in list5:
            #if(list3.index(i)<len(list3)):
                if list5.index(i) != 0:
                    a = list5[abs(list5.index(i)-1)]
                    b = i
                    c = int(((b-a)/b)*100)
                else:
                    a = list5[abs(list5.index(i))]
                    b = i
                    c = int(((b-a)/b)*100)
                list8.append(c)
        #for i in list8:
        for j in range(y):
            list9.append(list6[j])
            list9.append(list7[j])
            list9.append(list8[j])
       
        print(list9)
        return render(request, 'setsdeptper.html', {
            'dept': SETSdeptList,
            'yearfrom': yearlist,
            'yearto': yearlist,
            'selecteddept': dept,
            'revenuesemyear': list1,
            'revenue': list9,
            'totalrev': total,

            'search': 0,
            'segment': 'sets',
        })

    else:
        return render(request, 'setsdeptper.html', {
            'dept': SETSdeptList,
            'yearfrom': yearlist,
            'yearto': yearlist,
            'search': 1,
            'segment': 'sets',
        })
#####################################################################################################################################


def view_enrolment_details(request):
    if request.method == 'POST':
        sem = request.POST.get('sem')
        year = request.POST.get('year')

        sbe=[]
        sels=[]
        sets=[]
        slass=[]
        spph=[]

        sbe=details_enrollment('SBE',sem,year)
        sels=details_enrollment('SELS', sem, year)
        sets=details_enrollment('SETS',sem,year)
        slass=details_enrollment('SLASS',sem,year)
        spph=details_enrollment('SPPH', sem, year)

        selectedsem=sem+' '+year
        #print(sbe)
        #print(sels)

        
        
        m=[]
        m.append(max(sbe, key=itemgetter(0))[0])
        m.append(max(sels, key=itemgetter(0))[0])
        m.append(max(sets, key=itemgetter(0))[0])
        m.append(max(slass, key=itemgetter(0))[0])
        m.append(max(spph, key=itemgetter(0))[0])

        maxenroll=max(m)+1

        sbe = [element for tupl in sbe for element in tupl]
        sels = [element for tupl in sels for element in tupl]
        sets = [element for tupl in sets for element in tupl]
        slass = [element for tupl in slass for element in tupl]
        spph = [element for tupl in spph for element in tupl]

        listOddsbe = sbe[1::2] 
        listEvensbe = sbe[::2]
        listOddsels = sels[1::2] 
        listEvensels = sels[::2]
        listOddsets = sets[1::2]
        listEvensets = sets[::2]
        listOddslass = slass[1::2]
        listEvenslass = slass[::2]
        listOddspph = spph[1::2]
        listEvenspph = spph[::2]
        

        for i in range(maxenroll):
            if i not in listEvensbe:
                listEvensbe.insert(i,i)
                listOddsbe.insert(i,0)
        sumsbe = sum(listOddsbe)
        for i in range(maxenroll):
            if i not in listEvensels:
                listOddsels.insert(i, 0)
        sumsels = sum(listOddsels)
        for i in range(maxenroll):
            if i not in listEvensets:
                listOddsets.insert(i, 0)
        sumsets = sum(listOddsets)
        for i in range(maxenroll):
            if i not in listEvenslass:
                listOddslass.insert(i, 0)
        sumslass = sum(listOddslass)
        for i in range(maxenroll):
            if i not in listEvenspph:
                listOddspph.insert(i, 0)
        sumspph = sum(listOddspph)
        tabledata=[]
        totalsum=[]
        tabledata2=[]
        tabledata3=[]
        tabledata4=[]
        tabledata5=[]
        
        for i in range(maxenroll):
            a0 = listEvensbe[i]
            a1=listOddsbe[i]
            a2=listOddsels[i]
            a3=listOddsets[i]
            a4=listOddslass[i]
            a5=listOddspph[i]
            a6 = a1+a2+a3+a4+a5
            totalsum.append(a6)

            tabledata.append([a0,a1,a2,a3,a4,a5,a6])
        tabledata.append(['Total',sumsbe,sumsels,sumsets,sumslass,sumspph,sum(totalsum)])
        # print(sum(tabledata))
        
        return render(request, 'enrolmentdetails.html', {
            'semesters': semesterlist,
            'years': yearlist,
            'selectedsem': selectedsem,
            'selectedyear': year,
            'range': listEvensbe,
            'tabledata': tabledata,


            
            'search': 0,
            'segment': 'details',
        })

    else:
        return render(request, 'enrolmentdetails.html', {
            'semesters': semesterlist,
            'years': yearlist,
            'search': 1,
            'segment': 'details',
        })
