from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from .models import category, userModel, bookmodel, Writereview ,cartmodel
from django.contrib.auth import logout


def book(request):
    bookdata = bookmodel.objects.all()
    categorydata = category.objects.all()
    searchvalue=''
    catsearch =''
    
    if request.method == "POST":
        searchvalue = request.POST.get("search")
        catsearch = request.POST.get("category")
        price_order = request.POST.get("price_order")
        if searchvalue:
            bookdata = bookmodel.objects.filter(Q(bookname__icontains=searchvalue) | Q(userid__username__icontains=searchvalue) | Q(category_id__category_name__icontains=searchvalue))  
        if catsearch:
            bookdata = bookmodel.objects.filter(category_id=catsearch)   
        if price_order == 'asc':
            bookdata = bookdata.order_by('bookprice')
        elif price_order == 'desc':
            bookdata = bookdata.order_by('-bookprice')
     
        
    
    return render(request, "book.html", {"data": bookdata, "dataf": categorydata,"searched":searchvalue,"catsearched":catsearch})


def mainpage(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_password = request.POST.get("userpassword")
        userdata = userModel.objects.get(username=user_name)
        if user_password == userdata.password:
            request.session['user'] = user_name 
            print("Session exists:", 'user' in request.session)
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
    # reviews = Writereview.objects.filter(book_id=book_id)
    if 'user' in request.session:
        if request.method == 'POST':
            reviewdes = request.POST.get("review")
            
            if reviewdes:
                username = request.session['user']
                usernamefetch=userModel.objects.get(username=username)
                new_review = Writereview.objects.create(book_id=bookdata, review_des=reviewdes,userid=usernamefetch)
            
                
                new_review.save()
                
                return redirect(reverse('book_details', kwargs={'book_id': book_id}))
    else:
        return redirect("/run")

    return render(request, 'reviewpage.html', {"book": bookdata})


def logout_view(request):
    if 'user' in request.session:
        # print("Session exists:", 'user' in request.session)
        del request.session['user']
    return redirect('/')



def cart(request, book_id):
    book = get_object_or_404(bookmodel, book_id=book_id)
    cart=cartmodel.objects.all()
    if request.method=="POST":
        quantity = int(request.POST.get("quantity"))
        cartitems=request.POST.get("")
        print(quantity)
    if book.bookprice is not None:
        total_price = book.bookprice * quantity  
        print(total_price)
    else:
        total_price = None
    
    return render(request, "cart.html", {"book": book, "quantity": quantity, "total_price": total_price})


def add_book(request):
    if request.method == 'POST':
        new_book = bookmodel()
        # Retrieve data from the POST request
        new_book.book_id = request.POST.get('book_id')
        new_book.bookname = request.POST.get('bookname')
        new_book.quantity = request.POST.get('quantity')
        new_book.bookdes = request.POST.get('bookdes')
        new_book.bookprice = request.POST.get('bookprice')
        category_id = request.POST.get('category_id')
        username = request.session['user']
        new_book.book_img=request.FILES["book_img"]
        new_book.userid=userModel.objects.get(username=username)
        new_book.category_id = category.objects.get(category_id=category_id)
     
        

        new_book.save()
        
        return redirect('/')
    else:
        categories = category.objects.all()
        return render(request, 'add_book.html', {'categories': categories})