def count(str1, str2):
    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    counter = 0

    for char in str2:
        if char in char_count and char_count[char] > 0:
            counter += 1
            char_count[char] -= 1

    print("total matching characters are: " + str(counter))

ret = False
while True:
    print("\n================ count THE MATCHING characters =====================\n\n")

    str1 = input("enter 1st String: ")
    str2 = input("Enter 2nd string: ")

    count(str1, str2)

    opt = input("\ndo you want to try again?(yes/no):")

    if opt.lower() == 'yes':
        ret = False
    elif opt.lower() == 'no':
        ret = True
        print("Exiting program....")
    else:
        print("please enter yes/no:")
        break

    if ret == False:
        continue