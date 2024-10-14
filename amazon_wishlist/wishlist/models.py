from django.db import models

class WishlistItem(models.Model):
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	url = models.URLField()
	description = models.TextField(blank=True, null=True)
	added_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Product(models.Model):
	asin = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.title



# wishlist/models.py
class ProductData(models.Model):
	asin = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=255, null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	price_added = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	reviews = models.IntegerField(null=True, blank=True)
	stars = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
	stock_status = models.CharField(max_length=255, null=True, blank=True)
	image_url = models.URLField(null=True, blank=True)
	product_link = models.URLField(null=True, blank=True)
	affiliate_link = models.URLField(null=True, blank=True)
	pattern = models.CharField(max_length=255, null=True, blank=True)
	style = models.CharField(max_length=255, null=True, blank=True)
	wishlist_name = models.CharField(max_length=255, null=True, blank=True)
	date_added = models.DateField(null=True, blank=True)
	last_pricechange = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	last_pricechange_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	last_checkdate = models.DateField(null=True, blank=True)

	class Meta:
		db_table = 'product_data'
		managed = False

class ProductDataHistory(models.Model):
	asin = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	updated_at = models.DateField()

	class Meta:
		db_table = 'product_data_history'
		managed = False


# ProductPriceHistory model
class ProductPriceHistory(models.Model):
	product = models.ForeignKey(ProductData, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	updated_at = models.DateTimeField()

	class Meta:
		db_table = 'product_data_history'
		managed = False
		
