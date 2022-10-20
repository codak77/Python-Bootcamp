
def phoneNumb(phoneNumber):
    number = phoneNumber.spilt("-")
    areaCode = number[0]
    endNumber = number[1:]
    num = ""

    # Search conditions in alphabets versus numbers
    for n in endNumber:
        for i in range(len(n)):
            if n[i] in "ABC":
                num = num + "2"

            elif n[i] in "DEF":
                num = num + "3"

            elif n[i] in "GHI":
                num = num + "4"

            elif n[i] in "JKL":
                num = num + "5"

            elif n[i] in "MNO":
                num = num + "6"

            elif n[i] in "PQRS":
                num = num + "7"

            elif n[i] in "TUV":
                num = num + "8"

            elif n[i] in "WXYZ":
                num = num + "9"

        num = num + "-"
    return areaCode + "-" + num[:-1]


phoneNumber = str(
    input("Please enter a phone number in the format XXX-XXX-XXXX : "))
print("\n")

newNum = phoneNumb(phoneNumber)
print("The telephone number corresponding to your previous entry is : ",
      "'" + newNum + "'")
