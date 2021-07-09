# Tuples and Namedtuples in Python

## Part 1 - Is Namedtuples faster than dicstionaries?

The 4 step problem definition :

1. **Data**: Get data of random people with blood type, location, age etc. 
	**Solution**: Used the Faker library to get 10000 random profiles. 

2. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age.

3. Do the same thing above using a dictionary. 

4. Prove that namedtuple is faster.


### Solution - Part 1

1. Generated the 10000 fake profiles uing the faker library.

```
def get_fake_profiles(type, count):
    fake_profiles = []
    if type == 'namedtuple':
        profile = namedtuple('Profile', ['job', 'company', 'ssn', 'residence', 'current_location','blood_group', 'website', 'username', 'name', 'sex','address', 'mail', 'birthdate'])
        for _ in range(count):
            fake_profiles.append(profile(**fake.profile()))
    elif type == 'dict':
        for _ in range(count):
            fake_profiles.append(fake.profile())
    return fake_profiles
```

2. Identified the givn requirements using following functions. These are designed for both namedtuple and dictionary.

	- Find the oldest birthdate from the given data.
		```
		def get_oldest_birthdate(collection, type):
			oldest_birthdate = None
			if type == 'namedtuple':
				oldest_birthdate = min(collection, key=lambda a: a.birthdate).birthdate
			elif type == 'dict':
				oldest_birthdate = min(collection, key=lambda a: a['birthdate'])['birthdate']
			return oldest_birthdate
		```

	- Find the average age of the persons.
		```
		def get_average_age(collection, type):
			if type == 'namedtuple':
			return sum([relativedelta(date.today(), a.birthdate).years for a in collection])/len(collection)
			elif type == 'dict':
				return sum([relativedelta(date.today(), a['birthdate']).years for a in collection])/len(collection)
		```

	- Find the average time.
		```
		def get_average_time(n, func, *args, **kwargs):
			start = perf_counter()
			for i in range(n):
				value = func(*args, **kwargs)
			avg_run_time = (perf_counter() - start)/n
			return avg_run_time
		```

3. Profiling the both cases of namedtuple and dictionary. 

```
def faster(N,func,fake_profiles,fake_profiles_dict):
    t1 = get_average_time(N, func, fake_profiles, 'namedtuple')
    t2 = get_average_time(N, func, fake_profiles_dict, 'dict')
    if t1 < t2:
        return 'dict is faster'
    else:
        return 'named tuple is faster'
```

**Results** - In most of the cases, the implementation of namedtuples is found to be faster over disctionary.


----

## Part 2 - Compuations using Namedtuples

The 4 step problem definition :

1. **Data**: We are using here the fake data of Stock Market having points like name of stock, symbol of stock, market day open price, market day high price, market daya close price.
	**Solution**: Used the Faker library to get fake stock exchange data. 

2. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end.


### Solution - Part 2

The namedtuple is defined as `company_stck = namedtuple('Company', ['name', 'symbol', 'open', 'low', 'high', 'close','weight'])`. It has 7 features.

1. Generating the fake stock exchange data.

```
def get_company_stock(volatility,direction):              
    name = fake.unique.company()
    symbol = name[0:3].upper()+name[-3:].upper()
    open = round( uniform(10,1000),2)
    if direction == '-ve':
        volatility *= -1
    close =  round(open + (open * volatility * 0.2),2)
    high = close = round(open + (open * volatility * 0.5),2)
    low = close = round(open - (open * volatility * 0.5),2)
    return name, symbol, open, high,low, close
```

2. Wrting the functions to find the open, high and close price of a stock.

	- The stock open price
		```
		def stock_market_open(stock_list):
			stock_list.sort(key = lambda a: a.weight)
			st_open = sum([a.open for a in stock_list[:50]])
			print('stock market opened at:',st_open)
			return st_open
		```

	- The stock high price
		```
		def stock_market_high(stock_list):
			stock_list.sort(key = lambda a: a.weight)
			st_high = sum([a.high for a in stock_list[:50]])
			print('stock market highest value was:',st_high)
			return st_high
		```

	- The stock close price
		```
		def stock_market_close(stock_list):
			stock_list.sort(key = lambda a: a.weight)
			st_close = sum([a.close for a in stock_list[:50]])
			print('stock market closed at:',st_close)
			return st_close
		```


# Test cases

Both the problem solutions are tested against numerous test cases. All the test cases can be found in file `test_session9.py`.