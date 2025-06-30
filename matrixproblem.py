r1=['💀','💀','💀']
r2=['💀','💀','💀']
r3=['💀','💀','💀']
print(f"{r1}\n{r2}\n{r3}")
matrix=[r1,r2,r3]
choice=input("Enter the position where you want to store your money :")
row_choice=int(choice[0])
column_choice=int(choice[1])
row_select=matrix[row_choice-1]
row_select[column_choice-1]="X"
print(f"{r1}\n{r2}\n{r3}")
 