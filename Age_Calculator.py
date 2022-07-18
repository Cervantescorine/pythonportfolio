print("Hello, let's figure out your age!\n")
year_of_birth = input ("Please enter the year you were born:  ")
current_year = input ("Please enter the current year:  ")
age_result = int(current_year) - int(year_of_birth)

# no spaces needed after be" and before "by"
print( str("You will be") , age_result , str("by the end of the year."))
