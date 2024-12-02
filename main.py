
def main():
     #First code
    # print(str("Number of letters in your name: ") + str(len(input("Enter your name: "))))

    #Refactored Code

        name_of_the_user = input("Enter your name: ")
        len_of_name = len(name_of_the_user)

        # print(type("Number of letters in your name: ")) #str
        # print(type(len_of_name)) #int

        print("Number of letters in your name: " + str(len_of_name))
    

if __name__=="__main__":
     main()


