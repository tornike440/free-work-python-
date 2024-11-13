
print("please register first before you go to bank")

username = input("create username:")
password= input("create password:")
repass= input("repeat password:")
while repass != password:
    print("IT DOESN'T MATCH!")
    repass= input("repeat password:")




a= input("გსურთ თავხის შემოტანა თუ გატანა ")


while a not in ["გატანა", "შემოტანა"]:
     print("please, answer with 'შემოტანა' and 'გატანა'")
     a= input("გსურთ თავხის შემოტანა თუ გატანა ")

if a == "შემოტანა":
    print("გმადლობთ რომ ჩვენი ბანკით სარგებლობთ,")
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

        g = input("re-enter your password for one last time and money is yours!")
        if g!= password:
            print("ACCESED DENIED!") 
    if b== "ნაკლებად რისკიანი":
        c= int(input("how much:"))
        print("ნაკლებად რისკიანი ანაბრის  ყოველწლიური პროცენტია მარტრივი 15% ხოლო ეს თქვენს შემთხვევაში იქნება ---" + str(c*0.15)
         + "--- ყოველწლიურად")
        g = input("re-enter your password for one last time and money is yours!")
        if g!= password:
            print("ACCESED DENIED!") 

#ცვლადის სახელები რომლებიც უკვე გამოვიყენე {a,b,c}

if a=="გატანა":
    print("გმადლობთ რომ ჩვენი ბანკით სარგებლობთ,")
    d = int(input("რამდენ თვიანი სესხი გნებავთ"))
    
    while d not in [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90]:
     print("ჩვენს ბანკში სესხებს გავცემთ 3იდან 90 თვემდე 3თვიანი შუალედებით")
     d= int(input("რამდენ თვიანი სესხი გნებავთ"))
    if d in [3,6,9,12,15,18,21,24]:
        print("როგორც ჩანს მოკლევადიან სესხს ეძებ, ჩვენთან 2 წელიწადზე ნაკლები სესხი 20%-იანია")
        e= int(input("რამდენის გატანა გნებავთ"))
        print("თუ თქვენ გნებავთ " +str(e)+" თანხის გატანა, თქვენ " +
               str(d)+" თვეში მოგიწევთ დაფაროთ " + str(e*1.2)+". რაც თვეში გამოდის "+str(e*1.2/d)  )
        
        g = input("re-enter your password for one last time and money is yours!")
        if g!= password:
            print("ACCESED DENIED!")       
    if d in [27,30,33,36,39,42,45,48,51,54,57,60]:
        print("როგორც ჩანს 2-იდან 5-წლამდე სესხს ეძებ, ჩვენთან ამ ხანგრძლიბის სესხი 13%-იანია")
        e= int(input("რამდენის გატანა გნებავთ"))
        print("თუ თქვენ გნებავთ " +str(e)+" თანხის გატანა, თქვენ " +
               str(d)+" თვეში მოგიწევთ დაფაროთ " + str(e*1.13)+". რაც თვეში გამოდის "+str(e*1.13/d)  )
        
        g = input("re-enter your password for one last time and money is yours!")
        if g!= password:
            print("ACCESED DENIED!")     
    if d in [63,66,69,72,75,78,81,84,87,90]:
        print("როგორც ჩანს 5-იდან 7.5-წლამდე სესხს ეძებ, ჩვენთან ამ ხანგრძლიბის სესხი 7%-იანია")
        e= int(input("რამდენის გატანა გნებავთ"))
        print("თუ თქვენ გნებავთ " +str(e)+" თანხის გატანა, თქვენ " +
               str(d)+" თვეში მოგიწევთ დაფაროთ " + str(e*1.07)+". რაც თვეში გამოდის "+str(e*1.07/d)  )
        
        g = input("re-enter your password for one last time and money is yours!")
        if g!= password:
            print("ACCESED DENIED!")
