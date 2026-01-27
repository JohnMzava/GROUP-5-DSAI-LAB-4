subjects = ["Math", "Physics", "Chemistry", "Biology", "CS"]

# adds civics to a list
subjects.append('Civics')
print(subjects)

# adds English to a defined index 0
subjects.insert(0,'English')
print(subjects)

#Removes Physics from a list
subjects.remove('Physics')
print(subjects)

#removes using index
subjects.pop(3)
print(subjects)

#arrange values in alphabetic order within a list
subjects.sort()
print(subjects)

#reverse to the previous order
subjects.reverse()
print (subjects)