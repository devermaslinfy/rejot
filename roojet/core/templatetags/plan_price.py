from django import template

from roojet.services.models import Optimization, Product

register = template.Library()

@register.filter 
def get_price(price_plan,plan):
    plans = {'Roojet Bronze':'29','Roojet Silver':'79','Roojet Gold':'179'}
    try:
        price = plans[plan]
    except:
        price = '0.00 '
    return price

@register.filter 
def get_product_price(product, id):
	product_id = Product.objects.get(id=id)
	try:
		opti = Optimization.objects.filter(
		            Product__shopify_variant_id=product_id.shopify_variant_id).latest('updated')
		
		opt_price = opti.optimized_price
		if product_id.actual_shopify_price == opt_price:
			return "Price Updated"
		else:
			return '$ %s' %(opt_price)
	except:
		return 0