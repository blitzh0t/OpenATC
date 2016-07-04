import timeit
import requests
from bs4 import BeatifulSoup as bs
from getconf import *

base_url = 'http://www.adidas.com'
sizes = {
  650: '10',
  660: '10.5',
  670: '11',
  680: '11.5',
  690: '12'
}

def add_to_cart():
  #add to cart
  cart_url = 'http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct'
  print('Checking out')
  payload = {
    'layer': 'Add To Bag overlay',
    'pid': 'BB3933_660',
    'Quantity': 1,
    'masterPid': 'BB3933',
    'ajax': true
  }

  req.post(cart_url, data=payload)