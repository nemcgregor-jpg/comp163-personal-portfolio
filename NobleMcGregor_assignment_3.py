import math 
# stores user data (strings)
full_name = "Jordan Smith"
email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
grad_date = "Spring 2028"
major = "Computer Science"

# stores academic data organization (lists)
current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

# stores contact info (tuples)
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram = ("Instagram", "@jordan_codes", "312")
twitter = ("Twitter", "@jordandev", "127")
birthday = ("Birthday", "5, 22", "2006") 

# takes the info from the tuples and turns them into integers so they can be added to find all social followers
instagram_followers = int(instagram[2])
twitter_followers = int(twitter[2])
social_followers = instagram_followers + twitter_followers


# stores interest tracking (sets)
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography" }
skills_to_learn = {"Data structures", "Web design", "JavaScript", "Git", "Public speaking"}
career_interest = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# stores organizational mapping (dictionaries)
course_credits = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
study_hours = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
contacts = {"Mom": "704-555-0199", "Roomate": "336-555-7821", "Academic Advisor": "336-334-5000"}

daily_food_budget = monthly_budget["Food"] / 30
study_hourly_cost = monthly_budget["Books"] / 25

print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
# takes info from strings to find students info
print(f"Student: {full_name} | Email: {email}")
print(f"From: {hometown} | Graduating: {grad_date}")
print(f"Major: {major}")
print()
print("=== ACADEMIC PROFILE ===")
# gets the sum of the credit hours and current courses in the lists 
print(f"Current Semester: {sum(credit_hours)} credits across {len(current_courses)} courses")
# finds cumulative GPA by getting the sum from the gpa history list and dividing it by the amount of gpas there were
print(f"Cumulative GPA: {sum(gpa_history) / 4:.2f}")
# calculates study hours by addressing the dictionary for the class names and their values and adding
print(f"Weekly Study Time: {study_hours['Programming'] + study_hours['Math'] + study_hours['English'] + study_hours['History']} hours")
# finds academic investment by dividing the books by weekly study time
print(f"Academic Investment: ${monthly_budget['Books'] / 25} per study hour")
print()
print("Current Courses:")
# addresses lists to find what the classes are, how many hours they have, what the professors are, and what rooms they are in
print(f"{current_courses[0]} - {credit_hours[0]} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"{current_courses[1]} - {credit_hours[1]} credits - {course_professors['MATH 150']} - {course_rooms['MATH 150']}")
print(f"{current_courses[2]} - {credit_hours[2]} credits - {course_professors['ENG 101']} - {course_rooms['ENG 101']}")
print(f"{current_courses[3]} - {credit_hours[3]} credits - {course_professors['HIS 105']} - {course_rooms['HIS 105']}")
print()
print("=== PERSONAL DEVELOPMENT ===")
# Takes info from sets and prints
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_interest}")
# Takes info from sets and find sthe length of the items in the sets
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}")
print()
print("=== FINANCIAL OVERVIEW ===")

print(f"Monthly Budget: ${monthly_budget['Food'] + monthly_budget['Entertainment'] + monthly_budget['Books'] + monthly_budget['Transportation']}")
print(f"Food: ${monthly_budget['Food']} (${monthly_budget['Food'] / 30}/day)")
print(f"Daily Food Budget: ${round(daily_food_budget)}")
print(f"Study Hourly Cost: ${round(study_hourly_cost):.2f}")
print(f"Entertainment: ${monthly_budget['Entertainment']}")
print(f"Books: ${monthly_budget['Books']}")
print(f"Transportation: ${monthly_budget['Transportation']}")
print(f"Annual Projection: ${(monthly_budget['Food'] + monthly_budget['Entertainment'] + monthly_budget['Books'] + monthly_budget['Transportation']) * 12}")
print()
print("=== CONNECTIONS & CONTACTS ===")
# finds contacts and home address by taking the values from the tuples
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {social_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contacts)} people in directory")
print()
print("=== LIFE STATISTICS ===")
# gets length of courses, hobbies, and entertainment backlog from sets and finds academic workload by adding credit hours and study hours from lists
print(f"Total Courses Completed: {len(completed_courses)}")
print(f"Current Academic Load: {credit_hours[0] + credit_hours[1] + credit_hours[2] + credit_hours[3] + study_hours['Programming'] + study_hours['Math'] + study_hours['English'] + study_hours['History']} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("================================================================")
