# Q1
#z=input("enter your name ")
#print("welcome "+str(z))
#a=int(input("enter the number1 : "))
#print(a)
#b=int(input("enter the number2 : "))
#print(b)
#sum=a+b
#print("the sum =" + str(sum))
#if a>b :
 #   print(a)
#else:
 #   print(b)

#if(a%b==0):
 #   print("even")
#else:
#    print("odd")





#Q2
def count_letter(word,char):
    count=0
    for c in word:
        count+=(char==c)
        return count 

list1=list("python")
char=input("enter the string ")
print(count_letter(list1,char))
list1[0]=(char)
list1.pop()
list1.append(char)
print(list1)




#Q3
list_1 =("laptop", "iphone", "tablet", "printer", "Ipad")
for i in list_1:
   print(len(i))
    
