# Generated by Django 3.2.19 on 2023-06-26 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=55)),
                ('mobile', models.IntegerField(default=0)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(choices=[('Bihar', 'Bihar'), ('Jharkhand', 'Jharkhand'), ('WestBengal', 'WestBengal'), ('Maharastra', 'Mharastra'), ('Orissa', 'Orissa'), ('Telegana', 'Telegana'), ('Tamilnadu', 'Tamilnadu'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Punjab', 'Punjab'), ('Haryana', 'Haryana'), ('Rajasthan', 'Rajasthan'), ('Uttarakhand', 'Uttrakhand'), ('Madhya Pradesh', 'madhya Pradesh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Sikkim', 'Sikkim'), ('Assam', 'Assam'), ('Nagaland', 'Nagaland'), ('Arunchal Pradesh', 'Arunchal Pradesh'), ('Tripura', 'Tripura'), ('Mizoram', 'Mizorm'), ('Meghalaya', 'Meghalaya'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Kerela', 'Kerela'), ('Karnatka', 'Karnatka'), ('Himachal Pradesh', 'Himachal Pradesh'), ('New Delhi', 'New Delhi'), ('Jammu', 'Jammu'), ('Kashmir', 'kashmir'), ('Pudducherry', 'Pudducherry')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('discription', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice-Creams'), ('BL', 'Butter-Milk'), ('ST', 'Sweets')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razor_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razor_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razor_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('orderd_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Deleiverd', 'Deliverd'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='app.customer')),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
