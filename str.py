str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

print(len(str))  # number of charachters

comma=str.count(",")
letter=int(len(str))-int(comma)-int(str.count(" "))
print(letter) # number of letters

words=str.split() 
print(words) # all words in array

lowerStr=str.lower()

vovels=['a', 'e', 'i', 'o', 'u', 'ə' ,'ü', 'ö' ,'ı' ]
consonants=['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ç', 'ş', 'ğ']
vovel=0
consonant=0

for i in lowerStr:
    if i in vovels:
        vovel=vovel+1
    elif i in consonants:
        consonant=consonant+1

# second method below

# vovel=0
# consonant=0
# for i in lowerStr:
#     if(i=='a' or i=='i' or i=='o' or i=='u' or i=='e' or i=='ə' or i=='ö' or i=='ü' or i=='ı'):
#         vovel=vovel+1
#     elif(i=='q' or i=='w' or i=='r' or i=='t' or i=='y' or i=='p' or i=='s' or i=='d' or i=='f' or i=='g' or i=='h' or i=='j' or i=='k' or i=='l' or i=='z' or i=='x' or i=='c' or i=='v' or i=='b' or i=='n' or i=='m' or i=='ç' or i=='ş' or i=='ğ'):
#         consonant=consonant+1

print('Number of vovel', vovel) # number of vovel letters
print('Number of consonant', consonant) # number of consonant letters

rstr = str.rsplit(" ", 2)[0]
print(rstr)  # delete last two words


newArr = str.split(',')
print(newArr)  # split for comma


def searchforWord():
    i=input('Search for : ')
    if i in str:
        print('The word is in the list')
    else:
        print('The word is not in the list')
searchforWord()  # search for a word in the list

