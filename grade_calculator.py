# kukunin ang grade percentage sa user
percentage = float(input("Enter your grade percentage (0-100): "))

# Check if nasa range ang ilalagay na input kung valid or hindi
if percentage < 0 or percentage > 100:
    print("Error: Please enter a percentage between 0 and 100")
else:
    # determine kung saan percentage ang grade ng user
    if percentage >= 90:
        print("Grade: A (Excellent)")
    elif percentage >= 80:
        print("Grade: B (Good)")
    elif percentage >= 70:
        print("Grade: C (Average)")
    elif percentage >= 60:
        print("Grade: D (Needs Improvement)")
    else:
        print("Grade: F (Fail)")