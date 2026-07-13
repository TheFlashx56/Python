marks1 = int(input("Enter marks 1 :"))
marks2 = int(input("Enter marks 2 :"))
marks3 = int(input("Enter marks 3 :"))

# check for total percentage
total_percentage = ((marks1 + marks2 + marks3) * 100) / 300

if (
    total_percentage > 40
    and total_percentage <= 100
    and marks1 >= 33
    and marks2 >= 33
    and marks3 >= 33
):
    print(f"You are Pass with percentage of {total_percentage}%")
elif total_percentage <= 40 and total_percentage >= 0:
    print(f"Total percentage is {total_percentage},You are Failed")
