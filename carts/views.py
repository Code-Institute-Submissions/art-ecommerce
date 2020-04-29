from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Cart, CartItem
from products.models import PrintPainting, Product



def view_cart(request):
    try:
        cart_session_id = request.session['cart_id']
    except:
        cart_session_id = None
    if cart_session_id:
        cart = Cart.objects.get(id=cart_session_id)
        new_total = 0.00


        items = cart.cartitem_set.all()
        print(items)


        for item in cart.cartitem_set.all():
            print(item.product.id)
            line_total_for_product = float(item.line_total) * item.quantity          
            new_total += line_total_for_product
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()


        context = {"cart": cart}
    else:
        empty_message = "Your cart is empty, please keep shopping."
        context = {"empty": True, 'empty_message': empty_message}

    template = "cart.html"
    
    return render(request, template, context)


def remove_from_cart(request, pk):
    try:
        cart_session_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_session_id)
    except:
        return redirect(reverse('view_cart'))
    cartitem = CartItem.objects.get(pk=pk)
    #print(cartitem)
    cartitem.cart = None
    cartitem.save()
    # Send message that it's deleted
    return redirect(reverse('view_cart'))



def add_to_cart(request, pk):
    request.session.set_expiry(300000)
    # Check/Try if an instance of a cart session already exists and matches,
    # Otherwise create a new instance, match it with the id of the cart 
    # so it's unique for the current user.
    try:
        cart_session_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        cart_session_id = new_cart.id
    cart = Cart.objects.get(id=cart_session_id)
    
    # get the product
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        pass

    # Get the items and their quantity from the form from the user
    # If the value is qty there is a print of a painting that is processed
    # and handled differently from the original painting
    product_var = []
    if request.method == "POST":
        try:
            qty = request.POST['qty']
        except:
            pass

        try:
            original = request.POST['original']
            qty = int(1)
            #print(original)
        except:
            pass

        cart_item = CartItem.objects.create(cart=cart, product=product)
        #first if block handles the original painting, second the prints
        for item in request.POST:
            if item == "original":
                cart_item.product = product
                cart_item.quantity = qty
                cart_item.line_total = product.original_painting.price
                cart_item.save()
                return redirect(reverse('view_cart'))
    
            if item == "size":
                key = item
                val = request.POST[key]
                try:
                    single_product = PrintPainting.objects.get(product=product, id=val)
                    price = single_product.price
                    product_var.append(single_product)
                except:
                    pass

        #cart_item = CartItem.objects.create(cart=cart, product=product)
        
        if len(product_var) > 0:
            cart_item.print_variations.add(*product_var)
        cart_item.line_total = price
        cart_item.quantity = qty
        cart_item.save()
        # Success message
        return redirect(reverse('view_cart'))
    # Error message
    return redirect(reverse('view_cart'))
    