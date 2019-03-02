import hashlib
import random
import time
from collections import Iterable

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from app01.models import Lunbo, Register, Lunbo2, Product, Cart


def home(request):
    lunbo=Lunbo.objects.all()

    token=request.session.get('token')

    users=Register.objects.filter(token=token)

    if users.count():
        users=users.first()
    else:
        users=None



    data={
        'lunbos':lunbo,
        'users':users,

    }

    return render(request,'home.html',context=data)


def generate_password(password):
    sha=hashlib.sha256()
    sha.update(password.encode('utf-8'))

    return sha.hexdigest()


def generate_token():
    token=str(time.time)+str(random.random)
    md5=hashlib.md5()
    md5.update(token.encode('utf-8'))

    return md5.hexdigest()


def register(request):

    if request.method=='GET':
        # print("1111")
        return render(request,'register.html')
    elif request.method=='POST':
        # print("2222")
        user=Register()
        user.username=request.POST.get('username')
        # print("333")
        # print(user.password)
        # print("444")
        user.password=generate_password(request.POST.get('password'))
        user.token=generate_token()
        # print(user.token)
        # print(user.password)

        user.save()

        response=redirect('app01:home')

        request.session['token']=user.token

        return response


def checked(request):


   username=request.GET.get('username')

   password=request.GET.get('password')

   user=Register.objects.filter(username=username)

   if user.exists():

       return JsonResponse({'msg':"账户已存在",'status':0})
   else:

       return JsonResponse({'msg':'账户可使用','status':1})


def check_password(request):
    print("11111")

    username = request.GET.get('username')

    password = request.GET.get('password')

    user = Register.objects.filter(username=username)

    if user.exists():
        print("4444")
        return None
    else:

        if password:
            print("2222")
            return JsonResponse({'psw':'密码可使用','status':1})
        else:
            print("3333")
            return JsonResponse({'psw': "密码不可使用", 'status': 0})


def logout(request):

    request.session.flush()
    return redirect('app01:home')


# def login(request):

    # if request.method=='GET':
    #     print("aaaaaaa")
    #     return render(request,'login.html')
    #
    # elif request.method=='POST':
    #     print("bbbbbbb")
    #     username=request.POST.get('username')
    #     users=Register.objects.filter(username=username)
    #
    #     if users.count():
    #
    #         password=generate_password(request.POST.get('password'))
    #         user=Register.objects.filter(username=username)
    #
    #         # if user.count():
    #         #     user.token=generate_token()
    #         #     request.session['token']=user.token
    #         #     return redirect('app01：home')
    #         # else:
    #         #     return JsonResponse({'msg':'密码错误','status':1})
    #         return JsonResponse({'msg':'账户存在,可登录','status':1})
    #
    #
    #     else:
    #         return JsonResponse({'msg':'账户不存在','status':0})
def login(request):

    if request.method == 'GET':
        print("111")

        return render(request, 'login.html')

    elif request.method == 'POST':
        print("222")
        username = request.POST.get('username')
        password = generate_password(request.POST.get('password'))
        # password=request.POST.get('password')

        user = Register.objects.filter(username=username).filter(password=password)
        # print(user.exists())
        print("333")
        if user.count():
            response = redirect('app01:home')
            user = user.first()
            # print(user,type(user))
            user.token = generate_token()

            user.save()

            request.session['token'] = user.token
            print("444")

            return response
        else:
            print("555")
            return render(request, 'login.html')
        # , context = {'err': '账户或密码错误'}


def productDetail(request):



    lunbo2 = Lunbo2.objects.all()

    product=Product.objects.all()

    token=request.GET.get('token')

    user=Register.objects.filter(token=token)

    data={
        'lunbos':lunbo2,
        'product0':product[0],
        'product1':product[1],
        'product2':product[2],
        'product3':product[3],
        'product4':product[4],
        'user':user

    }

    return render(request,'productDetail.html',data)


def shopping(request):

    token=request.session.get('token')

    if token:
        user=Register.objects.filter(token=token)
        user=user.first()
        carts=Cart.objects.filter(user=user)
        data={
            'carts':carts,
            # 'cart_id':carts.first()
        }
        return render(request, 'shopping.html',context=data)
    else:
        return redirect('app01:login')





def addcart(request):

    token=request.session.get('token')
    print(request.GET.get('productid'))

    if token:
        print('第一步')

        user=Register.objects.filter(token=token)
        user=user.first()
        print(user)
        # print(user.first())
        # print(user[0])
        productid=request.GET.get('productid')
        product=Product.objects.get(pk=productid)
        print(product)

        print('第二步')

        cart=Cart.objects.filter(user=user).filter(product=product)
        cart = cart.first()
        print(cart)

        print('第三步')
        # print(cart)
        # print(cart.user.first())
        # print(cart.product)
        #
        if cart:
            print('第1步')
            # print(cart)
            # cart=Cart()
            print('第2步')
            print(cart.number)
            print(type(cart.number))
            cart.number=cart.number+1
            print('第3步')
            cart.save()
            print('成功')
        else:
            print(111)
            cart=Cart()
            print(222)
            # print(cart.user)
            cart.user=user
            print(333)
            cart.product=product
            print(444)
            cart.number=1
            print(555)
            cart.save()
            print(666)


        return JsonResponse({'msg': '{}-添加购物车成功'.format(product.img), 'status': 1,'number':cart.number})
    else:
        return JsonResponse({'msg': '尚未登录，请重新登录','status':0})


def minuscart(request):

    token=request.session.get('token')
    print(request.GET.get('productid'))

    if token:
        print('第一步')

        user=Register.objects.filter(token=token)
        user=user.first()
        print(user)
        # print(user.first())
        # print(user[0])
        productid=request.GET.get('productid')
        product=Product.objects.get(pk=productid)
        print(product)

        print('第二步')

        cart=Cart.objects.filter(user=user).filter(product=product)
        cart = cart.first()
        print(cart)

        print('第三步')
        # print(cart)
        # print(cart.user.first())
        # print(cart.product)
        #
        if cart:
            print('第1步')
            # print(cart)
            # cart=Cart()
            print('第2步')
            print(cart.number)
            print(type(cart.number))
            cart.number=cart.number-1
            print('第3步')
            cart.save()
            print('成功')
        else:
            pass

        return JsonResponse({'msg': '{}-减少购物车成功'.format(product.img), 'status': 1,'number':cart.number})
    else:
        return JsonResponse({'msg': '尚未登录，请重新登录','status':0})


def cart(request):
    token=request.session.get('token')

    if token:
        user=Register.objects.filter(token=token)
        user=user.first()
        carts=Cart.objects.filter(user=user)
        print(carts)
        print(type(carts))

        return JsonResponse({'msg': '测试连通','status':1})
    else:
        return JsonResponse({'msg':'Please Login','status':0})


def productDetail02(request):



    lunbo2 = Lunbo2.objects.all()

    product=Product.objects.all()

    token=request.GET.get('token')

    user=Register.objects.filter(token=token)

    data={
        'lunbos':lunbo2,
        'product0':product[0],
        'product1':product[1],
        'product2':product[2],
        'product3':product[3],
        'product4':product[4],
        'user':user

    }

    return render(request,'productDetail02.html',data)


def productDetail03(request):



    lunbo2 = Lunbo2.objects.all()

    product=Product.objects.all()

    token=request.GET.get('token')

    user=Register.objects.filter(token=token)

    data={
        'lunbos':lunbo2,
        'product0':product[0],
        'product1':product[1],
        'product2':product[2],
        'product3':product[3],
        'product4':product[4],
        'user':user

    }

    return render(request,'productDetail03.html',data)


def changestatus(request):

    token=request.session.get('token')

    if token:

        user=Register.objects.filter(token=token)
        user=user.first()

        carts=Cart.objects.filter(user=user)

        cartid=request.GET.get('cartid')

        cartlist=Cart.objects.get(pk=cartid)

        cartlist.isselect=not cartlist.isselect

        cartlist.save()

        return JsonResponse({'msg': '状态修改成功', 'status': 1,'cartid':cartid,'isselect':cartlist.isselect})
    else:
        return JsonResponse({'msg': '请登录','status':0})


def deleteall(request):
    token=request.session.get('token')

    if token:
        user=Register.objects.filter(token=token)
        user=user.first()

        cartid=request.GET.get('cartid')
        print(cartid)
        print(type(cartid))
        cart_list=Cart.objects.get(pk=int(cartid))
        isselect=not cart_list.isselect
        print(cart_list)
        print(type(cart_list))
        print(cart_list.id)
        print(type(cart_list.id))
        cart_list.delete()
        return JsonResponse({'msg':'全部删除成功','status':1,'isselect':isselect})

    else:
        return JsonResponse({'msg': '请先登录','status':0})

