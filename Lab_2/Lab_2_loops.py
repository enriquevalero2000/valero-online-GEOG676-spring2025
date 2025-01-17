#Q1: Multiply items together
q1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
final1 = 1

for i in q1:
    final1 = final1 * i

print("Answer to Question 1 is: ", final1)

#Q2: Add items together
q2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
final2 = 0

for i in q2:
    final2 = final2 + i

print("Answer to Question 2 is: ", final2)

#Q3: Add only even items together
q3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]
final3 = 0
q3even = []

for i in q3:
    if i % 2 == 0:
        q3even.append(i)
        final3 = final3 + i

print("Answer to Question 3 is: ", final3)