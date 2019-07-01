country = input("国家: ")
age = int(input("年龄: "))
if country == "马来西亚":
    if age >= 18:
        print("你可以考驾驶执照了")
    else:
        print("你还不可以考驾驶执照")
elif country == "美国":
    if age >= 16:
        print("你可以考驾驶执照了")
    else:
        print("你还不可以考驾驶执照")
