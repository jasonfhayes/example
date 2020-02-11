import random
my_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
how_many = int(input('How many rolls? '))
for i in range(how_many):
	total = (random.randrange(1, 7)) + (random.randrange(1, 7))
	my_dict[total] = my_dict[total] + 1
print('\nTotal:\tCount:\tPercetage:')
for i in range(2, 13):
	my_very_special_number = ('{:.1f}'.format((my_dict[i]/how_many)*100))
	print(f'{i}:\t{my_dict[i]}\t{my_very_special_number}%')
	
## Hello Worlds