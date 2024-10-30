try:
    nums = [int(i) for i in input().split(",")]
except Exception as e:
    print("your input is invalid")
    exit(1)

print("largest number: ", max(nums), ", count: ", nums.count(max(nums)), sep="") # sep set to "" to avoid unnecessary spaces
