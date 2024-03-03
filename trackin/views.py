from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from track.models import Track,Lead
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail




def index(request):
    
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

# def dynamic(request,dyna):
#     return HttpResponse(dyna)

def partner(request):
    return render(request,"partner1.html")

def track(request):
    # ref=""
    # try:
    #     if request.method=="POST":
    #         ref=request.POST['ref_no']
    #         print(ref)
    #         url='/ship/?out={}'.format(ref)
    #         # return HttpResponseRedirect(url)
            
    # except:
    #     pass
    return render(request,"track.html")

def ship(request):
    trackdata=Track.objects.all()
    try:
        if request.method=="POST":
            out=request.POST['ref_no']
            trackdata=Track.objects.filter(waybill=out)
            if trackdata.exists():

            
                d={
                    "trackin":trackdata
                }
                return render (request,"shipdetails.html",d)
            else:
                raise ObjectDoesNotExist
        # return render(request,"shipdetails.html",{"waybill":out})
    except ObjectDoesNotExist:

        # return HttpResponse("No Data Found")
        return render(request,"notfound.html")


def services(request):
    return render(request,"services.html")


def shipwithus(request):
    if request.method=="POST":
        typ=request.POST["type"]
        fname=request.POST["Fname"]
        lname=request.POST["Lname"]
        add1=request.POST["address1"]
        add2=request.POST["address2"]
        city=request.POST["city"]
        state=request.POST["state"]
        pin=request.POST["zip"]
        country=request.POST["country"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        feedback=request.POST["feedback"]

        leads=Lead(type=typ, fname=fname, lname=lname,address1=add1,address2=add2,city=city,state=state,pin=pin,country=country, phone=phone, email=email,feedback=feedback)   
        leads.save()

        msg="Dear {},\n\nWe would like to express our sincere gratitude for trying our logistics platform, Trackin. Your support means a lot to us, and we hope that you found our services helpful and efficient.\nShould you have any feedback or further inquiries, please feel free to reach out to our dedicated team. \nThank you once again for choosing Trackin! \n\n\nBest regards,\nShivam Sharma, \nTrackin Team".format(fname)


        send_mail(
        "Track_IN",
        msg,
        "trackin.com@gmail.com",
        [email],
        fail_silently=False,
        )


        return render(request,"leadsuccess.html")
    return render(request,"shipwithus.html")


def mapdetails(request):
    return render(request,"mapdetails.html")