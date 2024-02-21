from django.shortcuts import render,redirect,HttpResponse
from .models import category,userModel,bookmodel,Writereview
from django.shortcuts import get_object_or_404 
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import logout



def book(request):
    bookdata = bookmodel.objects.all()
    categorydata = category.objects.all()
    
    if request.method == "POST":
        searchvalue = request.POST.get("search")
        catsearch = request.POST.get("category")
        price_order = request.POST.get("price_order")
        # var e = document.getElementById("price_order");
        # var value = e.value;
        if price_order == 'asc':
            bookdata = bookdata.order_by('bookprice')
        elif price_order == 'desc':
            bookdata = bookdata.order_by('-bookprice')
        
        if catsearch:
            bookdata = bookmodel.objects.filter(category_id=catsearch)
            
        if searchvalue:
            bookdata = bookmodel.objects.filter(Q(bookname__icontains=searchvalue) | Q(userid__username__icontains=searchvalue))
    
    return render(request, "book.html", {"data": bookdata, "dataf": categorydata})

def mainpage(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_password = request.POST.get("userpassword")
        userdata = userModel.objects.get(username=user_name)
        if user_password == userdata.password:

            request.session['user'] = user_name
            return redirect('/run')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")
    
def book_details(request, book_id):

    book = get_object_or_404(bookmodel, book_id=book_id)
    reviews = Writereview.objects.filter(book_id=book_id)

    
    return render(request, 'bookdetails.html', {'book': book,'reviews': reviews})

def runcmd(request):
    if 'user' in request.session:
        return redirect("/")
    
    else:
        return redirect("/login")
    
def review(request, book_id):
    bookdata = bookmodel.objects.get(book_id=book_id)
    reviews = Writereview.objects.filter(book_id=book_id)
    
    
    if request.method == 'POST':
    
        reviewdes = request.POST.get("review")
        
        if reviewdes:
            new_review = Writereview.objects.create(book_id=bookdata, review_des=reviewdes)
            new_review.save()
            return redirect(reverse('book_details', kwargs={'book_id': book_id}))
    
    return render(request, 'reviewpage.html', {"book": bookdata, "reviews": reviews})
def sessiondelete(request):
    if 'user' in request.session:
        del request.session['user']
        print("Session Data After Logout:", request.session)
    return redirect('/')