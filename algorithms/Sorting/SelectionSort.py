def selection_sort(inp_list):
	for i in range(len(inp_list)):
		pos = i;
		for j in range(i+1, len(inp_list)):
			if inp_list[pos] > inp_list[j]:
				pos = j;
		inp_list[i], inp_list[pos] = inp_list[pos], inp_list[i];

Array = []
size = int(input("Input Array Size in integer: "));
for i in range(0, size):
	Array.append(input()); 

selection_sort(Array);

for i in range(len(Array)):
	print(Array[i], end = " "); 
print();