import numpy as np

#List of all english speaking countries codes
english_speaking_countries = [5170, 5309, 5502, 5303, 5305,5526, 5314, 5326,5339, 5308,5142, 5352, 5514, 5625, 5347, 5311, 5374,5390]


def import_data():
    return np.genfromtxt("befkbhalderstatkode.csv", delimiter=",", dtype=np.uint, skip_header=1)

def devide_nation(data):
    year_of_interest = 2015
    
    #getting the sum of all english speaking
    eng_mask = (data[:,0] == year_of_interest) & np.in1d(data[:,3], english_speaking_countries)
    eng_sum = np.sum(data[eng_mask][:,-1])

    #Getting the total sum
    total_mask = data[:,0] == year_of_interest
    total_sum = np.sum(data[total_mask][:,-1])

    #Getting the non native english speaking sum
    non_eng_sum = total_sum - eng_sum

    return {"eng_sum": eng_sum, "non_eng_sum": non_eng_sum}

def filter(data, mask): 
    return data[mask]

def topic_sum(data, topic):
    return np.sum(data[:,topic])

#returns a mask that require a specific year in the array
def year_mask(data, year):
    return data[:,0] == year

def german_development(data):
    #generating set of all years
    all_years = set(data[:,0])
   
    sum_per_year = {}
    for year in all_years:
        #creating mask restricting year and nationality to be german
        mask = (data[:,0] == year) & (data[:,-2] == 5180)
        
        #setting dict value of the year to the sum of people
        sum_per_year[year] = np.sum(data[mask][:,-1])
    
    return sum_per_year

    


