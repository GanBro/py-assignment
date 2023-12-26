import random
import csv

random_numbers = [random.randint(1, 1000) for tmp in range(1000)]
with open('random_numbers.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(random_numbers)
print("随机整数已写入文件 'random_numbers.csv'。。。")
with open('random_numbers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data = [int(number) for number in row]
        sorted_data = sorted(data)
print("排序后的结果：", sorted_data)
