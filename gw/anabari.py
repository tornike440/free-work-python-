a= input("სესხი,ანაბარი,chashout თუ გადარიცხვა? ")

if a == "ანაბარი":
    b = input("რისკიანი ანაბარი გსურთ თუ ნაკლებად რისკიანი ")
    while b not in ["რისკიანი", "ნაკლებად რისკიანი"]:
     print("please, answer with 'შემოტანა' and 'გატანა'")
     b= input("რისკიანი ანაბარი გსურთ თუ ნაკლებად რისკიანი ")
    if b== "რისკიანი":

        c= int(input("how much:"))
        if c <= 1500:
             print("რისკიანი ანაბრის(<= 1500) ყოველწლიური პროცენტია მარტრივი 15% ხოლო ეს თქვენს შემთხვევაში იქნება ---" + str(c*0.15)
              + "--- ყოველწლიურად")
        else:
            print("რისკიანი ანაბრის(>= 1500) ყოველწლიური პროცენტია რთული 15% ხოლო ეს თქვენს შემთხვევაში იქნება ---")
            for i in range(1,10):
                c= int(c*1.15)
                print(str(i)+ " წელი: " + str(c))

        # g = input("re-enter your password for one last time and money is yours!")
        # if g!= password:
        #     print("ACCESED DENIED!") 
    if b== "ნაკლებად რისკიანი":
        c= int(input("how much:"))
        print("ნაკლებად რისკიანი ანაბრის  ყოველწლიური პროცენტია მარტრივი 15% ხოლო ეს თქვენს შემთხვევაში იქნება ---" + str(int(c*0.15))
         + "--- ყოველწლიურად")
        # g = input("re-enter your password for one last time and money is yours!")
        # if g!= password:
        #     print("ACCESED DENIED!") 




