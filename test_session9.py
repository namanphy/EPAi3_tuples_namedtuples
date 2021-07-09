import pytest
import session9
from random import shuffle, seed, randint, uniform, choice, sample
from collections import namedtuple, Counter

NO_OF_PROFILES = 100
fake_profiles = session9.get_fake_profiles('namedtuple', NO_OF_PROFILES)
fake_profiles_dict = session9.get_fake_profiles('dict', NO_OF_PROFILES)
weights = sample(range(1,200),100)
company_stck = namedtuple('Company', ['name', 'symbol', 'open', 'low', 'high', 'close','weight'])

def test_get_fake_profiles_named_tuple():
	assert type(session9.get_average_age(fake_profiles,'namedtuple')) == float,"fake profile(namedtuple) does not get created"

def test_get_fake_profiles_named_dictionary():
	assert type(session9.get_average_age(fake_profiles_dict,'dict')) == float,"fake profile(dictionary) does not get created"

def test_get_largest_blood_group():
	assert type(session9.get_largest_blood_group(fake_profiles,'namedtuple')) == tuple,"did not give tuple of blood group with count"

def test_get_oldest_birthdate():
	assert str(type(session9.get_oldest_birthdate(fake_profiles,'namedtuple'))) == "<class 'datetime.date'>","did not give date of birth"

def test_get_average_age():
	assert type(session9.get_average_age(fake_profiles,'namedtuple')) == float,"did not give date of birth"

def test_faster_get_average_age():
	N = 100
	a = session9.faster(N,session9.get_average_age,fake_profiles,fake_profiles_dict)
	assert a == 'named tuple is faster',"dictionary is faster"

def test_faster_get_largest_blood_group():
	N = 100
	a = session9.faster(N,session9.get_largest_blood_group,fake_profiles,fake_profiles_dict)
	assert a == 'named tuple is faster',"dictionary is faster"

def test_faster_get_oldest_birthdate():
	N = 100
	a = session9.faster(N,session9.get_oldest_birthdate,fake_profiles,fake_profiles_dict)
	assert a == 'named tuple is faster',"dictionary is faster"

def test_get_average_time():
	def add(x,y):
		return x+y

	n = session9.get_average_time(1000,add,10,35)
	assert type(n) == float,"it should give time in float value"

def test_faster_get_fake_profiles():
	N = 100
	a = session9.faster(N,session9.get_fake_profiles,fake_profiles,fake_profiles_dict)
	assert a == 'named tuple is faster',"dictionary is faster"

def test_get_company_stock():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	assert len(stock_list) == 100,"100 stock list should be created"

def test_stock_market_open():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	a = session9.stock_market_open(stock_list)
	assert type(a) == float,"it should return stock open market in float"

def test_stock_market_high():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	a = session9.stock_market_high(stock_list)
	assert type(a) == float,"it should return stock high market in float"

def test_stock_market_close():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	a = session9.stock_market_close(stock_list)
	assert type(a) == float,"it should return stock close market in float"

def test_get_company_stoc_len():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	assert len(stock_list[0]) == 7,"length of namedtuple should be 7"

def test_get_company_stoc_name():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	assert type(stock_list[0].name) == str,"type of name should be string"

def test_get_company_stoc_symbol():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	assert type(stock_list[0].symbol) == str,"type of symbol should be string"

def test_get_company_stoc_open():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	assert type(stock_list[0].open) == float,"type of open should be float"

def test_get_company_stoc_close():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	assert type(stock_list[0].close) == float,"type of close should be float"

def test_get_company_stoc_weight():
	stock_list = [company_stck(*session9.get_company_stock(volatility = uniform(.02, .2),direction=choice(['+ve','-ve'])),w) for w in weights]
	assert type(stock_list[0].weight) == int,"type of weight should be int"

