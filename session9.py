import collections
from datetime import date
from dateutil.relativedelta import *
from faker import Faker
from collections import namedtuple, Counter
from time import perf_counter
from functools import wraps
from random import shuffle, seed, randint, uniform, choice, sample
from faker.providers.company import Provider

Faker.seed(1)
fake = Faker()

def get_fake_profiles(type: str, count: int):
    '''
	it has two parameter:
	   1) type - dict , namedtuple
	   2) count - no. of fake profiles
	In this function we will create a count number of fake profile with there respective type
    '''
    fake_profiles = []
    if type == 'namedtuple':
        profile = namedtuple('Profile', ['job', 'company', 'ssn', 'residence', 'current_location',
                                         'blood_group', 'website', 'username', 'name', 'sex', 'address', 'mail', 'birthdate'])
        for _ in range(count):
            fake_profiles.append(profile(**fake.profile()))
    elif type == 'dict':
        for _ in range(count):
            fake_profiles.append(fake.profile())
    return fake_profiles


def get_largest_blood_group(collection: list, type: str):
    '''
	this funtion also have two parameter:
	   1) collection - collection of fake profiles
	   2) type - dict , namedtuple
	this basically return the most common blood group with count
    '''
    bg_counts = None
    if type == 'namedtuple':
        bg_counts = Counter(p.blood_group for p in collection)
    elif type == 'dict':
        bg_counts = Counter(p['blood_group'] for p in collection)
    return bg_counts.most_common()[0]


def get_oldest_birthdate(collection: list, type: str):
    '''
	this funtion also have two parameter:
	   1) collection - collection of fake profiles
	   2) type - dict , namedtuple
	this basically return the oldest birthday amoung the given collection
    '''
    oldest_birthdate = None
    if type == 'namedtuple':
        oldest_birthdate = min(
            collection, key=lambda a: a.birthdate).birthdate
    elif type == 'dict':
        oldest_birthdate = min(
            collection, key=lambda a: a['birthdate'])['birthdate']
    return oldest_birthdate


def get_average_age(collection: list, type: str):
    '''
	this funtion also have two parameter:
	   1) collection - collection of fake profiles
	   2) type - dict , namedtuple
	this basically return the average age amoung the given collection
    '''
    if type == 'namedtuple':
        return sum([relativedelta(date.today(), a.birthdate).years for a in collection])/len(collection)
    elif type == 'dict':
        return sum([relativedelta(date.today(), a['birthdate']).years for a in collection])/len(collection)


def get_average_time(n: int, func: 'funtion', *args, **kwargs):
    '''
    this basically return the running time of the given function upto n times
    '''
    start = perf_counter()
    for i in range(n):
        value = func(*args, **kwargs)
    avg_run_time = (perf_counter() - start)/n
    return avg_run_time


def faster(N: int,func: 'function',fake_profiles,fake_profiles_dict):
    '''
    this function has 4 parameter:
       1) N - no. of times it should run
       2) func - function
       3) fake_profiles - namedtuple fake profiles
       4) fake_profiles_dict - dictionary fake profile
    this function basically tells which is faster namedtuple or dictionary
    '''
    t1 = get_average_time(N, func, fake_profiles, 'namedtuple')
    t2 = get_average_time(N, func, fake_profiles_dict, 'dict')
    if t1 < t2:
        return 'dict is faster'
    else:
        return 'named tuple is faster'


company_stck = namedtuple('Company', ['name', 'symbol', 'open', 'low', 'high', 'close','weight'])

def get_company_stock(volatility,direction):   
    '''
    this function basically create fake company stocks
    '''           
    name = fake.unique.company()
    symbol = name[0:3].upper()+name[-3:].upper()
    open = round( uniform(10,1000),2)
    if direction == '-ve':
        volatility *= -1
    close =  round(open + (open * volatility * 0.2),2)
    high = close = round(open + (open * volatility * 0.5),2)
    low = close = round(open - (open * volatility * 0.5),2)
    return name, symbol, open, high,low, close


def stock_market_open(stock_list: list):
    '''
    this function tells us at which point market is open
    '''
    stock_list.sort(key = lambda a: a.weight)
    st_open = sum([a.open for a in stock_list[:50]])
    print('stock market opened at:',st_open)
    return st_open

def stock_market_high(stock_list: list):
	'''
    this function tells us at which point market is high
    '''
	stock_list.sort(key = lambda a: a.weight)
	st_high = sum([a.high for a in stock_list[:50]])
	print('stock market highest value was:',st_high)
	return st_high

def stock_market_close(stock_list: list):
	'''
    this function tells us at which point market is close
    '''
	stock_list.sort(key = lambda a: a.weight)
	st_close = sum([a.close for a in stock_list[:50]])
	print('stock market closed at:',st_close)
	return st_close