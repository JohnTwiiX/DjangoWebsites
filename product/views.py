from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from product.models import Product


# @csrf_exempt
def get_products(request):
    if(request.method == 'POST'):
        ext = request.POST['ext']
        if(ext == 'All'):
            products = Product.objects.filter(status=True).prefetch_related('images')
        else:
            products = Product.objects.filter(status=True, category=ext).prefetch_related('images')
        product_list = []
        for product in products:
            images = [{"url": image.image.url, "alt_text": image.alt_text} for image in product.images.all()]
            product_list.append({
                "name": product.name,
                "description": product.description,
                "sku": product.sku,
                "category": product.category,
                "status": product.status,
                "price": product.price,
                "weight": product.weight,
                "dimensions": product.dimensions,
                "material": product.material,
                "color": product.color,
                "images": images
            })

        return JsonResponse({"products": product_list}, status=200)
    else:
        return JsonResponse({"error":"Method not allowed"}, status=405)