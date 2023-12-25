import calculator
# 加法运算
print("请输入两个数字，进行加法运算：")
nums = input("两个数字（用空格分隔）：").split()
num1 = float(nums[0])
num2 = float(nums[1])
result = calculator.add(num1, num2)
print(f"{num1} + {num2} = {result}")

# 减法运算
print("请输入两个数字，进行减法运算：")
nums = input("两个数字（用空格分隔）：").split()
num1 = float(nums[0])
num2 = float(nums[1])
result = calculator.subtract(num1, num2)
print(f"{num1} - {num2} = {result}")

# 乘法运算
print("请输入两个数字，进行乘法运算：")
nums = input("两个数字（用空格分隔）：").split()
num1 = float(nums[0])
num2 = float(nums[1])
result = calculator.multiply(num1, num2)
print(f"{num1} × {num2} = {result}")

# 除法运算
print("请输入两个数字，进行除法运算：")
nums = input("两个数字（用空格分隔）：").split()
num1 = float(nums[0])
num2 = float(nums[1])
result = calculator.divide(num1, num2)
print(f"{num1} ÷ {num2} = {result}")