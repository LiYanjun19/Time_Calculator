## mode 1: input clock in, get lunch break start, lunch break end, clock out 
## mode 2: input clock in, lunch break start, get lunch break end, clock out
## mode 3: input clock in, lunch break start, lunch break end, get clock out
## mode 4: input clock out, get clock in, lunch break start, lunch break end, 

import math

workhour = 8    ## (hrs) input the working hours
lunchbreak = 30   ## (min) input the lunch break time in min
 
class HourMin:
    def __init__(self,hour, min):
        self.hour = hour
        self.min = min
    

def input_init(clock_in, lunchbreak_start, lunchbreak_end, clock_out):
    
    clockin = HourMin(0,0)
    lb_start = HourMin(0,0)
    lb_end = HourMin(0,0)
    clockout = HourMin(0,0)

    ## clock in
    if mode == 1 or mode == 2 or mode == 3: 
        if clock_in < 2400 and clock_in > 0:
            clock_in_hour = math.floor(clock_in/100)
            clock_in_min = clock_in - clock_in_hour*100
            if clock_in_min < 60 and clock_in_min >= 0:
                clockin = HourMin(clock_in_hour, clock_in_min)
            else: 
                print("clock in error")
                return 
        else: 
            print("clock in error")
            return

    ## lunch break start
    if mode == 2 or mode == 3: 
        if lunchbreak_start < 2400 and lunchbreak_start > clock_in:
            lunchbreak_start_hour = math.floor(lunchbreak_start/100)
            lunchbreak_start_min = lunchbreak_start - lunchbreak_start_hour*100
            if lunchbreak_start_min < 60 and lunchbreak_start_min >= 0:
                lb_start = HourMin(lunchbreak_start_hour, lunchbreak_start_min)
            else: 
                print("lunch break start error")
                return
        else: 
            print("lunch break start error")
            return
    
    ## lunch break end
    if mode == 3:
        if lunchbreak_end < 2400 and lunchbreak_end > lunchbreak_start:
            lunchbreak_end_hour = math.floor(lunchbreak_end/100)
            lunchbreak_end_min = lunchbreak_end - lunchbreak_end_hour*100
            if lunchbreak_end_min < 60 and lunchbreak_end_min >= 0:
                lb_end = HourMin(lunchbreak_end_hour, lunchbreak_end_min)
            else: 
                print("lunch break end error")
                return
        else: 
            print("lunch break end error")
            return

    ## clock out 
    if mode == 4:
        if clock_out < 2400 and clock_out > 0:
            clock_out_hour = math.floor(clock_out/100)
            clock_out_min = clock_out - clock_out_hour*100
            if clock_out_min < 60 and clock_out_min >=0:
                clockout = HourMin(clock_out_hour, clock_out_min)
    
            else:
                print("clock out error")
                return
        else: 
            print("clock out error")
            return
    
    
    return clockin, lb_start, lb_end, clockout

def time_add(time1, time2):
    min_sum = time1.min + time2.min
    hr_sum = time1.hour + time2.hour
    if min_sum > 60:
        hr_sum += 1
        min_sum -=60
    
    res = HourMin(hr_sum, min_sum)
    return res

def time_subr(time1, time2):
    if time2.min >= time1.min:
        min_res = time2.min - time1.min
        hr_res = time2.hour - time1.hour
    else:
        min_res = time2.min + 60 - time1.min
        hr_res = time2.hour - 1 - time1.hour
    
    res = HourMin(hr_res, min_res)
    return res


## select mode 
## input clockin time, lunch break starts time, lunch break ends tiem, clockout time
clock_in = lunchbreak_start = lunchbreak_end = clock_out = 0
mode = int(input("Which mode: "))
if mode == 1:
    clock_in = int(input('Please input the clockin time: '))
elif mode == 2:
    clock_in = int(input('Please input the clockin time: '))
    lunchbreak_start = int(input('Please input the lunch break starts time: '))
elif mode == 3:
    clock_in = int(input('Please input the clockin time: '))
    lunchbreak_start = int(input('Please input the lunch break starts time: '))
    lunchbreak_end = int(input('Please input the lunch break ends tiem: '))
elif mode == 4:
    clock_out = int(input('Please input the clockout time: '))

## init work time and lunch break time
if workhour < 0 or lunchbreak < 0:
    print("check define")
worktime = HourMin(workhour, 0)
lunchbreak_hour = lunchbreak // 60
lunchbreak_min = lunchbreak % 60
breaktime = HourMin(lunchbreak_hour, lunchbreak_min)



## init inputs
clockin, lb_start, lb_end, clockout = input_init(clock_in, lunchbreak_start, lunchbreak_end, clock_out)


## calculate 
match mode:
    case 0:
        print("input error")
    case 1: 
        
        if workhour % 2 != 0:
            worktime_half = HourMin(workhour//2, 30)
        else: 
            worktime_half = HourMin(workhour//2, 0)
        new_lb_start = time_add(clockin, worktime_half)
        new_lb_end = time_add(new_lb_start, breaktime)
        new_clockout = time_add(new_lb_end, worktime_half)
    case 2:
        temp = time_subr(clockin, lb_start)
        worktime_rest = time_subr(temp, worktime)
        new_lb_end = time_add(lb_start, breaktime)
        new_clockout = time_add(new_lb_end, worktime_rest)
    case 3: 
        temp = time_subr(clockin, lb_start)
        worktime_rest = time_subr(temp, worktime)
        new_clockout = time_add(lb_end, worktime_rest)
    case 4:
        if workhour % 2 != 0:
            worktime_half = HourMin(workhour//2, 30)
        else: 
            worktime_half = HourMin(workhour//2, 0)
        new_lb_end = time_subr(worktime_half, clockout)
        new_lb_start = time_subr(breaktime, new_lb_end)
        new_clockin = time_subr(worktime_half, new_lb_start)


## output 
match mode:
    case 0:
        print("input error")
    case 1:
        new_lb_start.min = "%02d" % new_lb_start.min
        new_lb_start.hour = "%02d" % new_lb_start.hour
        new_lb_end.min = "%02d" % new_lb_end.min
        new_clockout.min = "%02d" % new_clockout.min
        print("Take lunch break at: ", new_lb_start.hour, end="")
        print(new_lb_start.min)
        print("End lunch break at: ", new_lb_end.hour, end="")
        print(new_lb_end.min)
        print("Clock out at: ", new_clockout.hour, end="")
        print(new_clockout.min)
    case 2:
        new_lb_end.min = "%02d" % new_lb_end.min
        new_clockout.min = "%02d" % new_clockout.min
        print("End lunch break at: ", new_lb_end.hour, end="")
        print(new_lb_end.min)
        print("Clock out at: ", new_clockout.hour, end="")
        print(new_clockout.min)
    case 3:
        new_clockout.min = "%02d" % new_clockout.min
        print("Clock out at: ", new_clockout.hour, end="")
        print(new_clockout.min)
    case 4:
        new_clockin.min =  "%02d" % new_clockin.min
        new_clockin.hour =  "%02d" % new_clockin.hour
        new_lb_start.min = "%02d" % new_lb_start.min
        new_lb_start.hour = "%02d" % new_lb_start.hour
        new_lb_end.min = "%02d" % new_lb_end.min
        print("Clock in at: ", new_clockin.hour, end="")
        print(new_clockin.min)
        print("Take lunch break at: ", new_lb_start.hour, end="")
        print(new_lb_start.min)
        print("End lunch break at: ", new_lb_end.hour, end="")
        print(new_lb_end.min)
        