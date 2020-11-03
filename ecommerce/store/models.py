from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuario")
	name = models.CharField(max_length=200, null=True, verbose_name="Nombre")
	ape = models.CharField(max_length=200, null=True, verbose_name="Apellido")
	dni = models.CharField(max_length=7, null=True, verbose_name="DNI")
	phone = models.CharField(max_length=200, null=True, verbose_name="Celular")
	email = models.CharField(max_length=200, verbose_name="Correo electrónico")


	def __str__(self):
		return self.name

	class Meta:
		verbose_name= "Cliente"
		verbose_name_plural = "Clientes"

class Product(models.Model):
	CATEGORY = (
			('Refrigerante', 'Refrigerante'),
			('Frenos', 'Frenos'),
			('Baterías', 'Baterías'),
			('Sellador', 'Sellador'),
			) 


	name = models.CharField(max_length=200, verbose_name="Nombre")
	cod = models.CharField(max_length=7, null=True, blank=True, verbose_name="Código")
	brand = models.CharField(max_length=50, null=True, blank=True, verbose_name="Marca")
	category = models.CharField(max_length=200, null=True, choices=CATEGORY, verbose_name="Categoría")
	price = models.FloatField(verbose_name="Precio")
	description = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripción")
	image = models.ImageField(null=True, blank=True, verbose_name="Imagen")
	date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Fecha de creación")
	digital = models.BooleanField(default=False,null=True, blank=True)
	
	

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	class Meta:
		verbose_name= "Producto"
		verbose_name_plural = "Productos"

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
	date_ordered = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de orden")
	complete = models.BooleanField(default=False, verbose_name="Completado")
	transaction_id = models.CharField(max_length=100, null=True,verbose_name="N° de Transacción")

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 
	
	class Meta:
		verbose_name= "Orden"
		verbose_name_plural = "Órdenes"

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Productos")
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name="Orden")
	quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name="Cantidad")
	date_added = models.DateTimeField(auto_now_add=True, verbose_name="Fecha agregada")

	

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	class Meta:
		verbose_name= "Artículo Ordenado"
		verbose_name_plural = "Artículos ordenados"

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, verbose_name="Cliente")
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name="Orden")
	address = models.CharField(max_length=200, null=False, verbose_name="Dirección")
	city = models.CharField(max_length=200, null=False, verbose_name="Ciudad")
	state = models.CharField(max_length=200, null=False, verbose_name="Estado")
	zipcode = models.CharField(max_length=200, null=False, verbose_name="Código postal")
	date_added = models.DateTimeField(auto_now_add=True,verbose_name="Fecha agregada")

	def __str__(self):
		return self.address
	
	class Meta:
		verbose_name= "Dirección de Envio"
		