from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from datetime import datetime

class Product(models.Model):
    category_list = [("laptops","laptops") , 
    ("phones" , "phones") , ("tablets" , "tablets") , ("accessories" , "accessories")]
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    category = models.CharField(max_length=64, choices=category_list , default="accessories")
    date = models.DateTimeField(default=datetime.now)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/%d',blank = True , null = True)
    image2 = models.ImageField(upload_to='images/%d',blank = True , null = True)
    image3 = models.ImageField(upload_to='images/%d',blank = True , null = True)
    image4 = models.ImageField(upload_to='images/%d',blank = True , null = True)

    # thumbnail_image = models.ImageField( blank=True, null=True)





    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     from PIL import Image
    #     import os
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         self.thumbnail_image.name = "images/thumbnail_" + self.image.name
    #         img.save("images/thumbnail_" + self.image.name)
            
    #         print(os.path.join(self.image.path , ".\\"))

    def __str__(self):
        return f"{self.name} - {self.price} - {self.category} : {self.id}"







class CustomerUser(AbstractUser):
    image = models.ImageField(upload_to='images/user/%d',blank = True , null = True , default = "/images/avatar.png")

    pass
    def __str__(self):
        return f"{self.username}"






class Cart(models.Model):
    user = models.ForeignKey('CustomerUser', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"


class Wishlist(models.Model):
    user = models.ForeignKey('CustomerUser', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"




class Comment(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey('CustomerUser', on_delete=models.CASCADE)
    rate = models.IntegerField(default=5)
    def __str__(self):
        return f"{self.text}\n{self.user}  - {self.date}"
