def dollar_to_euro(dollar_value):
	return dollar_value * 0.91

def euro_to_yen(euro_value):
	return euro_value * 161.70

####### ↓ YOUR CODE BELOW ↓ #######
dollar_euro = dollar_to_euro(137)
euro_yen = euro_to_yen(dollar_euro)
yen_dollar = euro_yen * 137 
print(yen_dollar)