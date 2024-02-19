from django.db import models

# Create your models here.
class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField( max_length=50)
    
    class Meta:
        db_table="category_table"

    def __str__(self):
        return self.category_name

class userModel(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=255)
    

    class Meta:
       db_table="user_table"
    def __str__(self):
        return self.username
    
class bookmodel(models.Model):
    book_id=models.CharField(primary_key=True,max_length=50)
    bookname=models.CharField(max_length=50)
    bookdes=models.TextField(null=True)
    bookprice=models.CharField(max_length=50,null=True)
    book_img=models.ImageField(upload_to="images/",null=True)
    category_id=models.ForeignKey(category, on_delete=models.CASCADE)
    userid=models.ForeignKey(userModel,on_delete=models.CASCADE)

    

    class Meta:
        db_table="book"
        

    def __str__(self):
        return self.bookname



