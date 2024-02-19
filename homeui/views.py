from django.shortcuts import render,redirect,HttpResponse
from .models import category,userModel,bookmodel
from django.shortcuts import get_object_or_404




def book(request):
    bookdata=bookmodel.objects.all()
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
    # Fetch the book object from the database using the book_id
    book = get_object_or_404(bookmodel, book_id=book_id)

    
    # Render the book details page with the book object
    return render(request, 'bookdetails.html', {'book': book})

def runcmd(request):
    if 'user' in request.session:
        return HttpResponse("Bought")
    
    else:
        return redirect("/login")