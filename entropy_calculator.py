import math 


main_input = ""
while(True):
    try:
        main_input = input("First: ")
        x = int(main_input)
        y = int(input("Second: "))
        
    except:
        if (main_input == "q"):
            print("Byee")
            exit(0)
        print("Sorry, the input is invalid") 
    else:
        sum = x + y
        if (x == 0 or y == 0):
            entropy = 0
            print("Entropy: {}".format(entropy))
            continue
        try:
            entropy = (-(x/sum) * math.log(x/sum,2)) - ((y/sum) * math.log(y/sum,2))
            print("Entropy: {}".format(entropy))
        except:
            print("Something went wrong while calculating the entropy") 

