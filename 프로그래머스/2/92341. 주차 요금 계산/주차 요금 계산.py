import math

def solution(fees, records):
    answer = []
    cars = dict()
    cars_record = dict()
    
    basic_time, basic_fee, over_unit_time, over_unit_fee = fees
    
    for record in records:
        record = record.split()
        car_time, car_number, car_type = record
        
        if car_type == "OUT":
            in_time = cars_record[car_number]
            del cars_record[car_number]
                    
            parked_time = cal_time(in_time, car_time)
            cars[car_number] = cars.get(car_number, 0) + parked_time
        else:
            cars_record[car_number] = car_time
    
    for car_number, car_time in cars_record.items():
        parked_time = cal_time(car_time, "23:59")
        cars[car_number] = cars.get(car_number, 0) + parked_time
        
    print(cars.items())
    
    for car_number, value in cars.items():
        if value <= basic_time:
            answer.append([car_number, basic_fee])
        else:
            answer.append([car_number, basic_fee + math.ceil((value - basic_time) / over_unit_time) * over_unit_fee])
    
    answer.sort()
    
    return list(map(lambda row: row[1], answer))

def split_time(time):
    hour, minute = map(int, time.split(":"))
    return hour, minute

def cal_time(in_time, out_time):
    in_hour, in_minute = split_time(in_time)
    out_hour, out_minute = split_time(out_time)
    
    return ((out_hour * 60) + out_minute) - ((in_hour * 60) + in_minute)
