# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total=0
num=0
for i in student_heights:
  total=total+ i
  num+=1

print(total)  
print(num)
average=round(total/num);
print(f"Average sum of heights is {average}\n")


