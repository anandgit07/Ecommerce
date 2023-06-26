from django.contrib import admin
from app.models import Product,Customer,Cart,Payment,OrderPlaced

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
         list_display=  ['id','title','discounted_price','category','product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
        list_display=['id','user','locality','city','state','pincode']
        
        
        
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
        list_display=['id','user','product','quantity']       

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
        list_display=['id','user','amount','razor_order_id','razor_payment_status','razor_payment_id','paid']         


@admin.register(OrderPlaced)        
class OrderPlacedModelAdmin(admin.ModelAdmin):
        list_display=['id','user','customer','product','quantity','orderd_date','status','payment']
