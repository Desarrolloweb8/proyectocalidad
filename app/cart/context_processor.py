def cart_total_amount(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            total = total + (float(value['precio']) * value['existencia'])
    return {'cart_total_amount': total}
