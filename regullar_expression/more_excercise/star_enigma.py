import re

number = int(input())
message_list = []

for n in range(number):
    message = input()
    count = 0
    for el in message.lower():
        if el == "s" or el=="t" or el=="a" or el=="r":
            count += 1

    new_message = ""
    for el in message:
        new_message += chr(ord(el) - count)

    message_list.append(new_message)

pattern = r"@(?P<planet>[A-Za-z]+)[^-@!>:]*?\:(?P<population>\d+)[^-@!>:]*?!(?P<action>A|D)![^-@!>:]*?\-\>(?P<soldiers>\d+)[^-@!>:]*?"

attacked_planet = []
destroyed_planet = []
for el in message_list:
    names = re.finditer(pattern, el)
    for name in names:
        name_dict = name.groupdict()
        # print(name_dict)

        if name_dict["action"] == "A":
            attacked_planet.append(name_dict["planet"])
        elif name_dict["action"] == "D":
            destroyed_planet.append(name_dict["planet"])

attacked_planet.sort()
destroyed_planet.sort()
print(f"Attacked planets: {len(attacked_planet)}")
for el in attacked_planet:
    print(f"-> {el}")
print(f"Destroyed planets: {len(destroyed_planet)}")
for el in destroyed_planet:
    print(f"-> {el}")

# наименувана първа група, която започна с @ и съдържа букви от азбуката в низ @(?P<planet>[A-Za-z]+)
# всякакви чарактъри без изброените [^-@!>:]*? - нон грииди
# наименувана втора група която започва с ескейпнато : и съдържа цифри в низ \:(?P<population>\d+)
# всякакви чарактъри без изброените [^-@!>:]*? - нон грииди
# наименувана трета група, която започва и завършва с ! и съдържа A или D !(?P<action>A|D)!
# всякакви чарактъри без изброените [^-@!>:]*? - нон грииди
# наименована четвърта група, която започва с ескейпнати -> и съдържа цифри в низ \-\>(?P<soldiers>\d+)
# всякакви чарактъри без изброените [^-@!>:]*? - нон грииди













