price=0
size=''
# size=input('enter the pizza size:')
while size not in ['l','m','s']:
    print("choose the correcr size among l,m,s")
    size=input('enter the pizza size:')
if size=='l':
    price=30
elif size=='m':
    price=25
elif size=='s':
    price=20

if input("want pepparoni?") == 'y':
    if size=='s':
        price+=2
    else:
        price+=3
if input("want some extra cheese?")=='y':
    price+=5
    
cgst=0.1*price
sgst=0.15*price
check=price+cgst+sgst
print(f"your final bill is ${check}")
