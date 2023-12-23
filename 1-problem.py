summ=0
caunt=0
while(1):
    a=input(">>> ")
    try:
        a=int(a)
        summ+=a
        caunt+=1
    except:
        if a=="c":
            break
        else:
            continue
print(f"Sum of {caunt} numbers: {summ}")