def chcek(data):
    data = list(data)
    count = []
    for i in data:
        if i in data:
            print("Yes")
            return
        else:
            count.append(i)

    print("No")
    return 


data  = input()
chcek(data)