class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
    def __init__(self): # definindo os valores de hour, minute e second 
        self.hour = 0
        self.minute = 0
        self.second = 0

time = Time()
time.hour = 21
time.minute = 19
time.second = 24

print(time.hour)

print(type(time))

def format_time_less_than_zero(hour):
    if hour < 10:
        return '0' + str(hour)
    else:
        return str(hour)

def print_time(time):
    hour = format_time_less_than_zero(time.hour) 
    minute = format_time_less_than_zero(time.minute)
    second = format_time_less_than_zero(time.second)

    print(hour + ':' + second + ':' + minute)

print_time(time)


def is_after(t1, t2):
    print((t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second))

time_one = Time()

time_one.hour = 10
time_one.minute = 13
time_one.second = 22

time.hour = 9
time.minute = 12
time.second = 32

is_after(time_one, time)

def add_time(t1, t2): #função pura, não altera nenhum dos objetos passados a ela como argumentos
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    return sum

#melhorando o add_time
def new_add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second = 0
duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0
done = add_time(start, duration)
print_time(done)

