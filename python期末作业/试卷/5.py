import random
import csv

# 生成随机整数并写入CSV文件
random_numbers = [random.randint(1, 1000) for _ in range(1000)]

with open('random_numbers.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(random_numbers)

print("随机整数已写入文件 'random_numbers.csv'。")

# 从文件中读取数据并排序
with open('random_numbers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data = [int(number) for number in row]
        sorted_data = sorted(data)

# 输出排序后的结果
print("排序后的结果：", sorted_data)
