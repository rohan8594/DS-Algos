def insertion_sort(inp_list):
	for i in range(1, len(inp_list)):
		element = inp_list[i];
		j = i - 1;
		while j >= 0 and element < inp_list[j]:
			inp_list[j + 1] = inp_list[j];
			j -= 1;
		inp_list[j + 1] = element;

Array = []
size = int(input("Input Array Size in integer: "));
for i in range(0, size):
	Array.append(input()); 

insertion_sort(Array);

for i in range(len(Array)):
	print(Array[i], end = " "); 
print();