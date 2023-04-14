def greet(*names):
    for name in names:
        print(f"Hello, ${name}" )

def sum(*numbers):
    answer=0
    for num in numbers:
        answer+=num
    return answer

#Write a function any number of intergers snd returns the result multiplied by all
def product(*nums):
    times=1
    for n in nums:
        times*=n
    return times

def study(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}") 

def my_country(country="Kenya"):
    print(f"Hello my country is {country}")

#A function named concatenate_args that takes any number of string arguments 
# in positional arguments format and concatenates them into a single string

def concatenate_args(*shapes):
    new="".join(shapes)
    return new

print(concatenate_args("square,","circle,","star"))

#A function named concatenate_kwargs that takes any number of string arguments
#in keyword arguments format and concatenates them into a single string

def concatenate_kwargs(**business):
    newbrand=str()

    for key in business:
        newbrand += key + ": " + business[key] + ", "

    return newbrand
concatenate_kwargs(brand="Fila",product="shoes")





