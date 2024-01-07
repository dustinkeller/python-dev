# import modules.test.shopping.more_shopping.shopping_cart as shop
from shopping.more_shopping.shopping_cart import buy
from shopping.more_shopping import shopping_cart
from shopping.more_shopping.shopping_cart import max as maximum
from utility import multiply, divide


if __name__ == '__main__':
    print('please run this')
    # print(shopping_cart.max([1,2,3]))

    print(maximum([1,2,3]))
    print(max([1,2,3]))
    x = multiply(1,2)
    print(buy("cup"))  

    print(__name__) #prints out __main__
    # the file that we run is always given the name __main__