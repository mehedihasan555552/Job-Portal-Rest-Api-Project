from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
"""class Account(models.Model):
    User = models.ForeignKey(User,null=True,on_delete = models.SET_NULL)
    name = models.TextField(max_length=200)
    phone = models.TextField(max_length=200)
    hourly_rate = models.EmailField(max_length=200)
    country = models.TextField(max_length=200)
    state = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    zip = models.TextField(max_length=200)
    usertype = models.TextField(max_length=200)
    how_many_jobs = models.TextField(max_length=200,null=True,blank=True)
    stars_value = models.TextField(max_length=200,null=True,blank=True)
    distance_in_miles = models.TextField(max_length=200,null=True,blank=True)
    specializes = models.TextField(max_length=200,null=True,blank=True)
    last_reviews = models.TextField(max_length=200,null=True,blank=True)
    profile_picture = models.ImageField(default='default.jpg',max_length=200,null=True,blank=True)
    description = models.TextField(max_length=200,null=True,blank=True)
    wallet = models.FloatField(max_length=50, null=False, blank=False, )


    def __str__(self):
        return self.name


"""


"""

class Review(models.Model):
    job = models.PositiveSmallIntegerField( null=True, blank=False, default=None )
    created =  models.DateTimeField(auto_now_add=True)
    creator = models.PositiveSmallIntegerField( null=True, blank=False, default=None )
    user = models.PositiveSmallIntegerField( null=True, blank=False,  default=None)
    stars = models.PositiveSmallIntegerField( null=True, blank=False, default=None)
    review = models.TextField(null=True,blank=True, default=None)


    def __str__(self):
        return self.job.description





"""




from Apiproject.settings import ALLOWED_HOSTS

allowed_hosts =ALLOWED_HOSTS


import requests
import json
from django.db import models
from django.contrib.auth.models import AbstractUser

"""lass User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)



"""
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)
class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password):
        user = self.create_user(
            email,
            password=password,        
            username=username,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            password=password,
            username= username,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    #user = models.ForeignKey('User',null=True,on_delete = models.SET_NULL)
    #job = models.ForeignKey(Job,null=True,on_delete = models.SET_NULL)   ,PermissionsMixin
    date_of_birth= models.DateTimeField(null=True,blank=True)
    phone = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    #passwrod = models.PasswordField()
    phone = models.TextField(null=True,blank=True)
    country = models.TextField(null=True,blank=True)
    state = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    zip_code = models.TextField(null=True,blank=True)
    phone = models.TextField(null=True,blank=True)
    #type_of_ = models.TextField(null=True,blank=True) type most be a boolean from the seller field
    how_many_jobs = models.TextField(null=True,blank=True)
    stars_value = models.TextField(null=True,blank=True)
    distance_in_miles = models.TextField(null=True,blank=True)
    specializes = models.TextField(null=True,blank=True)
    last_reviews = models.TextField(null=True,blank=True)
    profile_picture = models.ImageField(default='default.jpg',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    seller=models.BooleanField(default=False)
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=40,default='null')
    last_name = models.CharField(max_length=140,default='null')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    firebase_id=models.IntegerField(null=True,blank=True)
    agro_id=models.IntegerField(null=True,blank=True)
    USERNAME_FIELD = "username"
    objects = UserManager()

    def add_specializes(self,specializes):
        self.specializes=specializes+';'+specializes
    def save(self,username=None, *args, **kwargs):
        if username and not User.objects.filter(username=username):
            self.username =username
        elif not self.username :
            self.username = self.first_name+str(self.id)
        super(User, self).save(*args, **kwargs) 


import datetime
class Job(models.Model):
    description = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    pay = models.TextField(null=True,blank=True)
    job_budget = models.FloatField(null=True,blank=True)
    job_hours = models.IntegerField(null=True,blank=True)
    job_type = models.TextField(null=True,blank=True)
    job_media = models.ImageField(default='default.jpg',null=True,blank=True)
    price_per_hour = models.TextField(null=True,blank=True)
    job_time=models.DateField(null=True,blank=True)
    buyer = models.ForeignKey(User,related_name ="Buyer_job",null=True,on_delete = models.SET_NULL)
    seller = models.ForeignKey(User,related_name ="seller_job",null=True,on_delete = models.SET_NULL)
    #offer = models.ForeignKey(offer,related_name ="seller_user",null=True,on_delete = models.SET_NULL)

"""

class Job(models.Model):
    description = models.TextField(null=True,blank=True)
    title = models.TextField(max_length=30,null=False)
    address = models.TextField(null=True,blank=True)
    pay = models.TextField(null=True,blank=True)
    specialize = models.TextField(max_length=50,null=False)
    open = models.BooleanField(default=True)
    job_price = models.TextField(null=True,blank=True)
    job_hours = models.TextField(null=True,blank=True)
    job_type = models.TextField(null=True,blank=True)
    job_media = models.ImageField(default='default.jpg',null=True,blank=True)
    creator = models.PositiveSmallIntegerField( null=True, blank=False,)
    assigned_to = models.PositiveSmallIntegerField(null=True,  blank=True, default=None)
    accepted_offer_id = models.PositiveSmallIntegerField( null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    start_time = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.description

"""


class Offer(models.Model):
    description = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    offer_price = models.FloatField(null=True,blank=True)
    offer_hours = models.IntegerField(null=True,blank=True)
    offer_type = models.TextField(null=True,blank=True)
    offer_media = models.FileField(default='default.jpg',null=True,blank=True)
    price_per_hour = models.IntegerField(null=True,blank=True)
    offer_time=models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(User,related_name ="Buyer_offer",null=True,on_delete = models.SET_NULL)
    seller = models.ForeignKey(User,related_name ="seller_offer",null=True,on_delete = models.SET_NULL)
    job = models.ForeignKey(Job,related_name ="job_offer",null=True,on_delete = models.SET_NULL)
    accepted=models.BooleanField(default=False)
    def accepte(self):
        if not self.offer_price:
            if self.price_per_hour and self.price_per_hour:
                self.offer_price=float(self.hours*self.price_per_hour)
            else:
                return self
        self.accepted=True
        self.save()
        return self
"""

class Offer(models.Model):
    job = models.PositiveSmallIntegerField( null=False, blank=False, default=0)
    created =  models.DateTimeField(auto_now_add=True)
    user = models.PositiveSmallIntegerField( null=False, blank=False, )
    user_name =  models.TextField( null=False, blank=False, )
    offer_amount = models.FloatField(max_length=50, null=False, blank=False, )
    offer_time = models.PositiveSmallIntegerField( null=False, blank=False, )
    message = models.TextField(null=True,blank=True)
    specialize = models.TextField(max_length=50,null=False,blank=False)
    stars_value = models.TextField(null=True,blank=False)


    def __str__(self):
        return self.job.description
"""
class Order(models.Model):
    buyer = models.ForeignKey(User,related_name ="Buyer_user",null=True,on_delete = models.SET_NULL)
    seller = models.ForeignKey(User,related_name ="seller_user",null=True,on_delete = models.SET_NULL)
    job = models.ForeignKey(Job,  null=True, blank=True, on_delete = models.SET_NULL)
    offer = models.ForeignKey(Offer,  null=True, blank=True, on_delete = models.SET_NULL)
    created =  models.DateTimeField(auto_now_add=True)
    succeful=models.BooleanField(default=False)
    accepted=models.BooleanField(default=False)
    paied=models.BooleanField(default=False)
    url_payment = models.TextField(null=True,blank=True)
    total_amount=models.FloatField(null=True,blank=True)
    def save(self, seller=None,buyer=None,offer=None,*args, **kwargs):
        if offer:
            self.offer=offer
        if buyer:
            self.buyer=buyer
        if seller:
            self.seller=seller
        try:
            self.total_amount=self.offer.offer_price
        except:
            pass
        super(Order, self).save(*args, **kwargs)
    def accepted(self):
        self.accepted=True
        self.save()
        return self
    def return_url(self,cancel=False):
        if cancel:
                url=allowed_hosts[0]+"/api/return_paid/"+str(self.pk)+"/"
        else :
            url=url=allowed_hosts[0]+"/api/return_notpaid/"+str(self.pk)+"/"
        return url
    def paypal(self):
        print("paypal")
        #print(request.data['client_id'])
        token = PaypalToken('client_id','client_secret')
        headers = {"Content-Type": "application/json", "Authorization": 'Bearer ' +"55563fea2bd2a181fd5c868b0c367a16" }#token['access_token']}
        url = 'https://api.sandbox.paypal.com/v2/checkout/orders'

        data = {
                    "intent": "CAPTURE",
                    "application_context": {
                        "return_url":self.return_url(),
                        "cancel_url": self.return_url(cancel=True),
                        "brand_name": "GlitchTec",
                        "landing_page": "BILLING",
                        "shipping_preference": "SET_PROVIDED_ADDRESS",
                        "user_action": "CONTINUE"
                    },
                   
                     
                    "purchase_units": [
                        {
                            "reference_id": "PUHF",
                            "description": 'your service asked from GlitchTec',
                            "custom_id": "GlitchTec-Services",
                            "soft_descriptor": "Tech service",
                            "amount": {
                            "currency_code": "USD",
                            "value": str(self.offer.offer_price)},
                            "items":[]
                            ,  
                      "shipping": {
                            "address": {
                                "address_line_1": self.buyer.address,
                                "name": {
                                    "full_name":self.buyer.first_name +" " +self.buyer.last_name 
                                },
                                "admin_area_2": "",
                                "admin_area_1": "",
                                "postal_code": self.buyer.zip_code ,
                                "state":self.buyer.state,
                                "country_code": self.buyer.country
                                        }
                                        }
                        }
                     ]
            }
        result = requests.post(url, data, headers=headers)
        print(result)
        if result["rel"] == "approve":
            self.url_payment=result["rel"] 
            self.save()
            return result["href"]
        return None

"""

"application_context": {
                    "return_url": "https://www.example.com",
                    "cancel_url": "https://www.example.com",
                    "brand_name": "EXAMPLE INC",
                    "landing_page": "BILLING",
                    "shipping_preference": "SET_PROVIDED_ADDRESS",
                    "user_action": "CONTINUE"
                },
                "purchase_units": [
                    {
                        "reference_id": "PUHF",
                        "description": "Sporting Goods",

                        "custom_id": "CUST-HighFashions",
                        "soft_descriptor": "HighFashions",
                        "amount": {
                            "currency_code": "USD",
                            "value": "220.00",
                            "breakdown": {
                                "item_total": {
                                    "currency_code": "USD",
                                    "value": "180.00"
                                },
                                "shipping": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                },
                                "handling": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "tax_total": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                },
                                "shipping_discount": {
                                    "currency_code": "USD",
                                    "value": "10"
                                }
                            }
                        },
                        "items": [
                            {
                                "name": "T-Shirt",
                                "description": "Green XL",
                                "sku": "sku01",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "90.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "quantity": "1",
                                "category": "PHYSICAL_GOODS"
                            },
                            {
                                "name": "Shoes",
                                "description": "Running, Size 10.5",
                                "sku": "sku02",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "45.00"
                                },"""
def PaypalToken(client_id,client_secret):

    url = "https://api.sandbox.paypal.com/v1/oauth2/token"
    data = {
                # "client_id":client_id,
                # "client_secret":client_secret,
                "grant_type":"client_credentials"
            }
    headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                # 'grant_type':'client_credentials'
            }

    token = requests.post(url, data, headers=headers,auth=(client_id, client_secret))
    print(token.status_code, json.loads(token.content))
    return json.loads(token.content)
"""


"""

class Review(models.Model):
    buyer = models.ForeignKey(User,related_name ="Review_buyer",null=True,on_delete = models.SET_NULL)
    sller = models.ForeignKey(User,related_name ="review_seller",null=True,on_delete = models.SET_NULL)
    job = models.ForeignKey(Job,  null=True, blank=True, on_delete = models.SET_NULL)
    created =  models.DateTimeField(auto_now_add=True)
    seller_review=models.BooleanField(default=False)
    description = models.TextField(null=True,blank=True)
    rate = models.IntegerField(default=5)
    order=models.ForeignKey(Order,  null=True, blank=True, on_delete = models.SET_NULL)

class Customer(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    email       = models.EmailField()
    customer_id = models.TextField(max_length=120, blank=True)
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email 




"""

class Card(models.Model):
    payment_profile = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_id         = models.TextField(max_length=60)
    brand           = models.TextField(max_length=120, null=True, blank=True)
    country         = models.TextField(max_length=20, null=True, blank=True)
    exp_month       = models.IntegerField(null=True, blank=True)
    exp_year        = models.IntegerField(null=True, blank=True)
    last4           = models.TextField(max_length=4, null=True, blank=True)
    default         = models.BooleanField(default=True)
    created_on      = models.DateTimeField(auto_now_add=True)


"""



class PaymentOrder(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('paid', 'Paid'),
        ('abandoned', 'Abandoned'),
    )
    order_id        = models.TextField(max_length=50)
    payment_profile = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    quantity        = models.PositiveIntegerField(default=1)
    total_amount    = models.DecimalField(default=0.00, max_digits=50, decimal_places=2)
    status          = models.TextField(max_length=50, choices=STATUS_CHOICES, default='created')
    active          = models.BooleanField(default=True)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.order_id





class Charge(models.Model):
    charge_id               = models.TextField(max_length=120)
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order                   = models.ForeignKey(PaymentOrder, on_delete=models.SET_NULL, blank=True, null=True)
    paid                    = models.BooleanField(default=False)
    refunded                = models.BooleanField(default=False)
    outcome                 = models.TextField(null=True, blank=True)
    outcome_type            = models.TextField(max_length=120, null=True, blank=True)
    seller_message          = models.TextField(max_length=120, null=True, blank=True)
    risk_level              = models.TextField(max_length=120, null=True, blank=True)
