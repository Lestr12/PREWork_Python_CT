
#Question 1

def hello_name(user_name):
 print(user_name)

hello_name("hello_USERNAME")

# Question 2

def first_odds(i):
  return

for i in range(1,100):
     if i%2!=0:
        print(i)

first_odds(i)

# Question 3

def max_num_in_list(a_list):
   
   max = a_list[0]
   for num in a_list:
     if (num > max):
      max = num

   return max
   
a_list = [1,2,3,4,54,78]

max=max_num_in_list(a_list)

print("Maximum num : " , max)

 
               
# Question 4

def is_leap_year(a_year): 
    if (a_year%4==0):
        print("it is a leap year")
        return True
    elif (a_year%100!=0) or (a_year%400==0):
        print("it is not a leap year")
        return False
    
print(is_leap_year(2024))
    
# Question 5


def is_consecutive(a_list):
    for i in range(0,len(a_list)-1):
        if (a_list[i]+1) != a_list[i+1]:
          return False
    else:
          return True

print(is_consecutive([1,2,9,4,5]))
        
   






