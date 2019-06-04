
LuckyNumbers=(657)

deposit = int(input("ENTER SUPER 3 NUMBER: "))
if(deposit<1000):
    #when the deposit is less than 1000
    print("YOU CAN'T DO ANYTHING")
    print("Deposit is < 10k")

elif(deposit == 10000):
    #when the deposit == 10000
    print("....SUPER 3 GAME .....")
    super3Number = int(input("Enter Super 3 Lucky Number"))

    print("You have entered : lucky No: {} !".format(super3Number))

    #return comaparison statement when he has won.
    if(super3Number == LuckyNumbers):
        print("Congratulations!")
        print("You have hit the jackpot!")

    else:
        #when you have failed to get it at all
        print("You have failed man!")
        print("The luck number is : {}".format(LuckyNumbers))
elif():
    #matching the first two numbers

    print("You matched the first two numbers")


else:
    print("Option invalid")










