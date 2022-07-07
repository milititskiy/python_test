import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    #to list
    reader = csv.reader(csv_file)
    data = list(reader)
    print(data)

    #to dictionary
    dict = csv.DictReader(csv_file)
    for line in dict:
        print(line)


    #to tuple



    #to set

    # for line in csv_reader:
    #     print(line['first_name'])

    with open('new_names.scv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)





# from inspect import stack
# import queue

# stack = []
# stack.append(1)
# stack.append(2)

# pop_elem = stack.pop()

# print(stack)

# queue = []
# queue.append(1)
# queue.append(2)

# pop_elem = queue.pop(0)

# print(queue)

# lst = [1,2,3,4,5,6,7]

# even_lst = [x for x in lst if x % 2 == 0]
# print(even_lst)

# square_lst  = [x ** 2 for x in lst]
# print(square_lst)

# from collections import Counter

# numbers = [1,1,5,2,3,5,2,1,4]

# counts = Counter(numbers)

# # print(counts)

# top2 = counts.most_common(2)
# print(top2)
