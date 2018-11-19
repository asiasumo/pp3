tab = [7,5,[3,6,[2]],7,[1,[2,3,[4]],9,2],4]
def sum(tab):
	suma=0
	for elem in tab:
		if type(elem) == list:
			suma += sum(elem)               
		else:
			suma+=elem     
	return suma
print(sum(tab))



