from django.shortcuts import render,redirect,HttpResponse
from .models import category,userModel,bookmodel
from django.shortcuts import get_object_or_404 
from django.db.models import Q




def book(request):
    bookdata=bookmodel.objects.all()
    if request.method=="POST":
        searchvalue=request.POST.get("search")
        bookdata=bookmodel.objects.filter(Q(bookname__icontains =searchvalue)|Q(userid__username__icontains=searchvalue))
        
        
    return render(request, "book.html",{"data":bookdata})

def mainpage(request):
    if request.method=="POST":
        user_name = request.POST.get("username")
        user_password = request.POST.get("userpassword")
        if user_name=="athul" and user_password=="1234":
            request.session['user'] ='athul'
            return redirect('/run')
        
    return render(request,"login.html")
    
def book_details(request, book_id):

    book = get_object_or_404(bookmodel, book_id=book_id)

    
    return render(request, 'bookdetails.html', {'book': book})

def runcmd(request):
    if 'user' in request.session:
        return HttpResponse("Bought")
    
    else:
        return redirect("/login")