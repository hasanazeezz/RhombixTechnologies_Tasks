# Fibonacci Generator For My Internship At Rhombix Technologies
n = int(input("Enter the number of terms: "))
a, b = 0, 1

if n <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        