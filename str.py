str='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'

print(len(str))  # number of charachters

comma=str.count(",")
letter=int(len(str))-int(comma)-int(str.count(" "))
print(letter) # number of letters

words=str.split()
print(words) # all words in array

vovel=0
consonant=0
for i in str:
    if(i=='a' or i=='i' or i=='o' or i=='u' or i=='e' or i=='ə' or i=='ö' or i=='ü' or i=='ı'):
        vovel=vovel+1
    else:
        consonant=consonant+1

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

