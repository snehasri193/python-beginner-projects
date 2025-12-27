# Initialize count to store how many numbers are divisible by 3
count = 0
for i in range(1,31):
  
    # Check if the number is divisible by 3
    if i %3 ==0:
        print(i)
        count +=1    # Increase the count

# Print the total count of numbers divisible by 3
print("Total no. of numbers divisible by 3: ", count)
