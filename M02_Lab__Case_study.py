#Aasviben Patel
#06/16/2023
#program that accept student names and GPAs and 
#test if the student qualifies for either the Dean's List or the Honor Roll.

def main():

    lastname = input("Enter Student Last Name: ") 

    while (lastname != "ZZZ"):
        
        firstname = input("Enter Student First Name: ")    
        GPAs  = float(input("Enter Student GPA: "))     
            
        if GPAs  >= 3.5:
            
            print("{} {} has made the Dean's List.".format(firstname, lastname) )    

        else:
            
            if GPAs  >= 3.25:            
                 print("{} {} has made the Honor Roll.".format(firstname, lastname))

        lastname = input("\nEnter Student Last Name: ")     


if __name__ == "__main__":
    main()