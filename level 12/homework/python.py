number = int(input("აირჩიეთ რიცხვი 1-დან 7-ის ჩათვლით: "))

if number == 1:
    day = "ორშაბათი"
elif number == 2:
    day = "სამშაბათი"
elif number == 3:
    day = "ოთხშაბათი"
elif number == 4:
    day = "ხუთშაბათი"
elif number == 5:
    day = "პარასკევი"
elif number == 6:
    day = "შაბათი"
elif number == 7:
    day = "კვირა"
else:
    day = "არასწორი რიცხვი. გთხოვთ აირჩიოთ 1-დან 7-ის ჩათვლით."

print(f"შენ აირჩიე: {day}")