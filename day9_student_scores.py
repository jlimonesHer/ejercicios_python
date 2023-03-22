# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day9_student_scores.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: user <user@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/08 13:08:52 by user              #+#    #+#              #
#    Updated: 2022/11/08 13:08:54 by user             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] < 71:
        student_grades[key] ="Fail"
    elif student_scores[key] < 81:
        student_grades[key] ="Acceptable"
    elif student_scores[key] < 91:
        student_grades[key] ="Exceeds Expectations"
    elif student_scores[key] > 90 :
        student_grades[key] ="Outsanding"


# 🚨 Don't change the code below 👇
    print(key + ":")
    print(student_grades[key])

