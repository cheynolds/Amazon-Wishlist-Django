from .models import WishlistItem, ProductData, ProductDataHistory
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
import random


def wishlist_view(request):
	items = WishlistItem.objects.all()
	return render(request, 'wishlist/wishlist.html', {'items': items})


def home_view(request):
	return redirect('products')  # Redirects to the URL named 'products'


def top_price_changes_view(request):
	# Logic to fetch top price changes
	return render(request, 'wishlist/top_price_changes.html')

def categories_view(request):
	# Fetch distinct wishlist names from the database
	wishlists = ["Wishlist 1", "Wishlist 2", "Wishlist 3"]  # Replace with actual query logic
	
	return render(request, 'wishlist/categories.html', {'wishlists': wishlists})

def search_view(request):
	query = request.GET.get('q', '')  # Get the search query from the request
	if query:
		# Assuming you're searching through the title of the products
		products = ProductData.objects.filter(title__icontains=query)
	else:
		products = []
	
	return render(request, 'wishlist/search_results.html', {'products': products, 'query': query})	
	
	
def wishlist_products(request, wishlist_name):
	# Fetch products for the given wishlist
	# Example: products = Product.objects.filter(wishlist_name=wishlist_name)
	products = []  # Replace with actual query logic

	return render(request, 'wishlist/wishlist_products.html', {'products': products, 'wishlist_name': wishlist_name})

	
def index_view(request):
	return redirect('products')


def products_view(request):
	# Fetch all products from the database and randomize
	product_list = list(ProductData.objects.all())  # Convert QuerySet to list for randomization
	random.shuffle(product_list)  # Shuffle the product list randomly
	
	# Add pagination after shuffling
	paginator = Paginator(product_list, 20)  # Show 20 products per page
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	
	# Check if it's an AJAX request for infinite scroll
	if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
		return render(request, 'wishlist/product_list.html', {'products': page_obj})
	
	# Otherwise, render the full template
	return render(request, 'wishlist/products.html', {'products': page_obj, 'page_obj': page_obj})


def get_product_details(paginated_asins):
	if paginated_asins:
		products = ProductData.objects.filter(asin__in=paginated_asins)
		
		product_list = [
			{
				"asin": product.asin,
				"title": product.title,
				"subtitle": getattr(product, 'subtitle', None),
				"price": product.price,
				"price_added": product.price_added if hasattr(product, 'price_added') else None,
				"reviews": product.reviews if hasattr(product, 'reviews') else None,
				"stars": product.stars if hasattr(product, 'stars') else None,
				"stock_status": product.stock_status,
				"image_url": product.image_url,
				"product_link": product.product_link,
				"affiliate_link": getattr(product, 'affiliate_link', None),
				"pattern": getattr(product, 'pattern', None),
				"style": getattr(product, 'style', None),
				"wishlist_name": getattr(product, 'wishlist_name', None),
				"date_added": product.date_added.strftime('%Y-%m-%d') if product.date_added else None,
				"last_pricechange": product.last_pricechange,
				"last_pricechange_percent": float(product.last_pricechange_percent) if product.last_pricechange_percent else 0.00,
				"last_checkdate": product.last_checkdate.strftime('%Y-%m-%d') if product.last_checkdate else None,
			}
			for product in products
		]
	else:
		product_list = []
	
	return product_list




	
def product_detail_view(request, asin):
	# Fetch the product details from the product_data table
	product = get_object_or_404(ProductData, asin=asin)
	
	# Fetch pricing history from the product_data_history table
	pricing_history = ProductDataHistory.objects.filter(asin=asin).order_by('updated_at')
	
	# Ensure the current price and last_checkdate are included in the history
	current_price = product.price
	last_checkdate = product.last_checkdate.strftime('%Y-%m-%d') if product.last_checkdate else None
	
	# Build history data including price_added, date_added, and current price
	history_data = {
		'prices': [float(product.price_added)] + [float(entry.price) for entry in pricing_history] + [float(current_price)],
		'dates': [product.date_added.strftime('%Y-%m-%d')] + [entry.updated_at.strftime('%Y-%m-%d') for entry in pricing_history] + [last_checkdate]
	}

	
	
	# Prepare product data for rendering
	product_data = {
		'asin': product.asin,
		'title': product.title,
		'subtitle': product.subtitle,
		'price': product.price,
		'price_added': product.price_added,
		'reviews': product.reviews,
		'stars': product.stars,
		'stock_status': product.stock_status,
		'image_url': product.image_url,
		'product_link': product.product_link,
		'affiliate_link': product.affiliate_link,
		'pattern': product.pattern,
		'style': product.style,
		'wishlist_name': product.wishlist_name,
		'date_added': product.date_added.strftime('%Y-%m-%d') if product.date_added else None,
		'last_pricechange': product.last_pricechange,
		'last_pricechange_percent': float(product.last_pricechange_percent) if product.last_pricechange_percent is not None else None,
		'last_checkdate': last_checkdate
	}
	
	# Render the template with the product details and pricing history
	return render(request, 'wishlist/product_detail.html', {
		'product': product_data,
		'history_data': history_data
	})