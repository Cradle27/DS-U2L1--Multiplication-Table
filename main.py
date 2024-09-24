



# ONE LINE - NO MORE, NO LESS

table = [(num + 1) * (num2 + 1) for num in range(10) for num2 in range(10)]



########### NO TOUCHY ###########
for i, num in enumerate(table):
    if i % 10 == 0:
        print()
    
    print(num, end="\t")
print()
#################################